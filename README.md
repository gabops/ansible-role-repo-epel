gabops.repo_epel
================
[![Build Status](https://travis-ci.org/gabops/ansible-role-repo-epel.svg?branch=develop)](https://travis-ci.org/gabops/ansible-role-repo-epel)

Installs and configures Extra Packages for Enterprise Linux (EPEL) repository

Requirements
------------

This role requires the target system to be a Redhat family OS. Specifically:


1. Amazon Linux 1
2. Amazon Linux 2
3. CentOS 6
4. CentOS 7
 

Role Variables
--------------

| Variable | Default | Description |
|:--- |:--- |:--- |
|repo_epel_enable_epel | true | Controls if `epel` repo should be enabled or not |
|repo_epel_enable_epel_debuginfo | false | Controls if `epel-debuginfo` repo should be enabled or not |
|repo_epel_enable_epel_source | false | Controls if `epel-source` repo should be enabled or not |
|repo_epel_enable_epel_testing | false | Controls if `epel-testing` repo should be enabled or not |
|repo_epel_enable_epel_testing_debuginfo | false | Controls if `epel-testing-debuginfo` repo should be enabled or not |
|repo_epel_enable_epel_testing_source | false | Controls if `epel-testing-source` repo should be enabled or not |


Dependencies
------------

None.

Example Playbook
----------------

```yaml
    - hosts: servers
      vars:
        repo_epel_enable_epel: false
        repo_epel_enable_epel_testing: true
      roles:
         - role: gabops.repo_epel
```

License
-------

[MIT](./LICENSE)

Author Information
------------------

Gabriel Suarez ([Gabops](https://github.com/gabops/))
