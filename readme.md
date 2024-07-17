# Monthly Budget App

This is a simple Flask-based application to track monthly budgets and expenses. It provides an interface to view transactions, planned and actual expenses, income, and budget summaries for each month. Users can navigate between months using "Previous" and "Next" buttons.


## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/jmbehlmann/budget-track.git
    cd monthly-budget-app
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
    flask run
    ```

6. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:5000/
    ```

## Usage

1. **View the current month's budget:**

    The home page will display the budget summary for the current month, including total planned and actual expenses, total income, and a summary of budget categories and transactions.

2. **Navigate between months:**

    Use the "Previous" and "Next" buttons to navigate to the previous or next month's budget summary.

3. **Select a specific month:**

    Use the month picker to select a specific month and view the budget summary for that month.

## Project Structure

- **app**: Contains the main application code.
  - **models.py**: Defines the database models for transactions and budgets.
  - **routes.py**: Defines the application routes and view functions.
- **templates**: Contains the HTML templates.
  - **base.html**: Base template.
  - **home.html**: Home page template.
- **static**: Contains static files like CSS and JavaScript.
  - **styles.css**: Custom CSS styles.
- **migrations**: Database migration files.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push to your branch.
5. Create a new Pull Request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Flask: [Flask](https://flask.palletsprojects.com/)
- Chart.js: [Chart.js](https://www.chartjs.org/)
