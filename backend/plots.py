import matplotlib.pyplot as plt
from calculations import  wavelength_calculation , determine_wave_type , evaluate_group_speed , energy_density
from math import cos, pi , sin , cosh , sinh
import numpy as np


def wave_displacement_vs_x_plot(wave_height, wave_period, water_depth, time=0, z=0):
    z = water_depth / 2
    # Compute the wave displacement at each x value
    corrected_wavelength = wavelength_calculation(water_depth, wave_period)

    wave_number = 2 * np.pi / corrected_wavelength
    omega = 2 * np.pi / wave_period  # Compute angular frequency

    x = np.linspace(0, 2 * corrected_wavelength, 1000)

    delta_x = wave_height / 2 * (np.cosh(wave_number * (z + water_depth)) / np.sinh(wave_number * water_depth))
    delta_x = delta_x * np.cos(wave_number * x - omega * time)


    # Plot the wave displacement versus x
    fig, ax = plt.subplots()
    ax.plot(x, delta_x)
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Wave Displacement (m)")
    ax.set_title("Wave Displacement vs Distance")
    ax.grid(True)

    return fig

def horizontal_wave_vs_time_plot(wave_height, wave_period, water_depth, wave_number, x=0, z=0):
    # Constants
    g = 9.81  # acceleration due to gravity in m/s^2

    # Compute angular frequency (σ) from the wave period (T)
    omega = 2 * np.pi / wave_period

    # Define time array for plotting (from 0 to one full period)
    time = np.linspace(0, 2*wave_period, 1000)

    # Compute sinh(kd) and cosh(k(d+z)) for the velocity formula
    sinh_kd = np.sinh(wave_number * water_depth)
    cosh_kdz = np.cosh(wave_number * (water_depth + z))

    # Calculate the horizontal velocity at each time step using the given formula
    u = (np.pi * wave_height / wave_period) * (cosh_kdz / sinh_kd) * np.cos(wave_number * x - omega * time)

    # Plot the horizontal velocity versus time
    fig, ax = plt.subplots()
    ax.plot(time, u)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Horizontal Velocity (m/s)")
    ax.legend()
    ax.grid(True)

    return fig



def vertical_wave_vs_time_plot(wave_height, wave_period, water_depth, wave_number, x=0, z=0):
    # Constants
    g = 9.81  

    # Compute angular frequency (σ) from the wave period (T)
    omega = 2 * np.pi / wave_period

    # Define time array for plotting (from 0 to one full period)
    time = np.linspace(0, 2*wave_period, 1000)

    # Compute sinh(kd) and sinh(k(d+z)) for the velocity formula
    sinh_kd = np.sinh(wave_number * water_depth)
    sinh_kdz = np.sinh(wave_number * (water_depth + z))

    # Calculate the vertical velocity at each time step
    w = (-np.pi * wave_height / wave_period) * (sinh_kdz / sinh_kd) * np.sin(wave_number * x - omega * time)

    # Plot the velocity versus time
    fig, ax = plt.subplots()
    ax.plot(time, w)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Vertical Velocity (m/s)")
    ax.grid(True)

    return fig


def wave_velocity_vs_time_plot(wave_height, wave_period, water_depth, wave_number, x=0, z=0):
    # Constants
    g = 9.81  # acceleration due to gravity in m/s^2

    # Compute angular frequency (σ) from the wave period (T)
    omega = 2 * np.pi / wave_period

    # Define time array for plotting (from 0 to one full period)
    time = np.linspace(0, 2 * wave_period, 1000)

    # Compute sinh(kd) and cosh(k(d+z)) for horizontal velocity
    sinh_kd = np.sinh(wave_number * water_depth)
    cosh_kdz = np.cosh(wave_number * (water_depth + z))

    # Compute horizontal velocity (u)
    u = (np.pi * wave_height / wave_period) * (cosh_kdz / sinh_kd) * np.cos(wave_number * x - omega * time)

    # Compute sinh(k(d+z)) for vertical velocity
    sinh_kdz = np.sinh(wave_number * (water_depth + z))

    # Compute vertical velocity (w)
    w = (-np.pi * wave_height / wave_period) * (sinh_kdz / sinh_kd) * np.sin(wave_number * x - omega * time)

    # Create the combined plot
    fig, ax = plt.subplots()
    
    # Plot horizontal velocity
    ax.plot(time, u, label="Horizontal Velocity (u)", color='b')
    
    # Plot vertical velocity
    ax.plot(time, w, label="Vertical Velocity (w)", color='r')

    # Set labels and title
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Velocity (m/s)")
    ax.set_title("Horizontal and Vertical Wave Velocities vs Time")
    ax.legend(loc='upper right')
    ax.grid(True)

    return fig



