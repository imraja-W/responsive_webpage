-- schema.sql

CREATE TABLE IF NOT EXISTS user_inputs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    input_text TEXT NOT NULL
);
