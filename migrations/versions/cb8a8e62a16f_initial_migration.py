"""Initial migration

Revision ID: cb8a8e62a16f
Revises: 
Create Date: 2023-12-30 21:37:31.089626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb8a8e62a16f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('administrators',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('email')
    )
    op.create_table('users',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('email')
    )
    op.create_table('cats',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('create_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('passport_id', sa.String(length=255), nullable=True),
    sa.Column('microchip_id', sa.String(length=255), nullable=True),
    sa.Column('photo_url', sa.String(length=255), nullable=False),
    sa.Column('breed', sa.String(length=255), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.Column('dislikes', sa.Integer(), nullable=True),
    sa.Column('votes', sa.Integer(), nullable=True),
    sa.Column('user_pk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_pk'], ['users.pk'], ),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('user_pk')
    )
    op.create_table('cats_of_the_week',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('create_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('passport_id', sa.String(length=255), nullable=False),
    sa.Column('microchip_id', sa.String(length=255), nullable=False),
    sa.Column('photo_url', sa.String(length=255), nullable=False),
    sa.Column('breed', sa.String(length=255), nullable=True),
    sa.Column('user_pk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_pk'], ['users.pk'], ),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_table('votes_history',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('voter_pk', sa.Integer(), nullable=True),
    sa.Column('cat_pk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cat_pk'], ['cats.pk'], ),
    sa.ForeignKeyConstraint(['voter_pk'], ['users.pk'], ),
    sa.PrimaryKeyConstraint('pk')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes_history')
    op.drop_table('cats_of_the_week')
    op.drop_table('cats')
    op.drop_table('users')
    op.drop_table('administrators')
    # ### end Alembic commands ###
