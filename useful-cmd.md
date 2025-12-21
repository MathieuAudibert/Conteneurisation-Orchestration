# Activer le virtual env
## Windows 

`<Nom_du_Venv>\Scripts\activate` ou `source <Nom_du_Venv>/Scripts/activate`

## MacOs/Linux

`source <Nom_du_Venv>/bin/activate`

# Desactiver le virtual env

`deactivate`

# Installer les dependances 

`pip install -e .` et les dependances optionnelles `pip install -e ".["dev"]"`

# Update les dependances 

rajoutez dans le pyproject.toml la nouvelle dependances dans dependencies

# Lancer un fichier 

`python -m <racine>.<dossier>.<fichier_sans_extension>`

exemple : `python -m backend.src.etl.test`

# Lancer un test pytest

`pytest -q <racine>/<folder>/<fichier>.py -q`

# Lancer la doc avec un port defini

`zensical serve -a localhost:<PORT>`