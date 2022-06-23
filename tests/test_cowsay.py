import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src.index import app
client = app.test_client()
    
def test_root_path():
    response = client.get('/')
    assert b'I do not understand' in response.data
    
def test_text_param():
    response = client.get('/?text=Hello%20World')
    assert b'Hello World' in response.data
