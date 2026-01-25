from .models import EnvironmentModel, State, Config
from .utils import (
  lora_rssi_hata_chip, compute_snr,
  calculate_delay, chunks_count, lora_time_on_air_ms,
  bytes_per_second, rtoa_ms, estimate_tx_energy
)

def get_ping_state_from_config(env_model: EnvironmentModel, config: Config) -> State:
  freq = config.get('FQ') * 10e6
  tx_power_dbm = config.get('TP')
  sf = config.get('SF')
  bw = config.get('BW') * 1000
  cr = config.get('CR')
  ih = config.get('IH')
  pl = config.get('PL')

  payload_size = 10

  rssi_chip = lora_rssi_hata_chip(
    distance_m=env_model.distance_m,
    freq_hz=freq,
    tx_power_dbm=tx_power_dbm,
    shadow_sigma_db=env_model.shadow_sigma_db,
    hb_m=env_model.hb_m,
    hm_m=env_model.hm_m,
    area=env_model.area_type
  )

  snr_chip = compute_snr(
    rssi_dbm=rssi_chip,
    sf=sf,
    bw_hz=bw
  )

  toa = lora_time_on_air_ms(sf, bw, payload_size, cr, pl)
  rtoa = rtoa_ms(toa_ms=toa, sf=sf, bw_hz=bw)

  delay = calculate_delay(
    toa_ms=rtoa,
    sf=sf,
    bw_hz=bw,
    cr=cr,
    pl_bytes=pl
  )

  energy = estimate_tx_energy(tx_power_dbm, rtoa, cr)

  state: State = {
    'BPS': bytes_per_second(payload_size, toa),
    'CHC': chunks_count(payload_size, ih, pl),
    'DELAY': delay,
    'RSSI': rssi_chip,
    'SNR': snr_chip,
    'RTOA': rtoa,
    'TOA': toa,
    'ETX': energy,
    'ATT': 1
  }

  state = { key: round(value, 3) if isinstance(value, (float, int)) else value for key, value in state.items() }

  return state

def parse_lora_config(s: str) -> Config:
  config: Config = {}

  for item in s.split(","):
    key, value = item.split("=")

    if "." in value:
      parsed_value = float(value)
    else:
      parsed_value = int(value)

    config[key] = parsed_value

  return config

def get_ping_state_from_str_config(env_model: EnvironmentModel, config: str) -> State:
  config: Config = parse_lora_config(config)
  return get_ping_state_from_config(env_model, config)