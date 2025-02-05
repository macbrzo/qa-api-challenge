# qa-api-challenge

## Description
This repository was created as part of a recruitment challenge

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/macbrzo/qa-api-challenge
   cd qa-api-challenge
   ```
2. **Install Poetry:**

    Follow the official Poetry installation guide if Poetry is not already installed.

3. **Install dependencies:**
   ```bash
    poetry install
   ```

## Usage

1. **Activate the virtual environment:**

   ```bash
   poetry shell
   ```
2. **Run automation:**

    ```bash
   pytest
   ```

## Test Scenarios
| Test ID | Test Scenario                 | Steps                                                                 | Expected Result                              | Status |
|---------|-------------------------------|-----------------------------------------------------------------------|----------------------------------------------|--------|
| **T001** | Basic API Response Validation | 1. Call `/get_random_fact` endpoint<br>2. Check status code<br>3. Validate response structure<br>4. Verify length consistency | 1. `200 OK`<br>2. Matches Pydantic model<br>3. `len(fact) == length` | 🟢     |
| **T002** | Valid max_length Behavior     | 1. Send GET with valid `max_length`<br>2. Check status code<br>3. Validate structure<br>4. Check length constraint | 1. `200 OK`<br>2. Valid structure<br>3. `len(fact) ≤ max_length` | 🟢     |
| **T003** | Invalid max_length Handling   | 1. Send GET with invalid `max_length`<br>2. Check status code<br>3. Verify response content | 1. `404 Not Found`<br>2. Empty response body | ❗     |g | 1. Send GET with invalid `max_length`<br>2. Verify status code<br>3. Check response content | 1. Status `404 Not Found`<br>2. No fields in response body | ⬜ |
