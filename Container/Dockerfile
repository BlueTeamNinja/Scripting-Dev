# You can change these variables to use a different base image, but
# you must ensure that your base image inherits from one of ours.
# You can also override these at build time with --build-arg flags
ARG BASE_REPO=gradescope/autograder-base
ARG TAG=latest

FROM ${BASE_REPO}:${TAG}

ADD source /autograder/source

RUN cp /autograder/source/run_autograder /autograder/run_autograder

# Ensure that scripts are Unix-friendly and executable
RUN dos2unix /autograder/run_autograder
RUN chmod +x /autograder/run_autograder

# Do whatever setup was needed in setup.sh, including installing apt packages
# Cleans up the apt cache afterwards in the same step to keep the image small
RUN apt-get update && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    wget https://github.com/PowerShell/PowerShell/releases/download/v7.3.7/powershell_7.3.7-1.deb_amd64.deb -O ./ps7.deb && \
    dpkg -i ./ps7.deb && \
    apt-get install -f

# You can also use RUN commands in the Dockerfile to install things
# instead of using a bash script

# The base image defines the CMD and ENTRYPOINT, so don't redefine those