"""empty message

Revision ID: 29ed574acaa1
Revises: 1b4ef83725ff
Create Date: 2020-12-10 05:19:54.974283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29ed574acaa1'
down_revision = '1b4ef83725ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('signers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('signers')
    # ### end Alembic commands ###
