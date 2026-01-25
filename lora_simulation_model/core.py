from .models import Config, State, EnvironmentModel
from .utils import lora_log
import logging
from .logger import default_logger
from .environment import LORA_SIMULATION_ENVIRONMENTS
from .state import get_ping_state_from_config

class LoraSimulationModel():
  @property
  def name(self) -> str:
    return "simulation"

  def __init__(
      self, logger: logging.Logger = default_logger, 
      env_model: EnvironmentModel = LORA_SIMULATION_ENVIRONMENTS['open_field']
    ):
    self.config: Config = None
    self.logger = logger
    self.env_model: EnvironmentModel = env_model

  async def start(self):
    pass

  async def stop(self):
    pass

  async def config_sync(self, id: int, params: Config) -> bool:
    self.logger.info(lora_log("CONFIG_SYNC", params))
    self.config = params
    return True

  async def config_get(self) -> Config:
    return self.config
  
  async def ping(self, id: int) -> State:
    state: State = get_ping_state_from_config(self.env_model, self.config)
    self.logger.info(lora_log("PING", state))

    return state