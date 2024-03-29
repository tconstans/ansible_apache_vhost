Role Name
=========

This will setup a basic vhost + php fpm (config, directories, dedicated account, logrotate )

Requirements
------------

Obviously an apache server, you'll probably want php and some certificates too.

Role Variables
--------------

apache_access_log: {{ apache_base_dir}}/logs/access_log
apache_allowoverride: all
apache_base_dir: /srv/{{ apache_server_name }}
apache_db_login_password: from my.cnf
apache_db_login_user: from root/.my.cnf
apache_db_name: no default
apache_db_password: no default
apache_db_user: no default
apache_document_root: {{ apache_base_dir }}/www
apache_php_socket: {{ apache_base_dir }}/php-fpm.sock
apache_server_alias (list)
apache_server_ip
apache_server_name
apache_ssl_certificate: /etc/letsencrypt/live/{{ apache_server_name }}/cert.pem
apache_ssl_chain: /etc/letsencrypt/live/{{ apache_server_name }}/fullchain.pem
apache_ssl_key: /etc/letsencrypt/live/{{ apache_server_name }}/privkey.pem
apache_ssl_root_email: email to use for certificate
apache_ssl_root_email: email used for letsencrypt certificate
apache_use_database: false
apache_use_dns: true - wether we setup up dns A and CNAME records
apache_use_php: true
apache_use_ssl: true
apache_use_stats: true
apache_user: {{ apache_server_name | regex_search( '([^.]+)' ) }} }}
apache_user_password: default undefined
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
