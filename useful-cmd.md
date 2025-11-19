# Activer le virtual env
## Windows 

`<Nom_du_Venv>\Scripts\activate` ou `source <Nom_du_Venv>/Scripts/activate`

## MacOs/Linux

`source <Nom_du_Venv>/bin/activate`

# Desactiver le virtual env

`deactivate`

# Update les dependances 

`pip freeze > requirements.txt`

# Lancer un fichier 

`python -m <racine>.<dossier>.<fichier_sans_extension>`

exemple : `python -m backend.src.etl.test`

# Lancer un test pytest

`pytest -q <racine>/<folder>/<fichier>.py -q`
