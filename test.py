from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict

from application import app # Import web app

def test_header_exists(dash_duo): # provides all test modules
    dash_duo.start_server(app) # starts server
    dash_duo.wait_for_element("#header", timeout=10) 
    # This waits for an HTML element with the ID #header to appear within 10 seconds of the app launching. "#" specifies id of element

def test_visulization(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#visualization", timeout=10)
    
def test_region_picker(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region_picker", timeout=10)