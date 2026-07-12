from dataclasses import dataclass



@dataclass(frozen=True)
class AtmosphericParameters:
    Air_density_0: float = 1.225
    Air_temperature_0: float = 288.15
    Air_pressure_0: float = 101325.0
    Temp_lapse_rate: float = 0.0065
    Air_gas_constant: float = 287.05
    Gravitational_acceleration: float = 9.80665


@dataclass(frozen=True)
class AircraftParameters:
    MTOW: float 
    Payload_mass: float
    Payload_free_mass: float
    Wing_area: float
    Wing_span: float
    Aspect_ratio: float
    Oswald_efficiency: float
    Zero_lift_drag_coeff: float
    Induced_drag_coeff: float
    Max_lift_to_drag_ratio: float

@dataclass(frozen=True)
class TurboShaftParameters:
    Engine_mass: float
    Engine_max_rpm: float
    BSFC: float
    Min_operating_power: float
    Altitude_power_lapse: float

@dataclass(frozen=True)
class GeneratorParameters:
    Generator_mass: float
    Generator_efficiency: float
    Generator_specific_power: float

@dataclass(frozen=True)
class BatteryParameters:
    Battery_mass: float
    Battery_specific_energy: float
    Battery_nominal_voltage: float
    Battery_internal_resistance: float
    Battery_max_charge_rate: float      
    Battery_max_discharge_rate: float
    Battery_soc_min: float
    Battery_soc_max: float
    Battery_initial_soc: float
    Battery_round_trip_efficiency: float


@dataclass(frozen=True)
class MotorParameters:
    Motor_mass: float
    Motor_specific_power: float
    Motor_efficiency: float
    Propeller_efficiency: float
    Inverter_effeciency: float

@dataclass(frozen=True)
class DesignBounds:
    Engine_power: tuple
    Battery_capacity: tuple
    Motor_number: tuple
    Power_split_setpoint: tuple










