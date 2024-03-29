"""empty message

Revision ID: 2c40bdc99697
Revises: 19cef1d14917
Create Date: 2019-07-30 21:47:33.231953

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2c40bdc99697'
down_revision = '19cef1d14917'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grocery_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=60), nullable=False),
    sa.Column('last_sold', sa.DateTime(), nullable=True),
    sa.Column('shelf_life', sa.String(length=5), nullable=False),
    sa.Column('department', sa.String(length=40), nullable=True),
    sa.Column('price', sa.String(length=20), nullable=False),
    sa.Column('unit', sa.String(length=10), nullable=False),
    sa.Column('x_for', sa.Integer(), nullable=False),
    sa.Column('cost', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('groceryItems')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groceryItems',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"groceryItems_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('description', sa.VARCHAR(length=60), autoincrement=False, nullable=False),
    sa.Column('lastSold', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('shelfLife', sa.VARCHAR(length=5), autoincrement=False, nullable=False),
    sa.Column('department', sa.VARCHAR(length=40), autoincrement=False, nullable=True),
    sa.Column('price', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('unit', sa.VARCHAR(length=10), autoincrement=False, nullable=False),
    sa.Column('xFor', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('cost', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='groceryItems_pkey')
    )
    op.drop_table('grocery_items')
    # ### end Alembic commands ###
