#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: insights_registration

short_description: This module registers the insights client

description:
    - This module will check the current registration status, unregister if needed,
    and then register the insights client (and update the display_name if needed)

options:
    insights_name:
        description:
            - For now, this is just 'insights-client', but it could change in the future
            so having it as a variable is just preparing for that
        required: true
    display_name:
        description:
            - When registering with insights an optional display_name can be configured
        required: false

author:
    - Jason Stephens (@Jason-RH)
'''

EXAMPLES = '''
# Register a fresh install
- name: Register the insights client on a fresh install
  insights_registration:
    insights_name: "{{ insights_name }}"

# Register a fresh install with a display name
- name: Register the insights client with display name
  insights_registration:
    insights_name: "{{ insights_name }}"
    display_name: "{{ insights_display_name }}"
'''

RETURN = '''
original_message:
    description: The original name param that was passed in
    type: str
message:
    description: The output message that the sample module generates
'''

from ansible.module_utils.basic import AnsibleModule
import subprocess

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        insights_name=dict(type='str', required=True),
        display_name=dict(type='str', required=False, default='')
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        return result

    result['original_message'] = 'Attempting to register insights-client'
    result['message'] = 'No registration changes have been made'

    insights_name = module.params['insights_name']
    display_name = module.params['display_name']

    reg_status = subprocess.call([insights_name, '--status'])

    if display_name and reg_status is 0:
        subprocess.call([insights_name, '--unregister'])
        reg_status = 1
        result['changed'] = True
        result['message'] = 'Insights-client has been unregistered'

    if reg_status is not 0:
        display_name_arg = '--display-name=' + display_name
        subprocess.call([insights_name, '--register', display_name_arg])
        result['changed'] = True
        result['message'] = 'Insights-client has been registered'

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
