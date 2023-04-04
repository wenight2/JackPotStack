import aws_cdk as core
import aws_cdk.assertions as assertions

from jack_pot.jack_pot_stack import JackPotStack

# example tests. To run these tests, uncomment this file along with the example
# resource in jack_pot/jack_pot_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = JackPotStack(app, "jack-pot")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
