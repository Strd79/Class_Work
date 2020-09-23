DROP TABLE lightsabers;
DROP TABLE characters;

CREATE TABLE characters(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    darkside BOOLEAN,
    age INT
);

create TABLE lightsabers(
    id SERIAL PRIMARY KEY,
    colour VARCHAR(255) NOT NULL,
    hilt_metal VARCHAR(255) NOT NULL,
    character_id INT REFERENCES characters(id)
);

INSERT INTO characters (name, darkside, age) VALUES ('Obi-Wan Kenobi', FALSE, 27);
INSERT INTO characters (name, darkside, age) VALUES ('Anakin Skywalker', FALSE, 19);
INSERT INTO characters (name, darkside, age) VALUES ('Darth Maul', TRUE, 32);
INSERT INTO characters (name, darkside) VALUES ('Yoda', TRUE);
INSERT INTO characters (name, darkside, age) VALUES ('Luke Skywalker', FALSE, 26);
INSERT INTO characters (name, darkside, age) VALUES ('Stormtrooper', true, 25);
INSERT INTO characters (name, darkside, age) VALUES ('Stormtrooper', true, 25);
INSERT INTO characters (name, darkside, age) VALUES ('Stormtrooper', true, 25);
INSERT INTO characters (name, darkside, age) VALUES ('Stormtrooper', true, 25);

SELECT * FROM characters;
SELECT * FROM lightsabers;

-- SELECT COUNT(*) FROM characters;

-- UPDATE characters SET darkside = TRUE WHERE name = 'Anakin Skywalker';

-- UPDATE characters SET (name, darkside) = ('Darth Vader', true) WHERE name = 'Anakin Skywalker';

-- UPDATE characters SET age = 50 WHERE name = 'Obi-Wan Kenobi';

-- SELECT * FROM characters;

-- DELETE FROM characters WHERE name = 'Darth Maul';
-- SELECT * FROM characters;

-- UPDATE characters SET age = 29 WHERE id = 9;
-- SELECT * FROM characters;

INSERT INTO lightsabers (colour, hilt_metal, character_id) VALUES ('green', 'palladium', 4);
INSERT INTO lightsabers (colour, hilt_metal, character_id) VALUES ('red', 'gold', 3);
INSERT INTO lightsabers (colour, hilt_metal, character_id) VALUES ('blue', 'gold', 3);

SELECT * FROM lightsabers;