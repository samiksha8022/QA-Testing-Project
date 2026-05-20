# DEMOBLAZE Automation Testing Project 🧪

## 📌 Project Overview
This project contains automated UI testing for the
[Demoblaze](https://www.demoblaze.com) e-commerce website
using Playwright and Pytest framework.

## 🛠️ Technologies Used
- Python
- Playwright
- Pytest
- Page Object Model (POM) Design Pattern

## 📁 Project Structure
playwright/DEMOBLAZE_AUTOMATION/
│
├── Pages/
│   ├── cart_page.py
│   ├── contact_page.py
│   ├── home_page.py
│   ├── login_page.py
│   └── signup_page.py
│
├── Tests/
│   ├── test_cart.py
│   ├── test_contact.py
│   ├── test_home.py
│   ├── test_login.py
│   └── test_signup.py
│
├── utils/
│   ├── base_page.py
│   ├── cart_locators.py
│   ├── helpers.py
│   └── test_data.py
│
└── screenshots/

## ✅ Test Cases Covered
- 🔐 Login Testing (Valid & Invalid)
- 📝 Signup Testing
- 🏠 Home Page Testing
- 🛒 Cart Testing
- 📞 Contact Page Testing

## ▶️ How to Run Tests

# Install dependencies
pip install pytest-playwright
playwright install

# Run all tests
python -m pytest Tests/ -s -v --headed
# Run specific test or # Run with headed browser (visible)
python -m pytest Tests/test_home.py -s -v --headed
python -m pytest Tests/test_login.py -s -v --headed
python -m pytest Tests/test_cart.py -s -v --headed
python -m pytest Tests/test_contact.py -s -v --headed
python -m pytest Tests/test_signup.py -s -v --headed



## 📸 Screenshots
Test execution screenshots are saved in the `screenshots/` folder.

## 👩‍💻 Author
Samiksha
QA Automation Tester
