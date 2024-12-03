# Cookie Clicker Automation Script

This script is an automation tool for the **Cookie Clicker** game, designed to repeatedly click the main cookie (`bigCookie`) for 5 minutes and calculate the average clicks per second (CPS).

---

## Features

- **Automated clicking:** Automatically clicks the main cookie for 5 minutes.
- **CPS calculation:** Computes the number of clicks per second (CPS) during the runtime.
- **Language selection:** Sets the game to English at the start.

---

## Requirements

- Python 3.x
- Selenium library
- Google Chrome browser
- ChromeDriver

---

## Installation

1. Clone or download the repository.
2. Install the required dependencies using pip:
   ```bash
   pip install selenium
   ```
3. Ensure you have Google Chrome and the corresponding version of ChromeDriver installed.  
   [Download ChromeDriver](https://sites.google.com/chromium.org/driver/)

---

## Usage

1. Open a terminal and navigate to the script directory.
2. Run the script:
   ```bash
   python cookie_clicker.py
   ```
3. The script will:
   - Open the Cookie Clicker website.
   - Click the main cookie continuously for 5 minutes.
   - Calculate and display the clicks per second (CPS).

4. Press Enter to close the browser after the script completes.

---

## How It Works

1. **Language Selection:**  
   The script identifies and clicks the button to set the game's language to English.

2. **Clicking Loop:**  
   The script repeatedly clicks the main cookie (`bigCookie`) for a fixed duration of 5 minutes.

3. **CPS Calculation:**  
   After the loop, it calculates the clicks per second using the formula:
   ```python
   cps = clicks / elapsed_time
   ```

4. **Output:**  
   Displays the CPS and waits for the user to press Enter before closing the browser.

---

## Example Output

```
100.25 clicks per second.
Press Enter to close the browser...
```

---