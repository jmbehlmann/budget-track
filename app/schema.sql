CREATE TABLE budget_entry (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    amount REAL NOT NULL,
    type TEXT NOT NULL,
    month TEXT NOT NULL, -- Format: 'YYYY-MM'
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
