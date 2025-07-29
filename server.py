import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/KegenGuyll/api/dad-jokes'

mcp = FastMCP('dad-jokes')

@mcp.tool()
def random_jokes() -> dict: 
    '''Returns a joke object that contains a setup, punchline, type and id'''
    url = 'https://dad-jokes.p.rapidapi.com/random/joke'
    headers = {'x-rapidapi-host': 'dad-jokes.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def joke_count() -> dict: 
    '''returns number of jokes stored'''
    url = 'https://dad-jokes.p.rapidapi.com/joke/count'
    headers = {'x-rapidapi-host': 'dad-jokes.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def aijokes(jokeTopic: Annotated[str, Field(description='')]) -> dict: 
    '''Jokes powered by chat gpt'''
    url = 'https://dad-jokes.p.rapidapi.com/joke/ai/cow'
    headers = {'x-rapidapi-host': 'dad-jokes.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'jokeTopic': jokeTopic,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def joke_by_type(type: Annotated[str, Field(description='')]) -> dict: 
    '''you can search for a joke based on type.'''
    url = 'https://dad-jokes.p.rapidapi.com/joke/type/general'
    headers = {'x-rapidapi-host': 'dad-jokes.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search(term: Annotated[str, Field(description='')]) -> dict: 
    '''you can enter a term to search for a joke.'''
    url = 'https://dad-jokes.p.rapidapi.com/joke/search'
    headers = {'x-rapidapi-host': 'dad-jokes.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'term': term,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def joke_by_id(id: Annotated[str, Field(description='')]) -> dict: 
    '''Gets a specific by it's id'''
    url = 'https://dad-jokes.p.rapidapi.com/joke/5f80ccd641785ba7c7d27b66'
    headers = {'x-rapidapi-host': 'dad-jokes.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
