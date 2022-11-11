from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_auth_register_true():
    response = client.post(
        "/auth/register",
        json={
            "username": "new_test1",
            "email": "new_test1@mail.ru",
            "name": "new",
            "password": "new",
            "phone_number": "89372436091",
            "birth": "26-11-2002",
            "sex": "MALE"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "detail": "Successfully save data!"
    }


def test_auth_register_exist():
    response = client.post(
        "/auth/register",
        json={
            "username": "new_test1",
            "email": "new_test@mail.ru",
            "name": "new",
            "password": "new",
            "phone_number": "89372436091",
            "birth": "26-11-2002",
            "sex": "MALE"
        },
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Username already exists!"
    }


def test_auth_register_exist_username():
    response = client.post(
        "/auth/register",
        json={
            "username": "new_test1",
            "email": "new@mail.ru",
            "name": "new",
            "password": "new",
            "phone_number": "89372436091",
            "birth": "26-11-2002",
            "sex": "MALE"
        },
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Username already exists!"
    }


def test_auth_register_email():
    response = client.post(
        "/auth/register",
        json={
            "username": "new111",
            "email": "new@mail.ru",
            "name": "new",
            "password": "new",
            "phone_number": "89372436091",
            "birth": "26-11-2002",
            "sex": "MALE"
        },
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Email already exists!"
    }


def test_auth_register_sex():
    response = client.post(
        "/auth/register",
        json={
            "username": "new12",
            "email": "new12@mail.ru",
            "name": "new",
            "password": "new",
            "phone_number": "89372436091",
            "birth": "26-11-2002",
            "sex": "MALE123"
        },
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid input sex"
    }


def test_auth_register_phone():
    response = client.post(
        "/auth/register",
        json={
            "username": "new112",
            "email": "new112@mail.ru",
            "name": "new",
            "password": "new",
            "phone_number": "89372436091123123",
            "birth": "26-11-2002",
            "sex": "MALE"
        },
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid input phone number!"
    }


def test_login_true():
    response = client.post(
        "/auth/login",
        json={
            "username": "new1",
            "password": "new"
        },
    )
    assert response.status_code == 200


def test_login_not_exists_username():
    response = client.post(
        "/auth/login",
        json={
            "username": "new123123",
            "password": "new"
        },
    )
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Username not found !"
    }


def test_login_not_exists_password():
    response = client.post(
        "/auth/login",
        json={
            "username": "new1",
            "password": "new1"
        },
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid Password !"
    }


def test_forgot_pass_true():
    response = client.post(
        "/auth/forgot-password",
        json={
            "email": "new@mail.ru",
            "new_password": "newnew12"
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "detail": "Successfully update data!"
    }


def test_forgot_pass_email_not_exists():
    response = client.post(
        "/auth/forgot-password",
        json={
            "email": "new12312321@mail.ru",
            "new_password": "new"
        },
    )
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Email not found !"
    }


