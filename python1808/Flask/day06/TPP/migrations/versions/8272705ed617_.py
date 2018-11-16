"""empty message

Revision ID: 8272705ed617
Revises: e471819bf7c1
Create Date: 2018-10-16 15:04:04.617702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8272705ed617'
down_revision = 'e471819bf7c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('permission', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'permission')
    # ### end Alembic commands ###
