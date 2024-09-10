import React from "react";

const ResultDisplay = ({ resultData, setCheckSubmission }) => {
  return (
    <div className="container mt-5">
      <h2 className="text-center text-primary">Result</h2>
      <div className="accordion" id="accordionExample">
        <div className="accordion-item">
          <h2 className="accordion-header" id="heading0">
            <button
              className="accordion-button"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#collapse0"
              aria-expanded="true"
              aria-controls="collapse0"
            >
              WAVE LENGTH
            </button>
          </h2>
          <div
            id="collapse0"
            className="accordion-collapse collapse show"
            aria-labelledby="heading0"
            data-bs-parent="#accordionExample"
          >
            <div className="accordion-body">
              <strong>Wave Length (λ):</strong> {resultData.wave_length} m
            </div>
          </div>
        </div>

        <div className="accordion-item">
          <h2 className="accordion-header" id="heading1">
            <button
              className="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#collapse1"
              aria-expanded="false"
              aria-controls="collapse1"
            >
              WAVE TYPE
            </button>
          </h2>
          <div
            id="collapse1"
            className="accordion-collapse collapse"
            aria-labelledby="heading1"
            data-bs-parent="#accordionExample"
          >
            <div className="accordion-body">
              <strong>Wave Type:</strong> {resultData.wave_type}
            </div>
          </div>
        </div>

        <div className="accordion-item">
          <h2 className="accordion-header" id="heading2">
            <button
              className="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#collapse2"
              aria-expanded="false"
              aria-controls="collapse2"
            >
              PHASE SPEED
            </button>
          </h2>
          <div
            id="collapse2"
            className="accordion-collapse collapse"
            aria-labelledby="heading2"
            data-bs-parent="#accordionExample"
          >
            <div className="accordion-body">
              <strong>Phase Speed (c):</strong> {resultData.phase_speed} m/s
            </div>
          </div>
        </div>

        <div className="accordion-item">
          <h2 className="accordion-header" id="heading3">
            <button
              className="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#collapse3"
              aria-expanded="false"
              aria-controls="collapse3"
            >
              WAVE NUMBER
            </button>
          </h2>
          <div
            id="collapse3"
            className="accordion-collapse collapse"
            aria-labelledby="heading3"
            data-bs-parent="#accordionExample"
          >
            <div className="accordion-body">
              <strong>Wave Number (k):</strong> {resultData.wave_number} rad/m
            </div>
          </div>
        </div>

        <div className="accordion-item">
          <h2 className="accordion-header" id="heading4">
            <button
              className="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#collapse4"
              aria-expanded="false"
              aria-controls="collapse4"
            >
              TOTAL ENERGY
            </button>
          </h2>
          <div
            id="collapse4"
            className="accordion-collapse collapse"
            aria-labelledby="heading4"
            data-bs-parent="#accordionExample"
          >
            <div className="accordion-body">
              <strong>Total Energy (E):</strong> {resultData.total_energy} J
            </div>
          </div>
        </div>

        <div className="accordion-item">
          <h2 className="accordion-header" id="heading5">
            <button
              className="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#collapse5"
              aria-expanded="false"
              aria-controls="collapse5"
            >
              GROUP SPEED
            </button>
          </h2>
          <div
            id="collapse5"
            className="accordion-collapse collapse"
            aria-labelledby="heading5"
            data-bs-parent="#accordionExample"
          >
            <div className="accordion-body">
              <strong>Group Speed (cg):</strong> {resultData.group_speed} m/s
            </div>
          </div>
        </div>

        <div className="accordion-item">
          <h2 className="accordion-header" id="heading6">
            <button
              className="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#collapse6"
              aria-expanded="false"
              aria-controls="collapse6"
            >
              TOTAL POWER
            </button>
          </h2>
          <div
            id="collapse6"
            className="accordion-collapse collapse"
            aria-labelledby="heading6"
            data-bs-parent="#accordionExample"
          >
            <div className="accordion-body">
              <strong>Total Power (P):</strong> {resultData.total_power} W
            </div>
          </div>
        </div>

        <div className="accordion-item">
          <h2 className="accordion-header" id="heading7">
            <button
              className="accordion-button collapsed"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#collapse7"
              aria-expanded="false"
              aria-controls="collapse7"
            >
              SIGNIFICANT WAVE HEIGHT
            </button>
          </h2>
          <div
            id="collapse7"
            className="accordion-collapse collapse"
            aria-labelledby="heading7"
            data-bs-parent="#accordionExample"
          >
            <div className="accordion-body">
              <strong>Significant Wave Height (Hs):</strong>{" "}
              {resultData.significant_wave_height} m
            </div>
          </div>
        </div>
      </div>
      <button
        type="button"
        className="btn btn-primary mt-3"
        onClick={() => setCheckSubmission(false)}
      >
        Back
      </button>
    </div>
  );
};

export default ResultDisplay;
