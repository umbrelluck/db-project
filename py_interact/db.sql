/*
run from terminal
createdb aliens;
\connect aliens;
 */

DROP TABLE IF EXISTS on_boarding;
DROP TABLE IF EXISTS murder;
DROP TABLE IF EXISTS excursion_human;
DROP TABLE IF EXISTS experiment_alien;
DROP TABLE IF EXISTS experiment;
DROP TABLE IF EXISTS excursion;
DROP TABLE IF EXISTS human_passenger;
DROP TABLE IF EXISTS alien_passenger;
DROP TABLE IF EXISTS ship;
DROP TABLE IF EXISTS alien;
DROP TABLE IF EXISTS human;



CREATE TABLE human (
	id SERIAL PRIMARY KEY,
	first_name CHARACTER VARYING NOT NULL,
	last_name CHARACTER VARYING NOT NULL,
	gender CHARACTER,
	age INTEGER
);


CREATE TABLE alien (
	id SERIAL PRIMARY KEY,
	name CHARACTER VARYING NOT NULL,
	age INTEGER
);


CREATE TABLE ship (
	id SERIAL PRIMARY KEY,
	rgstr_num  BIGINT UNIQUE NOT NULL,
	max_speed INT,
	color VARCHAR(40)
);


CREATE TABLE human_passenger (
	id SERIAL PRIMARY KEY,
	id_human  INTEGER,
	id_ship INTEGER,
	FOREIGN KEY (id_human) REFERENCES human (id),
	FOREIGN KEY (id_ship) REFERENCES ship (id)
);


CREATE TABLE alien_passenger (
	id SERIAL PRIMARY KEY,
	id_alien  INTEGER,
	id_ship INTEGER,
	FOREIGN KEY (id_alien) REFERENCES alien (id),
	FOREIGN KEY (id_ship) REFERENCES ship (id)
);


CREATE TABLE excursion (
	id SERIAL PRIMARY KEY,
	date DATE NOT NULL,
	duration INT,
	price INT NOT NULL,
	id_alien  INTEGER,
	id_ship INTEGER,
	FOREIGN KEY (id_alien) REFERENCES alien (id),
	FOREIGN KEY (id_ship) REFERENCES ship (id)
);


CREATE TABLE experiment (
	id SERIAL PRIMARY KEY,
	date DATE NOT NULL,
	duration INT,
	description CHARACTER VARYING,
	id_human  INTEGER,
	id_ship INTEGER,
	FOREIGN KEY (id_human) REFERENCES human (id),
	FOREIGN KEY (id_ship) REFERENCES ship (id)
);


CREATE TABLE experiment_alien (
	id_experiment INTEGER,
	id_alien INTEGER,
	FOREIGN KEY (id_experiment) REFERENCES experiment (id),
	FOREIGN KEY (id_alien) REFERENCES alien (id)
);


CREATE TABLE excursion_human (
	id_excursion INTEGER,
	id_human INTEGER,
	FOREIGN KEY (id_excursion) REFERENCES excursion (id),
	FOREIGN KEY (id_human) REFERENCES human (id)
);


CREATE TABLE murder (
    date DATE,
    weapon CHARACTER VARYING,
    id_ship INTEGER,
    id_human  INTEGER,
    id_alien INTEGER,
    FOREIGN KEY (id_ship) REFERENCES ship (id),
    FOREIGN KEY (id_human) REFERENCES human (id),
    FOREIGN KEY (id_alien) REFERENCES alien (id)
);


CREATE TABLE on_boarding (
    date DATE,
    id_ship_from INTEGER,
    id_ship_to INTEGER,
    id_human  INTEGER,
    id_alien INTEGER,
    FOREIGN KEY (id_ship_from) REFERENCES ship (id),
    FOREIGN KEY (id_ship_to) REFERENCES ship (id),
    FOREIGN KEY (id_human) REFERENCES human (id),
    FOREIGN KEY (id_alien) REFERENCES alien (id)
);




INSERT INTO human (first_name, last_name, age, gender)
VALUES  ('Anna',      'Melon',   21, 'f'),
        ('Iva',       'Petrova', 37, 'f'),
        ('Jakob',     'Black',   19, 'm'),
        ('Itan',      'Lambert', 33, 'm'),
        ('Leo',       'Finigan', 53, 'm'),
        ('Lia',       'Jonsson', 24, 'f'),
        ('Olivia',    'Wilson',  75, 'f'),
        ('Adam',      'Finberg', 59, 'm'),
        ('Ruslan',    'Ceban',   28, 'm'),
        ('Stephan',   'Leone',   80, 'm'),
        ('Victoria',  'Wolf',    41, 'f'),
        ('Alexander', 'Kontos',  26, 'm'),
        ('Tereza',    'Green',   19, 'f'),
        ('Zoe',       'Meyer',   66, 'f'),
        ('Ben',       'Salo',    28, 'm'),
		('Artos',   'Guttenberg', 10, 'm');


