import os
import uuid
from generator.template.utility import writer

template = """
{
  "dependencies": {
    "com.unity.editorcoroutines": {
      "version": "1.0.0",
      "depth": 1,
      "source": "registry",
      "dependencies": {},
      "url": "https://packages.unity.com"
    },
    "com.unity.ext.nunit": {
      "version": "1.0.6",
      "depth": 1,
      "source": "registry",
      "dependencies": {},
      "url": "https://packages.unity.com"
    },
    "com.unity.feature.development": {
      "version": "1.0.1",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.ide.visualstudio": "2.0.15",
        "com.unity.ide.rider": "3.0.14",
        "com.unity.ide.vscode": "1.2.5",
        "com.unity.editorcoroutines": "1.0.0",
        "com.unity.performance.profile-analyzer": "1.1.1",
        "com.unity.test-framework": "1.1.31",
        "com.unity.testtools.codecoverage": "1.0.1"
      }
    },
    "com.unity.ide.visualstudio": {
      "version": "2.0.15",
      "depth": 0,
      "source": "registry",
      "dependencies": {
        "com.unity.test-framework": "1.1.9"
      },
      "url": "https://packages.unity.com"
    },
    "com.unity.performance.profile-analyzer": {
      "version": "1.1.1",
      "depth": 1,
      "source": "registry",
      "dependencies": {},
      "url": "https://packages.unity.com"
    },
    "com.unity.settings-manager": {
      "version": "1.0.3",
      "depth": 2,
      "source": "registry",
      "dependencies": {},
      "url": "https://packages.unity.com"
    },
    "com.unity.test-framework": {
      "version": "1.1.31",
      "depth": 0,
      "source": "registry",
      "dependencies": {
        "com.unity.ext.nunit": "1.0.6",
        "com.unity.modules.imgui": "1.0.0",
        "com.unity.modules.jsonserialize": "1.0.0"
      },
      "url": "https://packages.unity.com"
    },
    "com.unity.testtools.codecoverage": {
      "version": "1.0.1",
      "depth": 1,
      "source": "registry",
      "dependencies": {
        "com.unity.test-framework": "1.0.16",
        "com.unity.settings-manager": "1.0.1"
      },
      "url": "https://packages.unity.com"
    },
    "com.unity.textmeshpro": {
      "version": "3.0.6",
      "depth": 0,
      "source": "registry",
      "dependencies": {
        "com.unity.ugui": "1.0.0"
      },
      "url": "https://packages.unity.com"
    },
    "com.unity.timeline": {
      "version": "1.6.4",
      "depth": 0,
      "source": "registry",
      "dependencies": {
        "com.unity.modules.director": "1.0.0",
        "com.unity.modules.animation": "1.0.0",
        "com.unity.modules.audio": "1.0.0",
        "com.unity.modules.particlesystem": "1.0.0"
      },
      "url": "https://packages.unity.com"
    },
    "com.unity.ugui": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.ui": "1.0.0",
        "com.unity.modules.imgui": "1.0.0"
      }
    },
    "com.unity.visualscripting": {
      "version": "1.7.8",
      "depth": 0,
      "source": "registry",
      "dependencies": {
        "com.unity.ugui": "1.0.0",
        "com.unity.modules.jsonserialize": "1.0.0"
      },
      "url": "https://packages.unity.com"
    },
    "com.unity.modules.ai": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {}
    },
    "com.unity.modules.androidjni": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {}
    },
    "com.unity.modules.animation": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {}
    },
    "com.unity.modules.assetbundle": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {}
    },
    "com.unity.modules.audio": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {}
    },
    "com.unity.modules.cloth": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.physics": "1.0.0"
      }
    },
    "com.unity.modules.director": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.audio": "1.0.0",
        "com.unity.modules.animation": "1.0.0"
      }
    },
    "com.unity.modules.imageconversion": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {}
    },
    "com.unity.modules.imgui": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {}
    },
    "com.unity.modules.jsonserialize": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {}
    },
    "com.unity.modules.particlesystem": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {}
    },
    "com.unity.modules.physics": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {}
    },
    "com.unity.modules.physics2d": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {}
    },
    "com.unity.modules.screencapture": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.imageconversion": "1.0.0"
      }
    },
    "com.unity.modules.subsystems": {
      "version": "1.0.0",
      "depth": 1,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.jsonserialize": "1.0.0"
      }
    },
    "com.unity.modules.terrain": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {}
    },
    "com.unity.modules.terrainphysics": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.physics": "1.0.0",
        "com.unity.modules.terrain": "1.0.0"
      }
    },
    "com.unity.modules.tilemap": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.physics2d": "1.0.0"
      }
    },
    "com.unity.modules.ui": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {}
    },
    "com.unity.modules.uielements": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.ui": "1.0.0",
        "com.unity.modules.imgui": "1.0.0",
        "com.unity.modules.jsonserialize": "1.0.0",
        "com.unity.modules.uielementsnative": "1.0.0"
      }
    },
    "com.unity.modules.uielementsnative": {
      "version": "1.0.0",
      "depth": 1,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.ui": "1.0.0",
        "com.unity.modules.imgui": "1.0.0",
        "com.unity.modules.jsonserialize": "1.0.0"
      }
    },
    "com.unity.modules.umbra": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {}
    },
    "com.unity.modules.unityanalytics": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.unitywebrequest": "1.0.0",
        "com.unity.modules.jsonserialize": "1.0.0"
      }
    },
    "com.unity.modules.unitywebrequest": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {}
    },
    "com.unity.modules.unitywebrequestassetbundle": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.assetbundle": "1.0.0",
        "com.unity.modules.unitywebrequest": "1.0.0"
      }
    },
    "com.unity.modules.unitywebrequestaudio": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.unitywebrequest": "1.0.0",
        "com.unity.modules.audio": "1.0.0"
      }
    },
    "com.unity.modules.unitywebrequesttexture": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.unitywebrequest": "1.0.0",
        "com.unity.modules.imageconversion": "1.0.0"
      }
    },
    "com.unity.modules.unitywebrequestwww": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.unitywebrequest": "1.0.0",
        "com.unity.modules.unitywebrequestassetbundle": "1.0.0",
        "com.unity.modules.unitywebrequestaudio": "1.0.0",
        "com.unity.modules.audio": "1.0.0",
        "com.unity.modules.assetbundle": "1.0.0",
        "com.unity.modules.imageconversion": "1.0.0"
      }
    },
    "com.unity.modules.vehicles": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.physics": "1.0.0"
      }
    },
    "com.unity.modules.video": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.audio": "1.0.0",
        "com.unity.modules.ui": "1.0.0",
        "com.unity.modules.unitywebrequest": "1.0.0"
      }
    },
    "com.unity.modules.vr": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.jsonserialize": "1.0.0",
        "com.unity.modules.physics": "1.0.0",
        "com.unity.modules.xr": "1.0.0"
      }
    },
    "com.unity.modules.wind": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {}
    },
    "com.unity.modules.xr": {
      "version": "1.0.0",
      "depth": 0,
      "source": "builtin",
      "dependencies": {
        "com.unity.modules.physics": "1.0.0",
        "com.unity.modules.jsonserialize": "1.0.0",
        "com.unity.modules.subsystems": "1.0.0"
      }
    }
  }
} 
"""


def generate(_options, _outputdir: str):
    output_dir = os.path.join(_outputdir, "Packages")
    os.makedirs(output_dir, exist_ok=True)

    contents = template
    output_path = os.path.join(output_dir, "packages-lock.json")
    writer.write(output_path, contents, False)
