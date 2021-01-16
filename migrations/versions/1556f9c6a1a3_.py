"""empty message

Revision ID: 1556f9c6a1a3
Revises: a7b49bcdab75
Create Date: 2021-01-16 18:24:42.069386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1556f9c6a1a3'
down_revision = 'a7b49bcdab75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('real_avatar', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'real_avatar')
    # ### end Alembic commands ###
