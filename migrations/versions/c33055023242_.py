"""empty message

Revision ID: c33055023242
Revises: 6283ad73afec
Create Date: 2020-12-14 04:24:48.663394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c33055023242'
down_revision = '6283ad73afec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('signers', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'signers', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'signers', type_='foreignkey')
    op.drop_column('signers', 'user_id')
    # ### end Alembic commands ###
