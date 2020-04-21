from flask import Blueprint, render_template, jsonify, request
from flask_restful import Api

blueprint = Blueprint('flask_api',
                      __name__,
                      template_folder='flask_api',
                      url_prefix='/api')

api_route = Api(blueprint)
blueprint = Blueprint('flask_api',
                      __name__,
                      template_folder='flask_api')
# url_prefix='/api')
api_route = Api(blueprint)


@blueprint.route('/')
def get_index():
    return 'Hello world'
    # return render_template('index.html', title='Vehicle information')


@blueprint.route('/hello')
def get_hello_world():
    return 'Hello world 2'
    # return render_template('index.html', title='Vehicle information')
