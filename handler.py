import asyncio
import json
import os
import requests
from datetime import datetime, timedelta
from tesla_api import TeslaApiClient
from tesla_api.exceptions import VehicleUnavailableError
from cognite.client import CogniteClient

vehicle_keys = ["api_version", "car_version", "df", "dr", "fd_window", "fp_window", "ft", "is_user_present", "locked", "odometer", "pf", "pr", "rd_window", "rp_window", "rt", "sentry_mode", "valet_mode"]
climate_keys = ["battery_heater", "defrost_mode", "driver_temp_setting", "is_auto_conditioning_on", "is_climate_on", "is_front_defroster_on", "is_preconditioning", "is_rear_defroster_on", "remote_heater_control_enabled", "side_mirror_heaters", "wiper_blade_heater", "fan_status", "inside_temp", "left_temp_direction", "max_avail_temp", "min_avail_temp", "outside_temp", "passenger_temp_setting", "right_temp_direction", "seat_heater_left", "seat_heater_rear_center", "seat_heater_rear_left", "seat_heater_rear_right", "seat_heater_right"]
drive_keys = ["heading", "latitude", "longitude", "native_latitude", "native_longitude", "power", "shift_state", "speed"]
charge_keys = ["battery_heater_on", "battery_level", "battery_range", "charge_current_request", "charge_current_request_max", "charge_energy_added", "charge_limit_soc", "charge_limit_soc_max", "charge_limit_soc_min", "charge_limit_soc_std", "charge_miles_added_ideal", "charge_miles_added_rated", "charge_port_cold_weather_mode", "charge_port_door_open", "charge_port_latch", "charge_rate", "charge_to_max_range", "charger_actual_current", "charger_pilot_current", "charger_power", "charger_voltage", "charging_state", "conn_charge_cable", "est_battery_range", "fast_charger_brand", "fast_charger_present", "fast_charger_type", "ideal_battery_range", "managed_charging_active", "max_range_charge_counter", "minutes_to_full_charge", "not_enough_power_to_heat", "scheduled_charging_pending", "time_to_full_charge", "trip_charging", "usable_battery_level"]

def handle_data_point(data_point):
    convert_miles_to_km_keys = ["speed", "est_battery_range", "ideal_battery_range", "odometer"]

    key = data_point["externalId"]
    now = data_point["datapoints"][0][0]
    value = data_point["datapoints"][0][1]
    if key in ["shift_state", "not_enough_power_to_heat"] and value is None:
        # print(f"Setting {key} to None")
        return None
    if type(value) == bool:
        # print(f"Converting {key} with value bool to number")
        value = 1 if value else 0
        data_point["datapoints"][0] = (now, value)
    if key == "speed" and value in [None, ""]:
        # print(f"Setting {key} to 0.0")
        value = 0
        data_point["datapoints"][0] = (now, value)
    if key in convert_miles_to_km_keys:
        # print(f"Converting {key} to km")
        data_point["datapoints"][0] = (now, value * 1.609344)
    if type(value) not in [str, float, int]:
        return None

    if key == "inside_temp":
        print(data_point)

    return data_point

async def handle_data(data):
    now = datetime.utcnow()
    data_points = []

    for key in vehicle_keys:
        data_points.append({"externalId": key, "datapoints":[(now, data["vehicle_state"][key])]})
    for key in climate_keys:
        data_points.append({"externalId": key, "datapoints":[(now, data["climate_state"][key])]})
    for key in drive_keys:
        data_points.append({"externalId": key, "datapoints":[(now, data["drive_state"][key])]})
    for key in charge_keys:
        data_points.append({"externalId": key, "datapoints":[(now, data["charge_state"][key])]})
    data_points = list(map(handle_data_point, data_points))
    data_points = list(filter(lambda x: x is not None, data_points))
    return data_points

async def main(tesla_password):
    try:
        async with TeslaApiClient('andershaf@gmail.com', tesla_password) as client:
            vehicles = await client.list_vehicles()
            
            for v in vehicles:
                try:
                    data = await v.get_data()
                    data_points = await handle_data(data)
                    return data_points
                except VehicleUnavailableError:
                    print("Car is unavailable, waking up ...")
                    await v.wake_up()
                    return []
    except:
        print("Got error with Tesla API ...")

def handle(client, secrets):
    started_at = datetime.utcnow()
    ends_at = started_at + timedelta(minutes=10)
    while datetime.utcnow() < ends_at:
        now = datetime.utcnow()
        data_points = asyncio.run(main(secrets["tesla-password"]))
        if data_points and len(data_points) > 0:
            client.datapoints.insert_multiple(data_points)
        formatted_date = now.strftime("%d/%m/%y %H:%M:%S")
        print(f"{formatted_date}: Inserted {len(data_points)} data points")
    print("Stopping fetching")
    
if __name__ == "__main__":
    client = CogniteClient(project="andershaf", api_key=os.environ["COGNITE_API_KEY_ANDERSHAF"])
    handle(client, {"tesla-password": os.environ["TESLA_PASSWORD"]})
