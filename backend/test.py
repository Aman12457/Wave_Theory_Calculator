import matplotlib.pyplot as plt
from calculations import  wavelength_calculation , determine_wave_type , evaluate_group_speed , energy_density
from math import cos, pi , sin 
import numpy as np
def corrected_wave_height_with_modified_factor(wave_height ,water_depth, wave_period ,step_size = 0.1 , min_depth = 0.1 ):

    # Define range of depths from initial_depth to min_depth with step_size
    depths = np.arange(water_depth, min_depth, -step_size)

    angles = np.linspace(0, np.pi / 2, 100)

    refraction_coefficients = []

    shoaling_coefficients = []

    deep_water_celerity = (9.81 * wave_period  / (2 * pi))
   

    # Calculate for each depth in the range

    for d in depths:
        # Calculate wavelength using the corrected_wavelength function
        L = wavelength_calculation(d, wave_period)
        # Calculate shoaling coefficient
        wave_type = determine_wave_type(d, L)
        group_speed = evaluate_group_speed(wave_period , d ,wave_type , L / wave_period , 2 * pi / L)
        shoaling_coefficients.append(((deep_water_celerity* 0.5)/group_speed)**0.5)

        wave_celerity = L/ wave_period
        deep_water_celerity = (9.81 * wave_period  / (2 * pi))

        temp_refraction_coeffs = []
        for theta in angles:
            alpha = np.arcsin((wave_celerity / deep_water_celerity) * np.sin(theta))*(pi/180)
            refraction_coefficient = (np.cos(theta) / np.cos(alpha))**0.5
            temp_refraction_coeffs.append(refraction_coefficient)
        refraction_coefficients.append(temp_refraction_coeffs)

    refraction_coefficients = np.array(refraction_coefficients)
    shoaling_coefficients = np.array(shoaling_coefficients)

    shoaling_coefficients_reshaped = shoaling_coefficients[:, np.newaxis]

    # combinig refraction_coeffiecient_with_shoaling_coefficient

    # Product of those two will give final modifying factor
    
    modified_factor = np.multiply(refraction_coefficients , shoaling_coefficients_reshaped)

    # Calculate the corrected wave height
    broadcaseted_wave_height = np.broadcast_to(wave_height, len(angles))
    
    deep_water_broadcasted_height = np.divide(broadcaseted_wave_height, modified_factor[0])

    deep_water_broadcasted_height = np.broadcast_to(deep_water_broadcasted_height, (len(depths), len(angles)))

    corrected_height = np.multiply(deep_water_broadcasted_height , modified_factor)

    fig, ax = plt.subplots()
    X, Y = np.meshgrid(angles, depths)  # Create grid for angles and depths
    contour = ax.contourf(X, Y, corrected_height, cmap='viridis')
    
    cbar = plt.colorbar(contour)
    cbar.set_label('Corrected Wave Height')

    ax.set_xlabel('Incident Angle (radians)')

    ax.set_ylabel('Water Depth (m)')

    ax.set_title('Corrected Wave Height vs Incident Angle and Water Depth') 

    ax.grid(True)

    plt.show()

corrected_wave_height_with_modified_factor(8 ,10 ,8 ,0.1,0.1)