import streamlit as st

def mostrar_productos():
    st.header("Gestión de Productos")
    st.write("Bienvenido al módulo de productos.")
    st.info("Aquí se mostrará el inventario y catálogo de productos en el futuro.")
    
    # Un formulario visual de demostración
    with st.form("form_producto"):
        st.text_input("Nombre del nuevo producto")
        st.text_area("Descripción")
        st.form_submit_button("Guardar producto")
