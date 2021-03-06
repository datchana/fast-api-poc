"""third

Revision ID: b19a1b22dfd7
Revises: 8f518ec992a9
Create Date: 2021-08-16 18:24:36.510465

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b19a1b22dfd7'
down_revision = '8f518ec992a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'hashed_password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hashed_password', mysql.VARCHAR(length=30), nullable=True))
    # ### end Alembic commands ###
