"""add names column to posts table

Revision ID: b8ee95b1983b
Revises: af707ce753e7
Create Date: 2023-11-09 20:49:55.271897

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8ee95b1983b'
down_revision: Union[str, None] = 'af707ce753e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('names', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'names')
    pass
