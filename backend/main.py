from flask import Flask ,request , jsonify
import json
# import psycopg2
import pandas as pd
import io
import base64
from flask_cors import CORS
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from calculations import wavelength_calculation , determine_wave_type , evaluate_group_speed , energy_density
from math import pi
from plots import wave_displacement_vs_x_plot, wave_velocity_vs_time_plot , wave_acceleration_vs_time_plot,shoaling_coefficient_vs_water_depth_plot,corrected_height_due_to_shoaling_vs_water_depth , refraction_coefficient_vs_angle_plot,shoaling_plus_refraction_effect , corrected_wave_height_with_modified_factor

# No connection to Database ,, we are just testing the API ,, see in the output in React UI 


app = Flask(__name__)
CORS(app)

def encode_plot_to_base64(fig):
    """Helper function to encode a matplotlib figure to base64."""
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    output.seek(0)
    return base64.b64encode(output.getvalue()).decode('utf-8')

@app.route("/result_display" , methods = ['POST'])   
def result():
   data = request.json
   
   wave_period = float(data['wave_period'])
   water_depth = float(data['water_depth'])
   wave_height = float(data['wave_height'])
   wave_theory = data['wave_theory']
   
   # wave properties calculation
   wave_length = wavelength_calculation(water_depth , wave_period)
   wave_type = determine_wave_type(water_depth , wave_length)
   wave_celerity = wave_length / wave_period
   wave_number = 2 * pi / wave_length
  

  # Further calculations
   group_speed = evaluate_group_speed (wave_period, water_depth ,wave_type, wave_celerity , wave_number)
   total_energy = energy_density(wave_height)
   total_power =  total_energy * group_speed
   

   ##  Wave Plots


   plots = []
   # Displacement at t=0 , z=0 
   displacement_at_t0_z0 = wave_displacement_vs_x_plot(wave_height, wave_period, water_depth, time=0, z=0)
   displacement_at_t0_z0 = encode_plot_to_base64(displacement_at_t0_z0)
   plots.append([displacement_at_t0_z0 , "Displacement at t=0 , z=0"])
   
   # wave velocity vs time plot
   combined_wave_velocity_vs_time_plot = wave_velocity_vs_time_plot(wave_height, wave_period, water_depth, wave_number, 0, 0)
   combined_wave_velocity_vs_time_plot = encode_plot_to_base64(combined_wave_velocity_vs_time_plot)

   plots.append([combined_wave_velocity_vs_time_plot , "Wave Velocity vs Time"])

   # acceleration vs time plot 

   wave_acceleration_vs_time = wave_acceleration_vs_time_plot(wave_height, wave_period, water_depth, wave_number, 0, 0)
   wave_acceleration_vs_time = encode_plot_to_base64(wave_acceleration_vs_time)
   plots.append([wave_acceleration_vs_time ,"Wave Acceleration vs Time"])
   


   ## wave transformations

   # Shoaling Coefficient vs Depth Plot
   
   shoaling_coefficient_vs_water_depth = shoaling_coefficient_vs_water_depth_plot(water_depth, wave_period, 0.1 ,0.1)
   shoaling_coefficient_vs_water_depth = encode_plot_to_base64(shoaling_coefficient_vs_water_depth)
   
   plots.append([shoaling_coefficient_vs_water_depth , "Shoaling Coefficient vs Water Depth"])

   corrected_wave_height_vs_depth = corrected_height_due_to_shoaling_vs_water_depth(water_depth, wave_height, wave_period, 0.1 ,0.1)
   corrected_wave_height_vs_depth = encode_plot_to_base64(corrected_wave_height_vs_depth)
   plots.append([corrected_wave_height_vs_depth , "Corrected Wave Height vs Water Depth"])


   # Refraction factor vs angle plot 
   refraction_coefficient_vs_angle_vs_water_depth = refraction_coefficient_vs_angle_plot(water_depth, wave_period, 0.1 , 0.1)
   refraction_coefficient_vs_angle_vs_water_depth = encode_plot_to_base64(refraction_coefficient_vs_angle_vs_water_depth)
   plots.append([refraction_coefficient_vs_angle_vs_water_depth , "Refraction Coefficient vs Angle vs Water Depth"])

   # Modified factor vs angle and water depth plot
   modified_factor_vs_angle_and_depth = shoaling_plus_refraction_effect(water_depth, wave_period, 0.1 , 0.1)
   modified_factor_vs_angle_and_depth = encode_plot_to_base64(modified_factor_vs_angle_and_depth)
   plots.append([modified_factor_vs_angle_and_depth , "Modified Factor vs Angle and Water Depth"])

   # modified height using ks and kr vs angle and water depth plot
   modified_height_using_ks_and_kr = corrected_wave_height_with_modified_factor( wave_height,water_depth, wave_period, 0.1 , 0.1)
   modified_height_using_ks_and_kr = encode_plot_to_base64(modified_height_using_ks_and_kr)
   plots.append([modified_height_using_ks_and_kr , "Modified Height using ks and kr vs Angle and Water Depth"])

   # response data
   response_data={
      "status_message": "success",
      "result":{
         "wave_length": wave_length,
            "wave_type": wave_type,
         "phase_speed": wave_celerity, 
         "wave_number": wave_number  ,
         "total_energy": total_energy,
         "group_speed": group_speed,
            "total_power": total_power,
            "significant_wave_height": 1.4 * wave_height,
            "plots": plots

      }
   }
   return jsonify(response_data)

   
if __name__ == '__main__':
  app.run(debug=True, port=5000)