const pool = require("../config/db");
// Save candidate information including the CV path
const saveCandidate = async (cvPath) => {
  const query =
    "INSERT INTO candidates ( cv_path) VALUES ($1) RETURNING id,  cv_path";
  const values = [cvPath];

  try {
    const result = await pool.query(query, values);
    return result.rows[0];
  } catch (error) {
    console.error("Error saving candidate:", error);
    throw error;
  }
};

// Get all candidates
const getAllCandidates = async () => {
  const query = "SELECT * FROM candidates";
  try {
    const result = await pool.query(query);
    return result.rows;
  } catch (error) {
    console.error("Error fetching candidates:", error);
    throw error;
  }
};

module.exports = {
  saveCandidate,
  getAllCandidates,
};
