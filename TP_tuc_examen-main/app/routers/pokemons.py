from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter,  Depends
from app import actions, schemas
from app.utils.utils import get_db
from app.utils.pokeapi import *
router = APIRouter()


@router.get("/", response_model=List[schemas.Pokemon])
def get_pokemons(skip: int = 0, limit: int = 100, database: Session = Depends(get_db)):
    """
        Return all pokemons
        Default limit is 100
    """
    pokemons = actions.get_pokemons(database, skip=skip, limit=limit)
    return pokemons

@router.get("/battle")
def get_battle_pokemon(first_poke_api_id, second_poke_api_id):
    """
        Return the winner pokemon between 2
    """ 
    return battle_pokemon(first_poke_api_id, second_poke_api_id)


@router.get("/random")
def get_three_random_pokemon():
    """
        Return 3 random pokemons
    """
    return generate_three_random_pokemon()
