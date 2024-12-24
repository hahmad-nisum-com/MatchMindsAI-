const express = require("express");
const app = express();
const candidateRoutes = require("./routes/candidateRoutes");
const path = require("path");

// Middleware to parse JSON request body
app.use(express.json());

// Serve uploaded CVs as static files
app.use("/uploads", express.static(path.join(__dirname, "uploads")));

// Use candidate routes
app.use("/api/candidates", candidateRoutes);

// Start the server
const PORT = process.env.PORT || 3009;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
