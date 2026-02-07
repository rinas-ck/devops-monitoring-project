from flask import Flask, render_template_string
import socket
import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Project</title>
    <style>
        body {
            font-family: Arial;
            background: linear-gradient(to right,#141e30,#243b55);
            color: white;
            text-align: center;
            padding: 50px;
        }

        .card {
            background: #1f2933;
            padding: 30px;
            border-radius: 15px;
            width: 70%;
            margin: auto;
            box-shadow: 0px 0px 20px black;
        }

        h1 { color: #38bdf8; }

        .badge {
            background: #22c55e;
            padding: 8px 15px;
            border-radius: 20px;
            font-weight: bold;
        }

        footer {
            margin-top: 40px;
            color: #aaa;
        }
    </style>
</head>

<body>

<div class="card">

<h1>🚀 DevOps CI/CD Project</h1>

<p class="badge">LIVE DEPLOYMENT SUCCESS</p>

<p><b>Server:</b> {{host}}</p>
<p><b>Time:</b> {{date}}</p>

<hr>

<h3>Technology Stack</h3>

<p>AWS | Docker | Terraform | GitHub Actions | Prometheus | Grafana</p>

<p>✅ Application Running<br>
✅ Pipeline Active<br>
✅ Monitoring Enabled</p>

</div>

<footer>
Built by Rinas | DevOps Engineer 💻
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        HTML,
        host=socket.gethostname(),
        date=datetime.datetime.now()
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