def wave_acceleration_vs_time_plot(wave_height, wave_period, water_depth, wave_number, x=0, z=0):
    # Constants
    g = 9.81  # acceleration due to gravity in m/s^2

    # Compute angular frequency (σ) from the wave period (T)
    omega = 2 * np.pi / wave_period

    # Define time array for plotting (from 0 to two full periods)
    time = np.linspace(0, 2 * wave_period, 1000)

    # Compute sinh(kd) and cosh(k(d+z)) for horizontal acceleration
    sinh_kd = np.sinh(wave_number * water_depth)
    cosh_kdz = np.cosh(wave_number * (water_depth + z))

    # Horizontal acceleration (ü)
    u_dot_dot = (-2 * np.pi**2 * wave_height / wave_period**2) * (cosh_kdz / sinh_kd) * np.cos(wave_number * x - omega * time)

    # Compute sinh(k(d+z)) for vertical acceleration
    sinh_kdz = np.sinh(wave_number * (water_depth + z))

    # Vertical acceleration (ẅ)
    w_dot_dot = (-2 * np.pi**2 * wave_height / wave_period**2) * (sinh_kdz / sinh_kd) * np.sin(wave_number * x - omega * time)

    # Create the combined plot for accelerations
    fig, ax = plt.subplots()

    # Plot horizontal acceleration
    ax.plot(time, u_dot_dot, label="Horizontal Acceleration (ü)", color='b')

    # Plot vertical acceleration
    ax.plot(time, w_dot_dot, label="Vertical Acceleration (ẅ)", color='r')

    # Set labels and title
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Acceleration (m/s²)")
    ax.set_title("Horizontal and Vertical Wave Accelerations vs Time")
    ax.legend(loc='upper right')
    ax.grid(True)

    return fig



def shoaling_coefficient_vs_water_depth_plot(water_depth, wave_period, step_size=0.1, min_depth=0.1):
    # Compute angular frequency (omega) from the wave period (T)

    omega = 2 * np.pi / wave_period

    # Define range of depths from initial_depth to min_depth with step_size
    depths = np.arange(water_depth, min_depth, -step_size)

    # Initialize lists for d/L and shoaling coefficient
    d_over_L = []
    shoaling_coefficients = []

    deep_water_celerity = (9.81 * wave_period  / (2 * pi))

    # Calculate for each depth in the range
    for d in depths:
        # Calculate wavelength using the corrected_wavelength function
        L = wavelength_calculation(d, wave_period)
        
        # Calculate d/L
        d_over_L.append(d / L)

        # Calculate shoaling coefficient
        wave_type = determine_wave_type(d, L)
        group_speed = evaluate_group_speed(wave_period , d ,wave_type , L / wave_period , 2 * pi / L)
        shoaling_coefficients.append(((deep_water_celerity* 0.5)/group_speed)**0.5)


    # Create the plot
    fig, ax = plt.subplots()

    # Plot d/L
    ax.plot(depths, d_over_L, label='d/L', color='b')

    # Plot shoaling coefficient
    ax.plot(depths, shoaling_coefficients, label='Shoaling Coefficient', color='orange')

    # Set labels and title
    ax.set_xlabel('Water Depth (m)')
    ax.set_ylabel('Shoaling Coefficient(ks)')
    ax.set_title('Variation of d/L and Shoaling Coefficient with Water Depth')
    ax.legend(loc='upper right')
    ax.grid(True)

    return fig


