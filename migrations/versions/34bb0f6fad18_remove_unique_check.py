"""Remove unique check

Revision ID: 34bb0f6fad18
Revises: 50e79e826739
Create Date: 2023-07-14 15:58:54.727873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34bb0f6fad18'
down_revision = '50e79e826739'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cat_of_the_day', schema=None) as batch_op:
        batch_op.drop_constraint('cat_of_the_day_uploader_pk_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cat_of_the_day', schema=None) as batch_op:
        batch_op.create_unique_constraint('cat_of_the_day_uploader_pk_key', ['uploader_pk'])

    # ### end Alembic commands ###