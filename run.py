from web_app import app, db
from web_app.schema import Sequence, Taxonomy

if __name__ == '__main__':
    db.create_all()
    app.run()