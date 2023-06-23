from aws_cdk import (
    Stack,
    aws_apigateway as api_gw,
    aws_lambda as awslambda,
    CfnOutput,
)
from constructs import Construct

class JackPotStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_five = awslambda.Function(self, "LambdaForFive", runtime=awslambda.Runtime.PYTHON_3_8, handler="index.handler", code= awslambda.Code.from_asset(('script-five')))
        Lambda_euro = awslambda.Function(self, "LambdaForEuro", runtime=awslambda.Runtime.PYTHON_3_8, handler="index.handler", code= awslambda.Code.from_asset(('script-euro')))

        guess_what_another_lambda = awslambda.Function(self, "LambdaPrices", runtime=awslambda.Runtime.PYTHON_3_8, handler="index.handler", code= awslambda.Code.from_asset(('prices')))

        api = api_gw.RestApi(self, "MYApi", rest_api_name="Hululu", description="aaaaaaaaaa", endpoint_types=[api_gw.EndpointType.REGIONAL])

        resoruce_five = api.root.add_resource("resoruce_five")
        five_integration = api_gw.LambdaIntegration(lambda_five)
        resoruce_five.add_method("GET", five_integration)
        
        resoruce_euro = api.root.add_resource("resoruce_euro")
        euro_integration = api_gw.LambdaIntegration(Lambda_euro)
        resoruce_euro.add_method("GET", euro_integration)

        resoruce_price = api.root.add_resource("resoruce_euro")
        price_integration = api_gw.LambdaIntegration(guess_what_another_lambda)
        resoruce_price.add_method("GET", price_integration)


        CfnOutput(self, "LambdaFiveURL", value=f"https://{api.rest_api_id}.execute-api.{Stack.of(self).region}.amazonaws.com/prod/resoruce_five")
        CfnOutput(self, "LambdaEuroURL", value=f"https://{api.rest_api_id}.execute-api.{Stack.of(self).region}.amazonaws.com/prod/resoruce_euro")
        CfnOutput(self, "LambdaPrice", value=f"https://{api.rest_api_id}.execute-api.{Stack.of(self).region}.amazonaws.com/prod/resoruce_price")

        