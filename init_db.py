# init_db.py

# Importer votre application Flask et l'instance SQLAlchemy
# Assurez-vous que 'app' est le nom de votre application Flask
# et que 'db' est l'instance SQLAlchemy (ex: db = SQLAlchemy(app))
from app import app, db

# Importez vos modèles si nécessaire, par exemple :
# from app import Eleve, Professeur, Classe # Si vos modèles sont définis dans app.py

with app.app_context():
    # Crée toutes les tables définies dans vos modèles SQLAlchemy
    db.create_all()
    print("Toutes les tables de la base de données ont été créées avec succès !")
