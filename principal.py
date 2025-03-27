import streamlit as st
from conexion import init_connection

# Función para inicializar la conexión
@st.cache_resource
def get_connection():
    return init_connection()
# Llamar a la función que obtiene la conexión
conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
