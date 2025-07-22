from flask import Flask, request, render_template_string, redirect
import json

app = Flask(__name__)

PASSWORD = "12345"

HTML_FORM = '''
<!DOCTYPE html>
<html>
<head>
    <title>Insta Bot Panel</title>
</head>
<body>
    <h2>Insta Takip Paneli</h2>
    <form method="POST">
        <label>Şifre:</label><br>
        <input type="password" name="password"><br><br>
        <label>Hedef Kullanıcı Adı (@kullanicinick):</label><br>
        <input type="text" name="username"><br><br>
        <label>Takip Sayısı:</label><br>
        <input type="number" name="amount"><br><br>
        <input type="submit" value="Sipariş Ver">
    </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def panel():
    if request.method == 'POST':
        if request.form.get('password') != PASSWORD:
            return "Hatalı şifre!"

        username = request.form.get('username')
        amount = int(request.form.get('amount'))

        with open("orders.json", "w") as f:
            json.dump({"username": username, "amount": amount}, f)

        return f"Sipariş oluşturuldu: @{username} - {amount} takipçi"

    return render_template_string(HTML_FORM)

if __name__ == '__main__':
    app.run(debug=True, port=5000)