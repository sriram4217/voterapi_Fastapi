"""add foregin-key to posts tabel

Revision ID: e7e3293c38f2
Revises: 7fa4bf574205
Create Date: 2025-01-01 19:10:06.547686

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e7e3293c38f2'
down_revision: Union[str, None] = '7fa4bf574205'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk',source_table="posts",referent_table="users",local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint(constraint_name='post_users_fk',table_name="posts")
    op.drop_column('posts','owner_id')
    
    pass
