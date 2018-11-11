import boto3
from database.dynamotable import AudiencePulseTable

client = boto3.client('cloudformation')
db_table = AudiencePulseTable()
print db_table.get_cft()
# client.create_stack(
#
# )
