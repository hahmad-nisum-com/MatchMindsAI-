import { useState, useEffect } from "react";
import { Alert } from "flowbite-react";

const useAlert = () => {
  const [alertVisible, setAlertVisible] = useState(false);
  const [alertMessage, setAlertMessage] = useState("");
  const [alertType, setAlertType] = useState("success"); // success | error | info

  // Function to show alert and dismiss after a delay
  const showAlert = (message, type = "success", duration = 5000) => {
    setAlertMessage(message);
    setAlertType(type);
    setAlertVisible(true);

    // Automatically hide alert after `duration` milliseconds
    setTimeout(() => {
      setAlertVisible(false);
    }, duration);
  };

  const hideAlert = () => {
    setAlertVisible(false);
  };

  // Component to render the Alert
  const AlertComponent = () =>
    alertVisible && (
      <Alert
        color={alertType}
        onClose={hideAlert} // This dismisses the alert when clicked
        className="mb-4"
      >
        <span className="font-medium">{alertMessage}</span>
      </Alert>
    );

  return { showAlert, AlertComponent };
};

export default useAlert;
