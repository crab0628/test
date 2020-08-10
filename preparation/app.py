import sqlite3
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "Hello World."

@app.route("/<name>")
def greet(name):
    return name + "さん、こんにちは"

@app.route("/template")
def template():
    py_name = "サワガニ"
    return render_template("index.html", name = py_name)

@app.route("/hello")
def hello():
    return render_template("hello.html")
    
@app.route("/hi")
def hi():
    return render_template("hi.html")

@app.route("/weather")
def whether():
    py_weather = "くもり"
    return render_template("weather.html", weather = py_weather)

@app.route("/dbtest")
def dbtest():
    conn = sqlite3.connect("flasktest.db")
    c = conn.cursor()
# 課題1 誰か一人分の情報
    c.execute("SELECT name, age, address FROM staff WHERE id = 1")
    staff_info = c.fetchone() # fetchall()は複数行
    c.close()
    print(staff_info)
        

# 課題2 誰か一名の情報を表示するＨＴＭＬを作成し、表示（天気参照）
    return render_template("dbtest.html", staff_info = staff_info)



# todoリスト
@app.route("/task_list")
def task_list():
    conn = sqlite3.connect("tasklist.db")
    c = conn.cursor()

    c.execute("SELECT * FROM task")
    task_list = []

    for row in c.fetchall():
        task_list.append({"id":row[0], "task":row[1], "limit":row[2]})
    c.close()
    print(task_list)
        
    return render_template("tasklist.html", task_list = task_list)

# todo追加(GET)
@app.route("/add", methods=["GET"])
def add_get():
    return render_template("add.html")

# todo追加(POST)
@app.route("/add", methods=["POST"])
def add_post():
    name = request.form.get("task")
    limit = request.form.get("limit")
    conn = sqlite3.connect("tasklist.db")
    c = conn.cursor()
    c.execute("INSERT INTO task VALUES(null,?,?)",(name, limit))
    conn.comit()
    conn.close()
    print(task_list)
        
    return redirect("/task_list")

# タスク編集
@app.route("/edit<int:id>")
def edit(id):

    conn = sqlite3.connect("tasklist.db")
    c = conn.cursor()
    c.execute("select name,limit from task where id = ?",(id,))
    task = c.fetchone()
    conn.close()
    if task is not None:
        task = task[0]
        limit = task[1]
    else:
        return "タスクはありません"

    item = {"id":id, "task":task, "limit":limit}
        
    return render_template("edit.html", task = item)    
# 課題：edit.html作成




if __name__ == "__main__":
    app.run(debug=True)