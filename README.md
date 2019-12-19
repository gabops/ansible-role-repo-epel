gabops.repo_epel
================
[![Build Status](https://travis-ci.org/gabops/ansible-role-repo-epel.svg?branch=develop)](https://travis-ci.org/gabops/ansible-role-repo-epel)

Installs and configures Extra Packages for Enterprise Linux (EPEL) repository

Requirements
------------

This role requires the target system to be a Redhat family OS. Specifically: (See meta/main.yml):

```yaml
  platforms:
    - name: EL
      versions:
        - 6
        - 7
    - name: Amazon
      versions:
        - 2016.09
        - 2017.03
        - 2017.09
        - 2017.12
        - Candidate
```
 

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
|repo_epel_url | "https://dl.fedoraproject.org/pub/epel/epel-release-latest-{{ ansible_distribution_major_version }}.noarch.rpm" | The url pointing to the epel repository package that will be installed |
|repo_epel_yum_repo_file | /etc/yum.repos.d/epel.repo | The path to the epel repo file |
|repo_epel_testing_yum_repo_file | /etc/yum.repos.d/epel-testing.repo | The path to the epel testing repo file |


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
