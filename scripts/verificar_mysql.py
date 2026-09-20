import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

def verificar_conexion():
    try:
        conexion = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        print("✅ Conexión MySQL correcta")
        print(f"📦 Base de datos: {os.getenv('DB_NAME')}")
        cursor = conexion.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()[0]
        print(f"🔧 Versión MySQL: {version}")
        conexion.close()
        return True
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

if __name__ == "__main__":
    verificar_conexion()