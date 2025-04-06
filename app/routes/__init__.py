
from .home import home_bp 
from .usuarios import usuarios_bp 
from .register import register_bp
from .login import login_bp
from .user import user_bp
from .perfil import perfil_bp

def init_app(app):
    app.register_blueprint(home_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(register_bp) 
    app.register_blueprint(login_bp) 
    app.register_blueprint(user_bp) 
    app.register_blueprint(perfil_bp) 