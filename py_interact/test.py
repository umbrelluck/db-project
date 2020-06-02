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
def select_human_ships(сonn, human_id, date_from, date_to):
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


#TODO: заповнити наступні таблички по прикладу попередніх
# відповідні назви SELECTів в ексельці, SELECTи в db.sql

# def select_human_kidnapping_aliens()

# def select_human_murder()

# def select_human_revenge()

# def select_aliens_kidnapping()

# def select_all_human_kidnapping()

# def select_joint_exc_exp()

# def select_alien_excursion()

# def select_human_experimentalists()

# def select_all_kidnappings()

# def select_alien_ships_experiments()


if __name__ == '__main__':
    # Connect to an existing database
    conn = psycopg2.connect("dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")

    res = select_alien_kidnapping(conn, 'Bardan%', 2, '01-05-1972', '01-06-1993')
    res2 = select_human_ships(conn, 5, '02-02-1970', '09-06-1990')

    print(res)
    print(res2)
