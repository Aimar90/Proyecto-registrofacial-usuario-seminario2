from flask import Blueprint

user_bp = Blueprint('user', __name__)


@user_bp.route('/user')

def register():
    return '''
 <!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Administración de Usuarios - Sistema de Registro Facial</title>
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
        }

        .admin-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
        }

        h1 {
            font-size: 2.2rem;
            text-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
        }

        .search-bar {
            display: flex;
            align-items: center;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50px;
            padding: 0.5rem 1rem;
            width: 300px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }

        .search-bar input {
            background: transparent;
            border: none;
            color: white;
            width: 100%;
            padding: 0.5rem;
            outline: none;
        }

        .search-bar input::placeholder {
            color: rgba(255, 255, 255, 0.6);
        }

        .search-bar i {
            color: rgba(255, 255, 255, 0.6);
        }

        .btn {
            background: #00c6ff;
            color: white;
            padding: 0.7rem 1.5rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.3s;
            border: none;
            cursor: pointer;
            font-size: 1rem;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            box-shadow: 0 4px 15px rgba(0, 198, 255, 0.3);
        }

        .btn:hover {
            background: #00e1ff;
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(0, 198, 255, 0.4);
        }

        .btn-danger {
            background: #ff3860;
            box-shadow: 0 4px 15px rgba(255, 56, 96, 0.3);
        }

        .btn-danger:hover {
            background: #ff526f;
            box-shadow: 0 6px 20px rgba(255, 56, 96, 0.4);
        }

        .btn-warning {
            background: #ffdd57;
            color: #333;
            box-shadow: 0 4px 15px rgba(255, 221, 87, 0.3);
        }

        .btn-warning:hover {
            background: #ffe066;
            box-shadow: 0 6px 20px rgba(255, 221, 87, 0.4);
        }

        .btn-small {
            padding: 0.4rem 0.8rem;
            font-size: 0.9rem;
        }

        .card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin-bottom: 2rem;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 1rem;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            overflow: hidden;
        }

        th, td {
            padding: 1rem;
            text-align: left;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }

        th {
            background: rgba(0, 0, 0, 0.2);
            font-weight: 600;
            color: rgba(255, 255, 255, 0.9);
        }

        tr:hover {
            background: rgba(255, 255, 255, 0.1);
        }

        .actions {
            display: flex;
            gap: 0.5rem;
        }

        .action-btn {
            width: 35px;
            height: 35px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(255, 255, 255, 0.1);
            color: white;
            border: none;
            cursor: pointer;
            transition: all 0.3s;
        }

        .action-btn:hover {
            transform: translateY(-2px);
        }

        .view-btn {
            background: rgba(0, 198, 255, 0.2);
        }

        .view-btn:hover {
            background: rgba(0, 198, 255, 0.4);
        }

        .edit-btn {
            background: rgba(255, 221, 87, 0.2);
        }

        .edit-btn:hover {
            background: rgba(255, 221, 87, 0.4);
        }

        .delete-btn {
            background: rgba(255, 56, 96, 0.2);
        }

        .delete-btn:hover {
            background: rgba(255, 56, 96, 0.4);
        }

        .pagination {
            display: flex;
            justify-content: center;
            gap: 0.5rem;
            margin-top: 2rem;
        }

        .page-item {
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            cursor: pointer;
            transition: all 0.3s;
        }

        .page-item:hover, .page-item.active {
            background: rgba(0, 198, 255, 0.3);
        }

        /* Modal */
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.7);
            z-index: 1000;
            overflow: auto;
            backdrop-filter: blur(5px);
        }

        .modal-content {
            background: linear-gradient(135deg, #203a43, #2c5364);
            margin: 5% auto;
            padding: 2rem;
            border-radius: 15px;
            max-width: 600px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.1);
            position: relative;
        }

        .close {
            position: absolute;
            top: 1rem;
            right: 1.5rem;
            font-size: 1.5rem;
            cursor: pointer;
            transition: color 0.3s;
        }

        .close:hover {
            color: #ff3860;
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }

        input, select {
            width: 100%;
            padding: 0.8rem 1rem;
            border: 1px solid rgba(255, 255, 255, 0.2);
            background: rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            color: white;
            font-size: 1rem;
            transition: all 0.3s;
        }

        input:focus, select:focus {
            outline: none;
            border-color: #00c6ff;
            background: rgba(255, 255, 255, 0.15);
            box-shadow: 0 0 0 3px rgba(0, 198, 255, 0.2);
        }

        .modal-footer {
            display: flex;
            justify-content: flex-end;
            gap: 1rem;
            margin-top: 2rem;
        }

        .user-details {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
        }

        .detail-item {
            margin-bottom: 1rem;
        }

        .detail-label {
            font-size: 0.9rem;
            color: rgba(255, 255, 255, 0.7);
            margin-bottom: 0.3rem;
        }

        .detail-value {
            font-size: 1.1rem;
            font-weight: 500;
        }

        .user-avatar {
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.2);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.5rem;
            margin: 0 auto 2rem;
            color: white;
        }

        .status-badge {
            display: inline-block;
            padding: 0.3rem 0.8rem;
            border-radius: 50px;
            font-size: 0.8rem;
            font-weight: 500;
        }

        .status-active {
            background: rgba(72, 199, 142, 0.2);
            color: #48c78e;
        }

        .status-inactive {
            background: rgba(241, 70, 104, 0.2);
            color: #f14668;
        }

        .status-pending {
            background: rgba(255, 221, 87, 0.2);
            color: #ffdd57;
        }

        .empty-state {
            text-align: center;
            padding: 3rem;
        }

        .empty-state i {
            font-size: 4rem;
            margin-bottom: 1rem;
            opacity: 0.5;
        }

        .empty-state h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }

        .empty-state p {
            color: rgba(255, 255, 255, 0.7);
            margin-bottom: 2rem;
        }

        footer {
            background: rgba(0, 0, 0, 0.3);
            padding: 1.5rem;
            text-align: center;
            margin-top: 2rem;
        }

        @media (max-width: 768px) {
            .container {
                padding: 1rem;
            }
            
            .admin-header {
                flex-direction: column;
                align-items: flex-start;
                gap: 1rem;
            }
            
            .search-bar {
                width: 100%;
            }
            
            table {
                display: block;
                overflow-x: auto;
            }
            
            .user-details {
                grid-template-columns: 1fr;
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
                <li><a href="#">Dashboard</a></li>
                <li><a href="#" class="active">Usuarios</a></li>
                <li><a href="#">Configuración</a></li>
            </ul>
        </nav>
    </header>

    <div class="container">
        <div class="admin-header">
            <h1>Administración de Usuarios</h1>
            <div class="search-bar">
                <input type="text" id="search-input" placeholder="Buscar usuario...">
                <i class="fas fa-search"></i>
            </div>
            <button class="btn" id="add-user-btn">
                <i class="fas fa-plus"></i> Nuevo Usuario
            </button>
        </div>

        <div class="card">
            <table id="users-table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nombre</th>
                        <th>Apellidos</th>
                        <th>Correo</th>
                        <th>Estado</th>
                        <th>Fecha Registro</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody id="users-table-body">
                    <!-- Los datos de usuarios se cargarán dinámicamente -->
                </tbody>
            </table>
            <div id="empty-state" class="empty-state" style="display: none;">
                <i class="fas fa-users-slash"></i>
                <h3>No se encontraron usuarios</h3>
                <p>No hay usuarios registrados o ninguno coincide con tu búsqueda.</p>
                <button class="btn" id="add-first-user-btn">
                    <i class="fas fa-plus"></i> Agregar Usuario
                </button>
            </div>
        </div>

        <div class="pagination" id="pagination">
            <!-- La paginación se generará dinámicamente -->
        </div>
    </div>

    <!-- Modal para Crear/Editar Usuario -->
    <div id="user-modal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <h2 id="modal-title">Nuevo Usuario</h2>
            <form id="user-form">
                <input type="hidden" id="user-id">
                <div class="form-group">
                    <label for="nombre">Nombre</label>
                    <input type="text" id="nombre" name="nombre" required>
                </div>
                <div class="form-group">
                    <label for="apellidos">Apellidos</label>
                    <input type="text" id="apellidos" name="apellidos" required>
                </div>
                <div class="form-group">
                    <label for="correo">Correo Electrónico</label>
                    <input type="email" id="correo" name="correo" required>
                </div>
                <div class="form-group">
                    <label for="password">Contraseña</label>
                    <input type="password" id="password" name="password">
                    <small style="color: rgba(255,255,255,0.6); display: block; margin-top: 0.5rem;">
                        Dejar en blanco para mantener la contraseña actual (solo en edición).
                    </small>
                </div>
                <div class="form-group">
                    <label for="estado">Estado</label>
                    <select id="estado" name="estado" required>
                        <option value="activo">Activo</option>
                        <option value="inactivo">Inactivo</option>
                        <option value="pendiente">Pendiente</option>
                    </select>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-danger" id="cancel-btn">Cancelar</button>
                    <button type="submit" class="btn" id="save-btn">Guardar</button>
                </div>
            </form>
        </div>
    </div>

    <!-- Modal para Ver Detalles de Usuario -->
    <div id="view-modal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <h2>Detalles del Usuario</h2>
            <div class="user-avatar" id="user-avatar"></div>
            <div class="user-details" id="user-details">
                <!-- Los detalles del usuario se cargarán dinámicamente -->
            </div>
            <div class="modal-footer">
                <button type="button" class="btn" id="close-view-btn">Cerrar</button>
            </div>
        </div>
    </div>

    <!-- Modal de Confirmación para Eliminar -->
    <div id="delete-modal" class="modal">
        <div class="modal-content" style="max-width: 400px;">
            <span class="close">&times;</span>
            <h2>Confirmar Eliminación</h2>
            <p style="margin: 1.5rem 0;">¿Estás seguro de que deseas eliminar a este usuario? Esta acción no se puede deshacer.</p>
            <div class="modal-footer">
                <button type="button" class="btn" id="cancel-delete-btn">Cancelar</button>
                <button type="button" class="btn btn-danger" id="confirm-delete-btn">Eliminar</button>
            </div>
        </div>
    </div>

    <footer>
        &copy; 2025 Sistema de Registro Facial. Todos los derechos reservados.
    </footer>

    <script>
        // Datos de ejemplo para usuarios
        let users = [
            {
                id: 1,
                nombre: 'Juan',
                apellidos: 'Pérez González',
                correo: 'juan.perez@ejemplo.com',
                password: 'password123',
                estado: 'activo',
                fechaRegistro: '2025-03-15'
            },
            {
                id: 2,
                nombre: 'María',
                apellidos: 'López Rodríguez',
                correo: 'maria.lopez@ejemplo.com',
                password: 'password123',
                estado: 'activo',
                fechaRegistro: '2025-03-18'
            },
            {
                id: 3,
                nombre: 'Carlos',
                apellidos: 'Sánchez Martínez',
                correo: 'carlos.sanchez@ejemplo.com',
                password: 'password123',
                estado: 'inactivo',
                fechaRegistro: '2025-02-10'
            },
            {
                id: 4,
                nombre: 'Ana',
                apellidos: 'Martín Jiménez',
                correo: 'ana.martin@ejemplo.com',
                password: 'password123',
                estado: 'pendiente',
                fechaRegistro: '2025-04-01'
            },
            {
                id: 5,
                nombre: 'Roberto',
                apellidos: 'Fernández Díaz',
                correo: 'roberto.fernandez@ejemplo.com',
                password: 'password123',
                estado: 'activo',
                fechaRegistro: '2025-01-25'
            }
        ];

        // Variables para paginación
        const itemsPerPage = 5;
        let currentPage = 1;
        let filteredUsers = [...users];

        // Referencias a elementos DOM
        const userModal = document.getElementById('user-modal');
        const viewModal = document.getElementById('view-modal');
        const deleteModal = document.getElementById('delete-modal');
        const userForm = document.getElementById('user-form');
        const modalTitle = document.getElementById('modal-title');
        const usersTableBody = document.getElementById('users-table-body');
        const paginationContainer = document.getElementById('pagination');
        const searchInput = document.getElementById('search-input');
        const emptyState = document.getElementById('empty-state');

        // Botones
        const addUserBtn = document.getElementById('add-user-btn');
        const addFirstUserBtn = document.getElementById('add-first-user-btn');
        const cancelBtn = document.getElementById('cancel-btn');
        const closeViewBtn = document.getElementById('close-view-btn');
        const cancelDeleteBtn = document.getElementById('cancel-delete-btn');
        const confirmDeleteBtn = document.getElementById('confirm-delete-btn');

        // Variable para almacenar el ID del usuario a eliminar
        let userToDeleteId = null;

        // Inicializar la aplicación
        document.addEventListener('DOMContentLoaded', () => {
            renderUsers();
            setupEventListeners();
        });

        // Configurar los event listeners
        function setupEventListeners() {
            // Botones para abrir modales
            addUserBtn.addEventListener('click', () => openUserModal());
            addFirstUserBtn.addEventListener('click', () => openUserModal());
            
            // Cerrar modales
            document.querySelectorAll('.close').forEach(closeBtn => {
                closeBtn.addEventListener('click', closeAllModals);
            });
            
            cancelBtn.addEventListener('click', closeAllModals);
            closeViewBtn.addEventListener('click', closeAllModals);
            cancelDeleteBtn.addEventListener('click', closeAllModals);
            
            // Formulario de usuario
            userForm.addEventListener('submit', handleUserFormSubmit);
            
            // Búsqueda
            searchInput.addEventListener('input', handleSearch);
            
            // Eliminar usuario
            confirmDeleteBtn.addEventListener('click', deleteUser);
            
            // Cerrar modales al hacer clic fuera de ellos
            window.addEventListener('click', (e) => {
                if (e.target === userModal || e.target === viewModal || e.target === deleteModal) {
                    closeAllModals();
                }
            });
        }

        // Renderizar la tabla de usuarios
        function renderUsers() {
            const startIndex = (currentPage - 1) * itemsPerPage;
            const paginatedUsers = filteredUsers.slice(startIndex, startIndex + itemsPerPage);
            
            if (filteredUsers.length === 0) {
                document.getElementById('users-table').style.display = 'none';
                emptyState.style.display = 'block';
            } else {
                document.getElementById('users-table').style.display = 'table';
                emptyState.style.display = 'none';
                
                usersTableBody.innerHTML = '';
                
                paginatedUsers.forEach(user => {
                    const row = document.createElement('tr');
                    
                    // Determinar la clase de estado
                    let statusClass = '';
                    switch(user.estado) {
                        case 'activo':
                            statusClass = 'status-active';
                            break;
                        case 'inactivo':
                            statusClass = 'status-inactive';
                            break;
                        case 'pendiente':
                            statusClass = 'status-pending';
                            break;
                    }
                    
                    row.innerHTML = `
                        <td>${user.id}</td>
                        <td>${user.nombre}</td>
                        <td>${user.apellidos}</td>
                        <td>${user.correo}</td>
                        <td><span class="status-badge ${statusClass}">${capitalizeFirstLetter(user.estado)}</span></td>
                        <td>${formatDate(user.fechaRegistro)}</td>
                        <td class="actions">
                            <button class="action-btn view-btn" data-id="${user.id}" title="Ver detalles">
                                <i class="fas fa-eye"></i>
                            </button>
                            <button class="action-btn edit-btn" data-id="${user.id}" title="Editar usuario">
                                <i class="fas fa-edit"></i>
                            </button>
                            <button class="action-btn delete-btn" data-id="${user.id}" title="Eliminar usuario">
                                <i class="fas fa-trash-alt"></i>
                            </button>
                        </td>
                    `;
                    
                    usersTableBody.appendChild(row);
                });
                
                // Agregar event listeners a los botones de acción
                document.querySelectorAll('.view-btn').forEach(btn => {
                    btn.addEventListener('click', () => viewUser(parseInt(btn.dataset.id)));
                });
                
                document.querySelectorAll('.edit-btn').forEach(btn => {
                    btn.addEventListener('click', () => editUser(parseInt(btn.dataset.id)));
                });
                
                document.querySelectorAll('.delete-btn').forEach(btn => {
                    btn.addEventListener('click', () => confirmDeleteUser(parseInt(btn.dataset.id)));
                });
            }
            
            renderPagination();
        }

        // Renderizar la paginación
        function renderPagination() {
            const totalPages = Math.ceil(filteredUsers.length / itemsPerPage);
            paginationContainer.innerHTML = '';
            
            if (totalPages <= 1) {
                return;
            }
            
            // Botón anterior
            const prevBtn = document.createElement('div');
            prevBtn.className = 'page-item';
            prevBtn.innerHTML = '<i class="fas fa-chevron-left"></i>';
            prevBtn.addEventListener('click', () => {
                if (currentPage > 1) {
                    currentPage--;
                    renderUsers();
                }
            });
            paginationContainer.appendChild(prevBtn);
            
            // Páginas
            for (let i = 1; i <= totalPages; i++) {
                const pageBtn = document.createElement('div');
                pageBtn.className = `page-item ${i === currentPage ? 'active' : ''}`;
                pageBtn.textContent = i;
                pageBtn.addEventListener('click', () => {
                    currentPage = i;
                    renderUsers();
                });
                paginationContainer.appendChild(pageBtn);
            }
            
            // Botón siguiente
            const nextBtn = document.createElement('div');
            nextBtn.className = 'page-item';
            nextBtn.innerHTML = '<i class="fas fa-chevron-right"></i>';
            nextBtn.addEventListener('click', () => {
                if (currentPage < totalPages) {
                    currentPage++;
                    renderUsers();
                }
            });
            paginationContainer.appendChild(nextBtn);
        }

        // Abrir modal para crear/editar usuario
        function openUserModal(userId = null) {
            modalTitle.textContent = userId ? 'Editar Usuario' : 'Nuevo Usuario';
            userForm.reset();
            
            if (userId) {
                const user = users.find(u => u.id === userId);
                if (user) {
                    document.getElementById('user-id').value = user.id;
                    document.getElementById('nombre').value = user.nombre;
                    document.getElementById('apellidos').value = user.apellidos;
                    document.getElementById('correo').value = user.correo;
                    document.getElementById('estado').value = user.estado;
                    // No establecemos la contraseña por seguridad
                }
            } else {
                document.getElementById('user-id').value = '';
            }
            
            userModal.style.display = 'block';
        }

        // Manejar el envío del formulario de usuario
        function handleUserFormSubmit(e) {
            e.preventDefault();
            
            const userId = document.getElementById('user-id').value;
            const userData = {
                nombre: document.getElementById('nombre').value,
                apellidos: document.getElementById('apellidos').value,
                correo: document.getElementById('correo').value,
                estado: document.getElementById('estado').value
            };
            
            if (userId) {
                // Actualizar usuario existente
                const userIndex = users.findIndex(u => u.id === parseInt(userId));
                if (userIndex !== -1) {
                    // Si se proporciona una nueva contraseña, actualizarla
                    const password = document.getElementById('password').value;
                    if (password) {
                        userData.password = password;
                    } else {
                        userData.password = users[userIndex].password;
                    }
                    
                    users[userIndex] = {
                        ...users[userIndex],
                        ...userData
                    };
                    
                    showNotification('Usuario actualizado correctamente');
                }
            } else {
                // Crear nuevo usuario
                const newId = users.length > 0 ? Math.max(...users.map(u => u.id)) + 1 : 1;
                const password = document.getElementById('password').value || 'defaultPassword123';
                
                const newUser = {
                    id: newId,
                    ...userData,
                    password: password,
                    fechaRegistro: new Date().toISOString().split('T')[0]
                };
                
                users.push(newUser);
                showNotification('Usuario creado correctamente');
            }
            
            closeAllModals();
            filteredUsers = [...users];
            renderUsers();
        }

        // Ver detalles de usuario
        function viewUser(userId) {
            const user = users.find(u => u.id === userId);
            if (!user) return;
            
            const userDetails = document.getElementById('user-details');
            const userAvatar = document.getElementById('user-avatar');
            
            // Iniciales para el avatar
            const initials = `${user.nombre.charAt(0)}${user.apellidos.charAt(0)}`;
            userAvatar.textContent = initials;
            
            // Generar detalles del usuario
            userDetails.innerHTML = `
                <div class="detail-item">
                    <div class="detail-label">ID</div>
                    <div class="detail-value">${user.id}</div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">Nombre Completo</div>
                    <div class="detail-value">${user.nombre} ${user.apellidos}</div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">Correo Electrónico</div>
                    <div class="detail-value">${user.correo}</div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">Estado</div>
                    <div class="detail-value">
                        <span class="status-badge ${getStatusClass(user.estado)}">
                            ${capitalizeFirstLetter(user.estado)}
                        </span>
                    </div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">Fecha de Registro</div>
                    <div class="detail-value">${formatDate(user.fechaRegistro)}</div>
                </div>
                <div class="detail-item">
                    <div class="detail-label">Última Actualización</div>
                    <div class="detail-value">No disponible</div>
                </div>
            `;
            
            viewModal.style.display = 'block';
        }

        // Editar usuario
        function editUser(userId) {
            openUserModal(userId);
        }

        // Confirmar eliminación de usuario
        function confirmDeleteUser(userId) {
            userToDeleteId = userId;
            deleteModal.style.display = 'block';
        }

        // Eliminar usuario
        function deleteUser() {
            if (userToDeleteId) {
                users = users.filter(user => user.id !== userToDeleteId);
                filteredUsers = [...users];
                currentPage = 1;
                showNotification('Usuario eliminado correctamente');
                closeAllModals();
                renderUsers();
            }
        }

        // Manejar búsqueda
        function handleSearch() {
            const searchTerm = searchInput.value.toLowerCase();
            
            if (searchTerm === '') {
                filteredUsers = [...users];
            } else {
                filteredUsers = users.filter(user => 
                    user.nombre.toLowerCase().includes(searchTerm) ||
                    user.apellidos.toLowerCase().includes(searchTerm) ||
                    user.correo.toLowerCase().includes(searchTerm)
                );
            }
            
            currentPage = 1;
            renderUsers();
        }

        // Cerrar todos los modales
        function closeAllModals() {
            userModal.style.display = 'none';
            viewModal.style.display = 'none';
            deleteModal.style.display = 'none';
        }

        // Mostrar notificación (simulado)
        function showNotification(message) {
            alert(message);
        }

        // Funciones de utilidad
        function capitalizeFirstLetter(string) {
            return string.charAt(0).toUpperCase() + string.slice(1);
        }

        function formatDate(dateString) {
            const options = { year: 'numeric', month: 'long', day: 'numeric' };
            return new Date(dateString).toLocaleDateString('es-ES', options);
        }

        function getStatusClass(status) {
            switch(status) {
                case 'activo': return 'status-active';
                case 'inactivo': return 'status-inactive';
                case 'pendiente': return 'status-pending';
                default: return '';
            }
        }
    </script>
</body>
</html>
    '''