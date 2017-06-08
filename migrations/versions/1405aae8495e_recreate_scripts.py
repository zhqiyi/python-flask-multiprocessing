"""recreate scripts

Revision ID: 1405aae8495e
Revises: 76f28dc9db68
Create Date: 2017-06-08 16:23:39.574438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1405aae8495e'
down_revision = '76f28dc9db68'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
