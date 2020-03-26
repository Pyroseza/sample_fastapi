"""create user table

Revision ID: b18274474e71
Revises: 
Create Date: 2020-03-26 19:02:53.950302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b18274474e71'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('age', sa.Integer),
    )


def downgrade():
    op.drop_table('user')
