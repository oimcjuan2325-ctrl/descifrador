import streamlit as st

st.title("Descifrador Automático Multialgoritmo")
texto_cifrado = st.text_area("Pega aquí el texto cifrado para análisis masivo:")

def es_texto_espanol(texto):
    # Palabras muy comunes en español para puntuar la legibilidad
    palabras_clave = ["el", "la", "de", "que", "y", "en", "un", "ser", "se", "no", "haber", "por", "con", "su", "para", "como", "practica", "maestro"]
    texto_lower = texto.lower()
    return any(p in texto_lower for p in palabras_clave)

if st.button("Iniciar análisis exhaustivo"):
    encontrado = False
    
    with st.spinner("Probando algoritmos y combinaciones en segundo plano..."):
        # 1. Probar todas las variantes de César (0 a 25)
        for clave in range(1, 26):
            descifrado = []
            for c in texto_cifrado:
                if c.isalpha():
                    base = ord('A') if c.isupper() else ord('a')
                    descifrado.append(chr((ord(c) - base - clave) % 26 + base))
                else:
                    descifrado.append(c)
            resultado = "".join(descifrado)
            
            if es_texto_espanol(resultado):
                st.success(f"¡Coincidencia encontrada con César (Clave {clave})!")
                st.write(f"**Resultado:** {resultado}")
                encontrado = True
                break

        # 2. Probar Atbash (espejo del abecedario) si el César no dio resultado claro
        if not encontrado:
            atbash = []
            for c in texto_cifrado:
                if c.isalpha():
                    base = ord('A') if c.isupper() else ord('a')
                    atbash.append(chr(base + (25 - (ord(c) - base))))
                else:
                    atbash.append(c)
            resultado_atbash = "".join(atbash)
            if es_texto_espanol(resultado_atbash):
                st.success("¡Coincidencia encontrada con cifrado Atbash!")
                st.write(f"**Resultado:** {resultado_atbash}")
                encontrado = True

        if not encontrado:
            st.warning("No se ha encontrado un patrón claro con los métodos automáticos básicos introducidos.")
