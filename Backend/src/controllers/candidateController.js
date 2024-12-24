const path = require("path");

const candidateModel = require("../models/candidateModel");
const { sendFileToPythonAPI } = require("../services/python_data_service");

const uploadCv = async (req, res) => {
  const cvPath = `/uploads/cvs/${req.file.filename}`; // Store the relative path of the CV
  try {
    const user_data = await sendFileToPythonAPI(cvPath);
    const newCandidate = await candidateModel.saveCandidate(cvPath);
    res.status(201).json({
      message: "Candidate uploaded successfully",
      candidate: newCandidate,
      userdata: user_data,
    });
  } catch (error) {
    res.status(500).json({ error: "Database error", details: error.message });
  }
};

// Controller method for fetching all candidates
const getCandidates = async (req, res) => {
  try {
    const candidates = await candidateModel.getAllCandidates();
    res.status(200).json({ candidates });
  } catch (error) {
    res.status(500).json({ error: "Database error", details: error.message });
  }
};

module.exports = {
  uploadCv,
  getCandidates,
};