INSERT INTO alien (name, age)
VALUES ('Paul',     22),
       ('Ax',       14),
       ('Bardan',    5),
       ('Corran',   13),
       ('Elihu',    19),
       ('Darran',   34),
       ('Eldreth',  83),
       ('Kyp',      43),
       ('Groot',    28),
       ('Liara',    19),
       ('Sarek',    26),
       ('Oola',     26),
       ('Vorian',   31),
       ('Luminara', 48),
       ('Vito',     56);



INSERT INTO ship (rgstr_num, max_speed, color)
VALUES (6235174, 300,  'red'),
       (1844353, 280,  'black'),
       (9317372, 400,  'blue'),
       (3352847, 180,  'red'),
       (9442480, 245,  'green'),
       (2487542, 220,  'purple'),
       (4897359, 445,   NULL),
       (3187429, 275,  'black'),
       (7543984, NULL, 'black'),
       (7592843, 360,  'red'),
       (6734949, 210,  'white'),
       (7452374, 280,  'green'),
       (1236232, NULL, 'red');


INSERT INTO human_passenger (id_human, id_ship)
VALUES (3, 5),
       (3, 6),
       (2, 8),
       (4, 4),
       (6, 3),
       (9, 3),
       (1, 3),
       (6, 6),
       (7, 5),
       (4, 7),
       (6, 5),
	   (16, 1),
	   (16, 2),
	   (16, 3);


INSERT INTO alien_passenger (id_alien, id_ship)
VALUES (4, 6),
       (2, 5),
       (3, 7),
       (5, 4),
       (3, 3),
       (4, 9),
       (5, 4),
       (2, 6),
       (8, 5),
       (9, 7),
       (3, 8);


INSERT INTO excursion (date, duration, price, id_alien, id_ship)
VALUES ('01-02-1979', 3, 20, 2, 2),
       ('03-03-1980', 2, 30, 4, 6),
       ('08-11-1985', 1, 15, 3, 1),
       ('02-08-1986', 4, 24, 2, 2),
       ('01-02-1989', 2, 30, 4, 8),
       ('06-06-1989', 3, 23, 7, 2),
       ('04-08-1990', 3, 22, 5, 3),
       ('01-02-1995', 2, 20, 2, 6),
       ('03-02-1999', 1, 25, 1, 9),
       ('09-05-2000', 4, 20, 8, 5);


INSERT INTO experiment (date, duration, description, id_human, id_ship)
VALUES ('01-02-1979', 3, 'First excursion for humans on alien`s space ship',         2, 2),
       ('03-03-1980', 2, 'New excursion. Our last space ship model. Don`t miss it.', 4, 6),
       ('08-11-1985', 1, 'Another excursion, yep',                                   3, 1),
       ('03-08-1986', 4, 'We want to teach stupid people, how to build space ships', 2, 2),
       ('01-02-1989', 2, NULL,                                                       4, 8),
       ('06-06-1989', 3, NULL,                                                       7, 2),
       ('04-08-1990', 3, 'It`s excursion. We don`t want to kidnap you..',            5, 3),
       ('01-02-1995', 2, NULL,                                                       2, 6),
       ('03-02-1999', 1, 'Super cool excursion for smart people. Come on :)',        1, 9),
       ('09-05-2000', 4, NULL,                                                       8, 5);


INSERT INTO excursion_human (id_human, id_excursion)
VALUES (5, 3),
       (5, 2),
       (3, 6),
       (4, 4),
       (6, 3),
       (1, 3),
       (8, 3),
       (2, 9),
       (9, 1),
       (9, 7),
       (6, 8),
       (1, 1);


INSERT INTO experiment_alien (id_alien, id_experiment)
VALUES (1, 3),
       (3, 2),
       (5, 1),
       (7, 4),
       (9, 3),
       (8, 9),
       (6, 4),
       (4, 9),
       (2, 1),
       (5, 7),
       (6, 8),
       (7, 1),
	   (3, 1);


INSERT INTO murder (date, weapon, id_ship, id_human, id_alien)
VALUES ('03-01-1981', 'bluster',      5, 12, 10),
       ('05-02-1983', 'knife',        1, 2,  4),
       ('03-07-1983', 'bluster',      3, 14, 3),
       ('03-03-1987', 'bluster',      3, 10, 6),
       ('03-04-1992',  NULL,          4, 8,  2),
       ('03-06-1993', 'gun',          6, 5,  6),
       ('03-09-1993', 'blunt object', 9, 4,  6),
       ('03-07-1994',  NULL,          4, 9,  1),
       ('03-10-1996', 'bluster',      3, 3,  3),
       ('03-11-1997', 'knife',        1, 1,  12),
	   ('03-01-1998', 'bluster',      5, 12, 5),
	   ('03-01-1998', 'bluster',      5, 12, 7),
	   ('03-07-1998', 'bluster',      5, 16, 3),
	   ('03-07-1998', 'bluster',      5, 11, 8);


