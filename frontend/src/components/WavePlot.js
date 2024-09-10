import React from "react";

const WavePlot = (props) => {
  const { resultData, setPlotClicked } = props;
  const handlePlotBack = () => {
    setPlotClicked(false);
  };

  const plotsData = resultData.plots || [];

  return (
    <div className="container mt-5">
      <h2 className="text-center text-primary">Plots</h2>
      <div className="accordion" id="accordionExample">
        {plotsData.map((plot, index) => (
          <div className="accordion-item" key={index}>
            <h2 className="accordion-header" id={`heading${index}`}>
              <button
                className={`accordion-button ${index !== 0 ? "collapsed" : ""}`}
                type="button"
                data-bs-toggle="collapse"
                data-bs-target={`#collapse${index}`}
                aria-expanded={index === 0 ? "true" : "false"}
                aria-controls={`collapse${index}`}
              >
                {plot[1].replace("_", " ").toUpperCase()}
              </button>
            </h2>
            <div
              id={`collapse${index}`}
              className={`accordion-collapse collapse ${
                index === 0 ? "show" : ""
              }`}
              aria-labelledby={`heading${index}`}
              data-bs-parent="#accordionExample"
            >
              <div className="accordion-body">
                <div className="mt-3">
                  <strong>{plot[1].replace("_", " ").toUpperCase()}:</strong>
                  <img
                    src={`data:image/png;base64,${plot[0]}`}
                    alt={plot[1]}
                    className="img-fluid mt-2"
                  />
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
      <button
        type="button"
        className="btn btn-primary mt-3"
        onClick={handlePlotBack}
      >
        Back
      </button>
    </div>
  );
};

export default WavePlot;
