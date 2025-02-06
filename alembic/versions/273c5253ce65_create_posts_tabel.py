"""create posts tabel

Revision ID: 273c5253ce65
Revises: 
Create Date: 2025-01-01 11:47:43.813996

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '273c5253ce65'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("posts",
    sa.Column('id',sa.Integer,nullable=False,primary_key=True),
    sa.Column('title',sa.String,nullable=False))

    pass

    


def downgrade() -> None:
    op.drop_table("posts")

    pass