INSERT INTO on_boarding (date, id_ship_from, id_ship_to, id_human, id_alien)
VALUES ('02-02-1981', 1,    2,    5,    6),
       ('03-07-1981', NULL, 4,    2,    8),
       ('03-04-1982', 7,    1,    NULL, 4),
       ('03-03-1985', 9,    NULL, 3,    NULL),
	   ('03-11-1986', NULL,    8,    11,   8),
       ('03-11-1986', 8,    3,    11,   8),
       ('03-10-1987', 1,    9,    5,    12),
       ('03-08-1987', 3,    NULL, 14,   NULL),
       ('03-07-1987', NULL, 5,    12,   12),
       ('03-02-1988', NULL, 8,    4,    12),
       ('03-03-1989', 2,    3,    7,    14),
	   ('02-07-1990', NULL,    3,    5,    3),
       ('03-05-1992', 5,    7,    NULL, 7),
	   ('03-06-1992', NULL, 3,    16,   3),
	   ('03-06-1992', 3, NULL,    16,   NULL),
	   ('03-06-1992', NULL, 3,    16,   3),
	   ('03-06-1992', 3, NULL,    16,   NULL),
	   ('03-07-1992', 3,    4,    5,    3);

-----------------------------------------------------------------

--1. для прибульця A знайти усiх людей, яких вiн викрадав хоча б N разiв за вказаний перiод
-- вважаємо, що при викраденні id_ship_from = NULL

SELECT human.first_name, COUNT(on_boarding.id_human) AS n_times FROM human
JOIN on_boarding ON on_boarding.id_human = human.id
JOIN alien ON alien.id = on_boarding.id_alien
-- date condition
WHERE on_boarding.date >= '01-05-1992'::date
AND on_boarding.date < ('01-06-1993'::date + '1 day'::interval)
-- alien condition
AND alien.name LIKE 'Bardan%'
-- from earth condition
AND on_boarding.id_ship_from is NULL
GROUP BY human.first_name
-- N times condition
HAVING COUNT(on_boarding.id_human)>=2;


-- 2. • для людини H знайти усi кораблi, де вона побувала за вказаний перiод

SELECT DISTINCT ship.id, ship.rgstr_num, ship.color FROM ship
JOIN on_boarding ON on_boarding.id_ship_to = ship.id
JOIN human ON human.id = on_boarding.id_human
-- data condition
WHERE on_boarding.date >= '02-02-1981'::date
AND on_boarding.date < ('09-06-1982'::date + '1 day'::interval)
-- human condition
AND human.id = 5;


-- 3. • для людини H знайти усiх прибульцiв, якi викрадали її хоча б N разiв за вказаний перiод

SELECT DISTINCT alien.name, COUNT(on_boarding.id_human) AS n_times
FROM alien
JOIN on_boarding ON on_boarding.id_alien = alien.id
JOIN human ON human.id = on_boarding.id_human
-- data condition
WHERE on_boarding.date >= '02-02-1981'::date
AND on_boarding.date < ('21-06-1993'::date + '1 day'::interval)
-- human condition
AND human.id = 5
GROUP BY alien.name
-- N times condition
HAVING COUNT(on_boarding.id_alien)>=1 ;


-- 4. • для людини H знайти усiх прибульцiв, яких вона вбила за вказаний перiод

SELECT  alien.name FROM alien
JOIN murder ON murder.id_alien = alien.id
JOIN human ON human.id = murder.id_human
-- hyman condition
WHERE human.first_name LIKE 'Alexander%'
-- date condition
AND murder.date >= '02-02-1980'::date
AND murder.date < ('05-06-1983'::date + '1 day'::interval);

-- 5. • для людини H знайти усiх прибульцiв, якi викрадали її та були вбитi нею ж;
-- for humans : 16, 11

SELECT DISTINCT alien.name, murder.id_human FROM alien
JOIN on_boarding ON on_boarding.id_alien = alien.id
JOIN human ON human.id = on_boarding.id_human
JOIN murder ON murder.id_human = human.id
WHERE on_boarding.id_alien = murder.id_alien
AND on_boarding.id_ship_from IS NULL
GROUP BY murder.id_human, alien.name;

-- 6. • знайти усiх прибульцiв якi викрали щонайменше N рiзних людей за вказаний перiод

SELECT DISTINCT alien.id FROM alien
JOIN on_boarding on on_boarding.id_alien = alien.id
GROUP BY alien.id
-- n times human condition
HAVING COUNT(DISTINCT on_boarding.id_human)>=2;


