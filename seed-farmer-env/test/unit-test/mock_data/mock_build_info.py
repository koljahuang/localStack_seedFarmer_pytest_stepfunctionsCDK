codebuild_response = {
    "builds": [
        {
            "id": "codeseeder-idf:7f53415b-f47d-4e5e-860f-93d7f440aa30",
            "arn": "arn:aws:codebuild:us-east-1:123456789012:build/codeseeder-idf:7f53415b-f47d-4e5e-860f-93d7f440aa30",
            "buildNumber": 7,
            "startTime": "2024-03-13T20:24:02.191000-04:00",
            "endTime": "2024-03-13T20:26:33.189000-04:00",
            "currentPhase": "COMPLETED",
            "buildStatus": "SUCCEEDED",
            "projectName": "codeseeder-idf",
            "phases": [
                {
                    "phaseType": "SUBMITTED",
                    "phaseStatus": "SUCCEEDED",
                    "startTime": "2024-03-13T20:24:02.191000-04:00",
                    "endTime": "2024-03-13T20:24:02.360000-04:00",
                    "durationInSeconds": 0
                },
                {
                    "phaseType": "QUEUED",
                    "phaseStatus": "SUCCEEDED",
                    "startTime": "2024-03-13T20:24:02.360000-04:00",
                    "endTime": "2024-03-13T20:24:03.331000-04:00",
                    "durationInSeconds": 0
                },
                {
                    "phaseType": "PROVISIONING",
                    "phaseStatus": "SUCCEEDED",
                    "startTime": "2024-03-13T20:24:03.331000-04:00",
                    "endTime": "2024-03-13T20:24:11.188000-04:00",
                    "durationInSeconds": 7,
                    "contexts": [
                        {
                            "statusCode": "",
                            "message": ""
                        }
                    ]
                },
                {
                    "phaseType": "DOWNLOAD_SOURCE",
                    "phaseStatus": "SUCCEEDED",
                    "startTime": "2024-03-13T20:24:11.188000-04:00",
                    "endTime": "2024-03-13T20:24:17.501000-04:00",
                    "durationInSeconds": 6,
                    "contexts": [
                        {
                            "statusCode": "",
                            "message": ""
                        }
                    ]
                },
                {
                    "phaseType": "INSTALL",
                    "phaseStatus": "SUCCEEDED",
                    "startTime": "2024-03-13T20:24:17.501000-04:00",
                    "endTime": "2024-03-13T20:26:16.074000-04:00",
                    "durationInSeconds": 118,
                    "contexts": [
                        {
                            "statusCode": "",
                            "message": ""
                        }
                    ]
                },
                {
                    "phaseType": "PRE_BUILD",
                    "phaseStatus": "SUCCEEDED",
                    "startTime": "2024-03-13T20:26:16.074000-04:00",
                    "endTime": "2024-03-13T20:26:16.246000-04:00",
                    "durationInSeconds": 0,
                    "contexts": [
                        {
                            "statusCode": "",
                            "message": ""
                        }
                    ]
                },
                {
                    "phaseType": "BUILD",
                    "phaseStatus": "SUCCEEDED",
                    "startTime": "2024-03-13T20:26:16.246000-04:00",
                    "endTime": "2024-03-13T20:26:31.774000-04:00",
                    "durationInSeconds": 15,
                    "contexts": [
                        {
                            "statusCode": "",
                            "message": ""
                        }
                    ]
                },
                {
                    "phaseType": "POST_BUILD",
                    "phaseStatus": "SUCCEEDED",
                    "startTime": "2024-03-13T20:26:31.774000-04:00",
                    "endTime": "2024-03-13T20:26:32.877000-04:00",
                    "durationInSeconds": 1,
                    "contexts": [
                        {
                            "statusCode": "",
                            "message": ""
                        }
                    ]
                },
                {
                    "phaseType": "UPLOAD_ARTIFACTS",
                    "phaseStatus": "SUCCEEDED",
                    "startTime": "2024-03-13T20:26:32.877000-04:00",
                    "endTime": "2024-03-13T20:26:32.931000-04:00",
                    "durationInSeconds": 0,
                    "contexts": [
                        {
                            "statusCode": "",
                            "message": ""
                        }
                    ]
                },
                {
                    "phaseType": "FINALIZING",
                    "phaseStatus": "SUCCEEDED",
                    "startTime": "2024-03-13T20:26:32.931000-04:00",
                    "endTime": "2024-03-13T20:26:33.189000-04:00",
                    "durationInSeconds": 0,
                    "contexts": [
                        {
                            "statusCode": "",
                            "message": ""
                        }
                    ]
                },
                {
                    "phaseType": "COMPLETED",
                    "startTime": "2024-03-13T20:26:33.189000-04:00"
                }
            ],
            # "source": {
            #     "type": "S3",
            #     "location": "codeseeder-idf-123456789012-jbkeyw/codeseeder/dummy-ecr-ecr-ml-images/bzchpmli/bundle.zip",
            #     "buildspec": "version: 0.2\nenv:\n    shell: bash\n    variables: {}\n    exported-variables:\n    - SEEDFARMER_MODULE_METADATA\n    - AWS_CODESEEDER_OUTPUT\nphases:\n    install:\n        commands:\n        - mkdir -p /var/scripts/\n        - mv $CODEBUILD_SRC_DIR/bundle/retrieve_docker_creds.py /var/scripts/retrieve_docker_creds.py\n            || "true"\n        - /var/scripts/retrieve_docker_creds.py && echo 'Docker logins successful'\n            || echo 'Docker logins failed'\n        - aws codeartifact login --tool pip --domain aws-codeseeder-idf --repository\n            python-repository\n        - python3 -m venv ~/.venv\n        - . ~/.venv/bin/activate\n        - cd ${CODEBUILD_SRC_DIR}/bundle\n        - pip install aws-codeseeder~=0.11.1\n        - pip install seed-farmer==3.3.0.dev0\n        - cd module/\n        - npm install -g aws-cdk@2.114.1\n        - pip install -r requirements.txt\n        on-failure: ABORT\n        runtime-versions:\n            nodejs: '16'\n            python: '3.10'\n            java: corretto17\n    pre_build:\n        commands:\n        - . ~/.venv/bin/activate\n        - cd ${CODEBUILD_SRC_DIR}/bundle\n        - nohup /usr/local/bin/dockerd --host=unix:///var/run/docker.sock --host=tcp://127.0.0.1:2375\n            --storage-driver=overlay2 &\n        - timeout 15 sh -c \"until docker info; do echo .; sleep 1; done\"\n        - cd module/\n        - export DEPLOYMENT=dummy\n        - export GROUP=ecr\n        - export MODULE=ecr-ml-images\n        on-failure: ABORT\n    build:\n        commands:\n        - . ~/.venv/bin/activate\n        - cd ${CODEBUILD_SRC_DIR}/bundle\n        - codeseeder execute --args-file fn_args.json --debug\n        - if [[ -f /tmp/codeseeder_export.sh ]]; then source /tmp/codeseeder_export.sh;\n            else echo 'No return value to export'; fi\n        - cd module/\n        - cdk destroy --force --app \"python app.py\"\n        on-failure: ABORT\n    post_build:\n        commands:\n        - . ~/.venv/bin/activate\n        - cd ${CODEBUILD_SRC_DIR}/bundle\n        - cd module/\n        - seedfarmer remove moduledata -d dummy -g ecr -m ecr-ml-images\n        on-failure: ABORT\n",
            #     "insecureSsl": "false"
            # },
            "secondarySources": [],
            "secondarySourceVersions": [],
            "artifacts": {
                "location": ""
            },
            "cache": {
                "type": "NO_CACHE"
            },
            "environment": {
                "type": "LINUX_CONTAINER",
                "image": "aws/codebuild/standard:6.0",
                "computeType": "BUILD_GENERAL1_SMALL",
                "environmentVariables": [
                    {
                        "name": "AWS_CODESEEDER_DOCKER_SECRET",
                        "value": "NONE",
                        "type": "PLAINTEXT"
                    },
                    {
                        "name": "SEEDFARMER_PARAMETER_REPOSITORY_NAME",
                        "value": "ml-mnist-images",
                        "type": "PLAINTEXT"
                    },
                    {
                        "name": "AWS_CODESEEDER_NAME",
                        "value": "idf",
                        "type": "PLAINTEXT"
                    },
                    {
                        "name": "SEEDFARMER_MODULE_NAME",
                        "value": "ecr-ecr-ml-images",
                        "type": "PLAINTEXT"
                    },
                    {
                        "name": "SEEDFARMER_VERSION",
                        "value": "3.3.0.dev0",
                        "type": "PLAINTEXT"
                    },
                    {
                        "name": "SEEDFARMER_MODULE_METADATA",
                        "value": "{\"AwsCodeSeederDeployed\": \"0.11.1\", \"EcrRepositoryArn\": \"arn:aws:ecr:us-east-1:123456789012:repository/ml-mnist-images\", \"EcrRepositoryName\": \"ml-mnist-images\", \"LifecycleMaxImages\": \"10\", \"SeedFarmerDeployed\": \"3.3.0.dev0\"}",
                        "type": "PLAINTEXT"
                    },
                    {
                        "name": "SEEDFARMER_DEPLOYMENT_NAME",
                        "value": "dummy",
                        "type": "PLAINTEXT"
                    },
                    {
                        "name": "AWS_PARTITION",
                        "value": "aws",
                        "type": "PLAINTEXT"
                    },
                    {
                        "name": "AWS_CODESEEDER_VERSION",
                        "value": "0.11.1",
                        "type": "PLAINTEXT"
                    },
                    {
                        "name": "AWS_ACCOUNT_ID",
                        "value": "123456789012",
                        "type": "PLAINTEXT"
                    },
                    {
                        "name": "SEEDFARMER_PROJECT_NAME",
                        "value": "idf",
                        "type": "PLAINTEXT"
                    },
                    {
                        "name": "SEEDFARMER_HASH",
                        "value": "074ff5b4",
                        "type": "PLAINTEXT"
                    },
                    {
                        "name": "SEEDFARMER_PARAMETER_LIFECYCLE_MAX_IMAGE_COUNT",
                        "value": "10",
                        "type": "PLAINTEXT"
                    },
                    {
                        "name": "SEEDFARMER_PARAMETER_IMAGE_TAG_MUTABILITY",
                        "value": "MUTABLE",
                        "type": "PLAINTEXT"
                    }
                ],
                "privilegedMode": "true",
                "imagePullCredentialsType": "CODEBUILD"
            },
            "serviceRole": "arn:aws:iam::123456789012:role/idf-dummy-ecr-ecr-ml-images-074ff5b4",
            "logs": {
                "groupName": "/aws/codebuild/codeseeder-idf",
                "streamName": "codeseeder-bzchpmli/7f53415b-f47d-4e5e-860f-93d7f440aa30",
                "deepLink": "https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#logsV2:log-groups/log-group/$252Faws$252Fcodebuild$252Fcodeseeder-idf/log-events/codeseeder-bzchpmli$252F7f53415b-f47d-4e5e-860f-93d7f440aa30",
                "cloudWatchLogsArn": "arn:aws:logs:us-east-1:123456789012:log-group:/aws/codebuild/codeseeder-idf:log-stream:codeseeder-bzchpmli/7f53415b-f47d-4e5e-860f-93d7f440aa30",
                "cloudWatchLogs": {
                    "status": "ENABLED",
                    "groupName": "/aws/codebuild/codeseeder-idf",
                    "streamName": "codeseeder-bzchpmli"
                },
                "s3Logs": {
                    "status": "DISABLED",
                    "encryptionDisabled": "false"
                }
            },
            "timeoutInMinutes": 120,
            "queuedTimeoutInMinutes": 480,
            "buildComplete": "true",
            "initiator": "seedfarmer-idf-deployment-role/deployment_role",
            "exportedEnvironmentVariables": [
                {
                    "name": "AWS_CODESEEDER_OUTPUT",
                    "value": "\"{\\\"aws_region\\\": \\\"us-east-1\\\", \\\"aws_account_id\\\": \\\"123456789012\\\", \\\"aws_partition\\\": \\\"aws\\\", \\\"codebuild_build_id\\\": \\\"codeseeder-idf:7f53415b-f47d-4e5e-860f-93d7f440aa30\\\", \\\"codebuild_log_path\\\": \\\"codeseeder-bzchpmli/7f53415b-f47d-4e5e-860f-93d7f440aa30\\\"}\""
                },
                {
                    "name": "SEEDFARMER_MODULE_METADATA",
                    "value": "{\"AwsCodeSeederDeployed\": \"0.11.1\", \"EcrRepositoryArn\": \"arn:aws:ecr:us-east-1:123456789012:repository/ml-mnist-images\", \"EcrRepositoryName\": \"ml-mnist-images\", \"LifecycleMaxImages\": \"10\", \"SeedFarmerDeployed\": \"3.3.0.dev0\"}"
                }
            ]
        }
    ],
    "buildsNotFound": [],
    "ResponseMetadata": {
        "RequestId": "11701f62-9639-4fe3-82d9-dcbc38ac41af",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "11701f62-9639-4fe3-82d9-dcbc38ac41af",
            "content-type": "application/x-amz-json-1.1",
            "content-length": "7670",
            "date": "Fri, 29 Mar 2024 14:38:06 GMT"
        },
        "RetryAttempts": 0
    }
}
