import connexion
import six

from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def users_get():  # noqa: E501
    """List all users

    Returns a list of users # noqa: E501


    :rtype: List[User]
    """
    return 'do some magic!'


def users_post(body):  # noqa: E501
    """Create a new user

    Creates a new user with the provided data # noqa: E501

    :param body: User object that needs to be added
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_user_id_delete(user_id):  # noqa: E501
    """Delete a user

    Deletes a user identified by ID # noqa: E501

    :param user_id: ID of the user to delete
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def users_user_id_get(user_id):  # noqa: E501
    """Find user by ID

    Returns a single user # noqa: E501

    :param user_id: ID of user to return
    :type user_id: int

    :rtype: User
    """
    return 'do some magic!'


def users_user_id_put(body, user_id):  # noqa: E501
    """Update an existing user

    Updates an existing user identified by the ID # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param user_id: ID of user to update
    :type user_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
