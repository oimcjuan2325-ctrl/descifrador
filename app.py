from flask import Flask, render_template_string, request

app = Flask(__name__)

# Plantilla HTML integrada para la interfaz visual
TEMPLATE = '''
<!doctype html>
<html lang="es">
<head><meta charset="utf-8"><title>Descifrador Web</title></head>
<body style="font-family: sans-serif; margin: 40px;">
    <h2>Herramientas de Descifrado Python</h2>
    <form method="POST">
        <textarea name="texto" rows="4" cols="40" placeholder="Pega aquí el texto cifrado..."></textarea><br><br>
        <input type="submit" value="Descifrar">
    </form>
    {% if resultado %}
        <h3>Resultado del análisis:</h3>
        <p style="background: #f4f4f4; padding: 10px; border-radius: 5px;">{{ resultado }}</p>
    {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = ""
    if request.method == "POST":
        texto_cifrado = request.form.get("texto", "")
        # Lógica de ejemplo: descifrado César básico (desplazamiento de 3 posiciones)
        descifrado = []
        for char in texto_cifrado:
            if char.isalpha():
                codigo = ord(char)
                base = ord('A') if char.isupper() else ord('a')
                descifrado.append(chr((codigo - base - 3) % 26 + base))
            else:
                descifrado.append(char)
        resultado = "".join(descifrado)
    return render_template_string(TEMPLATE, resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
