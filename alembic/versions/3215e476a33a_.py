"""empty message

Revision ID: 3215e476a33a
Revises: 027df6ec26ee
Create Date: 2020-06-06 20:10:03.593143

"""

# revision identifiers, used by Alembic.
revision = '3215e476a33a'
down_revision = '027df6ec26ee'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('renders', sa.Column('progress', sa.SmallInteger(), nullable=True))
    op.add_column('renders', sa.Column('status_msg', sa.String(length=50), nullable=True))
    with op.batch_alter_table('renders') as batch_op:
        batch_op.drop_column('state')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('renders', sa.Column('state', sa.VARCHAR(length=50), nullable=True))
    with op.batch_alter_table('renders') as batch_op:
        batch_op.drop_column('status_msg')
    with op.batch_alter_table('renders') as batch_op:
        batch_op.drop_column('progress')
    # ### end Alembic commands ###
