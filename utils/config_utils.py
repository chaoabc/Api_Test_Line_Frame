import os
import configparser

current_dir = os.path.abspath(os.path.dirname(__file__))
config_path = os.path.join(current_dir,'..', 'config',"conf.ini")

class ConfigUtils(object):
    def __init__(self,path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(path)

    @property
    def hosts(self):
        hosts_value = self.cfg.get('default','hosts')
        return hosts_value

    @property
    def report_path(self):
        report_path_value = self.cfg.get('default', 'report_path')
        return report_path_value

local_config = ConfigUtils()

if __name__=='__main__':
    config = ConfigUtils()
    print(type(local_config.hosts),local_config.hosts)
    print( config.report_path )