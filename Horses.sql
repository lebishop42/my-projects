-- A DATABASE FOR USE WITH THE HORSE EXCHANGE PROGRAMME
CREATE DATABASE horses;

USE horses;

-- A TABLE FOR HORSES AVAILABLE TO BUY
CREATE TABLE IF NOT EXISTS catalogue (
horse_name VARCHAR(25) NOT NULL,
age INTEGER,
colour VARCHAR(20),
price INTEGER NOT NULL,
status VARCHAR(20)
);


INSERT INTO catalogue (horse_name, age, colour, price, status)
VALUES
("Thunderbolt", 8, "Bay", 8000, "for sale"),
("Starlight", 6, "Palomino", 6500, "for sale"),
("Midnight", 10, "Black", 10000, "for sale"),
("Bella", 7, "Chestnut", 7200, "sold"),
("Cinnamon", 5, "Sorrel", 5500, "for sale"),
("Snowflake", 9, "Grey", 9000, "for sale"),
("Apache", 11,"Appaloosa", 12000, "for sale"),
("Jasper", 8 , "Roan", 8500, "for sale"),
("Duchess", 7, "Dark Bay", 9500, "sold"),
("Apollo", 12, "Dun", 11500, "for sale")
;

-- AN EMPTY TABLE TO POPULATE WITH SALES
CREATE TABLE IF NOT EXISTS sold_list (
buyer_name VARCHAR(20),
sold_horse_name VARCHAR(25)
);
