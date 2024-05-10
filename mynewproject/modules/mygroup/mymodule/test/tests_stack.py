import pytest
import boto3
import json
import time
# from . import stack_name


@pytest.mark.parametrize("stack_name", ['aws-stepfunctions-demo'])
def test_aws_stepfunctions_demo(stack_name):
    client = boto3.client('stepfunctions', 
                          aws_access_key_id='test',
                          aws_secret_access_key='test',
                          endpoint_url='http://localhost:4566')

    input_data = {
        "status": "FAILED"
    }

    response = client.list_state_machines()
    for state_machine in response['stateMachines']:
        if state_machine['name'].startswith(stack_name):
            state_machine_arn = state_machine['stateMachineArn']
            print('State Machine ARN:', state_machine_arn)
            break

    # execute State Machine
    response = client.start_execution(
        stateMachineArn=state_machine_arn,
        input=json.dumps(input_data)
    )
    execution_arn = response['executionArn']


    while True:
        response = client.get_execution_history(
            executionArn=execution_arn,
            reverseOrder=True,
            maxResults=1,
        )
        events = response['events']
        last_event = events[0] 
        if last_event['type'] == 'ExecutionSucceeded':
            print('Execution succeeded!')
            break
        elif last_event['type'] == 'ExecutionFailed':
            print('Execution failed!')
            break
        time.sleep(3)

    # terminate State Machine if execution State Machine failed
    # response = client.stop_execution(
    #     executionArn='arn:aws:states:us-east-1:000000000000:stateMachine:aws-stepfunctions-demo-StateMachine2E01A3A5-5a962482',
    #     error='good boy'  # 中断时的错误消息，可选
    # )

    # what last_event['executionSucceededEventDetails'] looks like?
    # {'output': '{"status":"SUCCEEDED","event":{"event":{"status":"SUCCESS"},"status":"SUCCEEDED"}}', 'outputDetails': {'truncated': False}}
    assert '"status":"SUCCEEDED"' in last_event['executionSucceededEventDetails']['output']