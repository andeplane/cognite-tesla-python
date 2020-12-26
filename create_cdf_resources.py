import json
import os
from cognite.client import CogniteClient
from cognite.client.data_classes import Asset, TimeSeries

client = CogniteClient(client_name="Tesla AH builder", api_key=os.environ["COGNITE_API_KEY_ANDERSHAF"])

def create_asset_hierarchy():
  assets = []

  assets.append(Asset(name="Tesla Model 3", external_id="tesla"))
  assets.append(Asset(name="Climate", description="Climate data", external_id="tesla_climate", parent_external_id="tesla"))
  assets.append(Asset(name="Charge", description="Charge data", external_id="tesla_charge", parent_external_id="tesla"))
  assets.append(Asset(name="Drive", description="Drive data", external_id="tesla_drive", parent_external_id="tesla"))
  assets.append(Asset(name="Vehicle", description="Vehicle data", external_id="tesla_vehicle", parent_external_id="tesla"))
  
  client.assets.create_hierarchy(assets)

def create_time_series():
  assets = client.assets.retrieve_subtree(external_id="tesla")
  asset_by_external_id = {}
  for asset in assets:
    asset_by_external_id[asset.external_id] = asset
  
  # Create time series for Vehicle
  print("Creating time series for Vehicle")
  client.time_series.create(TimeSeries(name="api_version", external_id="api_version", asset_id=asset_by_external_id["tesla_vehicle"].id, is_step=True))
  client.time_series.create(TimeSeries(name="car_version", external_id="car_version", asset_id=asset_by_external_id["tesla_vehicle"].id, is_string=True))
  client.time_series.create(TimeSeries(name="df", external_id="df", asset_id=asset_by_external_id["tesla_vehicle"].id))
  client.time_series.create(TimeSeries(name="dr", external_id="dr", asset_id=asset_by_external_id["tesla_vehicle"].id))
  client.time_series.create(TimeSeries(name="fd_window", external_id="fd_window", asset_id=asset_by_external_id["tesla_vehicle"].id))
  client.time_series.create(TimeSeries(name="fp_window", external_id="fp_window", asset_id=asset_by_external_id["tesla_vehicle"].id))
  client.time_series.create(TimeSeries(name="ft", external_id="ft", asset_id=asset_by_external_id["tesla_vehicle"].id))
  client.time_series.create(TimeSeries(name="is_user_present", external_id="is_user_present", asset_id=asset_by_external_id["tesla_vehicle"].id, is_step=True))
  client.time_series.create(TimeSeries(name="locked", external_id="locked", asset_id=asset_by_external_id["tesla_vehicle"].id, is_step=True))
  client.time_series.create(TimeSeries(name="odometer", external_id="odometer", asset_id=asset_by_external_id["tesla_vehicle"].id, unit="km"))
  client.time_series.create(TimeSeries(name="pf", external_id="pf", asset_id=asset_by_external_id["tesla_vehicle"].id))
  client.time_series.create(TimeSeries(name="pr", external_id="pr", asset_id=asset_by_external_id["tesla_vehicle"].id))
  client.time_series.create(TimeSeries(name="rd_window", external_id="rd_window", asset_id=asset_by_external_id["tesla_vehicle"].id))
  client.time_series.create(TimeSeries(name="rp_window", external_id="rp_window", asset_id=asset_by_external_id["tesla_vehicle"].id))
  client.time_series.create(TimeSeries(name="rt", external_id="rt", asset_id=asset_by_external_id["tesla_vehicle"].id))
  client.time_series.create(TimeSeries(name="sentry_mode", external_id="sentry_mode", asset_id=asset_by_external_id["tesla_vehicle"].id, is_step=True))
  client.time_series.create(TimeSeries(name="valet_mode", external_id="valet_mode", asset_id=asset_by_external_id["tesla_vehicle"].id, is_step=True))
  
  # Create time series for Climate
  print("Creating time series for Climate")
  client.time_series.create(TimeSeries(name="battery_heater", external_id="battery_heater", asset_id=asset_by_external_id["tesla_climate"].id, is_step=True))
  client.time_series.create(TimeSeries(name="defrost_mode", external_id="defrost_mode", asset_id=asset_by_external_id["tesla_climate"].id, is_step=True))
  client.time_series.create(TimeSeries(name="driver_temp_setting", external_id="driver_temp_setting", asset_id=asset_by_external_id["tesla_climate"].id, unit="°C"))
  client.time_series.create(TimeSeries(name="is_auto_conditioning_on", external_id="is_auto_conditioning_on", asset_id=asset_by_external_id["tesla_climate"].id, is_step=True))
  client.time_series.create(TimeSeries(name="is_climate_on", external_id="is_climate_on", asset_id=asset_by_external_id["tesla_climate"].id, is_step=True))
  client.time_series.create(TimeSeries(name="is_front_defroster_on", external_id="is_front_defroster_on", asset_id=asset_by_external_id["tesla_climate"].id, is_step=True))
  client.time_series.create(TimeSeries(name="is_preconditioning", external_id="is_preconditioning", asset_id=asset_by_external_id["tesla_climate"].id, is_step=True))
  client.time_series.create(TimeSeries(name="is_rear_defroster_on", external_id="is_rear_defroster_on", asset_id=asset_by_external_id["tesla_climate"].id, is_step=True))
  client.time_series.create(TimeSeries(name="remote_heater_control_enabled", external_id="remote_heater_control_enabled", asset_id=asset_by_external_id["tesla_climate"].id, is_step=True))
  client.time_series.create(TimeSeries(name="side_mirror_heaters", external_id="side_mirror_heaters", asset_id=asset_by_external_id["tesla_climate"].id, is_step=True))
  client.time_series.create(TimeSeries(name="wiper_blade_heater", external_id="wiper_blade_heater", asset_id=asset_by_external_id["tesla_climate"].id, is_step=True))

  client.time_series.create(TimeSeries(name="fan_status", external_id="fan_status", asset_id=asset_by_external_id["tesla_climate"].id))
  client.time_series.create(TimeSeries(name="inside_temp", external_id="inside_temp", asset_id=asset_by_external_id["tesla_climate"].id, unit="°C"))
  client.time_series.create(TimeSeries(name="left_temp_direction", external_id="left_temp_direction", asset_id=asset_by_external_id["tesla_climate"].id))
  client.time_series.create(TimeSeries(name="max_avail_temp", external_id="max_avail_temp", asset_id=asset_by_external_id["tesla_climate"].id, unit="°C"))
  client.time_series.create(TimeSeries(name="min_avail_temp", external_id="min_avail_temp", asset_id=asset_by_external_id["tesla_climate"].id, unit="°C"))
  client.time_series.create(TimeSeries(name="outside_temp", external_id="outside_temp", asset_id=asset_by_external_id["tesla_climate"].id, unit="°C"))
  client.time_series.create(TimeSeries(name="passenger_temp_setting", external_id="passenger_temp_setting", asset_id=asset_by_external_id["tesla_climate"].id, unit="°C"))
  client.time_series.create(TimeSeries(name="right_temp_direction", external_id="right_temp_direction", asset_id=asset_by_external_id["tesla_climate"].id))
  client.time_series.create(TimeSeries(name="seat_heater_left", external_id="seat_heater_left", asset_id=asset_by_external_id["tesla_climate"].id))
  client.time_series.create(TimeSeries(name="seat_heater_rear_center", external_id="seat_heater_rear_center", asset_id=asset_by_external_id["tesla_climate"].id))
  client.time_series.create(TimeSeries(name="seat_heater_rear_left", external_id="seat_heater_rear_left", asset_id=asset_by_external_id["tesla_climate"].id))
  client.time_series.create(TimeSeries(name="seat_heater_rear_right", external_id="seat_heater_rear_right", asset_id=asset_by_external_id["tesla_climate"].id))
  client.time_series.create(TimeSeries(name="seat_heater_right", external_id="seat_heater_right", asset_id=asset_by_external_id["tesla_climate"].id))
  
  # Create time series for Drive
  print("Creating time series for Drive")
  client.time_series.create(TimeSeries(name="heading", external_id="heading", asset_id=asset_by_external_id["tesla_drive"].id))
  client.time_series.create(TimeSeries(name="latitude", external_id="latitude", asset_id=asset_by_external_id["tesla_drive"].id))
  client.time_series.create(TimeSeries(name="longitude", external_id="longitude", asset_id=asset_by_external_id["tesla_drive"].id))
  client.time_series.create(TimeSeries(name="native_latitude", external_id="native_latitude", asset_id=asset_by_external_id["tesla_drive"].id))
  client.time_series.create(TimeSeries(name="native_longitude", external_id="native_longitude", asset_id=asset_by_external_id["tesla_drive"].id))
  client.time_series.create(TimeSeries(name="power", external_id="power", asset_id=asset_by_external_id["tesla_drive"].id))
  client.time_series.create(TimeSeries(name="shift_state", external_id="shift_state", asset_id=asset_by_external_id["tesla_drive"].id, is_string=True))
  client.time_series.create(TimeSeries(name="speed", external_id="speed", asset_id=asset_by_external_id["tesla_drive"].id, unit="km/h"))
  client.time_series.create(TimeSeries(name="elevation", external_id="elevation", asset_id=asset_by_external_id["tesla_drive"].id))

  # Create time series for Charge
  print("Creating time series for Charge")
  client.time_series.create(TimeSeries(name="battery_heater_on", external_id="battery_heater_on", asset_id=asset_by_external_id["tesla_charge"].id, is_step=True))
  client.time_series.create(TimeSeries(name="battery_level", external_id="battery_level", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="battery_range", external_id="battery_range", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="charge_current_request", external_id="charge_current_request", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="charge_current_request_max", external_id="charge_current_request_max", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="charge_energy_added", external_id="charge_energy_added", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="charge_limit_soc", external_id="charge_limit_soc", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="charge_limit_soc_max", external_id="charge_limit_soc_max", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="charge_limit_soc_min", external_id="charge_limit_soc_min", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="charge_limit_soc_std", external_id="charge_limit_soc_std", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="charge_miles_added_ideal", external_id="charge_miles_added_ideal", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="charge_miles_added_rated", external_id="charge_miles_added_rated", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="charge_port_cold_weather_mode", external_id="charge_port_cold_weather_mode", asset_id=asset_by_external_id["tesla_charge"].id, is_step=True))
  client.time_series.create(TimeSeries(name="charge_port_door_open", external_id="charge_port_door_open", asset_id=asset_by_external_id["tesla_charge"].id, is_step=True))
  client.time_series.create(TimeSeries(name="charge_port_latch", external_id="charge_port_latch", asset_id=asset_by_external_id["tesla_charge"].id, is_string=True))
  client.time_series.create(TimeSeries(name="charge_rate", external_id="charge_rate", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="charge_to_max_range", external_id="charge_to_max_range", asset_id=asset_by_external_id["tesla_charge"].id, is_step=True))
  client.time_series.create(TimeSeries(name="charger_actual_current", external_id="charger_actual_current", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="charger_pilot_current", external_id="charger_pilot_current", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="charger_power", external_id="charger_power", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="charger_voltage", external_id="charger_voltage", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="charging_state", external_id="charging_state", asset_id=asset_by_external_id["tesla_charge"].id, is_string=True))
  client.time_series.create(TimeSeries(name="conn_charge_cable", external_id="conn_charge_cable", asset_id=asset_by_external_id["tesla_charge"].id, is_string=True))
  client.time_series.create(TimeSeries(name="est_battery_range", external_id="est_battery_range", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="fast_charger_brand", external_id="fast_charger_brand", asset_id=asset_by_external_id["tesla_charge"].id, is_string=True))
  client.time_series.create(TimeSeries(name="fast_charger_present", external_id="fast_charger_present", asset_id=asset_by_external_id["tesla_charge"].id, is_step=True))
  client.time_series.create(TimeSeries(name="fast_charger_type", external_id="fast_charger_type", asset_id=asset_by_external_id["tesla_charge"].id, is_string=True))
  client.time_series.create(TimeSeries(name="ideal_battery_range", external_id="ideal_battery_range", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="managed_charging_active", external_id="managed_charging_active", asset_id=asset_by_external_id["tesla_charge"].id, is_step=True))
  client.time_series.create(TimeSeries(name="max_range_charge_counter", external_id="max_range_charge_counter", asset_id=asset_by_external_id["tesla_charge"].id, is_step=True))
  client.time_series.create(TimeSeries(name="minutes_to_full_charge", external_id="minutes_to_full_charge", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="not_enough_power_to_heat", external_id="not_enough_power_to_heat", asset_id=asset_by_external_id["tesla_charge"].id, is_step=True))
  client.time_series.create(TimeSeries(name="scheduled_charging_pending", external_id="scheduled_charging_pending", asset_id=asset_by_external_id["tesla_charge"].id, is_step=True))
  client.time_series.create(TimeSeries(name="time_to_full_charge", external_id="time_to_full_charge", asset_id=asset_by_external_id["tesla_charge"].id))
  client.time_series.create(TimeSeries(name="trip_charging", external_id="trip_charging", asset_id=asset_by_external_id["tesla_charge"].id, is_step=True))
  client.time_series.create(TimeSeries(name="usable_battery_level", external_id="usable_battery_level", asset_id=asset_by_external_id["tesla_charge"].id))

create_asset_hierarchy()
create_time_series()