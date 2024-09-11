from math import tanh, pi , sinh

def wavelength_calculation(water_depth, wave_period):
    # Initial estimate using deep water wave length
    assumed_wave_length = 1.56 * wave_period ** 2

    # Iterative procedure
    while True:
        wave_length = 1.56 * wave_period ** 2 * (tanh(2 * pi * water_depth / assumed_wave_length))
        if abs(wave_length - assumed_wave_length) < 0.01:
            break
        assumed_wave_length = wave_length

    return wave_length

# Function to determine wave type based on depth and wavelength ratio

def determine_wave_type(depth, wavelength):
    ratio = depth / wavelength
    if ratio > 0.5:
        return "Deep water", ratio
    elif 0.05 <= ratio <= 0.5:
        return "Intermedate water", ratio
    else:
        return "Shallow water", ratio
    


def evaluate_group_speed(wave_period, water_depth , wave_type , wave_celerity , wave_number):
    # Group speed calculation
    if wave_type == "Shallow water":
        return (9.81 * water_depth) ** 0.5
    
    elif wave_type == "Deep water":
        assumed_wave_length = 1.56 * wave_period ** 2
        deep_water_celerity = (9.81*assumed_wave_length/(2*pi))**0.5
        return (deep_water_celerity/2)
    
    else:
        n = 0.5*(1+(2*wave_number*water_depth)/(sinh(2*wave_number*water_depth)))
        return n* wave_celerity
    


def energy_density(wave_height):
    # Energy density calculation
    return (0.125 * 1025 * 9.81 * wave_height ** 2)


        

                
