"""empty message

Revision ID: 19cef1d14917
Revises: 
Create Date: 2019-07-30 21:43:26.064115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19cef1d14917'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groceryItems',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=60), nullable=False),
    sa.Column('lastSold', sa.DateTime(), nullable=True),
    sa.Column('shelfLife', sa.String(length=5), nullable=False),
    sa.Column('department', sa.String(length=40), nullable=True),
    sa.Column('price', sa.String(length=20), nullable=False),
    sa.Column('unit', sa.String(length=10), nullable=False),
    sa.Column('xFor', sa.Integer(), nullable=False),
    sa.Column('cost', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('groceryItems')
    # ### end Alembic commands ###
