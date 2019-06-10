# The json and pygments library will help with the pretty-printing of the JSON
import json
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

# Function for pretty printing JSON
def pretty_print_json(raw_json):
    print(highlight(json.dumps(raw_json, indent=4), JsonLexer(), TerminalFormatter()))

