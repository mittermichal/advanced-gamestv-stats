"""empty message

Revision ID: 3d584460aeb9
Revises: e2e6df884138
Create Date: 2017-02-20 15:19:10.661673

"""

# revision identifiers, used by Alembic.
revision = '3d584460aeb9'
down_revision = 'e2e6df884138'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    #op.add_column('renders',sa.Column('player_id', sa.Integer(),sa.ForeignKey('players.id'), nullable=True))
    return


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'renders', type_='foreignkey')
    op.drop_column('renders', 'player_id')
    op.drop_table('players')
    ### end Alembic commands ###
