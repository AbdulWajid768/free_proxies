# FreeProxy

FreeProxy is a Python utility to retrieve and test free proxies from the web. It scrapes a website providing free
proxies, filters proxies by anonymity level, and checks their availability.

## Prerequisites

![Python](https://img.shields.io/badge/Python-3.6+-grey?labelColor=red&style=flat)

## Features

### Fetch Proxies:

Retrieve a list of free proxies from https://free-proxy-list.net/. Only extracts "elite" proxies, which provide a higher
level of anonymity.

### Check Proxy Availability:

Verify if the proxy is active by making a request to an external server.

### Get Working Proxies:

Obtain a list of proxies that are currently operational.

## How to setup

### 1. Clone Repository

`git clone https://github.com/AbdulWajid768/free_proxies.git`

`cd free_proxies`

### 2. Install Requirements

`pip install requirements.txt`

### 3. Run program

`python app.py`
