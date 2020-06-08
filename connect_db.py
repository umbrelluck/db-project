# host: 142.93.163.88
# port: 6006
# user: team1
# database: db1
# password: password1

# How to install: $ pip install psycopg2-binary
import psycopg2


# 1. для прибульця A знайти усiх людей, яких вiн викрадав хоча б N разiв за вказаний перiод
def select_alien_kidnapping(conn, alien_name, n_times, date_from, date_to):
    cur = conn.cursor()
    query = """
        SELECT human.first_name, COUNT(on_boarding.id_human) AS n_times FROM human
        JOIN on_boarding ON on_boarding.id_human = human.id
        JOIN alien ON alien.id = on_boarding.id_alien
        -- date condition
        WHERE on_boarding.date >= %s::date
        AND on_boarding.date < (%s::date + '1 day'::interval)
        -- alien condition
        AND alien.name LIKE %s 
        -- from earth condition
        AND on_boarding.id_ship_from is NULL
        GROUP BY human.first_name
        -- N times condition
        HAVING COUNT(on_boarding.id_human)>=%s;
    """
    data = (date_from, date_to, alien_name, n_times)
    cur.execute(query, data)
    return cur.fetchall()


# 2. для людини H знайти усi кораблi, де вона побувала за вказаний перiод
def select_human_ships(conn, human_id, date_from, date_to):
    cur = conn.cursor()

    query = """
        SELECT DISTINCT ship.id, ship.rgstr_num, ship.color FROM ship
        JOIN on_boarding ON on_boarding.id_ship_to = ship.id
        JOIN human ON human.id = on_boarding.id_human
        -- data condition
        WHERE on_boarding.date >= %s::date
        AND on_boarding.date < (%s::date + '1 day'::interval)
        -- human condition
        AND human.id = %s;
    """
    data = (date_from, date_to, human_id)
    cur.execute(query, data)
    return cur.fetchall()


# TODO: заповнити наступні таблички по прикладу попередніх
# відповідні назви SELECTів в ексельці, SELECTи в db.sql

# 3. • для людини H знайти усiх прибульцiв, якi викрадали її хоча б N разiв за вказаний перiод
def select_human_kidnapping_aliens(conn, human_id, n_times, date_from, date_to):
    cur = conn.cursor()

    query = """
            SELECT DISTINCT alien.name, COUNT(on_boarding.id_human) AS n_times
            FROM alien
            JOIN on_boarding ON on_boarding.id_alien = alien.id
            JOIN human ON human.id = on_boarding.id_human
            -- data condition
            WHERE on_boarding.date >= %s::date
            AND on_boarding.date < (%s::date + '1 day'::interval)
            -- human condition
            AND human.id = %s
            GROUP BY alien.name
            -- N times condition
            HAVING COUNT(on_boarding.id_alien)>=%s ;
        """
    data = (date_from, date_to, human_id, n_times)
    cur.execute(query, data)
    return cur.fetchall()


# -- 4. • для людини H знайти усiх прибульцiв, яких вона вбила за вказаний перiод
def select_human_murder(conn, human_first_name, date_from, date_to):
    query = """
            SELECT  alien.name FROM alien
            JOIN murder ON murder.id_alien = alien.id
            JOIN human ON human.id = murder.id_human
            -- hyman condition
            WHERE human.first_name LIKE %s
            -- date condition
            AND murder.date >= %s::date
            AND murder.date < (%s::date + '1 day'::interval);
    """

    cur = conn.cursor()
    data = (human_first_name, date_from, date_to)
    cur.execute(query, data)
    return cur.fetchall()


# -- 5. • для людини H знайти усiх прибульцiв, якi викрадали її та були вбитi нею ж;
# -- for humans : 16, 11
def select_human_revenge(conn, human_id):
    query = """
            SELECT DISTINCT alien.name, murder.id_human FROM alien
            JOIN on_boarding ON on_boarding.id_alien = alien.id
            JOIN human ON human.id = on_boarding.id_human
            JOIN murder ON murder.id_human = human.id
            WHERE on_boarding.id_alien = murder.id_alien
            AND on_boarding.id_ship_from IS NULL
            AND human.id = %s
            GROUP BY murder.id_human, alien.name;
    """
    cur = conn.cursor()
    data = [human_id]
    cur.execute(query, data)
    return cur.fetchall()


# -- 6. • знайти усiх прибульцiв якi викрали щонайменше N рiзних людей за вказаний перiод
def select_aliens_kidnapping(conn, n_people, date_from, date_to):
    query = """
        SELECT DISTINCT alien.name FROM alien
        JOIN on_boarding on on_boarding.id_alien = alien.id
        WHERE on_boarding.date >= %s::date
        AND on_boarding.date < (%s::date + '1 day'::interval)
        AND on_boarding.id_ship_from IS NULL
        GROUP BY alien.id
        -- n times human condition
        HAVING COUNT(DISTINCT on_boarding.id_human)>=%s;
    """

    cur = conn.cursor()
    data = (date_from, date_to, n_people)
    cur.execute(query, data)
    return cur.fetchall()


