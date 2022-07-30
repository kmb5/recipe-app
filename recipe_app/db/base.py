
# Import all the models, so that Base has them before being
# imported by Alembic
from recipe_app.db.base_class import Base  # noqa
from recipe_app.models.user import User  # noqa
from recipe_app.models.recipe import Recipe  # noqa
