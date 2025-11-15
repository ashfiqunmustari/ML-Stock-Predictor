import React from "react";

const Main = () => {
  return (
    <div className="d-flex flex-column justify-content-center align-items-center" style={{ flex: 1, padding: "3rem 1rem", backgroundColor: "#0d1b2a" }}>
      <div className="p-5 rounded text-center" style={{ backgroundColor: "#1f2a44", color: "#fff", maxWidth: "600px", width: "100%" }}>
        <h1 className="mb-3">Stock Predictor</h1>
        <p className="lead mb-4">Predict market trends with ease! Our Stock Predictor analyzes historical data and patterns to give you insights, helping you make smarter investment decisions.</p>
        <a className="btn btn-outline-info" href="#">Sign In</a>
      </div>
    </div>
  );
};

export default Main;
