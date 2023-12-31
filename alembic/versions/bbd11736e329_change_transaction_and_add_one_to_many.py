"""change transaction and add one to many

Revision ID: bbd11736e329
Revises: c8e3326a86b1
Create Date: 2023-08-10 18:01:04.829126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbd11736e329'
down_revision = 'c8e3326a86b1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('success_transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('telegram_payment_charge_id', sa.String(), nullable=True),
    sa.Column('provider_payment_charge_id', sa.String(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('transaction', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'transaction', 'users', ['user_id'], ['id'])
    op.drop_column('transaction', 'username')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transaction', sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'transaction', type_='foreignkey')
    op.drop_column('transaction', 'user_id')
    op.drop_table('success_transaction')
    # ### end Alembic commands ###
