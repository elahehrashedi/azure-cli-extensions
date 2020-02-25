# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# import random
import json
import sys
import re
import os
import requests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from azure.cli.core import telemetry as telemetry_core

EXTENSION_NAME = 'recom'

RECOM_EXTENSION_PREFIX = 'Context.Default.Extension.Recom.'

RECOM_TABLE = 'C:/Elaheh/AzureExt_Branch/azure-cli-extensions/src/recom/azext_recom/data/CLI_top_recoms.json'
# TODO delete fail table
#FAIL_TABLE = 'C:/Elaheh/AzureExt_Branch/azure-cli-extensions/src/recom/azext_recom/data/top_fails.json'
HELP_TABLE = 'C:/Elaheh/AzureExt_Branch/azure-cli-extensions/src/recom/azext_recom/data/help_dump.json'


def process_query(cli_term):

    with open(HELP_TABLE, encoding='utf8') as jsonfile:
        help_dump = json.load(jsonfile)

    with open(RECOM_TABLE, encoding='utf8') as jsonfile:
        recom_table = json.load(jsonfile)

    #with open(FAIL_TABLE, encoding='utf8') as jsonfile:
    #    fail_table = json.load(jsonfile)

    # remove placeholders and values and sort the parameters
    command = get_parent_command_for_example(help_dump, cli_term)
    # if command is not valid
    if command is None:
        print("\n***Sorry! this command is unknown: [" + cli_term + "].")
    else:
        sorted_params = get_sorted_param_list(help_dump, command, cli_term)
        key = " ".join([command] + sorted_params).strip()

        if key in recom_table:
            # if key exists in in recom_table
            print_message(cli_term)
            for item in recom_table[key]['recoms']:
                print("\t\t***az " + item[0])
        else:
            # if key exists in fail_table, and it has no parameters
            # call "Find" API
            find_process_query("az " + key)
        """else:
            if key in fail_table:
                if sorted_params:
                    # if key exists in fail_table, and it has parameters
                    print_message(cli_term)
                    for item in fail_table[key]['recoms']:
                        print("\t\t***az " + item[0])
                else:
                    # if key exists in fail_table, and it has no parameters
                    # call "Find" API
                    find_process_query("az " + key)
            else:
                print("\n\t***Sorry! I am not able to help with [" + cli_term + "].")"""

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


def print_message(cli_term):
    print("\n\tHere are three ways users succeeded after [" + cli_term + "] has failed:\n")


def find_process_query(cli_term):
    response = call_aladdin_service(cli_term)

    answer_list = json.loads(response.content)
    if (not answer_list or answer_list[0]['source'] == 'bing'):
        print("\n\tSorry! I am not able to help with [" + cli_term + "].")
    else:
        print_message(cli_term)
        num_results_to_show = min(3, len(answer_list))
        for i in range(num_results_to_show):
            current_title = answer_list[i]['title'].strip()
            current_snippet = answer_list[i]['snippet'].strip()
            if current_title.startswith("az "):
                current_title, current_snippet = current_snippet, current_title
                current_title = current_title.split('\r\n')[0]
            elif '```azurecli\r\n' in current_snippet:
                start_index = current_snippet.index('```azurecli\r\n') + len('```azurecli\r\n')
                current_snippet = current_snippet[start_index:]
            current_snippet = current_snippet.replace('```', '').replace(current_title, '').strip()
            current_snippet = re.sub(r'\[.*\]', '', current_snippet).strip()
            print("\t\t" + current_snippet)


def call_aladdin_service(query):
    context = {
        'session_id': telemetry_core._session._get_base_properties()['Reserved.SessionId'],  # pylint: disable=protected-access
        'subscription_id': telemetry_core._get_azure_subscription_id(),  # pylint: disable=protected-access
        'client_request_id': telemetry_core._session.application.data['headers']['x-ms-client-request-id'],  # pylint: disable=protected-access
        'installation_id': telemetry_core._get_installation_id()  # pylint: disable=protected-access
    }

    service_input = {
        'paragraphText': "<div id='dummyHeader'></div>",
        'currentPageUrl': "",
        'query': "ALADDIN-CLI:" + query,
        'context': context
    }

    api_url = 'https://aladdinservice-prod.azurewebsites.net/api/aladdin/generateCards'
    headers = {'Content-Type': 'application/json'}

    response = requests.post(api_url, headers=headers, json=service_input)

    return response

# Replacements for core functions
def provide_recommendations(cli_term):
    process_query(cli_term)
