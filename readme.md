# Agent-Assisted Automation Project

This project demonstrates the integration of an automated agent system using the autogen library to perform specific web scraping tasks. It showcases how to set up and deploy an automated agent to search for accommodations on Airbnb for Mendoza, Argentina, from March 10, 2024, to March 17, 2024, gather the results, and organize them into a Pandas DataFrame.

## Overview

The codebase uses autogen to configure and deploy two types of agents: AssistantAgent and UserProxyAgent. These agents interact to automate the task of web scraping Airbnb search results without human input, adhering to specified configurations and conditions. The primary goal is to automate data collection and processing tasks efficiently and programmatically.

# Installation

To run this project, you'll need Python 3.6 or later. Clone this repository, and install the required dependencies in your virtual environment:

```bash
git clone <repository-url>
cd <repository-name>
pip install pyautogen
```
## Dependencies
Make sure to create an OAI_CONFIG_LIST.json file with your specific configurations for the autogen agents.

## Usage

To execute the automated agent task, run the following command:

```bash
python <your-script-name>.py
Replace <your-script-name> with the name of your Python script file.
```
Ensure that the OAI_CONFIG_LIST.json configuration file is correctly set up in your project directory as the script relies on it for agent configurations.
