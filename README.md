# AgroSFT

AgroSFT es una plataforma Django + Vue/Vite para gestión de inventario, ventas, clientes y usuarios con roles.

## Estado actual

- Login con roles mediante `is_staff` / `is_superuser`.
- CRUD en inventario, ventas y clientes.
- SPA parcial con Vue en frontend (`frontend/src`).
- Alertas documentadas y parte de la interfaz.
- Bootstrap ahora se sirve localmente desde `static/vendor/bootstrap/`.
- Validaciones regex aplicadas en formularios de usuario.
- Seguridad reforzada con `@login_required`, middleware de seguridad y validaciones de campo.

> Nota: la bitácora de trabajo no fue incluida por solicitud expresa.

## Características implementadas

- Login y manejo de roles.
- CRUD completo de productos e inventario.
- Rutas protegidas con autenticación.
- Bootstrap local (sin CDN) en la plantilla base.
- Validaciones de teléfono, correo y contraseña con regex.
- Documentación técnica en `docs/`.
- Diagramas de patrones en `docs/design_patterns.puml`.

## Instalación

1. Crear y activar entorno virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

3. Iniciar servidor Django:

```powershell
.venv\Scripts\python.exe manage.py runserver
```

4. Abrir en el navegador:

```text
http://127.0.0.1:8000/
```

## Archivos clave

- `templates/base.html`: ahora usa Bootstrap local.
- `static/vendor/bootstrap/css/bootstrap.min.css`
- `static/vendor/bootstrap/js/bootstrap.bundle.min.js`
- `apps/usuarios/forms/auth_forms.py`: validaciones regex.
- `docs/ARCHITECTURE.md`: arquitectura y patrones.
- `docs/design_patterns.puml`: diagramas PlantUML.

## Documentación

- `docs/ARCHITECTURE.md`
- `docs/REQUIREMENTS.md`
- `docs/USER_STORIES.md`
- `docs/CHANGELOG.md`
- `docs/PROJECT_CONTEXT.md`

## Observaciones

- El proyecto requiere configuración de base de datos MySQL/MariaDB para funcionar plenamente.
