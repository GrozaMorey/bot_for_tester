"""add expired

Revision ID: c2dafaf725a0
Revises: bbd11736e329
Create Date: 2023-08-11 02:52:51.963879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2dafaf725a0'
down_revision = 'bbd11736e329'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('expired', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'expired')
    # ### end Alembic commands ###
