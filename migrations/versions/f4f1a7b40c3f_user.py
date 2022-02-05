"""user

Revision ID: f4f1a7b40c3f
Revises: b8884e60d4fd
Create Date: 2022-02-05 20:38:28.245571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4f1a7b40c3f'
down_revision = 'b8884e60d4fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=True)
    op.add_column('microblog_post', sa.Column('user', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'microblog_post', 'user', ['user'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'microblog_post', type_='foreignkey')
    op.drop_column('microblog_post', 'user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
