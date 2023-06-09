"""adding table

Revision ID: 12d06d7dd6d1
Revises: ef22a60c590b
Create Date: 2023-04-27 13:09:14.770402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12d06d7dd6d1'
down_revision = 'ef22a60c590b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('uri',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('origin', sa.String(), nullable=True),
    sa.Column('short_code', sa.String(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('origin')
    )
    op.create_index(op.f('ix_uri_id'), 'uri', ['id'], unique=False)
    op.create_index(op.f('ix_uri_short_code'), 'uri', ['short_code'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_uri_short_code'), table_name='uri')
    op.drop_index(op.f('ix_uri_id'), table_name='uri')
    op.drop_table('uri')
    # ### end Alembic commands ###
