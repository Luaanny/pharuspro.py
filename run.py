from app import create_app
from app.Controllers.admin_controller import create_admin

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
