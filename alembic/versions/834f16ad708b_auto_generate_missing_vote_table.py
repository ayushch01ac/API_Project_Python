"""auto generate missing vote table

Revision ID: 834f16ad708b
Revises: 00a8b9277263
Create Date: 2023-11-09 21:35:45.246085

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '834f16ad708b'
down_revision: Union[str, None] = '00a8b9277263'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
