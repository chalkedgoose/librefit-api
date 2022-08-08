from optparse import Option
from src.dao.User import User
from typing import List, Optional


class UserRepo:
    """
     Repository for interacting with user data.
    """

    USER_MOCK_DB = [
        User(1, "Carlos", age=22),
        User(2, "Haley", age=21),
        User(3, "Charles", age=20),
        User(4, "Shadi", age=20)
    ]

    def get_users(self) -> List[User]:
        return self.USER_MOCK_DB

    def get_user_by_id(self, id: int) -> Optional[User]:
        return [user for user in self.get_users() if user.id == id][0] or None
