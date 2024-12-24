import axios from "axios";
import FormData from "form-data";
import fs from "fs";
// Function to send file in FormData
export async function sendFileToPythonAPI(filePath) {
  try {
    const form = new FormData();

    // Append file to the FormData object
    form.append("file", fs.createReadStream(`.${filePath}`));

    // Set headers to include the form's boundary for multipart/form-data
    const headers = {
      ...form.getHeaders(),
      "Content-Type": "multipart/form-data",
    };

    // Send POST request to the FastAPI server with file in FormData
    const response = await axios.post("http://127.0.0.1:8000/scrape", form, {
      headers,
    });
    return response.data;
    console.log("Python API Response:", response.data);
  } catch (error) {
    console.error("Error sending file to Python API:", error);
  }
}
