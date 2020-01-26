"""followers

Revision ID: 63febf0cc2b2
Revises: cccfcd451d61
Create Date: 2020-01-11 19:24:37.500071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63febf0cc2b2'
down_revision = 'cccfcd451d61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
