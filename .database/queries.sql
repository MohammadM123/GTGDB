-- CREATE TABLE Guesses (id INTEGER PRIMARY KEY AUTOINCREMENT, 
--                       user_id INTEGER, 
--                       date TEXT NOT NULL, 
--                       score INTEGER,
--                       game TEXT NOT NULL);

-- CREATE TABLE Users (id INTEGER PRIMARY KEY AUTOINCREMENT,
--                     username TEXT UNIQUE NOT NULL,
--                     password NOT NULL);

-- ALTER TABLE Users ADD COLUMN failed_attempts INTEGER DEFAULT 0;
-- ALTER TABLE Users ADD COLUMN lock_until INTEGER DEFAULT 0;

-- INSERT INTO Guesses(user_id, date, game, score) VALUES (5, '2026-01-03', 'Minecraft', 7);
-- INSERT INTO Guesses(user_id, date, game, score) VALUES (6, '2026-01-10', 'Fortnite', 5);
-- INSERT INTO Guesses(user_id, date, game, score) VALUES (7, '2026-01-15', 'Call of Duty', 8);
-- INSERT INTO Guesses(user_id, date, game, score) VALUES (8, '2026-01-22', 'Grand Theft Auto V', 6);
-- INSERT INTO Guesses(user_id, date, game, score) VALUES (9, '2026-01-28', 'FIFA 23', 4);

-- INSERT INTO Guesses(user_id, date, game, score) VALUES (10, '2026-02-02', 'The Legend of Zelda', 9);
-- INSERT INTO Guesses(user_id, date, game, score) VALUES (11, '2026-02-08', 'Elden Ring', 7);
-- INSERT INTO Guesses(user_id, date, game, score) VALUES (12, '2026-02-14', 'Roblox', 3);
-- INSERT INTO Guesses(user_id, date, game, score) VALUES (13, '2026-02-20', 'Among Us', 6);
-- INSERT INTO Guesses(user_id, date, game, score) VALUES (14, '2026-02-27', 'Valorant', 8);

-- INSERT INTO Guesses(user_id, date, game, score) VALUES (5, '2026-03-03', 'Overwatch', 5);
-- INSERT INTO Guesses(user_id, date, game, score) VALUES (6, '2026-03-10', 'Apex Legends', 7);
-- INSERT INTO Guesses(user_id, date, game, score) VALUES (7, '2026-03-15', 'League of Legends', 4);
-- INSERT INTO Guesses(user_id, date, game, score) VALUES (8, '2026-03-21', 'Counter-Strike', 9);
-- INSERT INTO Guesses(user_id, date, game, score) VALUES (9, '2026-03-28', 'Rocket League', 6);

-- INSERT INTO Guesses(user_id, date, game, score) VALUES (10, '2026-04-02', 'Cyberpunk 2077', 7);
-- INSERT INTO Guesses(user_id, date, game, score) VALUES (11, '2026-04-08', 'Red Dead Redemption 2', 10);
-- INSERT INTO Guesses(user_id, date, game, score) VALUES (12, '2026-04-12', 'Terraria', 5);
-- INSERT INTO Guesses(user_id, date, game, score) VALUES (13, '2026-04-18', 'Hollow Knight', 8);
-- INSERT INTO Guesses(user_id, date, game, score) VALUES (14, '2026-04-25', 'God of War', 9);