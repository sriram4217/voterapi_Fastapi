"""last few coloums to_post_tabel 

Revision ID: 25fbde1c96e6
Revises: e7e3293c38f2
Create Date: 2025-01-02 12:34:42.479977

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25fbde1c96e6'
down_revision: Union[str, None] = 'e7e3293c38f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
