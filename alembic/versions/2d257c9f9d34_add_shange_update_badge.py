"""add shange update badge

Revision ID: 2d257c9f9d34
Revises: 6b00929902e8
Create Date: 2023-08-18 17:57:06.770299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d257c9f9d34'
down_revision = '6b00929902e8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'update_badge')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('update_badge', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
