import os
from typing import Dict, List, Tuple
from generator.template.unity2021 import copy_dll
from generator.template.unity2021 import link_vendor
from generator.template.unity2021 import compile
from generator.template.unity2021 import Unity_csproj
from generator.template.unity2021.packages import manifest
from generator.template.unity2021.packages import packages_lock
from generator.template.unity2021.projectsettings import ProjectVersion
from generator.template.unity2021.projectsettings import ProjectSettings
from generator.template.unity2021.assets.editor import PackageTools
from generator.template.unity2021.assets.exports import config
from generator.template.unity2021.assets.exports import catalog
from generator.template.unity2021.assets.exports import ExportRoot
from generator.template.unity2021.assets.scenes import SampleScene
from generator.template.unity2021.assets.scripts import DebugEntry
from generator.template.unity2021.assets.scripts import Root
from generator.template.unity2021.assets.scripts.generated import RootBase
from generator.template.unity2021.assets.scripts.module import DummyView
from generator.template.unity2021.assets.scripts.module import DummyModel
from generator.template.unity2021.assets.scripts.module import MyConfig
from generator.template.unity2021.assets.scripts.module import MyCatalog
from generator.template.unity2021.assets.scripts.module import MyEntry 
from generator.template.unity2021.assets.scripts.module import MyInstance
from generator.template.unity2021.assets.scripts.module import MyRuntime
from generator.template.unity2021.assets.scripts.module import MySubject
from generator.template.unity2021.assets.scripts.module import UiBridge
from generator.template.unity2021.assets.scripts.module.generated import MyConfigBase
from generator.template.unity2021.assets.scripts.module.generated import MyCatalogBase
from generator.template.unity2021.assets.scripts.module.generated import MyEntryBase
from generator.template.unity2021.assets.scripts.module.generated import MyInstanceBase 
from generator.template.unity2021.assets.scripts.module.generated import MyRuntimeBase
from generator.template.unity2021.assets.scripts.module.generated import MySubjectBase
from generator.template.unity2021.assets.scripts.module.generated import UiBridgeBase
from generator.template.unity2021.assets.scripts.module.generated import DummyViewBase
from generator.template.unity2021.assets.scripts.module.generated import DummyModelBase
from generator.template.unity2021.assets.scripts.module.generated import ObjectsPool
from generator.template.unity2021.assets.scripts.module.generated import ResourceReader
from generator.template.unity2021.assets.scripts.module.generated import AssetReader
from generator.template.unity2021.assets.scripts.module.generated import AssetSchema
from generator.template.unity2021.assets.scripts.module.generated import Sequence
from generator.template.unity2021.assets.lib3rd import dll
from generator.template.unity2021 import gitignore


def generate(_options, _workdir: str):
    dir_unity2021 = os.path.join(_workdir, "unity2021")
    os.makedirs(dir_unity2021, exist_ok=True)
    # 生成Asset/.gitignore
    gitignore.generate(_options, dir_unity2021)
    # 生成copy_dll.json
    copy_dll.generate(_options, dir_unity2021)
    link_vendor.generate(_options, dir_unity2021)
    compile.generate(_options, dir_unity2021)
    Unity_csproj.generate(_options, dir_unity2021)

    dir_unity2021 = os.path.join(_workdir, "unity2021/{}".format(_options["module_name"]))
    os.makedirs(dir_unity2021, exist_ok=True)

    # 生成Packages/manifest.json
    manifest.generate(_options, dir_unity2021)
    # 生成Packages/packages-lock.json
    packages_lock.generate(_options, dir_unity2021)
    # 生成ProjectSettings/ProjectVersion.txt
    ProjectVersion.generate(_options, dir_unity2021)
    # 生成ProjectSettings/ProjectSettings.txt
    ProjectSettings.generate(_options, dir_unity2021)
    # 生成Asset/Editor/PackageTools.cs
    PackageTools.generate(_options, dir_unity2021)
    # 生成Asset/Exports/xxxx.xml
    config.generate(_options, dir_unity2021)
    # 生成Asset/Exports/xxxx.json
    catalog.generate(_options, dir_unity2021)
    # 生成Asset/Exports/[ExportRoot].prefab
    ExportRoot.generate(_options, dir_unity2021)
    # 生成Asset/Scenes/SampleScene.unity
    SampleScene.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/DebugEntry.cs
    DebugEntry.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Root.cs
    Root.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/_Generated_/RootBase.cs
    RootBase.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/DummyView.cs
    DummyView.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/DummyModel.cs
    DummyModel.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/MyConfig.cs
    MyConfig.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/MyCatalog.cs
    MyCatalog.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/MyEntry.cs
    MyEntry.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/MyInstance.cs
    MyInstance.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/MyRuntime.cs
    MyRuntime.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/MySubject.cs
    MySubject.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/UiBridge.cs
    UiBridge.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/_Generated_/MyConfigBase.cs
    MyConfigBase.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/_Generated_/MyCatalogBase.cs
    MyCatalogBase.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/_Generated_/MyEntryBase.cs
    MyEntryBase.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/_Generated_/MyInstanceBase.cs
    MyInstanceBase.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/_Generated_/MyRuntimeBase.cs
    MyRuntimeBase.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/_Generated_/MySubjectBase.cs
    MySubjectBase.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/_Generated_/UiBridgeBase.cs
    UiBridgeBase.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/_Generated_/DummyViewBase.cs
    DummyViewBase.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/_Generated_/DummyModelBase.cs
    DummyModelBase.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/_Generated_/ObjectsPool.cs
    ObjectsPool.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/_Generated_/ResourceReader.cs
    ResourceReader.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/_Generated_/AssetReader.cs
    AssetReader.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/_Generated_/AssetSchema.cs
    AssetSchema.generate(_options, dir_unity2021)
    # 生成Asset/Scripts/Module/_Generated_/Sequence.cs
    Sequence.generate(_options, dir_unity2021)
    # 生成Asset/3rd/xxx.dll
    dll.generate(_options, dir_unity2021)
