# from app import create_app, db

# app = create_app()

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)

from app import create_app, db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
