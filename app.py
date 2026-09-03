import streamlit as st

st.title("Descifrador Python")
texto_cifrado = st.text_area("Pega aquí el texto cifrado:")

if st.button("Descifrar"):
    # Lógica de descifrado César básica
    descifrado = "".join([chr(ord(c) - 3) if c.isalpha() else c for c in texto_cifrado])
    st.success(f"Resultado: {descifrado}")
