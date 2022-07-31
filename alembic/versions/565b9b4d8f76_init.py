"""init

Revision ID: 565b9b4d8f76
Revises: b1898cf1a65e
Create Date: 2022-07-31 18:25:22.021859

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '565b9b4d8f76'
down_revision = 'b1898cf1a65e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ingredient', 'name',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    op.create_index(op.f('ix_ingredient_name'),
                    'ingredient', ['name'], unique=False)
    op.alter_column('recipe', 'name',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    op.alter_column('recipe', 'cooking_time_min',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    op.alter_column('recipe', 'num_people',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    op.alter_column('recipe', 'kcal',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    op.create_index(op.f('ix_recipe_name'), 'recipe', ['name'], unique=False)
    op.alter_column('recipeingredient', 'amount',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    op.alter_column('recipeingredient', 'unit',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    op.alter_column('user', 'username',
                    existing_type=sa.VARCHAR(length=256),
                    nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'username',
                    existing_type=sa.VARCHAR(length=256),
                    nullable=True)
    op.alter_column('user', 'id',
                    existing_type=sa.INTEGER(),
                    nullable=False,
                    autoincrement=True)
    op.alter_column('recipeingredient', 'unit',
                    existing_type=sa.VARCHAR(),
                    nullable=True)
    op.alter_column('recipeingredient', 'amount',
                    existing_type=sa.INTEGER(),
                    nullable=True)
    op.alter_column('recipeingredient', 'ingredient_id',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    op.alter_column('recipeingredient', 'recipe_id',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    op.drop_index(op.f('ix_recipe_name'), table_name='recipe')
    op.alter_column('recipe', 'kcal',
                    existing_type=sa.INTEGER(),
                    nullable=True)
    op.alter_column('recipe', 'num_people',
                    existing_type=sa.INTEGER(),
                    nullable=True)
    op.alter_column('recipe', 'cooking_time_min',
                    existing_type=sa.INTEGER(),
                    nullable=True)
    op.alter_column('recipe', 'name',
                    existing_type=sa.VARCHAR(),
                    nullable=True)
    op.alter_column('recipe', 'id',
                    existing_type=sa.INTEGER(),
                    nullable=False,
                    autoincrement=True,
                    existing_server_default=sa.text("nextval('recipe_id_seq'::regclass)"))
    op.drop_index(op.f('ix_ingredient_name'), table_name='ingredient')
    op.alter_column('ingredient', 'name',
                    existing_type=sa.VARCHAR(),
                    nullable=True)
    op.alter_column('ingredient', 'id',
                    existing_type=sa.INTEGER(),
                    nullable=False,
                    autoincrement=True,
                    existing_server_default=sa.text("nextval('ingredient_id_seq'::regclass)"))
    # ### end Alembic commands ###
