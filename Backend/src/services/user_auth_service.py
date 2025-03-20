from src.models.users import User
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from src.utils.user_utils import generate_password_hash

from src.schemas.users import UserCreateModel


class UserService:
    async def get_user_by_email(self, email: str, session: AsyncSession):
        statement = select(User).where(User.email==email)
        result = await session.exec(statement)
        user = result.first()
        return user

    async def get_all_users(self, session: AsyncSession):
        statement_line = select(User)
        result = await session.exec(statement_line)
        return result

    async def user_exists(self, email: str, session: AsyncSession):
        user = await self.get_user_by_email(email, session)
        return True if user is not None else False

    async def create_user_acc(self, user_data: UserCreateModel, session: AsyncSession):
        user_data_dict = user_data.model_dump()
        new_user = User(**user_data_dict)
        new_user.password_hash = generate_password_hash(user_data_dict['password_hash'])
        session.add(new_user)
        await session.commit()
        return new_user