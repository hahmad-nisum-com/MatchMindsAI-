const express = require("express");
const path = require("path");
const multer = require("multer");
const router = express.Router();

// Configure Multer for file upload
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, "uploads/cvs/"); // Directory where the CVs will be saved
  },
  filename: (req, file, cb) => {
    const fileExtension = path.extname(file.originalname); // Get the file extension
    cb(null, Date.now() + fileExtension); // Filename with timestamp to ensure uniqueness
  },
});

const upload = multer({ storage: storage });
const candidateController = require("../controllers/candidateController");

// Route to upload a candidate's CV
router.post("/upload", upload.single("file"), candidateController.uploadCv);

// Route to get all candidates
router.get("/", candidateController.getCandidates);

module.exports = router;
