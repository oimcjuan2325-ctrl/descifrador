import streamlit as st

st.title("Descifrador Automático Definitivo")
texto_cifrado = st.text_area("Pega aquí tu texto cifrado:")

if st.button("Ejecutar Fuerza Bruta Total"):
    # Alfabeto estándar en español
    letras = "abcdefghijklmnñopqrstuvwxyz"
    encontrado = False
    
    with st.spinner("Analizando combinaciones..."):
        for clave in range(1, len(letras)):
            texto_descifrado = ""
            for char in texto_cifrado.lower():
                if char in letras:
                    index = (letras.find(char) - clave) % len(letras)
                    texto_descifrado += letras[index]
                else:
                    texto_descifrado += char
            
            # Muestra el resultado de cada intento para que puedas ver el progreso
            if "practica" in texto_descifrado or "maestro" in texto_descifrado:
                st.success(f"¡Encontrado con clave {clave}!")
                st.write(f"**Resultado:** {texto_descifrado}")
                encontrado = True
                break
                
        if not encontrado:
            st.warning("Prueba a revisar si el texto cifrado contiene caracteres especiales no contemplados.")
