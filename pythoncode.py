from flask import Flask, jsonify, request
from flask_cors import CORS
from connect_db import *

app = Flask(__name__, static_folder='./build', static_url_path='/')
CORS(app)


@app.route('/')
def index():
    return app.send_static_file('index.html')

# ...other code...

# 1. для прибульця A знайти усiх людей, яких вiн викрадав хоча б N разiв за вказаний перiод
@app.route('/get_select_alien_kidnapping', methods=["GET"])
def get_select_alien_kidnapping():
    try:
        alien_name, n_times, date_from, date_to = request.args.get('alien_name', ''), \
            int(request.args.get('n_times', '')), \
            request.args.get('date_from', ''), \
            request.args.get('date_to', '')

        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = select_alien_kidnapping(
            conn, alien_name, n_times, date_from, date_to)
        return jsonify(result=word)
    except Exception as e:
        return str(e)

# 2. для людини H знайти усi кораблi, де вона побувала за вказаний перiод
@app.route('/get_select_human_ships', methods=["GET"])
def get_select_human_ships():
    try:
        human_id, date_from, date_to = request.args.get('human_id', ''), \
            request.args.get('date_from', ''), \
            request.args.get('date_to', '')

        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = select_human_ships(conn, human_id, date_from, date_to)
        return jsonify(result=word)
    except Exception as e:
        return str(e)

# 3. • для людини H знайти усiх прибульцiв, якi викрадали її хоча б N разiв за вказаний перiод
@app.route('/get_select_human_kidnapping_aliens', methods=["GET"])
def get_select_human_kidnapping_aliens():
    try:
        human_id, n_times, date_from, date_to = request.args.get('human_id', ''), \
            request.args.get('n_times', ''), \
            request.args.get('date_from', ''), \
            request.args.get('date_to', '')

        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = select_human_kidnapping_aliens(
            conn, human_id, n_times, date_from, date_to)
        return jsonify(result=word)
    except Exception as e:
        return str(e)

# -- 4. • для людини H знайти усiх прибульцiв, яких вона вбила за вказаний перiод
@app.route('/get_select_human_murder', methods=["GET"])
def get_select_human_murder():
    try:
        human_first_name, date_from, date_to = request.args.get('human_first_name', ''), \
            request.args.get('date_from', ''), \
            request.args.get('date_to', '')

        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = select_human_murder(conn, human_first_name, date_from, date_to)
        return jsonify(result=word)
    except Exception as e:
        return str(e)

# -- 5. • для людини H знайти усiх прибульцiв, якi викрадали її та були вбитi нею ж;
# -- for humans : 16, 11
@app.route('/get_select_human_revenge', methods=["GET"])
def get_select_human_revenge():
    try:
        human_id = request.args.get('human_id', '')
        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = select_human_revenge(conn, human_id)
        return jsonify(result=word)
    except Exception as e:
        return str(e)


# -- 6. • знайти усiх прибульцiв якi викрали щонайменше N рiзних людей за вказаний перiод
@app.route('/get_select_aliens_kidnapping', methods=["GET"])
def get_select_aliens_kidnapping():
    try:
        n_people, date_from, date_to = int(request.args.get('n_people', '')), \
            request.args.get('date_from', ''), \
            request.args.get('date_to', '')

        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = select_aliens_kidnapping(conn, n_people, date_from, date_to)
        return jsonify(result=word)
    except Exception as e:
        return str(e)

# -- 7. • знайти усiх людей, яких викрадали хоча б N разiв за вказаний перiод (з дати F по дату T);
@app.route('/get_select_all_human_kidnapping', methods=["GET"])
def get_select_all_human_kidnapping():
    try:
        n_times, date_from, date_to = request.args.get('n_times', ''), \
            request.args.get('date_from', ''), \
            request.args.get('date_to', '')

        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = select_all_human_kidnapping(conn, n_times, date_from, date_to)
        return jsonify(result=word)
    except Exception as e:
        return str(e)

# --8. • знайти усi спiльнi екскурсiї та експерименти для прибульця A та людини H за вказаний період
@app.route('/get_select_joint_exc_exp', methods=["GET"])
def get_select_joint_exc_exp():
    try:
        human_first_name, alien_name, date_from, date_to = request.args.get('human_first_name', ''), \
            request.args.get('alien_name', ''), \
            request.args.get('date_from', ''), \
            request.args.get('date_to', '')

        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = select_joint_exc_exp(
            conn,  human_first_name, alien_name, date_from, date_to)
        return jsonify(result=word)
    except Exception as e:
        return str(e)


# -- 9. • для прибульця A та кожної екскурсiї, яку вiн проводив, знайти скiльки разiв за вказаний
# --      перiод (з дати F по дату T) вiн проводив екскурсiю для щонайменше N людей;
@app.route('/get_select_alien_excursion', methods=["GET"])
def get_select_alien_excursion():
    try:
        alien_id, n_humans, date_from, date_to = request.args.get('alien_id', ''), \
            request.args.get('n_humans', ''), \
            request.args.get('date_from', ''), \
            request.args.get('date_to', '')

        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = select_alien_excursion(
            conn,  alien_id, n_humans, date_from, date_to)
        return jsonify(result=word)
    except Exception as e:
        return str(e)

# --10. для людини H та кожного експерименту, у якому вона брала участь, знайти скiльки разiв
# --за вказаний перiод (з дати F по дату T) експеримент над нею проводили щонайменше N
# --прибульцiв;
@app.route('/get_select_human_experimentalists', methods=["GET"])
def get_select_human_experimentalists():
    try:
        human_id, n_aliens, date_from, date_to = request.args.get('human_id', ''), \
            request.args.get('n_aliens', ''), \
            request.args.get('date_from', ''), \
            request.args.get('date_to', '')

        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = select_human_experimentalists(
            conn,  human_id, n_aliens, date_from, date_to)
        return jsonify(result=word)
    except Exception as e:
        return str(e)

