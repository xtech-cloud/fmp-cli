import os
from typing import Dict, List, Tuple
from deploy.template import DSC

def buildCompose(_target:str, _workdir:str):
    if("DSC" == _target):
        DSC.build(_workdir)
