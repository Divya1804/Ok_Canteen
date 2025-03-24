"""Added role to user db.

Revision ID: 3897ece0c17d
Revises: cea518c2f289
Create Date: 2025-03-23 18:29:33.906363

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '3897ece0c17d'
down_revision: Union[str, None] = 'cea518c2f289'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('role', sa.VARCHAR(), server_default='USER', nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Users', 'role')
    # ### end Alembic commands ###
