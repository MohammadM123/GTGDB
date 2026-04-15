-- CREATE TABLE Guesses (id INTEGER PRIMARY KEY AUTOINCREMENT, 
--                       user_id INTEGER, 
--                       date TEXT NOT NULL, 
--                       score INTEGER,
--                       game TEXT NOT NULL);

-- CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT,
--                     username TEXT UNIQUE NOT NULL,
--                     password NOT NULL);

ALTER TABLE Users ADD COLUMN failed_attempts INTEGER DEFAULT 0;
ALTER TABLE Users ADD COLUMN lock_until INTEGER DEFAULT 0;