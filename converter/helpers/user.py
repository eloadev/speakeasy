from converter.models import User


def is_admin(user):
    return user.role == User.Role.ADMIN


def is_authenticated(user):
    return user.is_authenticated
