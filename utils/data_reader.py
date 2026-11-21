
import csv
import json
from pathlib import Path


# Ruta principal del proyecto
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Carpeta donde se encuentran los datos externos
DATA_DIR = PROJECT_DIR / "test_data"


def load_users():
    """
    Lee los usuarios desde el archivo users.json.
    """
    file_path = DATA_DIR / "users.json"

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_user(user_type):
    """
    Obtiene un usuario específico del archivo JSON.
    """
    users = load_users()

    if user_type not in users:
        raise ValueError(
            f"El usuario '{user_type}' no existe en users.json"
        )

    return users[user_type]


def load_products():
    """
    Lee los productos desde el archivo products.csv.
    """
    file_path = DATA_DIR / "products.csv"

    with file_path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))
