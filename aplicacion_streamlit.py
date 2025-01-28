# mineriadedatos
import streamlit as st
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np

def preprocess_image(image):
  image = image.convert('L') #Convertir a escala de grises
  image = image.resize((28,28))
  image_array = img_to_array(image) / 255.0
  image_array = np.expand_dims(image_array, axis=0)
  return image_array
  
def main():
  st.title("Clasificación de la base de datos mnist")
  st.markdown("Sube una imagen para clasificar")

  uploaded_file = st.file_uploader("Selecciona una imagen (PNG, JPG, JPEG)", type = ["jpg", "png", "jpeg"])
  if uploaded_file is not None:
    image = image.open(uploaded_file)
    st.image(image, caption = "Imagen cargada")

    preprocessed_image = preprocess_image(image)
    st.image(preprocess_image, caption = "Imagen cargada")

      if st.button("Clasificar imagen"):
  st.markdown("Imagen clasificada")

if __name__ == "__main__":
  main()

