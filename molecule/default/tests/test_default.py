import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_epel_repo_file(host):
    f = host.file('/etc/yum.repos.d/epel.repo')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_epel_testing_repo_file(host):
    f = host.file('/etc/yum.repos.d/epel-testing.repo')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_epel_yum(host):
    yum_list_return_code = host.run('yum --disablerepo="*" --enablerepo="epel" \
    list available').rc
    assert yum_list_return_code == 0
