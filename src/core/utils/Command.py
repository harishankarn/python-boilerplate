import os
import time
import subprocess
import sys
import argparse
import logging
from pathlib import Path
source_path = str(Path("./").resolve())
sys.path.append(source_path) 
from core.utils.Utilities import Utilities

class Command:
    def __init__(self):
        self.util=Utilities()
        logger = logging.getLogger(__name__)
        #print(util.get_value('CLIENT.SUBMIT_URL','../resources/config/config.json'))
    def execute(self,jobname,comp,command:None,arg:None):
        p =  subprocess.Popen('bash', stdin=subprocess.PIPE,
         stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf8')
        os.set_blocking(p.stdout.fileno(), False)
        os.set_blocking(p.stderr.fileno(), False)
        #print(self.util.get_value('CLIENT.SUBMIT_URL','../resources/config/config.json'))
        #print(self.get_pipeline_config_values('fetch.docker.image.name','../config/config.json'))
        #print(command)
        #some commands...
        cmds = ["/home/saju/nlp/src/pipelines/ros_serving_1/"+comp+"/dock.sh /home/saju/nlp/src/pipelines/ros_serving_1/"+comp+" "+jobname+" "+comp]
        i=0
        out = ['']
        try:
            for cmd in cmds:
                print(cmd)
                p.stdin.write(cmd +"\n")
                p.stdin.write("echo ================\n")
                more_out = []
                more_err = []
                while not more_out or more_out[-1]!="================\n":
                    p.stdin.flush()
                    p.stdout.flush()
                    p.stdout.flush()
                    time.sleep(.01)
                    more_out = p.stdout.readlines()
                    err = p.stdout.readlines()
                    if more_out:
                        out.extend(more_out)
                        value=''.join(more_out)
                    if more_err:
                        print('ERROR:', err)
                        break
        except Exception as e:
            raise ImportError(e)
        except RuntimeError as e:
            raise ImportError(e)
        else:
            print("Command Execution")
        finally:
            print('Submitted Command for  Execution  !!!')
    def get_pipeline_config_values(self,key,file_path):
        utilities=Utilities()
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, file_path)
        value=utilities.get_value(key,filename)
        return value

if __name__=="__main__":
    cmd=Command()
    cmd.execute()

