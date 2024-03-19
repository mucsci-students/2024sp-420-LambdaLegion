from Models.uml_diagram import UML_Diagram
from Models.error_handler import Error_Handler
from Models.uml_parser import parse
from Views.cli_view import CLI_View

class CLI_Controller:

    def __init__(self, diagram:UML_Diagram = UML_Diagram(), saved:bool = False):
        self._diagram = diagram
        self._should_quit = False
    
    def update(self, input:str):
        if len(input.strip()) > 0:
            data = parse(self._diagram, input)
            if not hasattr(CLI_View, str(input[:4])):
                return data[0](*data[1:])
            #print help menu
            print(data[0](*data[1:]))

    

