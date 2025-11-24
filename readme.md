# Lora Simulation — Lightweight LoRa PHY Simulator for Lora firmware

Lora Simulation is a lightweight and fast **LoRa physical layer simulator** implemented in Python.  
It is designed specifically for:

- Reinforcement Learning (RL) experiments  
- LoRa parameter auto-tuning  
- Rapid prototyping  
- Research in IoT/CPS and wireless communication  

LoRaSim models RSSI, SNR, propagation, packet success/failure, Time-on-Air, and more — using equations and assumptions close to Semtech SX1276/78 chips. 

More about physical level simulation in this [document](./physical-channel.md)

## 📦 Installation

```bash
pip install git+https://github.com/georgelviv/lora-simulation.git
```

## Commands

```bash
pytest -s --log-cli-level=DEBUG
```
