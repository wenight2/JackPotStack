#!/usr/bin/env python3
import os

import aws_cdk as cdk

from jack_pot.jack_pot_stack import JackPotStack


app = cdk.App()
JackPotStack(app, "JackPotStack")

app.synth()
