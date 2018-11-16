"""empty message

Revision ID: e471819bf7c1
Revises: 
Create Date: 2018-10-16 14:43:13.456294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e471819bf7c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city_letter',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('letter', sa.String(length=3), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=20), nullable=True),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('user_token', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('user_token'),
    sa.UniqueConstraint('username')
    )
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('parentId', sa.Integer(), nullable=True),
    sa.Column('regionName', sa.String(length=100), nullable=True),
    sa.Column('cityCode', sa.Integer(), nullable=True),
    sa.Column('pinYin', sa.String(length=50), nullable=True),
    sa.Column('letter_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['letter_id'], ['city_letter.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cityCode')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('city')
    op.drop_table('user')
    op.drop_table('city_letter')
    # ### end Alembic commands ###
