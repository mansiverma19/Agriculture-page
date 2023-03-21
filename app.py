from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
  return render_template("main.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
  return render_template("register.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
  return render_template("login.html")


if __name__ == '__main__':
  app.run('0.0.0.0', debug=True)
