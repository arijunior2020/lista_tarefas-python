"""empty message

Revision ID: 971343162110
Revises: 
Create Date: 2024-02-12 17:09:14.650712

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '971343162110'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('tarefas')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tarefas',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('descricao', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='tarefas_pkey')
    )
    op.drop_table('task')
    # ### end Alembic commands ###