from flask import Blueprint

home_bp = Blueprint('home_bp', __name__)

@home_bp.route("/")
def home():
    return """
   <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Registro Facial - Seminario 2</title>
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
        }

        header {
            background-color: rgba(0, 0, 0, 0.3);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
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
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
            text-align: center;
        }

        .hero {
            margin: 3rem 0;
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
            text-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
        }

        p {
            font-size: 1.1rem;
            max-width: 800px;
            margin: 0 auto 2rem;
            line-height: 1.6;
            opacity: 0.9;
        }

        .btn {
            display: inline-block;
            background: #00c6ff;
            color: white;
            padding: 0.8rem 2rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.3s;
            border: none;
            cursor: pointer;
            font-size: 1rem;
            box-shadow: 0 4px 15px rgba(0, 198, 255, 0.3);
        }

        .btn:hover {
            background: #00e1ff;
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0, 198, 255, 0.4);
        }

        /* Carrusel de imágenes */
        .carousel {
            max-width: 800px;
            margin: 3rem auto;
            position: relative;
            overflow: hidden;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        }

        .carousel-inner {
            display: flex;
            transition: transform 0.5s ease;
        }

        .carousel-item {
            min-width: 100%;
            height: 400px;
            background-size: cover;
            background-position: center;
        }

        .carousel-caption {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(0, 0, 0, 0.6);
            padding: 1rem;
            text-align: center;
        }

        .carousel-controls {
            position: absolute;
            top: 50%;
            width: 100%;
            display: flex;
            justify-content: space-between;
            transform: translateY(-50%);
        }

        .carousel-control {
            background: rgba(0, 0, 0, 0.5);
            color: white;
            border: none;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            font-size: 1.5rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 1rem;
            transition: background 0.3s;
        }

        .carousel-control:hover {
            background: rgba(0, 0, 0, 0.8);
        }

        .carousel-indicators {
            position: absolute;
            bottom: 20px;
            left: 0;
            right: 0;
            display: flex;
            justify-content: center;
            gap: 10px;
            z-index: 10;
        }

        .indicator {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.5);
            cursor: pointer;
            transition: background 0.3s;
        }

        .indicator.active {
            background: white;
        }

        .features {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 2rem;
            margin: 3rem 0;
        }

        .feature {
            background: rgba(255, 255, 255, 0.1);
            padding: 2rem;
            border-radius: 10px;
            flex: 1;
            min-width: 250px;
            max-width: 350px;
            backdrop-filter: blur(10px);
            transition: transform 0.3s;
        }

        .feature:hover {
            transform: translateY(-10px);
        }

        .feature h3 {
            margin-bottom: 1rem;
            color: #00e1ff;
        }

        footer {
            background: rgba(0, 0, 0, 0.3);
            padding: 2rem;
            text-align: center;
            margin-top: 3rem;
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">FaceReg</div>
        <nav>
            <ul>
                <li><a href="#">Inicio</a></li>
                <li><a href="#">Características</a></li>
                <li><a href="#">Cómo Funciona</a></li>
                <li><a href="#">Contacto</a></li>
            </ul>
        </nav>
    </header>

    <div class="container">
        <div class="hero">
            <h1>Bienvenido al Sistema de Registro Facial - Seminario 2</h1>
            <p>Nuestro sistema de reconocimiento facial de última generación proporciona una forma segura y eficiente de registrar asistencia y acceso a instalaciones.</p>
            <a href="/register" class="btn">Ir al Registro</a>
        </div>

        <div class="carousel">
            <div class="carousel-inner" id="carousel-inner">
                <div class="carousel-item" style="background-image: url('/placeholder.svg?height=400&width=800')"></div>
                <div class="carousel-item" style="background-image: url('/placeholder.svg?height=400&width=800')"></div>
                <div class="carousel-item" style="background-image: url('/placeholder.svg?height=400&width=800')"></div>
            </div>
            
            <div class="carousel-controls">
                <button class="carousel-control" onclick="prevSlide()">&#10094;</button>
                <button class="carousel-control" onclick="nextSlide()">&#10095;</button>
            </div>
            
            <div class="carousel-indicators" id="carousel-indicators">
                <span class="indicator active" onclick="goToSlide(0)"></span>
                <span class="indicator" onclick="goToSlide(1)"></span>
                <span class="indicator" onclick="goToSlide(2)"></span>
            </div>
        </div>

        <div class="features">
            <div class="feature">
                <h3>Reconocimiento Rápido</h3>
                <p>Nuestro sistema identifica rostros en menos de 1 segundo con una precisión del 99.8%.</p>
            </div>
            <div class="feature">
                <h3>Seguridad Avanzada</h3>
                <p>Protección de datos biométricos con encriptación de nivel militar.</p>
            </div>
            <div class="feature">
                <h3>Fácil Integración</h3>
                <p>Compatible con sistemas existentes y bases de datos institucionales.</p>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; 2025 Sistema de Registro Facial. Todos los derechos reservados.</p>
    </footer>

    <script>
        let currentSlide = 0;
        const slides = document.querySelectorAll('.carousel-item');
        const indicators = document.querySelectorAll('.indicator');
        const totalSlides = slides.length;
        
        updateCarousel();
        
        function updateCarousel() {
            document.getElementById('carousel-inner').style.transform = `translateX(-${currentSlide * 100}%)`;
            indicators.forEach((indicator, index) => {
                indicator.classList.toggle('active', index === currentSlide);
            });
        }

        function nextSlide() {
            currentSlide = (currentSlide + 1) % totalSlides;
            updateCarousel();
        }

        function prevSlide() {
            currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
            updateCarousel();
        }

        function goToSlide(slideIndex) {
            currentSlide = slideIndex;
            updateCarousel();
        }

        setInterval(nextSlide, 5000);
    </script>
</body>
</html>

    """

