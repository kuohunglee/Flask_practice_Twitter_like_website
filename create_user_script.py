from twittor import db, create_app
from twittor.models import User

def create_user(user, password):

    app = create_app()
    app.app_context().push()

    u = User(username=user, email=f'{user}@admin.com', about_me=f'{user} is the freshman of this social media!')

    u.set_password(password)

    db.session.add(u)
    db.session.commit()
    print(User.query.filter_by(username=user).first())
