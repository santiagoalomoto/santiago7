from flask import Flask

app = Flask(__name__)

# Página principal con un estilo moderno
@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Santiago | Flask + Traefik</title>
            <style>
                body {
                    margin: 0;
                    font-family: 'Segoe UI', sans-serif;
                    background: linear-gradient(135deg, #4f46e5, #06b6d4);
                    color: white;
                    height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }
                .card {
                    background: rgba(255, 255, 255, 0.15);
                    padding: 40px;
                    border-radius: 20px;
                    backdrop-filter: blur(10px);
                    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
                    text-align: center;
                    width: 450px;
                }
                h1 {
                    font-size: 32px;
                    margin-bottom: 10px;
                }
                p {
                    font-size: 18px;
                    opacity: 0.9;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Hola desde Flask con Traefik 🚀</h1>
                <p>Bienvenido a <strong>santiago.byronrm.com</strong></p>
            </div>
        </body>
    </html>
    """

# Ruta para saludar con una tarjeta bonita
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"""
    <html>
        <head>
            <title>Saludo</title>
            <style>
                body {{
                    margin: 0;
                    font-family: 'Segoe UI', sans-serif;
                    background: linear-gradient(135deg, #06b6d4, #4f46e5);
                    color: white;
                    height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }}
                .card {{
                    background: rgba(255, 255, 255, 0.15);
                    padding: 40px;
                    border-radius: 20px;
                    backdrop-filter: blur(10px);
                    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
                    text-align: center;
                    width: 450px;
                }}
                h2 {{
                    font-size: 30px;
                    margin-bottom: 10px;
                }}
                p {{
                    font-size: 18px;
                    opacity: 0.9;
                }}
            </style>
        </head>
        <body>
            <div class="card">
                <h2>Hola {nombre} 👋</h2>
                <p>Bienvenido a <strong>santiago.byronrm.com</strong></p>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
