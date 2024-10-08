"""add employee_meetings table

Revision ID: 029ad41447b5
Revises: e2615439d4d1
Create Date: 2024-10-03 20:58:58.174424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '029ad41447b5'
down_revision = 'e2615439d4d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee_meetings',
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('meeting_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_employee_meetings_employee_id_employees')),
    sa.ForeignKeyConstraint(['meeting_id'], ['meetings.id'], name=op.f('fk_employee_meetings_meeting_id_meetings'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee_meetings')
    # ### end Alembic commands ###
