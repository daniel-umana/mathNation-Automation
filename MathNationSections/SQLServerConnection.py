from paramiko import SSHClient, AutoAddPolicy
from sshtunnel import SSHTunnelForwarder
import mysql.connector


class SQLServerConnection(object):
    def __init__(self, my_driver):
        self.driver = my_driver
        self.db = 0
        self.server = 0
        self.ssh_client = SSHClient()

    def ssh_connection(self, ssh_server, ssh_user, ssh_host_file, db_host, db_user, db_pass, db_table):
        self.ssh_client.load_system_host_keys()
        self.ssh_client.load_host_keys(ssh_host_file)
        self.ssh_client.set_missing_host_key_policy(AutoAddPolicy())
        self.ssh_client.connect(ssh_server, port=22, username=ssh_user,
                                disabled_algorithms={'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']})
        # self.db = mysql.connector.connect(
        #    host=db_host,
        #    user=db_user,
        #    password=db_pass,
        #    database=db_table
        # )

    def server_connection(self, ssh_server, ssh_port, ssh_user, ssh_directory,
                          sql_hostname, sql_port, sql_user, sql_pass, database):

        self.server = SSHTunnelForwarder((ssh_server, ssh_port), ssh_username=ssh_user, ssh_pkey=ssh_directory,
                                         ssh_proxy_enabled=True, remote_bind_address=('127.0.0.1', 3306))
        try:
            self.server.start()
            print("good")
            connection = mysql.connector.connect(database=database, host=sql_hostname, user=sql_user, password=sql_pass,
                                                 auth_plugin='mysql_native_password', charset='utf8', port=sql_port)
            if connection is not None:
                print('Connected')
        except BaseException as e:
            print('Problem with --> ', e)
        finally:
            if self.server:
                self.server.close()
