from web_app import app, db
import resources
from web_app.schema import Sequence, Taxonomy

if __name__ == '__main__':
    db.create_all()
    #resources.add_resources()
    app.run()