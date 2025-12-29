from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb,
    aws_lambda as lambda_,
    aws_apigateway as apigw,

)
import os
from constructs import Construct

class TestProject1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id,description = "CRUD application made using AWS services ",  **kwargs)

        table = dynamodb.Table(
            self,
            "TasksTable",
            partition_key=dynamodb.Attribute(
                name="task_id",
                type=dynamodb.AttributeType.STRING
            )
        )

        task_lambda = lambda_.Function(
            self,
            
            "TasksHandler",
            runtime=lambda_.Runtime.PYTHON_3_10,
            handler="handler.main",
            code=lambda_.Code.from_asset("lambda")
        )

        api = apigw.RestApi(
            self,
            "TasksApi",
            rest_api_name="Tasks Service"
        )
        tasks = api.root.add_resource("tasks")
        tasks.add_method("GET", apigw.LambdaIntegration(task_lambda))
        tasks.add_method("POST", apigw.LambdaIntegration(task_lambda))

        task = tasks.add_resource("{id}")
        task.add_method("PUT", apigw.LambdaIntegration(task_lambda))
        task.add_method("DELETE", apigw.LambdaIntegration(task_lambda))

        table.grant_read_write_data(task_lambda)

        task_lambda.add_environment(
            "TABLE_NAME",
            table.table_name
        )   

       