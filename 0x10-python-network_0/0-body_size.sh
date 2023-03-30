#!/bin/bash
# takes in a url and sends a request to it and display size of body of response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
