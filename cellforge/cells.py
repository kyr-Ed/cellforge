"""
Cell properties for battery manufacturing.

Covers theoretical capacity, potential difference, and related electrode-balancing formulas.
"""

def th_cell_cap(anode_areal_capacity: float, cathode_areal_capacity: float) -> float:
    """
    Calculate the theoretical cell capacity.

    Args:
        anode_areal_capacity: Areal capacity of the anode (mAh/cm^2)
        cathode_areal_capacity: Areal capacity of the cathode (mAh/cm^2)

    Returns:
        Theoretical cell capacity (mAh/cm^2).
    """
    if cathode_areal_capacity <= 0:
        raise ValueError("Cathode areal capacity must be positive")
    if anode_areal_capacity < 0:
        raise ValueError("Anode areal capacity must be non-negative")

    if cathode_areal_capacity < anode_areal_capacity:
        return cathode_areal_capacity
    else:
        return anode_areal_capacity


def th_cell_voltage(anode_areal_potential: float, cathode_areal_potential: float) -> float:
    """
    Calculate the theoretical cell voltage.

    Args:
        anode_areal_potential: Areal potential of the anode (V)
        cathode_areal_potential: Areal potential of the cathode (V)

    Returns:
        Theoretical cell voltage (V).
    """
    if cathode_areal_potential <= 0:
        raise ValueError("Cathode areal potential must be positive")
    if anode_areal_potential < 0:
        raise ValueError("Anode areal potential must be non-negative")

    return anode_areal_potential - cathode_areal_potential