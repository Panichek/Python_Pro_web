"""Add a column

Revision ID: ce4f326563c8
Revises: d6160594255d
Create Date: 2023-08-23 11:08:06.685862

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ce4f326563c8'
down_revision: Union[str, None] = 'd6160594255d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
