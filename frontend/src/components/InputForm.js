import React, { useState } from "react";
import { result_display } from "../apis/api";
import ResultDisplay from "./ResultDisplay";
import WavePlot from "./WavePlot";
const InputForm = () => {
  const [formData, setFormData] = useState({
    wavePeriod: "",
    waterDepth: "",
    waveHeight: "",
    waveTheory: "linear",
  });
  const [checkSubmission, setCheckSubmission] = useState(false);
  const [plotClicked, setPlotClicked] = useState(false);
  const [plotCollected, setPlotCollected] = useState(false);
  const [resultData, setResultData] = useState({
    wave_length: null,
    wave_number: null,
    phase_speed: null,
    group_speed: null,
    total_energy: null,
    total_power: null,
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    await handleCalculate();
  };

  const handlePlot = () => {
    setPlotClicked(true);
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleReset = () => {
    setFormData({
      wavePeriod: "",
      waterDepth: "",
      waveHeight: "",
      waveTheory: "linear",
    });
    setCheckSubmission(false);
    setPlotCollected(false);
  };

  const handleCalculate = async () => {
    const calculated_data = await result_display({
      wave_period: formData.wavePeriod,
      water_depth: formData.waterDepth,
      wave_height: formData.waveHeight,
      wave_theory: formData.waveTheory,
    });
    if (calculated_data.status_message === "success") {
      console.log(calculated_data.result);
      setCheckSubmission(true);
      setPlotCollected(true);
      setResultData((prevData) => ({ ...prevData, ...calculated_data.result }));
    } else {
      console.error("Error:", calculated_data.error);
    }
  };

  return !checkSubmission && !plotClicked ? (
    <div className="container mt-5">
      <h3 className="text-center text-primary">Wave Theory Calculator</h3>
      <form onSubmit={handleSubmit} method="POST">
        <div className="form-group">
          <label>Wave Period(in s):</label>
          <input
            type="float"
            name="wavePeriod"
            className="form-control"
            value={formData.wavePeriod}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Water Depth(in m):</label>
          <input
            type="float"
            name="waterDepth"
            className="form-control"
            value={formData.waterDepth}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Wave Height(in m):</label>
          <input
            type="float"
            name="waveHeight"
            className="form-control"
            value={formData.waveHeight}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Wave Theory:</label>
          <select
            name="waveTheory"
            className="form-control"
            value={formData.waveTheory}
            onChange={handleChange}
          >
            <option value="linear">Linear</option>
            <option value="nonlinear">Nonlinear</option>
          </select>
        </div>
        <div className="form-group mt-4">
          <button type="submit" className="btn btn-primary mr-3">
            Calculate
          </button>

          <button
            type="button"
            className="btn btn-secondary"
            onClick={handleReset}
          >
            Reset
          </button>
          <button
            type="button"
            className="btn btn-primary"
            disabled={!plotCollected}
            onClick={handlePlot}
          >
            Plot
          </button>
        </div>
      </form>
    </div>
  ) : !plotClicked ? (
    <ResultDisplay
      setCheckSubmission={setCheckSubmission}
      resultData={resultData}
    />
  ) : (
    <WavePlot resultData={resultData} setPlotClicked={setPlotClicked} />
  );
};

export default InputForm;
