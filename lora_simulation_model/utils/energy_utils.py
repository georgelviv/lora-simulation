SX1276_TX_CURRENT = {
  20: 120, 
  17: 87,
  13: 29,
  7: 20,
  2: 15
}

def estimate_tx_current(tx_power: int) -> float:
  powers = sorted(SX1276_TX_CURRENT.keys())
  if tx_power in SX1276_TX_CURRENT:
    return SX1276_TX_CURRENT[tx_power]
  
  for i in range(len(powers) - 1):
    low_p = powers[i]
    high_p = powers[i + 1]
    if low_p < tx_power < high_p:
      low_i = SX1276_TX_CURRENT[low_p]
      high_i = SX1276_TX_CURRENT[high_p]
      interp_i = low_i + (high_i - low_i) * (tx_power - low_p) / (high_p - low_p)
      return interp_i

def estimate_tx_energy(tx_power_dbm: float, toa_s: float, current_limit: int, voltage_v: float = 3.3) -> float:
  current_mA = estimate_tx_current(tx_power_dbm)
  current_mA = min(current_limit, current_mA)
  current_a = current_mA / 1000.0
  energy_j = voltage_v * current_a * toa_s

  return energy_j