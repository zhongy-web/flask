"""empty message

Revision ID: 3b1d4b45d817
Revises: c33055023242
Create Date: 2020-12-14 04:44:14.553905

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3b1d4b45d817'
down_revision = 'c33055023242'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('signers_ibfk_1', 'signers', type_='foreignkey')
    op.drop_column('signers', 'user_id')
    op.add_column('users', sa.Column('signer_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'signers', ['signer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'signer_id')
    op.add_column('signers', sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('signers_ibfk_1', 'signers', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###
