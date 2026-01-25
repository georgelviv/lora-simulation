import random
import numpy as np

from lora_simulation_model import (
  get_ping_state_from_str_config, EnvironmentModel, AreaType,
  State
)

random.seed(1)
np.random.seed(1)

def test_check_ping():
  env_model: EnvironmentModel = EnvironmentModel(
    name=f"math-100-meters",
    path_loss_exponent=2.5,
    shadow_sigma_db=3.0,
    sigma_noise_db=2.0,
    distance_m=100,
    hb_m = 1.2,
    hm_m = 1.0,
    area_type=AreaType.SUBURBAN,
    description=f"Suburban 100 meters"
  )
  state: State = get_ping_state_from_str_config(env_model, 'SF=7,FQ=871,BW=500,CR=7,TP=20,IH=0,HS=200,PL=85,CL=140,RT=1')

  expected_state: State = {
    'BPS': 317.965,
    'CHC': 1.0,
    'DELAY': 128.996,
    'RSSI': -104.79,
    'SNR': 0.974,
    'TOA': 31.45,
    'ATT': 1,
    'ETX': 0.774, 
    'RTOA': 33.498
  }

  assert state == expected_state