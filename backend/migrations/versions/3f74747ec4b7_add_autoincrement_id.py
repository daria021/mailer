"""add autoincrement id

Revision ID: 3f74747ec4b7
Revises: d65fdbfa9353
Create Date: 2024-08-15 00:28:19.097923

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f74747ec4b7'
down_revision: Union[str, None] = 'd65fdbfa9353'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
