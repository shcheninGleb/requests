"""empty message

Revision ID: 3f6d659c2373
Revises: 
Create Date: 2022-07-20 18:42:51.615473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f6d659c2373'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
    'city',
    sa.Column('id', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table("city")
