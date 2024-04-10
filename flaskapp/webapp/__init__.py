from flask import Flask, render_template, request, jsonify

def not_found(e):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        response = jsonify({
            "Error": "Not Found"
        })
        response.status_code = 404
    return render_template("errors/404.html"), 404

def forbidden(e):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        response = jsonify({
            "Error": "Forbidden Access"
        })
        response.status_code = 403
    return render_template("errors/403.html"), 403

def internal_server(e):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        response = jsonify({
            "Error": "Internal server error"
        })
        response.status_code = 500
    return render_template("errors/500.html"), 500


def create_app(object):
    app = Flask(__name__.split('.')[0])
    app.config.from_object(object)
    
    from .main import create_module as main_create_module
    from .auth import create_module as auth_create_module
    
    main_create_module(app)
    auth_create_module(app)
    
    app.register_error_handler(403, forbidden)
    app.register_error_handler(404, not_found)
    app.register_error_handler(500, internal_server)
    
    return app
    
    
