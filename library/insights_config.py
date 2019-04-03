ANSIBLE_METADATA = {
     'metadata_version': '1.1',
     'status': ['preview'],
     'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: insights_config
short_description: This module handles initial configuration of the insights client on install
description:
  - Supply values for various configuration options that you would like to use. On install
  this module will add those values to the insights-client.conf file prior to registering.
version_added: "3.0"
options:
  insights_name:
    description:
    - For now this is just 'insights-client', but that could change in the future if the
    product name changes.
    required: true
  username:
    description:
    - Insights basic auth username. If defined this will change, set, or remove the username
    in the insights configuration. To remove a username set this value to an empty string.
    required: false
  password:
    description:
    - Insights basic auth password. If defined this will change, set, or remove the password
    in the insights configuration. To remove a password set this value to an empty string.
    required: false
  auto_config:
    description:
    - Attempt to auto-configure the network connection with Satellite or RHSM. Default is True.
    required: false
  authmethod:
    description:
    - Authentication method for the Portal (BASIC, CERT). Default is BASIC. Note: when
    auto_config is enabled, CERT will be used if RHSM or Satellite is detected.
    required: true
'''

EXAMPLES = '''
- insights_config:
    insights_name: 'insights-client' or "{{ insights_name }}"
    username: "rhn_support" or "{{ redhat_portal_username }}" if passing in as a role variable
    password: "rhn_password" or "{{ redhat_portal_password }}" if passing in as a role variable
    auto_config: True
    authmethod: BASIC
'''
