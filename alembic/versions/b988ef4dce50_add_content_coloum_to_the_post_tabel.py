"""add content coloum to the post tabel

Revision ID: b988ef4dce50
Revises: 273c5253ce65
Create Date: 2025-01-01 15:50:47.332699

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b988ef4dce50'
down_revision: Union[str, None] = '273c5253ce65'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String,nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
