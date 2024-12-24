// NavbarComponent.js
import React from "react";
import { Navbar, Dropdown, Avatar } from "flowbite-react";
import { Link } from "react-router-dom"; // Import Link for internal navigation

function NavbarComponent() {
  return (
    <Navbar fluid rounded>
      <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">
        Ai-Platform
      </span>

      <div className="flex md:order-2">
        {/* User Dropdown */}
        <Dropdown
          arrowIcon={false}
          inline
          label={
            <Avatar
              alt="User settings"
              img="https://flowbite.com/docs/images/people/profile-picture-5.jpg"
              rounded
            />
          }
        >
          <Dropdown.Header>
            <span className="block text-sm">Bonnie Green</span>
            <span className="block truncate text-sm font-medium">
              name@flowbite.com
            </span>
          </Dropdown.Header>
          <Dropdown.Divider />
          <Dropdown.Item>Sign out</Dropdown.Item>
        </Dropdown>
        {/* Toggle button for Navbar Collapse */}
        <Navbar.Toggle />
      </div>

      {/* Navbar links - Using Link for navigation */}
      <Navbar.Collapse hidden={"false"}>
        <Link to="/" className="text-gray-900 hover:text-blue-600">
          Home
        </Link>
        <Link to="/dashboard" className="text-gray-900 hover:text-blue-600">
          Dashboard
        </Link>
      </Navbar.Collapse>
    </Navbar>
  );
}

export default NavbarComponent;
