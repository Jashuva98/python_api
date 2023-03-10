"""empty message

Revision ID: ce186ebc0be4
Revises: 236c01592c43
Create Date: 2022-12-21 14:24:00.739258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce186ebc0be4'
down_revision = '236c01592c43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('participants', sa.Column('event_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'participants', 'events', ['event_id'], ['event_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'participants', type_='foreignkey')
    op.drop_column('participants', 'event_id')
    # ### end Alembic commands ###
