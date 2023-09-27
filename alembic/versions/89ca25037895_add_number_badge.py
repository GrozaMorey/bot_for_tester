"""add number_badge

Revision ID: 89ca25037895
Revises: c2dafaf725a0
Create Date: 2023-08-11 02:56:24.712872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89ca25037895'
down_revision = 'c2dafaf725a0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('number_badge', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'number_badge')
    # ### end Alembic commands ###
