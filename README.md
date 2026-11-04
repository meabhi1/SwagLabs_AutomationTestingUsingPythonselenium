Swag Labs Automation Testing Using Python & Selenium

!Python !Selenium !Pytest !Automation

📌 Project Overview

This project is an automated web application testing framework developed using Python, Selenium WebDriver, and Pytest to automate testing of the Swag Labs (SauceDemo) e-commerce application.

The framework follows the Page Object Model (POM) design pattern to maintain reusable, modular, and maintainable automation scripts.

It includes browser configuration, reusable Pytest fixtures, automated login setup, cart-related operations, external test data files, and test execution artifacts.

Application Under Test: https://www.saucedemo.com/

🎯 Project Objectives
Automate web application testing using Selenium WebDriver.
Implement the Page Object Model (POM) design pattern.
Organize test scripts using Pytest.
Create reusable browser and test setup fixtures.
Support Firefox and Microsoft Edge browsers.
Separate page locators and application interactions from test cases.
Maintain external test data using Excel and YAML files.
Organize test execution reports, screenshots, and logs.
🛠️ Technology Stack
Technology	Purpose
Python	Programming language
Selenium WebDriver	Browser automation
Pytest	Test execution and test management
Pytest HTML	HTML test reporting dependency
Pandas	Test data handling
OpenPyXL	Excel file handling
PyYAML	YAML test data handling
Firefox	Browser execution
Microsoft Edge	Browser execution
🏗️ Framework Architecture

This project uses the Page Object Model (POM) architecture.

The framework separates test execution, browser configuration, page interactions, and test data.

Project Structure
text
SwagLabs_AutomationTestingUsingPythonselenium/
│
├── Reports/
│   └── Test execution reports
│
├── Screenshots/
│   └── Captured screenshots
│
├── logs/
│   └── Execution logs
│
├── pages/
│   ├── Login_page.py
│   └── Cart_Page.py
│
├── testcase/
│   └── Automated test cases
│
├── conftest.py
│   └── Pytest fixtures and browser configuration
│
├── requirement.txt
│   └── Project dependencies
│
├── test_data.xlsx
│   └── Excel test data
│
├── test_yaml.yaml
│   └── YAML test data
│
├── .gitignore
│
└── README.md

⚙️ Framework Implementation
1. Page Object Model (POM)

The framework uses separate page classes to manage application interactions.

Login_page.py – Handles login page operations.
Cart_Page.py – Handles product and shopping cart operations.

This approach improves code reusability and makes maintenance easier.

2. Pytest Configuration

The conftest.py file contains reusable fixtures and browser configuration.

Implemented fixtures include:

setup – Initializes and closes the browser.
browser – Accepts the browser selection from the command line.
logged_in – Opens the SauceDemo application and performs login using the standard test account.
cartproductadded – Adds a product to the cart and opens the cart page.
3. Browser Support

The framework currently includes browser setup for:

Mozilla Firefox
Microsoft Edge

Browser selection is controlled through the --browse command-line option.

4. Test Data Management

The repository includes external test data files:

test_data.xlsx – Excel-based test data.
test_yaml.yaml – YAML-based test data.

The dependencies include Pandas, OpenPyXL, and PyYAML for working with external test data.

🚀 Installation and Setup
Prerequisites

Make sure the following are installed:

Python 3.x
pip
Mozilla Firefox or Microsoft Edge
Git
Compatible browser drivers or Selenium-supported driver management
Step 1: Clone the Repository
bash
git clone https://github.com/meabhi1/SwagLabs_AutomationTestingUsingPythonselenium.git

Step 2: Navigate to the Project
bash
cd SwagLabs_AutomationTestingUsingPythonselenium

Step 3: Create a Virtual Environment
bash
python -m venv venv


Activate the environment:

Windows:

bash
venv\Scripts\activate


macOS/Linux:

bash
source venv/bin/activate

Step 4: Install Dependencies
bash
pip install -r requirement.txt

▶️ Test Execution

Run the complete Pytest suite:

bash
pytest -v

Execute Tests in Firefox
bash
pytest -v --browse=firefox

Execute Tests in Microsoft Edge
bash
pytest -v --browse=edge

Execute a Specific Test File
bash
pytest -v testcase/<test_file_name>.py


Replace <test_file_name> with the actual test file name present in the testcase directory.

📊 Reports, Screenshots and Logs

The project maintains separate directories for execution artifacts:

Directory	Description
Reports/	Test execution reports
Screenshots/	Screenshots captured during testing
logs/	Execution logs

The project includes pytest-html as a reporting dependency.

🔍 Key Features
Python-based browser automation.
Selenium WebDriver integration.
Pytest-based test execution.
Page Object Model architecture.
Reusable browser setup and teardown.
Firefox and Edge browser configuration.
Reusable login and cart setup fixtures.
Excel and YAML test data files.
Separate folders for reports, screenshots, and logs.
🌐 Application Under Test

Swag Labs / SauceDemo

https://www.saucedemo.com/

The application provides an e-commerce environment suitable for practicing UI automation and validating shopping workflows.

📌 Future Enhancements
Add cross-browser execution through automated test pipelines.
Integrate Jenkins or GitHub Actions for CI/CD.
Implement automatic screenshot capture on test failures.
Improve structured logging and failure diagnostics.
Add data-driven test execution for multiple test scenarios.
Generate detailed HTML execution reports.
Add explicit assertions for checkout and order workflows.
👨‍💻 Author

Abhi

GitHub: https://github.com/meabhi1

⭐ Support

If you find this project useful, consider giving the repository a star!

This project is intended for learning and demonstrating web application test automation using Python, Selenium WebDriver, and Pytest.
