"""rev1

Revision ID: d2a6d2021f5e
Revises: a8a36cf866e7
Create Date: 2023-08-23 10:58:23.252963

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd2a6d2021f5e'
down_revision: Union[str, None] = 'a8a36cf866e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
