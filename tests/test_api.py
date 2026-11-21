
import logging
import requests


logger = logging.getLogger(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_api_get_post():
    """
    GET: consulta una publicación existente.
    """
    response = requests.get(
        f"{BASE_URL}/posts/1",
        timeout=15
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["userId"] == 1
    assert "title" in data
    assert "body" in data

    logger.info(
        "GET exitoso. Publicación consultada: %s",
        data["title"]
    )


def test_api_post():
    """
    POST: envía una nueva publicación.
    """
    new_post = {
        "title": "Prueba automatizada QA",
        "body": "Publicación creada mediante Requests y Pytest",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=new_post,
        timeout=15
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == new_post["title"]
    assert data["body"] == new_post["body"]
    assert data["userId"] == new_post["userId"]
    assert "id" in data

    logger.info(
        "POST exitoso. ID de publicación: %s",
        data["id"]
    )


def test_api_delete():
    """
    DELETE: solicita eliminar una publicación existente.
    """
    response = requests.delete(
        f"{BASE_URL}/posts/1",
        timeout=15
    )

    assert response.status_code == 200

    logger.info(
        "DELETE exitoso. Código HTTP: %s",
        response.status_code
    )
