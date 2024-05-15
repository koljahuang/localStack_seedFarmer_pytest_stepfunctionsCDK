#!/usr/bin/env python3

from aws_cdk import App
from stack import JobPollerStack

stack_name = "aws-stepfunctions-demo"

app = App()
JobPollerStack(app, stack_name)
app.synth()