# -- 11. •  знайти сумарну кiлькiсть викрадень по мiсяцях;
@app.route('/get_select_all_kidnappings', methods=["GET"])
def get_select_all_kidnappings():
    try:
        year = request.args.get('year', '')

        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = select_all_kidnappings(conn,  year)
        return jsonify(result=word)
    except Exception as e:
        return str(e)


# -- 12. • вивести кораблi у порядку спадання сумарної кiлькостi еспериментiв, що були проведенi на
# --       кораблi за участi даного прибульця A протягом вказаного перiоду (з дати F по дату T);
@app.route('/get_select_alien_ships_experiments', methods=["GET"])
def get_select_alien_ships_experiments():
    try:
        alien_id, date_from, date_to = request.args.get('alien_id', ''), \
            request.args.get('date_from', ''), \
            request.args.get('date_to', '')

        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = select_alien_ships_experiments(
            conn,  alien_id, date_from, date_to)
        return jsonify(result=word)
    except Exception as e:
        return str(e)


####################################################################################################

# -- прибулець викрадає людину
@app.route('/get_alien_kidnaps_human', methods=["GET"])
def get_alien_kidnaps_human():
    try:
        date, id_ship_to, id_human, id_alien = request.args.get('date', ''), \
            request.args.get('id_ship_to', ''), \
            request.args.get('id_human', ''), \
            request.args.get('id_alien', '')

        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = alien_kidnaps_human(conn,  date, id_ship_to, id_human, id_alien)
        return jsonify(result=word)
    except Exception as e:
        return str(e)


# -- людина тікає з космічного корабля
@app.route('/get_human_escapes_from_the_ship', methods=["GET"])
def get_human_escapes_from_the_ship():
    try:
        date, id_ship_from, id_human = request.args.get('date', ''), \
            request.args.get('id_ship_from', ''), \
            request.args.get('id_human', '')

        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = human_escapes_from_the_ship(conn,  date, id_ship_from, id_human)
        return jsonify(result=word)

    except Exception as e:
        return str(e)


# -- прибулець транспортує людину на iнший корабель
@app.route('/get_alien_transports_human', methods=["GET"])
def get_alien_transports_human():
    try:
        date, id_ship_from, id_ship_to, id_human, id_alien = request.args.get('date', ''), \
            request.args.get('id_ship_from', ''), \
            request.args.get('id_ship_to', ''), \
            request.args.get('id_human', ''), \
            request.args.get('id_alien', '')

        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = alien_transports_human(
            conn,  date, id_ship_from, id_ship_to, id_human, id_alien)
        return jsonify(result=word)

    except Exception as e:
        return str(e)


# -- людина вбиває прибульця
@app.route('/get_human_kills_alien', methods=["GET"])
def get_human_kills_alien():
    try:
        date, weapon, id_ship, id_human, id_alien = request.args.get('date', ''), \
            request.args.get('weapon', ''), \
            request.args.get('id_ship', ''), \
            request.args.get('id_human', ''), \
            request.args.get('id_alien', '')

        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = human_kills_alien(
            conn,  date, weapon, id_ship, id_human, id_alien)
        return jsonify(result=word)

    except Exception as e:
        return str(e)

###############################################################################################

# alien
# alien_passenger

# human
# human_passenger

# murder
# excursion
# excursion_human
# experiment
# experiment_aien

# ship
# on_boarding


# type(table_name) = string
@app.route('/get_whole_table', methods=["GET"])
def get_whole_table():
    try:
        table_name = request.args.get('table_name', '')

        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = whole_table(
            conn,  table_name)
        return jsonify(result=word)

    except Exception as e:
        return str(e)

# EXCURSION PART #################################################

@app.route('/get_excursion_set', methods=["GET"])
def get_excursion_set():
    try:
        date, duration, price, id_alien, id_ship = request.args.get('date', ''), \
            request.args.get('duration', ''), \
            request.args.get('price', ''), \
            request.args.get('id_alien', ''), \
            request.args.get('id_ship', '')

        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = excursion_set(conn, date, duration, price, id_alien, id_ship)
        return jsonify(result=word)

    except Exception as e:
        return str(e)

@app.route('/get_add_human_to_excursion', methods=["GET"])
def get_add_human_to_excursion():
    try:
        id_excursion, id_human = request.args.get('id_excursion', ''), \
            request.args.get('id_human', '')
            
        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = add_human_to_excursion(conn, id_excursion, id_human)
        return jsonify(result=word)

    except Exception as e:
        return str(e)

# EXPERIMENT PART #################################################

@app.route('/get_experiment_set', methods=["GET"])
def get_experiment_set():
    try:
        date, duration, description, id_human, id_ship = request.args.get('date', ''), \
            request.args.get('duration', ''), \
            request.args.get('description', ''), \
            request.args.get('id_human', ''), \
            request.args.get('id_ship', '')

        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = experiment_set(conn, date, duration, description, id_human, id_ship)
        return jsonify(result=word)

    except Exception as e:
        return str(e)

@app.route('/get_add_human_to_experiment', methods=["GET"])
def get_add_alien_to_experiment():
    try:
        id_experiment, id_alien = request.args.get('id_experiment', ''), \
            request.args.get('id_alien', '')
            
        conn = psycopg2.connect(
            "dbname=db1 user=team1 password=password1 host=142.93.163.88 port=6006")
        word = add_alien_to_experiment(conn, id_experiment, id_alien)
        return jsonify(result=word)

    except Exception as e:
        return str(e)



if __name__ == "__main__":
    app.run()

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', debug=False, port=os.environ.get('PORT', 80))