# -- 7. • знайти усiх людей, яких викрадали хоча б N разiв за вказаний перiод (з дати F по дату T);
def select_all_human_kidnapping(conn, n_times, date_from, date_to):
    query = """
        SELECT human.first_name ||' '|| human.last_name AS human_name, COUNT(on_boarding.id_human) AS n_times
        FROM human
        INNER JOIN on_boarding ON on_boarding.id_human = human.id
        WHERE on_boarding.date >= %s::date
        AND on_boarding.date < (%s::date + '1 day'::interval)
        AND on_boarding.id_ship_from is NULL
        GROUP BY human_name
        HAVING COUNT(on_boarding.id_human) >= %s;
    """
    cur = conn.cursor()
    data = (date_from, date_to, n_times)
    cur.execute(query, data)
    return cur.fetchall()


# --8. • знайти усi спiльнi екскурсiї та експерименти для прибульця A та людини H за вказаний період
def select_joint_exc_exp(conn, human_first_name, alien_name, date_from, date_to):
    query = """
        SELECT experiment.id AS experiment, excursion.id AS excursion
        FROM experiment
        INNER JOIN human ON human.id = experiment.id_human
        INNER JOIN experiment_alien ON experiment_alien.id_experiment = experiment.id
        INNER JOIN alien ON experiment_alien.id_alien = alien.id
        INNER JOIN excursion on alien.id = excursion.id_alien
        INNER JOIN excursion_human ON excursion_human.id_excursion = excursion.id
        WHERE alien.name LIKE %s
        AND human.first_name LIKE %s
        AND experiment.date >= %s::date
        AND experiment.date < (%s::date + '1 day'::interval)
        AND excursion.date >= %s::date
        AND excursion.date < (%s::date + '1 day'::interval);
    """
    cur = conn.cursor()
    data = (alien_name, human_first_name,
            date_from, date_to, date_from, date_to)
    cur.execute(query, data)
    return cur.fetchall()


# -- 9. • для прибульця A та кожної екскурсiї, яку вiн проводив, знайти скiльки разiв за вказаний
# --      перiод (з дати F по дату T) вiн проводив екскурсiю для щонайменше N людей;
def select_alien_excursion(conn, alien_id, n_humans, date_from, date_to):
    query = """
            SELECT COUNT(*) FROM
            (SELECT excursion.id FROM excursion
            JOIN alien ON alien.id = excursion.id_alien
            JOIN excursion_human ON excursion_human.id_excursion = excursion.id
            WHERE excursion.id_alien = %s -- A
            AND excursion.date >= %s::date		-- F T
            AND excursion.date < (%s::date + '1 day'::interval)
            GROUP BY excursion.id
            HAVING COUNT(excursion_human.id_excursion)>=%s)
            AS tab_1; -- N
    """

    cur = conn.cursor()
    data = (alien_id, date_from, date_to, n_humans)
    cur.execute(query, data)
    return cur.fetchall()


# --10. для людини H та кожного експерименту, у якому вона брала участь, знайти скiльки разiв
# --за вказаний перiод (з дати F по дату T) експеримент над нею проводили щонайменше N
# --прибульцiв;
def select_human_experimentalists(conn, human_id, n_aliens, date_from, date_to):
    query = """
            SELECT COUNT(*) FROM
            (SELECT DISTINCT experiment.id FROM experiment
            JOIN human ON human.id = experiment.id_human
            JOIN experiment_alien ON experiment_alien.id_experiment = experiment.id
            WHERE experiment.id_human = %s
            AND experiment.date >= %s::date
            AND experiment.date < (%s::date + '1 day'::interval)
            GROUP BY experiment.id
            HAVING COUNT(DISTINCT experiment_alien.id_alien) >= %s)
            as tab_2;
        """

    cur = conn.cursor()
    data = (human_id, date_from, date_to, n_aliens)
    cur.execute(query, data)
    return cur.fetchall()


# -- 11. •  знайти сумарну кiлькiсть викрадень по мiсяцях;
def select_all_kidnappings(conn, year):
    query = """
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
            WHERE id_ship_from IS NULL AND EXTRACT(YEAR FROM date) = %s
            GROUP BY month;
    """
    cur = conn.cursor()
    cur.execute(query, [year])
    return cur.fetchall()


