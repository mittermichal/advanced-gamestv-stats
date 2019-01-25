"""empty message

Revision ID: 3719fb5b193a
Revises: 831471f4db93
Create Date: 2018-06-24 17:42:28.632666

"""

# revision identifiers, used by Alembic.
revision = '3719fb5b193a'
down_revision = '831471f4db93'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_constraint(None, 'players', type_='foreignkey')
    with op.batch_alter_table("players", recreate='always') as batch_op:
        batch_op.drop_column('client_num')
        batch_op.drop_column('player_id')
        batch_op.drop_column('match_id')
    with op.batch_alter_table("renders", recreate='always') as batch_op:
        batch_op.create_foreign_key('fk_renders_player_id_players', 'players', ['player_id'], ['id'])
    # ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    # with op.batch_alter_table("players", recreate='always') as batch_op:
    #    batch_op.drop_constraint(op.f('fk_renders_player_id_players'), 'renders', type_='foreignkey')
    op.add_column('players', sa.Column('match_id', sa.INTEGER(), nullable=True))
    op.add_column('players', sa.Column('player_id', sa.INTEGER(), nullable=True))
    op.add_column('players', sa.Column('client_num', sa.INTEGER(), nullable=True))
    with op.batch_alter_table("renders", recreate='always') as batch_op:
        batch_op.drop_constraint('fk_renders_player_id_players', type_="foreignkey")
    # op.create_foreign_key(None, 'players', 'players', ['player_id'], ['id'])
    # ### end Alembic commands ###
