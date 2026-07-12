from config import AtmosphericParameters


def Temperature (altitude:float, parameters: AtmosphericParameters)->float:
    return parameters.Air_temperature_0 - parameters.Temp_lapse_rate * altitude

def Air_pressure (altitude:float, parameters: AtmosphericParameters)->float:
    T = Temperature(altitude, parameters)
    exponent = parameters.Gravitational_acceleration / (parameters.Air_gas_constant * parameters.Temp_lapse_rate)
    return parameters.Air_pressure_0 * (T / parameters.Air_temperature_0) ** exponent

def Density(altitude: float, parameters: AtmosphericParameters) -> float:
    T = Temperature(altitude, parameters)
    P = Air_pressure(altitude, parameters)
    return P / (parameters.Air_gas_constant * T)

def ISA_properties(altitude: float, parameters: AtmosphericParameters) -> tuple[float, float, float]:
    T = Temperature(altitude, parameters)
    P = Air_pressure(altitude, parameters)
    rho = Density(altitude, parameters)
    return T, P, rho

