# -*- coding: utf-8 -*-
from typing import Any, Dict, List

from chaoslib.types import Activity, Configuration, Experiment, Hypothesis, \
    Journal, Run, Secrets
# from chaoslib.exception import InterruptActivity
import click
from logzero import logger

__all__ = ["before_activity_control"]


def before_activity_control(context: Activity, **kwargs):
    """
    Prompt and wait for any key before an activity is executed.
    """
    print("#####BEFORE#####\n", context)
    # click.pause()

def after_activity_control(context: Activity, state: Run, **kwargs):
    """
    Prompt and wait for any key before an activity is executed.
    """
    print("#####AFTER####\n", context, state)
    # click.pause()
