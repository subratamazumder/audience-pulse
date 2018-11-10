from troposphere import Template, Ref, Parameter, Output
from troposphere.dynamodb import Table, KeySchema, AttributeDefinition, ProvisionedThroughput

t = Template()
t.add_description("CFT of Dynamo tables for Audience Pulse application")

# "Properties" : {
#     "AttributeDefinitions" : [ AttributeDefinition, ... ],
#     "GlobalSecondaryIndexes" : [ GlobalSecondaryIndexes, ... ],
#     "KeySchema" : [ KeySchema, ... ],
#     "LocalSecondaryIndexes" : [ LocalSecondaryIndexes, ... ],
#     "PointInTimeRecoverySpecification" : PointInTimeRecoverySpecification,
#     "ProvisionedThroughput" : ProvisionedThroughput,
#     "SSESpecification" : SSESpecification,
#     "StreamSpecification" : StreamSpecification,
#     "TableName" : String,
#     "Tags" : [ Resource Tag, ... ],
#     "TimeToLiveSpecification" : TimeToLiveSpecification
#   }

question_table = Table(
    "QuestionTable",
    AttributeDefinitions=[
        AttributeDefinition(
            AttributeName="question_id",
            AttributeType="S"
        ),
        AttributeDefinition(
            AttributeName="question_text",
            AttributeType="S"
        ),
        AttributeDefinition(
            AttributeName="question_image_url",
            AttributeType="S"
        ),
        AttributeDefinition(
            AttributeName="category",
            AttributeType="S"
        ),
        AttributeDefinition(
            AttributeName="answers",
            AttributeType="S"
        )
    ],
    KeySchema=[
        KeySchema(
            AttributeName="question_id",
            KeyType="HASH"
        )
    ],
    ProvisionedThroughput=ProvisionedThroughput(
        ReadCapacityUnits=10,
        WriteCapacityUnits=5
    )
)
t.add_resource(question_table)

print t.to_json()
