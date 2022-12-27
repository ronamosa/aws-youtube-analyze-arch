# AWS Youtube Analyser Architecture

## Overview

An AWS architecture project to use Lambda, DynamoDB, S3, SQS and Python to create an automated system that takes a channel id, fetches all available video transcripts and then analyses it with Amazon Athena to get a "vibe check" of the videos individually, and then the channel as a whole.

The intention is full automation, CDK for IaC, CICD for automated testing and deployment and a regular schedule of polling youtube channels for new videos and re-analysis of "vibe".

A front-end allowing submission of new channels to be analysed would be great, but let's be honest, this is a completely useless project whose purpose is to play and learn about these technologies and hopefully make a better architect, developer and engineer out of me.

## Requirements

* AWS Account
* aws-cli
* CDK cli

## Components

* Lambda Functions x 4
* DynamoDB NoSQL Database x 2 tables
* SQS Queue x 1
* S3 Bucket x 1
* IAM Roles (for everything)

Note: `processSqsVideoQueue` is a configured as a Lambda trigger for SQS queue, so that it picks up messages it polls on the Queue and fetches transcripts to store to S3.

TODO: architecture diagram.

## Setup

TODO: Full CDK deployment + GitHub Actions to come.
