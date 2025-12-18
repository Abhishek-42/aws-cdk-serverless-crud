import aws_cdk as core
import aws_cdk.assertions as assertions

from test_project1.test_project1_stack import TestProject1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in test_project1/test_project1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TestProject1Stack(app, "test-project1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
