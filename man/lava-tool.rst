Description
============

Summary
#######

``lava-tool`` is a command-line tool to interact with LAVA.

Usage
#####

lava-tool [-h] <subcommand> [args]

Optional arguments
##################

  -h, --help            show this help message and exit

Subcommands
###########

Type ``lava-tool <subcommand> -h`` for help on a specific subcommand.

Available subcommands
#####################

data-views
    Show data views defined on the server

      Usage:
        lava-tool data-views [-h] --dashboard-url URL [--verbose-xml-rpc]
        [--experimental-notice]

      Optional arguments:
        -h, --help            show this help message and exit

      Dashboard specific arguments:
        --dashboard-url URL   URL of your validation dashboard

      Debugging arguments:
        --verbose-xml-rpc     Show XML-RPC data

      Experimental commands:
        --experimental-notice
            Explain the nature of experimental commands

job-output
    Get job output from the scheduler

      Usage:
        lava-tool job-output [-h] [--overwrite] [--output OUTPUT] SERVER JOB_ID

      Positional arguments:
        SERVER
          Host to download job output from
        JOB_ID
          Job ID to download output file

      Optional arguments:
        -h, --help            show this help message and exit
        --overwrite           Overwrite files on the local disk
        --output OUTPUT, -o OUTPUT
                              Alternate name of the output file

help
    Show a summary of all available commands

deserialize
    Deserialize a bundle on the server

      Usage:
        lava-tool deserialize [-h] --dashboard-url URL [--verbose-xml-rpc] SHA1

      Positional arguments:
        SHA1
          SHA1 of the bundle to deserialize

      Optional arguments:
        -h, --help           show this help message and exit

      Dashboard specific arguments:
        --dashboard-url URL  URL of your validation dashboard

      Debugging arguments:
        --verbose-xml-rpc    Show XML-RPC data

get
    Download a bundle from the server

      Usage:
        lava-tool get [-h] --dashboard-url URL [--verbose-xml-rpc]
        [--overwrite] [--output OUTPUT] SHA1

      Positional arguments:
        SHA1
          SHA1 of the bundle to download

      Optional arguments:
        -h, --help            show this help message and exit
        --overwrite           Overwrite files on the local disk
        --output OUTPUT, -o OUTPUT  Alternate name of the output file

      Dashboard specific arguments:
        --dashboard-url URL   URL of your validation dashboard

      Debugging arguments:
        --verbose-xml-rpc     Show XML-RPC data

auth-add
    Add an authentication token

      Usage:
        lava-tool auth-add [-h] [--token-file TOKEN_FILE] [--no-check] HOST

      Positional arguments:
        HOST
          Endpoint to add token for, in the form scheme://username@host. The
          username will default to the currently logged in user.

      Optional arguments:
        -h, --help            show this help message and exit
        --token-file TOKEN_FILE
                              Read the secret from here rather than prompting
                              for it.
        --no-check            By default, a call to the remote server is made
                              to check that the added token works before
                              remembering it. Passing this option prevents this
                              check.

put
    Upload a bundle on the server

      Usage:
        lava-tool put [-h] --dashboard-url URL [--verbose-xml-rpc] LOCAL
        [REMOTE]

      Positional arguments:
        LOCAL
          pathname on the local file system
        REMOTE
          pathname on the server

      Optional arguments:
        -h, --help           show this help message and exit

      Dashboard specific arguments:
        --dashboard-url URL  URL of your validation dashboard

      Debugging arguments:
        --verbose-xml-rpc    Show XML-RPC data

bundles
    Show bundles in the specified stream

      Usage:
        lava-tool bundles [-h] --dashboard-url URL [--verbose-xml-rpc]
        [PATHNAME]

      Positional arguments:
        PATHNAME
          pathname on the server (defaults to /anonymous/)

      Optional arguments:
        -h, --help           show this help message and exit

      Dashboard specific arguments:
        --dashboard-url URL  URL of your validation dashboard

      Debugging arguments:
        --verbose-xml-rpc    Show XML-RPC data

server-version
    Display dashboard server version

      Usage:
        lava-tool server-version [-h] --dashboard-url URL [--verbose-xml-rpc]

      Optional arguments:
        -h, --help           show this help message and exit

      Dashboard specific arguments:
        --dashboard-url URL  URL of your validation dashboard

      Debugging arguments:
        --verbose-xml-rpc    Show XML-RPC data

cancel-job
    Cancel job

      Usage:
        lava-tool cancel-job [-h] SERVER JOB_ID

      Positional arguments:
        SERVER
          Host to cancel job on
        JOB_ID
          Job ID to cancel

      Optional arguments:
        -h, --help            show this help message and exit

resubmit-job
    Resubmit job

      Usage:
        lava-tool resubmit-job [-h] SERVER JOB_ID

      Positional arguments:
        SERVER
          Host to resubmit job on
        JOB_ID
          Job ID to resubmit

      Optional arguments:
        -h, --help            show this help message and exit

version
    Show dashboard client version

      Usage:
        lava-tool version [-h]

      Optional arguments:
        -h, --help            show this help message and exit

restore
    Restore a dashboard instance from backup

      Usage:
        lava-tool restore [-h] --dashboard-url URL [--verbose-xml-rpc]
        BACKUP_DIR

      Positional arguments:
        BACKUP_DIR
          Directory to backup from

      Optional arguments:
        -h, --help           show this help message and exit

      Dashboard specific arguments:
        --dashboard-url URL  URL of your validation dashboard

      Debugging arguments:
        --verbose-xml-rpc    Show XML-RPC data

