from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <body style="background:#111;color:white;
    font-family:Arial;text-align:center;padding:50px">
        <h1>IP LAB</h1>
        <h2>Моя первая лаборатория</h2>
        <p>Сервер успешно работает!</p>
        <a href="/test" style="color:cyan">Провести тест</a>
    </body>
    </html>
    """

@app.route("/test")
def test():
    print("Новый тестовый запрос!")
    print("Время:", datetime.now())
    print("IP:", request.remote_addr)
    print("Браузер:", request.headers.get("User-Agent"))
    return "<h1>Тест завершён!</h1>"

if __name__ == "__main__":

  app.run(host="0.0.0.0", port=5000, debug=False)
