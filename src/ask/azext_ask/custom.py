# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import random
import json
import re
import sys
import platform
import requests
import colorama  # pylint: disable=import-error


from azure.cli.core import telemetry as telemetry_core
from knack.prompting import prompt
from knack.log import get_logger
logger = get_logger(__name__)

WAIT_MESSAGE = ['I\'m an AI bot (learn more: aka.ms/aladdin); Let me see how I can help you...']

EXTENSION_NAME = 'ask'

FIND_EXTENSION_PREFIX = 'Context.Default.Extension.Ask.'

RECOM_TABLE = './data/top_recoms.json'
HELP_TABLE = './data/help_dump.json'

def process_query(cli_term):
    print(random.choice(WAIT_MESSAGE))
    
    with open(RECOM_TABLE, encoding='utf8') as jsonfile:
        recom_table = json.load(jsonfile)

    with open(HELP_TABLE, encoding='utf8') as jsonfile:
        help_dump = json.load(jsonfile)

    #remove 'az ' from the beginning of the command
    if cli_term.startswith('az '):
        cli_term = cli_term[3:]
    # remove placeholders and values and sort the parameters
    command = get_parent_command_for_example (help_dump, cli_term)

    # if command is not valid
    if command not in help_dump:
        print("\nSorry this command is unknown [" + command + "].") 
        return

    sorted_params = sorted_param_list (command, cli_term)
    key = " ".join([command]+sorted_params)

    if key in recom_table:
        print("\nHere are the most succesful commands to use after [" + cli_term + "] is failed: \n")
        for item in recom_table[key]:
            print ("az "+item[0])

    else:
        print("\nSorry I am not able to help with [" + cli_term + "].")

def get_sorted_param_list(help_dump, command, example_command):
    """ convert the list of parameters to a sorted list of standardize parameters

    Attributes:
        command (str): the command
        example_command (str): the commands and its parameters 
    output:
        paramset (list(str)): the sorted list of standard parameters
    """
    params = []
    param_set = set()

    terms = example_command.split()
    for item in terms:
        if item.startswith('-'):
            params += [item]

    # standardize the parameter
    for param in params:
        standard_param = get_standard_form_for_parameter(help_dump, command, param)
        param_set.add(standard_param)

    # sort the params and return the list
    return sorted(param_set)


def get_standard_form_for_parameter(help_dump, command, parameter):
    long_parameter = parameter
    for command_parameter in help_dump[command]['parameters']:
        if parameter == command_parameter or parameter in help_dump[command]['parameters'][command_parameter]['name']:
            long_parameter = command_parameter
            break

    return long_parameter


def get_parent_command_for_example(help_dump, example_command):
    commands = help_dump.keys()
    for command in sorted(commands, reverse=True):
        if example_command.startswith('az ' + command):
            return command

    return None