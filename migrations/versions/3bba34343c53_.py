"""empty message

Revision ID: 3bba34343c53
Revises: 
Create Date: 2019-11-27 21:41:32.007500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bba34343c53'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_username', table_name='user')
    op.drop_table('user')
    op.drop_index('ix_submission_timestamp', table_name='submission')
    op.drop_table('submission')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('submission',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('score', sa.FLOAT(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_submission_timestamp', 'submission', ['timestamp'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=64), nullable=True),
    sa.Column('email', sa.VARCHAR(length=120), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_user_username', 'user', ['username'], unique=1)
    op.create_index('ix_user_email', 'user', ['email'], unique=1)
    # ### end Alembic commands ###