def corrected_height_due_to_shoaling_vs_water_depth(water_depth ,wave_height , wave_period ,step_size = 0.1 , min_depth = 0.1):
    # Define range of depths from initial_depth to min_depth with step_size
    depths = np.arange(water_depth, min_depth, -step_size)

    # Initialize lists for d/L and shoaling coefficient
    d_over_L = []
    shoaling_coefficients = []

    deep_water_celerity = (9.81 * wave_period / (2 * pi))

    # Calculate for each depth in the range
    # Define range of depths from initial_depth to min_depth with step_size
    depths = np.arange(water_depth, min_depth, -step_size)

    # Initialize lists for d/L and shoaling coefficient
    d_over_L = []
    shoaling_coefficients = []

    deep_water_celerity = (9.81 * wave_period ** 2 / (2 * pi)) ** 0.5

    # Calculate for each depth in the range
    for d in depths:
        # Calculate wavelength using the corrected_wavelength function
        L = wavelength_calculation(d, wave_period)
        
        # Calculate d/L
        d_over_L.append(d / L)

        # Calculate shoaling coefficient
        wave_type = determine_wave_type(d, L)
        group_speed = evaluate_group_speed(wave_period , d ,wave_type , L / wave_period , 2 * pi / L)
        shoaling_coefficients.append(((deep_water_celerity* 0.5)/group_speed)**0.5)


    # Calculate the corrected wave height
    deep_water_wave_height = wave_height / shoaling_coefficients[0]

    corrected_wave_heights = [shoaling_coefficients[i] * deep_water_wave_height for i in range(len(depths))]    

    # Create the plot
    fig, ax = plt.subplots()

    # Plot d/L
    ax.plot(depths, d_over_L, label='d/L', color='b')

    # Plot corrected wave height
    ax.plot(depths, corrected_wave_heights, label='Corrected Wave Height', color='orange')

    # Set labels and title
    ax.set_xlabel('Water Depth (m)')
    ax.set_ylabel('Corrected Wave Height (m)')
    ax.set_title('Variation of d/L and Corrected Wave Height with Water Depth')
    ax.legend(loc='upper right')
    ax.grid(True)

    return fig


def refraction_coefficient_vs_angle_plot(water_depth , wave_period , step_size=0.1 , min_depth = 0.1):
    # Define depth range and incident angles
    depths = np.arange(water_depth, min_depth, -step_size)

    angles = np.linspace(0, np.pi / 2, 100)

    refraction_coefficients = []
     
    for depth in depths:
        wave_length = wavelength_calculation(depth, wave_period)
        wave_celerity = wave_length / wave_period
        deep_water_celerity = (9.81 * wave_period  / (2 * pi))

        temp_refraction_coeffs = []
        for theta in angles:
            alpha = np.arcsin((wave_celerity / deep_water_celerity) * np.sin(theta))*(pi/180)
            refraction_coefficient = (np.cos(theta) / np.cos(alpha))**0.5
            temp_refraction_coeffs.append(refraction_coefficient)
        refraction_coefficients.append(temp_refraction_coeffs) 

    refraction_coefficients = np.array(refraction_coefficients)

    # Create a contour plot (2D)

    fig, ax = plt.subplots()
    X, Y = np.meshgrid(angles, depths)  # Create grid for angles and depths
    contour = ax.contourf(X, Y, refraction_coefficients, cmap='viridis')

    cbar = plt.colorbar(contour)
    cbar.set_label('Refraction Coefficient(Kr)')

    ax.set_xlabel('Incident Angle (radians)')
    ax.set_ylabel('Water Depth (m)')
    ax.set_title('Refraction Coefficient vs Incident Angle and Water Depth')
    ax.grid(True)
    return fig



def shoaling_plus_refraction_effect(water_depth, wave_period ,step_size = 0.1 , min_depth = 0.1):
    
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

    fig, ax = plt.subplots()
    X, Y = np.meshgrid(angles, depths)  # Create grid for angles and depths
    contour = ax.contourf(X, Y, modified_factor, cmap='viridis')

    cbar = plt.colorbar(contour)
    cbar.set_label('Modified Factor')

    ax.set_xlabel('Incident Angle (radians)')
    ax.set_ylabel('Water Depth (m)')
    ax.set_title('Modified Factor(ks*kr) vs Incident Angle and Water Depth')
    ax.grid(True)
    return fig


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
    cbar.set_label('Corrected Wave Height using ks and kr')

    ax.set_xlabel('Incident Angle (radians)')

    ax.set_ylabel('Water Depth (m)')

    ax.set_title('Corrected Wave Height vs Incident Angle and Water Depth') 

    ax.grid(True)

    return fig






  
    



