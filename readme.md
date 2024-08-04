# Monthly Budget App

This is a simple Flask-based application to make monthly budgets and track expenses. It provides an interface to add transactions, see planned and actual expenses, track income, and see budget summaries for each month.


## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/jmbehlmann/budget-track.git
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. **Run the application:**

    ```bash
    python3 run.py
    ```

6. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:5000/
    ```


## License

This project is licensed under the MIT License.

## Acknowledgements

- Flask: [Flask](https://flask.palletsprojects.com/)
- Chart.js: [Chart.js](https://www.chartjs.org/)