query-data-view
    Invoke a specified data view

      Usage:
        lava-tool restore [-h] --dashboard-url URL [--verbose-xml-rpc]
        [--experimental-notice] QUERY

      Positional arguments:
        QUERY
          Data view name and any optional and required arguments

      Optional arguments:
        -h, --help           show this help message and exit

      Dashboard specific arguments:
        --dashboard-url URL  URL of your validation dashboard

      Debugging arguments:
        --verbose-xml-rpc    Show XML-RPC data

      Experimental commands:
        --experimental-notice	Explain the nature of experimental commands

submit-job
    Submit a job to lava-scheduler

      Usage:
        lava-tool submit-job [-h] SERVER JSON_FILE

      Positional arguments:
        SERVER
          Host to resubmit job on
        JSON_FILE
          JSON file with test defenition to submit

      Optional arguments:
        -h, --help            show this help message and exit

      Experimental commands:
        --experimental-notice	Explain the nature of experimental commands

streams
    Show streams you have access to

      Usage:
        lava-tool streams [-h] --dashboard-url URL [--verbose-xml-rpc]

      Optional arguments:
        -h, --help           show this help message and exit

      Dashboard specific arguments:
        --dashboard-url URL  URL of your validation dashboard

      Debugging arguments:
        --verbose-xml-rpc    Show XML-RPC data

backup
    Backup data uploaded to a dashboard instance.

      Usage:
        lava-tool backup [-h] --dashboard-url URL [--verbose-xml-rpc]
        BACKUP_DIR

      Positional arguments:
        BACKUP_DIR
          Directory to backup to

      Optional arguments:
        -h, --help           show this help message and exit

      Dashboard specific arguments:
        --dashboard-url URL  URL of your validation dashboard

      Debugging arguments:
        --verbose-xml-rpc    Show XML-RPC data

      Not all data is preserved. The following data is lost: identity of the
      user that uploaded each bundle, time of uploading and deserialization on
      the server, name of the bundle stream that contained the data.

make-stream
    Create a bundle stream on the server

      Usage:
        lava-tool make-stream [-h] --dashboard-url URL [--verbose-xml-rpc]
        [--name NAME] pathname

      Positional arguments:
        pathname
          Pathname of the bundle stream to create

      Optional arguments:
        -h, --help           show this help message and exit
        --name NAME          Name of the bundle stream (description)

      Dashboard specific arguments:
        --dashboard-url URL  URL of your validation dashboard

      Debugging arguments:
        --verbose-xml-rpc    Show XML-RPC data

pull
    Copy bundles and bundle streams from one dashboard to another

      Usage:
        lava-tool pull [-h] --dashboard-url URL [--verbose-xml-rpc]
        [--experimental-notice] FROM [STREAM [STREAM ...]]

      Positional arguments:
        FROM
          URL of the remote validation dashboard

      Optional arguments:
        -h, --help            show this help message and exit

      Dashboard specific arguments:
        --dashboard-url URL   URL of your validation dashboard

        STREAM
          Streams to pull from (all by default)

      Debugging arguments:
        --verbose-xml-rpc     Show XML-RPC data

      Experimental commands:
        --experimental-notice	Explain the nature of experimental commands

      This command checks for two environment varialbes: The value of
      DASHBOARD_URL is used as a replacement for --dashbard-url. The value of
      REMOTE_DASHBOARD_URL as a replacement for FROM. Their presence
      automatically makes the corresponding argument optional.


LAVA test definitions
#####################

A LAVA Test Definition comprises of two parts:

* the data to setup the test, expressed as a JSON file.
* the instructions to run inside the test, expressed as a YAML file.

This allows the same tests to be easily migrated to a range of different
devices, environments and purposes by using the same YAML files in
multiple JSON files. It also allows tests to be built from a range of
components by aggregating YAML files inside a single JSON file.

Contents of the JSON file
#########################

The JSON file is submitted to the LAVA server and contains:

* Demarcation as a health check or a user test.
* The default timeout of each action within the test.
* The logging level for the test, DEBUG or INFO.
* The name of the test, shown in the list of jobs.
* The location of all support files.
* All parameters necessary to use the support files.
* The declaration of which device(s) to use for the test.
* The location to which the results should be uploaded.
* The JSON determines how the test is deployed onto the device and
  where to find the tests to be run.

Basic JSON file
###############

Your first LAVA test should use the ``DEBUG`` logging level so that it
is easier to see what is happening.

A suitable ``timeout`` for your first tests is 900 seconds.

Make the ``job_name`` descriptive and explanatory, you will want to be
able to tell which job is which when reviewing the results.

Make sure the ``device_type`` matches exactly with one of the suitable
device types listed on the server to which you want to submit this job.

Change the stream to one to which you are allowed to upload results, on
your chosen server.

::

 {
   "health_check": false,
   "logging_level": "DEBUG",
   "timeout": 900,
   "job_name": "kvm-basic-test",
   "device_type": "kvm",
   "actions": [
       {
           "command": "deploy_linaro_image",
           "parameters": {
               "image": "http://images.validation.linaro.org/kvm-debian-wheezy.img.gz"
           }
       },
       {
           "command": "lava_test_shell",
           "parameters": {
               "testdef_repos": [
                   {
                       "git-repo": "git://git.linaro.org/qa/test-definitions.git",
                       "testdef": "ubuntu/smoke-tests-basic.yaml"
                   }
               ],
               "timeout": 900
           }
       },
       {
           "command": "submit_results_on_host",
           "parameters": {
               "stream": "/anonymous/example/",
               "server": "http://localhost/RPC2/"
           }
       }
   ]
 }

Note
####

Always check your JSON syntax. A useful site for this is http://jsonlint.com.
