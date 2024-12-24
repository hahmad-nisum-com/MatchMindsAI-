import { FileInput, Label } from "flowbite-react";
import { useState } from "react";
import axios from "axios";
import useAlert from "../hooks/useAlert";

const FileUploader = () => {
  const { showAlert, AlertComponent } = useAlert(); // Destructure the utility functions

  const handleFileChange = (e) => {
    // Create a FormData object
    const formData = new FormData();
    formData.append("file", e.target.files[0]); // 'file' is the key the server expects

    // Send the form data with the file to the backend
    axios
      .post("http://localhost:5001/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data", // This is the required header for file uploads
        },
      })
      .then((response) => {
        showAlert("Data uploaded successfully!", "success");
        console.log("File uploaded successfully:", response.data);
      })
      .catch((error) => {
        console.error("Error uploading file:", error);
      });
  };
  return (
    <div className="flex justify-center items-center ">
      <div className="max-w-[500px] w-full">
        <div className="mb-4">
          <Label htmlFor="file-upload-helper-text" value="Upload CV/Resume" />
        </div>
        <FileInput
          id="file-upload-helper-text"
          helperText="docx,pdf"
          onChange={handleFileChange}
        />
        <AlertComponent />
      </div>
    </div>
  );
};

export default FileUploader;
