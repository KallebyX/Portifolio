from alembic import op
import sqlalchemy as sa

revision = '8a73bd71620d'
down_revision = '1b20e38f88ad'
branch_labels = None
depends_on = None

def upgrade():
    # adiciona coluna 'ordem' com valor default 0 para todas as linhas existentes
    with op.batch_alter_table('projetos', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                'ordem',
                sa.Integer(),
                nullable=False,
                server_default='0'   # <<< aqui
            )
        )

def downgrade():
    with op.batch_alter_table('projetos', schema=None) as batch_op:
        batch_op.drop_column('ordem')