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
        n_people, date_from, date_to = request.args.get('n_people', ''), \
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


if __name__ == "__main__":
    app.run()
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', debug=False, port=80)
