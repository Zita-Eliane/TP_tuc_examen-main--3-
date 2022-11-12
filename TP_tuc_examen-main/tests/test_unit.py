from http import client
from urllib import response
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends
from app.utils.utils import get_db
import pytest
from main import app
from random import randint
from app import actions
client = TestClient(app)


####################################
#           UNIT TESTS             #
####################################

# Test 1 
# Check the get trainers by name endpoint
def test_get_trainer_by_name():
    trainer_name = 'Alexis'
    response = client.get(f"/trainers/by_name/{trainer_name}")
    assert response.status_code == 200 
    assert response.json()['id'] == 2

# Test 2
# Check the get trainers endpoint
def test_get_trainers():
    response = client.get("/trainers")
    assert response.status_code == 200
    assert len(response.json()) > 0

# Test 3
# Check the get items endpoint
def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) > 0

# Test 4
# Check the get pokemons endpoint
def test_get_pokemon():
    response = client.get("/pokemons")
    assert response.status_code == 200
    assert len(response.json()) > 0

# Test 5
# Check the get trainer by id endpoint
def test_get_trainer():
    """
        Recuperation d'un trainer précis via id
    """
    response = client.get("trainers/2")
    assert response.status_code == 200
    assert response.json() == {"name": "Alexis", "birthdate": "2002-10-20", "id":2, "inventory": [], "pokemons": []}

# Test 6
# Check the get pokemon random endpoint : the 3 pokemons are different
def test_pokemons_random_different():
    """
        Recuperation de 3 pokemons aleatoires different
    """
    response = client.get("/pokemons/random/")
    assert response.status_code == 200
    assert response.json()[0]["name"] != response.json()[1]["name"] != response.json()[2]["name"]

# Test 7
# Check the get pokemon random endpoint : it return exactly 3 pokemons
def test_3_pokemons_random():
    """
        Recuperation d'exactement 3 pokemons aleatoires
    """
    response = client.get("/pokemons/random/")
    assert response.status_code == 200
    assert len(response.json()) == 3

