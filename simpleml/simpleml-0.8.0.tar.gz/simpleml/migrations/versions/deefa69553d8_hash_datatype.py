"""hash datatype

Revision ID: deefa69553d8
Revises: 0680f18b52ca
Create Date: 2019-01-22 20:17:27.981443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'deefa69553d8'
down_revision = '9df691c76c63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('datasets') as batch_op:
        batch_op.alter_column('hash',
                              existing_type=sa.BIGINT(),
                              type_=sa.String(),
                              existing_nullable=False)
    with op.batch_alter_table('metrics') as batch_op:
        batch_op.alter_column('hash',
                              existing_type=sa.BIGINT(),
                              type_=sa.String(),
                              existing_nullable=False)
    with op.batch_alter_table('models') as batch_op:
        batch_op.alter_column('hash',
                              existing_type=sa.BIGINT(),
                              type_=sa.String(),
                              existing_nullable=False)
    with op.batch_alter_table('pipelines') as batch_op:
        batch_op.alter_column('hash',
                              existing_type=sa.BIGINT(),
                              type_=sa.String(),
                              existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pipelines', 'hash',
                    existing_type=sa.String(),
                    type_=sa.BIGINT(),
                    existing_nullable=False,
                    postgresql_using='hash::bigint')
    op.alter_column('models', 'hash',
                    existing_type=sa.String(),
                    type_=sa.BIGINT(),
                    existing_nullable=False,
                    postgresql_using='hash::bigint')
    op.alter_column('metrics', 'hash',
                    existing_type=sa.String(),
                    type_=sa.BIGINT(),
                    existing_nullable=False,
                    postgresql_using='hash::bigint')
    op.alter_column('datasets', 'hash',
                    existing_type=sa.String(),
                    type_=sa.BIGINT(),
                    existing_nullable=False,
                    postgresql_using='hash::bigint')
    # ### end Alembic commands ###
