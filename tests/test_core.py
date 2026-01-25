import random
import numpy as np
import pytest
from lora_simulation_model import (
  Config, LORA_SIMULATION_ENVIRONMENTS, LoraSimulationModel,
  parse_lora_config
)

@pytest.mark.asyncio
async def test_lora_simulation():
  random.seed(1)
  np.random.seed(1)

  lora_sim = LoraSimulationModel(env_model=LORA_SIMULATION_ENVIRONMENTS['open_field'])
  lora_config: Config = {
    "SF": 12,
    "FQ": 878,
    "BW": 500.0,
    "CR": 8.0,
    "TP": 20,
    "IH": 0.0,
    "HS": 10.0,
    "PL": 10.0,
    "CL": 45.0,
    "RT": 1.0
  }
  await lora_sim.config_sync(
    1, 
    lora_config
  )

  cfg = await lora_sim.config_get()
  assert cfg == lora_config

  state = await lora_sim.ping(1)

  assert state == {
    'BPS': 31.847,
    'CHC': 1.0,
    'DELAY': 1019.072,
    'RSSI': -71.52,
    'SNR': 8.81,
    'TOA': 314,
    'ATT': 1,
    'ETX': 10.02, 
    'RTOA': 379.536
  }

def test_parse_lora_config():
  lora_config: Config = {
    "SF": 7,
    "FQ": 871,
    "BW": 500.0,
    "CR": 7.0,
    "TP": 20,
    "IH": 0.0,
    "HS": 200.0,
    "PL": 85.0,
    "CL": 140.0,
    "RT": 1.0
  }
  assert parse_lora_config("SF=7,FQ=871,BW=500,CR=7,TP=20,IH=0,HS=200,PL=85,CL=140,RT=1") == lora_config