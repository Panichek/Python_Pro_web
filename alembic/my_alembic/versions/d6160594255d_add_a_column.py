"""Add a column

Revision ID: d6160594255d
Revises: d2a6d2021f5e
Create Date: 2023-08-23 11:05:42.932894

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd6160594255d'
down_revision: Union[str, None] = 'd2a6d2021f5e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