# -- 12. • вивести кораблi у порядку спадання сумарної кiлькостi еспериментiв, що були проведенi на
# --       кораблi за участi даного прибульця A протягом вказаного перiоду (з дати F по дату T);
def select_alien_ships_experiments(conn, alien_id, date_from, date_to):
    query = """
            -- x = SELECT MAX(id)  FROM experiment;
            SELECT experiment.id_ship, COUNT(*) AS num
            FROM experiment_alien LEFT JOIN experiment
            ON experiment_alien.id_experiment = experiment.id
            WHERE experiment_alien.id_alien = %s
            AND experiment.date >= %s::DATE
            AND experiment.date < (%s::DATE + '1 day'::INTERVAL)
            GROUP BY experiment.id_ship
            ORDER BY num DESC;
    """

    cur = conn.cursor()
    data = (alien_id, date_from, date_to)
    cur.execute(query, data)
    return cur.fetchall()


# -- прибулець викрадає людину
def alien_kidnaps_human(conn, date, id_ship_to, id_human, id_alien):
    query = """
            INSERT INTO on_boarding (date, id_ship_from, id_ship_to, id_human, id_alien)
            VALUES (%(date)s::date, NULL, %(id_ship_to)s, %(id_human)s, %(id_alien)s);
            UPDATE human_passenger 
            SET id_ship = (SELECT id_ship_to FROM on_boarding)
            WHERE id_human = %(id_human)s
            AND id_ship = NULL;
    """

    cur = conn.cursor()
    data = ({"date": date,
             "id_ship_to": id_ship_to, "id_human": id_human, "id_alien": id_alien})
    try:
        cur.execute(query, data)
        return 0

    except Exception as e:
        return str(e)


# -- людина тікає з космічного корабля
def human_escapes_from_the_ship(conn, date, id_ship_from, id_human):
    query = """
           INSERT INTO on_boarding (date, id_ship_from, id_ship_to, id_human, id_alien)
            VALUES (%(date)s::date, %(id_ship_from)s, NULL, %(id_human)s, NULL);
            UPDATE human_passenger 
            SET id_ship = NULL
            WHERE id_human = %(id_human)s
            AND id_ship = (SELECT id_ship_from FROM on_boarding);
    """

    cur = conn.cursor()
    data = ({"date": date, "id_ship_from": id_ship_from, "id_human": id_human})

    try:
        cur.execute(query, data)
        return 0

    except Exception as e:
        return str(e)


# -- прибулець транспортує людину на iнший корабель
def alien_transports_human(conn, date, id_ship_from, id_ship_to, id_human, id_alien):
    query = """
            INSERT INTO on_boarding (date, id_ship_from, id_ship_to, id_human, id_alien)
            VALUES (%(date)s::date, %(id_ship_from)s, %(id_ship_to)s, %(id_human)s, %(id_alien)s);
            UPDATE human_passenger 
            SET id_ship = (SELECT id_ship_from FROM on_boarding)
            WHERE id_human = %(id_human)s
            AND id_ship = (SELECT id_ship_to FROM on_boarding);
    """

    cur = conn.cursor()
    data = ({"date": date, "id_ship_from": id_ship_from,
             "id_ship_to": id_ship_to, "id_human": id_human, "id_alien": id_alien})
    
    try:
        cur.execute(query, data)
        return 0

    except Exception as e:
        return str(e)



# -- людина вбиває прибульця
def human_kills_alien(conn, date, weapon, id_ship, id_human, id_alien):
    query = """
            INSERT INTO murder (date, weapon, id_ship, id_human, id_alien)
            VALUES (%(date)s::date, %(weapon)s, %(id_ship)s, %(id_human)s, %(id_alien)s);
            UPDATE alien_passenger
            SET id_ship = NULL
            WHERE id_alien = %(id_alien)s
            AND id_ship = (SELECT id_ship FROM murder)
    """

    cur = conn.cursor()
    data = ({"date": date, "weapon": weapon, "id_ship": id_ship,
             "id_human": id_human, "id_alien": id_alien})
    try:
        cur.execute(query, data)
        return 0

    except Exception as e:
        return str(e)



if __name__ == '__main__':
    pass
    # Connect to an existing database
    # conn = psycopg2.connect("dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
    # alien_kidnaps_human(conn, '02-05-1972', 1, 8, 1, 1)
    # alien_transports_human(conn, '02-05-1972', 1, 8, 1, 1)
    # res = select_alien_kidnapping(conn, 'Paul%', 1, '01-05-1972', '01-06-1993')

    # human_kills_alien(conn, '11-07-1980', 'bluster', 5, 2, 1)
    # res2 = select_human_ships(conn, 5, '02-02-1970', '09-06-1990')
    # res3 = select_human_kidnapping_aliens(conn, 16, '1992-03-06', '1992-03-06')
    # res4 = select_human_murder(conn, 'Iva', '02-02-1979', '05-06-1988')
    # res5 = select_alien_ships_experiments(conn, 7, '02-02-1978', '02-02-2001')
    # print(res5)

    # print(res4)
