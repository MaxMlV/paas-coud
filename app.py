from flask import Flask, render_template

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='secret',
        PROJECT_NAME='paas-cloud'
    )
    
    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')

    import sites 

    app.register_blueprint(sites.bp)

    import virtual_machines

    app.register_blueprint(virtual_machines.bp)

    return app

