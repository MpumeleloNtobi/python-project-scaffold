import sys

# Add the project src directory tp the python search path
sys.path.insert(0, "src")

import hello

def test_hello():
    assert hello.hello() == "Hello, world!"
    assert hello.hello("Jane") == "Hello, Jane!"
    assert hello.hello("John") == "Hello, John!"
