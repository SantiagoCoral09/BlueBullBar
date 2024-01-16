from app import app
from app.config.config import mail

if __name__ == '__main__':
    
    mail.init_app(app)
    app.run(
        # host='0.0.0.0'
    )