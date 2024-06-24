"""create todos table

Revision ID: 75335f579a3e
Revises: 
Create Date: 2024-06-21 10:57:38.106598

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75335f579a3e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.execute("""
    create table todos(
        id bigserial primary key,
        name text,
        completed boolean not null default false
    )
    """)


def downgrade() -> None:
    op.execute("drop table todos;")
