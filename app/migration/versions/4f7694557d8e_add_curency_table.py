"""add curency table

Revision ID: 4f7694557d8e
Revises: 00c67b7a5799
Create Date: 2024-11-18 14:50:45.113674

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f7694557d8e'
down_revision: Union[str, None] = '00c67b7a5799'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currencyrates',
    sa.Column('bank_name', sa.String(), nullable=False),
    sa.Column('bank_en', sa.String(), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.Column('usd_buy', sa.Float(), nullable=False),
    sa.Column('usd_sell', sa.Float(), nullable=False),
    sa.Column('eur_buy', sa.Float(), nullable=False),
    sa.Column('eur_sell', sa.Float(), nullable=False),
    sa.Column('update_time', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bank_en'),
    sa.UniqueConstraint('bank_name'),
    sa.UniqueConstraint('link')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('currencyrates')
    # ### end Alembic commands ###
