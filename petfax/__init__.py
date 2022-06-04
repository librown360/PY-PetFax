from flask import Flask

# factory
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def Hello():
        return 'Hello, PetFax!'

    # register pet blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    return app

