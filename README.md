Role Name
=========

This will setup a basic vhost + php fpm (config, directories, dedicated account, logrotate )

Requirements
------------

Obviously an apache server, you'll probably want php and some certificates too.

Role Variables
--------------

apache_server_name
apache_server_alias (list)
apache_base_dir: /srv/{{ apache_server_name }}
apache_document_root: {{ apache_base_dir }}/www
apache_access_log: {{ apache_base_dir}}/logs/access_log
apache_php_socket: {{ apache_base_dir }}/php-fpm.sock
apache_use_php: true
apache_use_ssl: true
apache_use_zabbix: true - wether we install script to monitor certificate expiry date
apache_use_certbot: true
apache_stats: true
apache_ssl_certificate: /etc/letsencrypt/live/{{ apache_server_name }}/cert.pem
apache_ssl_chain: /etc/letsencrypt/live/{{ apache_server_name }}/fullchain.pem
apache_ssl_key: /etc/letsencrypt/live/{{ apache_server_name }}/privkey.pem
apache_user: {{ apache_server_name }}
apache_allowoverride: all

Example Playbook
----------------

- name: setup apache vhost for mdv
  hosts: alpine
  vars:
    apache_server_name: maisonduvelolyon.org
    apache_server_alias:
    - stats.maisonduvelolyon.org
    - pignonsurrue.org
    apache_use_ssl: true
  roles:
    - apache_vhost

License
-------

BSD

Author Information
------------------

Thomas C <thomas@opendoor.fr>
