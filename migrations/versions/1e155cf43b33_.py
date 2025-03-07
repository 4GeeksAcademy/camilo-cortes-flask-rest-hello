"""empty message

Revision ID: 1e155cf43b33
Revises: 4a331e8cc17c
Create Date: 2025-02-23 13:30:01.162893

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e155cf43b33'
down_revision = '4a331e8cc17c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('starships')
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.drop_constraint('favorites_starships_id_fkey', type_='foreignkey')
        batch_op.drop_column('starships_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites', schema=None) as batch_op:
        batch_op.add_column(sa.Column('starships_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('favorites_starships_id_fkey', 'starships', ['starships_id'], ['id'])

    op.create_table('starships',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('model', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('passanger', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('cargo_capacity', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='starships_pkey')
    )
    # ### end Alembic commands ###
