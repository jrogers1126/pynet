#!/usr/bin/env python
DOCUMENTATION = '''
---
module: eapi_vlan
short_description: VLAN Commands for Arista, via eapi
'''

EXAMPLES = '''
- name: configures the vlan name
  eapi_vlan: vlanid=1 name=TEST_VLAN_1
'''

from ansible.module_utils.basic import AnsibleModule
if __name__ == '__main__':
    main()
