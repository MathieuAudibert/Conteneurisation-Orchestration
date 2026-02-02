---
icon: lucide/square-terminal
---

# Usefull commands :lucide-terminal:

This is a list of usefull commands you might wanna use

## Activate Virtual env

=== "Windows :fontawesome-brands-windows:"
    ```cmd
    <VENV_NAME>\Scripts\activate
    ```
    or
    ```bash 
    source <VENV_NAME>/Scripts/activate
    ```
    

=== "Macos :simple-apple: /Linux :simple-linux:"
    ```bash
    source <VENV_NAME>/bin/activate
    ```

## Disactivate Virtual env

```bash
deactivate
```

## Install dependencies

```python
pip install -e .
``` 

Optionnal dependencies 

```python
pip install -e ".["dev"]"
```

## Update dependencies

Add in the [pyproject.toml](../../pyproject.toml) the dependencies

## Run a file

```python
python -m <ROOT>.<FOLDER>.<FILE_NO_EXTENSION>
```

example : 
```python
python -m backend.src.etl.test
```

## Run a pytest file

```bash
pytest -q <racine>/<folder>/<fichier>.py -q
```

## Run the doc w/ a defined port

````bash
zensical serve -a localhost:<PORT>
```