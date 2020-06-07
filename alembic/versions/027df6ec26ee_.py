"""empty message

Revision ID: 027df6ec26ee
Revises: 
Create Date: 2020-06-06 12:48:20.678895

"""

# revision identifiers, used by Alembic.
revision = '027df6ec26ee'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('renders',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('streamable_short', sa.String(length=8), nullable=True),
        sa.Column('state', sa.String(length=50), nullable=True),
        sa.Column('title', sa.String(length=255), nullable=True),
        sa.Column('gtv_match_id', sa.Integer(), nullable=True),
        sa.Column('map_number', sa.Integer(), nullable=True),
        sa.Column('client_num', sa.Integer(), nullable=True),
        sa.Column('start', sa.Integer(), nullable=True),
        sa.Column('end', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_renders'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('renders')
    # ### end Alembic commands ###