-- 7. • знайти усiх людей, яких викрадали хоча б N разiв за вказаний перiод (з дати F по дату T);
SELECT human.first_name ||' '|| human.last_name AS human_name, COUNT(on_boarding.id_human) AS n_times
FROM human
INNER JOIN on_boarding ON on_boarding.id_human = human.id
WHERE on_boarding.date >= '02-05-1992'::date
AND on_boarding.date < ('10-06-1993'::date + '1 day'::interval)
AND on_boarding.id_ship_from is NULL
GROUP BY human_name
HAVING COUNT(on_boarding.id_human) >= 2;

--8. • знайти усi спiльнi екскурсiї та експерименти для прибульця A та людини H за вказаний період
SELECT experiment.id AS experiment, excursion.id AS excursion
FROM experiment
INNER JOIN human ON human.id = experiment.id_human
INNER JOIN experiment_alien ON experiment_alien.id_experiment = experiment.id
INNER JOIN alien ON experiment_alien.id_alien = alien.id
INNER JOIN excursion on alien.id = excursion.id_alien
INNER JOIN excursion_human ON excursion_human.id_excursion = excursion.id
WHERE alien.name LIKE 'Elihu%'
AND human.first_name LIKE 'Iva%'
AND experiment.date >= '01-02-1979'::date
AND experiment.date < ('09-05-2000'::date + '1 day'::interval)
AND excursion.date >= '01-02-1979'::date
AND excursion.date < ('09-05-2000'::date + '1 day'::interval);


-- 9. • для прибульця A та кожної екскурсiї, яку вiн проводив, знайти скiльки разiв за вказаний
--      перiод (з дати F по дату T) вiн проводив екскурсiю для щонайменше N людей;

SELECT COUNT(*) FROM
(SELECT excursion.id FROM excursion
JOIN alien ON alien.id = excursion.id_alien
JOIN excursion_human ON excursion_human.id_excursion = excursion.id
WHERE excursion.id_alien = 2 -- A
AND excursion.date >= '02-02-1978'::date		-- F T
AND excursion.date < ('12-06-2000'::date + '1 day'::interval)
GROUP BY excursion.id
HAVING COUNT(excursion_human.id_excursion)>=1)
AS tab_1; -- N


--10. для людини H та кожного експерименту, у якому вона брала участь, знайти скiльки разiв
--за вказаний перiод (з дати F по дату T) експеримент над нею проводили щонайменше N
--прибульцiв;

SELECT COUNT(*) FROM
(SELECT DISTINCT experiment.id FROM experiment
JOIN human ON human.id = experiment.id_human
JOIN experiment_alien ON experiment_alien.id_experiment = experiment.id
WHERE experiment.id_human = 2
AND experiment.date >= '01-02-1979'::date
AND experiment.date < ('09-05-2000'::date + '1 day'::interval)
GROUP BY experiment.id
HAVING COUNT(DISTINCT experiment_alien.id_alien) >= 1)
as tab_2;




-- 11. •  знайти сумарну кiлькiсть викрадень по мiсяцях;
SELECT CASE
  WHEN EXTRACT(MONTH FROM date) = 1 THEN 'January'
  WHEN EXTRACT(MONTH FROM date) = 2 THEN 'February'
  WHEN EXTRACT(MONTH FROM date) = 3 THEN 'March'
  WHEN EXTRACT(MONTH FROM date) = 4 THEN 'April'
  WHEN EXTRACT(MONTH FROM date) = 5 THEN 'May'
  WHEN EXTRACT(MONTH FROM date) = 6 THEN 'June'
  WHEN EXTRACT(MONTH FROM date) = 7 THEN 'July'
  WHEN EXTRACT(MONTH FROM date) = 8 THEN 'August'
  WHEN EXTRACT(MONTH FROM date) = 9 THEN 'September'
  WHEN EXTRACT(MONTH FROM date) = 10 THEN 'October'
  WHEN EXTRACT(MONTH FROM date) = 11 THEN 'November'
  WHEN EXTRACT(MONTH FROM date) = 12 THEN 'December'
END AS month, COUNT(*)
FROM on_boarding
WHERE id_ship_from IS NULL AND EXTRACT(YEAR FROM date) = '1992'
GROUP BY month;


-- 12. • вивести кораблi у порядку спадання сумарної кiлькостi еспериментiв, що були проведенi на
--       кораблi за участi даного прибульця A протягом вказаного перiоду (з дати F по дату T);
SELECT experiment.id_ship, COUNT(*) AS num
FROM experiment_alien LEFT JOIN experiment
ON experiment_alien.id_experiment = experiment.id
WHERE experiment_alien.id_alien = 7
AND experiment.date >= '02-02-1978'::DATE
AND experiment.date < ('09-06-2000'::DATE + '1 day'::INTERVAL)
GROUP BY experiment.id_ship
ORDER BY num DESC;

