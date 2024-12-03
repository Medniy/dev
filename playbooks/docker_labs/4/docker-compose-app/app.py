from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

# Конфигурация подключения к базе данных
DATABASE = {
    'dbname': 'test_db',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'db',
    'port': 5432
}

# Функция для подключения к базе данных
def get_db_connection():
    conn = psycopg2.connect(
        dbname=DATABASE['dbname'],
        user=DATABASE['user'],
        password=DATABASE['password'],
        host=DATABASE['host'],
        port=DATABASE['port']
    )
    return conn

# Главная страница
@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        # Получение данных из формы
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")

        try:
            # Уязвимый SQL-запрос для сохранения данных
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO users (name) VALUES ('{first_name} {last_name}');")  # Уязвимость
            conn.commit()
            cursor.close()
            conn.close()
            message = f"Регистрация успешна: {first_name} {last_name}"
        except Exception as e:
            message = f"Ошибка: {e}"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)