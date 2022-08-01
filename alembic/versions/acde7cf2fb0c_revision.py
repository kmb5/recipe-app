"""revision

Revision ID: acde7cf2fb0c
Revises: 85b3c9fdad54
Create Date: 2022-08-01 12:06:45.249436

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'acde7cf2fb0c'
down_revision = '85b3c9fdad54'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ingredient', 'id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    op.alter_column('recipe', 'id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)
    op.alter_column('user', 'id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True,
               existing_server_default=sa.text("nextval('user_id_seq'::regclass)"))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True,
               existing_server_default=sa.text("nextval('user_id_seq'::regclass)"))
    op.alter_column('recipe', 'id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    op.alter_column('ingredient', 'id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###