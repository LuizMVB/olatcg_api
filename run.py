import web_app
import resources
from web_app.schema import Sequence, Taxonomy

if __name__ == '__main__':
    web_app.db.create_all()
    resources.add_resources()
    web_app.app.run(debug=True)