#!/bin/bash

set -euxo pipefail

main () {
    expected_filename=main.py

    cd /code_execution

    submission_files=$(zip -sf ./submission/submission.zip)
    if ! grep -q ${expected_filename}<<<$submission_files; then
        echo "Submission zip archive must include $expected_filename"
    return 1
    fi

    echo "Unpacking submission"
    unzip ./submission/submission.zip -d ./

    ls -alh

    if $IS_SMOKE_TEST; then
        echo "Running smoke test"
        python main.py
    else
        echo "Running submission"
        python main.py &> "/code_execution/submission/private_log.txt"
    fi

    echo "Exporting submission.csv result..."

    # Valid scripts must create a "submission.csv" file within the same directory as main
    if [ -f "submission.csv" ]
    then
        echo "Script completed its run."
        cp submission.csv ./submission/submission.csv
    else
        echo "ERROR: Script did not produce a submission.csv file in the main directory."
        exit_code=1
    fi
}

main |& tee "/code_execution/submission/log.txt"
exit_code=${PIPESTATUS[0]}

cp /code_execution/submission/log.txt /tmp/log

exit $exit_code
