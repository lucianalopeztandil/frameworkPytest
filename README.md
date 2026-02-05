# frameworkPytest

## 🧪 Test Automation Framework – Selenium + Pytest

This repository contains a **Python-based test automation framework** built with **Selenium WebDriver** and **Pytest**, designed to validate the main user flow of an e-commerce shop.

The framework automates a complete end-to-end scenario, from user interaction to order placement, following best practices used in real-world automation projects.

---

## 🚀 Automated Scenario Coverage

The framework validates the following workflow:

1. Navigate to the e-commerce shop
2. User login
3. Browse products and select **Blackberry**
4. Add product to cart
5. Proceed to checkout
6. Complete the order and validate the confirmation

---

## 🛠️ Tech Stack

* **Python**
* **Selenium WebDriver**
* **Pytest**
* **Page Object Model (POM)**
* **Explicit & Implicit Waits**
* **Git & GitHub**

---

## 📂 Project Structure

```
frameworkPytest/
│
├── pages/              # Page Objects
├── tests/              # Test cases
├── utils/              # Utilities and helpers
├── conftest.py         # Pytest configuration
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## ▶️ How to Run the Tests

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/frameworkPytest.git
cd frameworkPytest
```

2. Create and activate a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\\Scripts\\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the tests:

```bash
pytest -v
```

---

## ✅ Key Automation Practices

* Clear separation between test logic and UI locators
* Reusable page components
* Stable synchronization using waits
* Clean and readable test cases
* Scalable structure for adding new scenarios

---

## 📌 Notes

* The framework is intended for learning, practice, and demonstration purposes
* It can be easily extended to cover additional products and flows

---

## 👩‍💻 Author

Luciana

---

⭐ If you find this project useful, feel free to explore, fork, or improve it!
