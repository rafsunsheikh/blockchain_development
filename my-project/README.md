### Use Poetry
```
poetry env activate
```

Copy the outout and paste in the terminal to activate the virtual environment

```
poetry run python <filename>
```
run the python file using the python

### Interact with the code using ipyton
```
ipython -i src/my-project/blockchain_0.0.py
```

### Networking
- Run the server
```
python my_server.py
```
- In the second terminal, connect to the server using nc
```
nc 127.0.0.1 8888
```
- or telnet on Windows
```
telnet 127.0.0.1 8888
```