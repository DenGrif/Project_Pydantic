"""Add slug column to User

Revision ID: a83491470d7f
Revises: 91ca65396b3e
Create Date: 2024-11-25 00:19:43.187645

"""
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'a83491470d7f'
down_revision = '91ca65396b3e'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('slug', sa.String(), nullable=False))
        batch_op.create_unique_constraint('uq_users_slug', ['slug'])


def downgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint('uq_users_slug', type_='unique')
        batch_op.drop_column('slug')


# from typing import Sequence, Union
#
# from alembic import op
# import sqlalchemy as sa
#
#
# # revision identifiers, used by Alembic.
# revision: str = 'a83491470d7f'
# down_revision: Union[str, None] = '91ca65396b3e'
# branch_labels: Union[str, Sequence[str], None] = None
# depends_on: Union[str, Sequence[str], None] = None
#
#
# def upgrade() -> None:
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.add_column('users', sa.Column('slug', sa.String(), nullable=False))
#     op.create_unique_constraint(None, 'users', ['slug'])
#     # ### end Alembic commands ###
#
#
# def downgrade() -> None:
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.drop_constraint(None, 'users', type_='unique')
#     op.drop_column('users', 'slug')
#     # ### end Alembic commands ###
