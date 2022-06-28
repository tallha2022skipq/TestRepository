import aws_cdk as core
import aws_cdk.assertions as assertions

from trial2_practice.trial2_practice_stack import Trial2PracticeStack

# example tests. To run these tests, uncomment this file along with the example
# resource in trial2_practice/trial2_practice_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Trial2PracticeStack(app, "trial2-practice")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
