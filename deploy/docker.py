import os
from typing import Dict, List, Tuple
from deploy.template import DSC
from deploy.template import MSA

def buildCompose(_target:str, _workdir:str):
    if("DSC" == _target):
        DSC.build(_workdir)
    elif("MSA" == _target):
        MSA.build(_workdir)
