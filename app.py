from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

users = {
    "carat": "123456",
    "svt": "05260214"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/carat-island')
def carat_island():
    return render_template('carat_island.html')

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        return jsonify({"code":200,"msg":"💎 登录成功！欢迎回到 CARAT TTT"})
    return jsonify({"code":400,"msg":"❌ 用户名或密码错误"})

@app.route('/api/register', methods=['POST'])
def api_register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    confirm_pwd = data.get('confirm_pwd')

    if not username or not password or not confirm_pwd:
        return jsonify({"code":400,"msg":"❌ 请填写完整信息"})
    if password != confirm_pwd:
        return jsonify({"code":400,"msg":"❌ 两次密码不一致"})
    if username in users:
        return jsonify({"code":400,"msg":"❌ 用户名已被使用"})

    users[username] = password
    return jsonify({"code":200,"msg":"💎 注册成功！快去登录吧～"})
