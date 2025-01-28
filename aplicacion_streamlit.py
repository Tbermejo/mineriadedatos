# mineriadedatos
import streamlit as st
def main():
  st.title("Clasificación de la base de datos mnist")
  st.markdown("Sube una imagen para clasificar")

  uploaded_file = st.file_uploader("Selecciona una imagen (PNG, JPG, JPEG)", type = ["jpg", "png", "jpeg"])
  if uploaded_file is not None:
    image = image.open(uploaded_file)
    st.image(image, caption = "Imagen cargada")
if __name__ == "__main__":
  main()

