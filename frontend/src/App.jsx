import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Dashboard from "./views/dashboard";
import Home from "./views/home";
import NavbarComponent from "./components/sys_navbar";

function App() {
  return (
    <Router>
      <NavbarComponent />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />{" "}
      </Routes>
    </Router>
  );
}

export default App;
