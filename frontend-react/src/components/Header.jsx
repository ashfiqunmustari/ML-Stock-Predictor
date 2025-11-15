import React from "react";

const Header = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark align-items-start" style={{ backgroundColor: "#0d1b2a", padding: "0.8rem 2rem" }}>
      <a className="navbar-brand fw-bold" href="#">
        Stock Predictor
      </a>
      <div className="ms-auto d-flex gap-3">
        <a className="btn btn-outline-light" href="#">Sign In</a>
        <a className="btn btn-info" href="#">Sign Up</a>
      </div>
    </nav>
  );
};

export default Header;
