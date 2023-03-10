"""empty message

Revision ID: 236c01592c43
Revises: defc6fb8fb87
Create Date: 2022-12-07 18:45:41.542814

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '236c01592c43'
down_revision = 'defc6fb8fb87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('event_title', sa.String(length=256), nullable=False),
    sa.Column('event_venue', sa.String(length=256), nullable=False),
    sa.Column('event_address', sa.String(length=256), nullable=False),
    sa.Column('event_date', sa.String(length=128), nullable=False),
    sa.Column('event_time', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('event_id')
    )
    op.create_table('participants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(), nullable=False),
    sa.Column('designation', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('mobilenumber', sa.String(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('district', sa.String(), nullable=False),
    sa.Column('block', sa.String(), nullable=False),
    sa.Column('grampanchayat', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('mobilenumber')
    )
    op.create_table('tokenblocklist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('tokenblocklist', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_tokenblocklist_jti'), ['jti'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tokenblocklist', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_tokenblocklist_jti'))

    op.drop_table('tokenblocklist')
    op.drop_table('participants')
    op.drop_table('events')
    # ### end Alembic commands ###
