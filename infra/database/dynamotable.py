from troposphere import Template, Ref, Parameter, Output
from troposphere.dynamodb import Table, KeySchema, AttributeDefinition, ProvisionedThroughput

PARAMETER_WRITE_CAPACITY = "WriteCapacityUnits"
PARAMETER_READ_CAPACITY = "ReadCapacityUnits"
TABLE_QUESTION = "QuestionTable"


class AudiencePulseTable:
    t = Template()

    def __init__(self):
        self.add_description()
        self.add_parameters()
        self.create_question_table()

    def add_description(self):
        self.t.add_description("CFT of Dynamo tables for Audience Pulse application")

    def add_parameters(self):
        wcu = Parameter(
            PARAMETER_WRITE_CAPACITY,
            Description="Provisioned write throughput",
            Type="Number",
            Default="5",
            MinValue="1",
            MaxValue="8",
            ConstraintDescription="should be between 1 and 8 to be under free tier"
        )
        rcu = Parameter(
            PARAMETER_READ_CAPACITY,
            Description="Provisioned read throughput",
            Type="Number",
            Default="5",
            MinValue="1",
            MaxValue="8",
            ConstraintDescription="should be between 1 and 8 to be under free tier"
        )
        self.t.add_parameter(rcu)
        self.t.add_parameter(wcu)

    def create_question_table(self):
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
            TABLE_QUESTION,
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
                ),
                AttributeDefinition(
                    AttributeName="create_date",
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
                ReadCapacityUnits=Ref(PARAMETER_READ_CAPACITY),
                WriteCapacityUnits=Ref(PARAMETER_WRITE_CAPACITY)
            )
        )
        self.t.add_resource(question_table)

    def get_cft(self):
        return self.t.to_json()
