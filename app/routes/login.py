from flask import Blueprint

login_bp = Blueprint('login', __name__)


@login_bp.route('/login')

def register():
    return '''
  <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Iniciar Sesión - Sistema de Registro Facial</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: white;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 2rem;
        }

        header {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background-color: rgba(0, 0, 0, 0.3);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
            z-index: 100;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
        }

        nav ul {
            display: flex;
            list-style: none;
        }

        nav ul li {
            margin-left: 1.5rem;
        }

        nav ul li a {
            color: white;
            text-decoration: none;
            transition: color 0.3s;
        }

        nav ul li a:hover {
            color: #00e1ff;
        }

        .container {
            max-width: 450px;
            width: 100%;
            margin: 4rem auto;
        }

        .form-container {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 2.5rem;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        h1 {
            text-align: center;
            margin-bottom: 2rem;
            font-size: 2.2rem;
            color: white;
            text-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }

        input {
            width: 100%;
            padding: 0.8rem 1rem;
            border: 1px solid rgba(255, 255, 255, 0.2);
            background: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            color: white;
            font-size: 1rem;
            transition: all 0.3s;
        }

        input:focus {
            outline: none;
            border-color: #00c6ff;
            background: rgba(255, 255, 255, 0.15);
            box-shadow: 0 0 0 3px rgba(0, 198, 255, 0.2);
        }

        input::placeholder {
            color: rgba(255, 255, 255, 0.6);
        }

        .forgot-password {
            text-align: right;
            margin-top: -0.5rem;
            margin-bottom: 1.5rem;
        }

        .forgot-password a {
            color: rgba(255, 255, 255, 0.8);
            text-decoration: none;
            font-size: 0.9rem;
            transition: color 0.3s;
        }

        .forgot-password a:hover {
            color: #00e1ff;
            text-decoration: underline;
        }

        .btn {
            display: block;
            width: 100%;
            background: #00c6ff;
            color: white;
            padding: 0.9rem;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.3s;
            border: none;
            cursor: pointer;
            font-size: 1rem;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0, 198, 255, 0.3);
        }

        .btn:hover {
            background: #00e1ff;
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0, 198, 255, 0.4);
        }

        .divider {
            display: flex;
            align-items: center;
            margin: 2rem 0;
            color: rgba(255, 255, 255, 0.7);
        }

        .divider::before,
        .divider::after {
            content: "";
            flex: 1;
            height: 1px;
            background: rgba(255, 255, 255, 0.2);
        }

        .divider span {
            padding: 0 1rem;
        }

        .social-login {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 1rem;
        }

        .social-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.1);
            color: white;
            font-size: 1.2rem;
            transition: all 0.3s;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .social-btn:hover {
            transform: translateY(-3px);
            background: rgba(255, 255, 255, 0.2);
        }

        .google:hover {
            color: #DB4437;
        }

        .github:hover {
            color: #f0f6fc;
        }

        .facebook:hover {
            color: #4267B2;
        }

        .twitter:hover {
            color: #1DA1F2;
        }

        .register-link {
            text-align: center;
            margin-top: 1.5rem;
            color: rgba(255, 255, 255, 0.8);
        }

        .register-link a {
            color: #00e1ff;
            text-decoration: none;
            font-weight: 500;
        }

        .register-link a:hover {
            text-decoration: underline;
        }

        footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(0, 0, 0, 0.3);
            padding: 1rem;
            text-align: center;
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.7);
        }

        @media (max-width: 768px) {
            .container {
                padding: 1rem;
            }
            
            .form-container {
                padding: 1.5rem;
            }
            
            h1 {
                font-size: 1.8rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">FaceReg</div>
        <nav>
            <ul>
                <li><a href="index.html">Inicio</a></li>
                <li><a href="#">Características</a></li>
                <li><a href="#">Cómo Funciona</a></li>
                <li><a href="#">Contacto</a></li>
            </ul>
        </nav>
    </header>

    <div class="container">
        <h1>Iniciar Sesión</h1>
        <div class="form-container">
            <form id="login-form">
                <div class="form-group">
                    <label for="correo">Correo Electrónico</label>
                    <input type="email" id="correo" name="correo" placeholder="ejemplo@correo.com" required>
                </div>
                
                <div class="form-group">
                    <label for="password">Contraseña</label>
                    <input type="password" id="password" name="password" placeholder="Ingresa tu contraseña" required>
                </div>
                
                <div class="forgot-password">
                    <a href="#">¿Olvidaste tu contraseña?</a>
                </div>
                
                <button type="submit" class="btn">Iniciar Sesión</button>
            </form>
            
            <div class="divider">
                <span>O inicia sesión con</span>
            </div>
            
            <div class="social-login">
                <a href="#" class="social-btn google">
                    <i class="fab fa-google"></i>
                </a>
                <a href="#" class="social-btn github">
                    <i class="fab fa-github"></i>
                </a>
                <a href="#" class="social-btn facebook">
                    <i class="fab fa-facebook-f"></i>
                </a>
                <a href="#" class="social-btn twitter">
                    <i class="fab fa-twitter"></i>
                </a>
            </div>
            
            <div class="register-link">
                ¿No tienes una cuenta? <a href="/register">Regístrate</a>
            </div>
        </div>
    </div>

    <footer>
        &copy; 2025 Sistema de Registro Facial. Todos los derechos reservados.
    </footer>

    <script>
        document.getElementById('login-form').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Aquí iría el código para validar y enviar los datos de inicio de sesión
            alert('Inicio de sesión exitoso! Redirigiendo...');
            
            // Redirección simulada
            setTimeout(() => {
                window.location.href = 'index.html';
            }, 1500);
        });
    </script>
</body>
</html>
    '''