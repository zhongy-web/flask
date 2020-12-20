"""empty message

Revision ID: fec34b6907da
Revises: ec04f2abee30
Create Date: 2020-12-18 20:00:37.181395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fec34b6907da'
down_revision = 'ec04f2abee30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('signout',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('signout_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('signers', sa.Column('signout_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('signers', 'signout_time')
    op.drop_table('signout')
    # ### end Alembic commands ###
