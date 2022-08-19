import os
import uuid
from generator.template.utility import writer

template = """%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!129 &1
PlayerSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 23
  productGUID: fb7927a229388f242b8e328c390982ae
  AndroidProfiler: 0
  AndroidFilterTouchesWhenObscured: 0
  AndroidEnableSustainedPerformanceMode: 0
  defaultScreenOrientation: 4
  targetDevice: 2
  useOnDemandResources: 0
  accelerometerFrequency: 60
  companyName: XTC
  productName: FMP
  defaultCursor: {fileID: 0}
  cursorHotspot: {x: 0, y: 0}
  m_SplashScreenBackgroundColor: {r: 0.12156863, g: 0.12156863, b: 0.1254902, a: 1}
  m_ShowUnitySplashScreen: 1
  m_ShowUnitySplashLogo: 1
  m_SplashScreenOverlayOpacity: 1
  m_SplashScreenAnimation: 1
  m_SplashScreenLogoStyle: 1
  m_SplashScreenDrawMode: 0
  m_SplashScreenBackgroundAnimationZoom: 1
  m_SplashScreenLogoAnimationZoom: 1
  m_SplashScreenBackgroundLandscapeAspect: 1
  m_SplashScreenBackgroundPortraitAspect: 1
  m_SplashScreenBackgroundLandscapeUvs:
    serializedVersion: 2
    x: 0
    y: 0
    width: 1
    height: 1
  m_SplashScreenBackgroundPortraitUvs:
    serializedVersion: 2
    x: 0
    y: 0
    width: 1
    height: 1
  m_SplashScreenLogos: []
  m_VirtualRealitySplashScreen: {fileID: 0}
  m_HolographicTrackingLossScreen: {fileID: 0}
  defaultScreenWidth: 1920
  defaultScreenHeight: 1080
  defaultScreenWidthWeb: 960
  defaultScreenHeightWeb: 600
  m_StereoRenderingPath: 0
  m_ActiveColorSpace: 0
  m_MTRendering: 1
  mipStripping: 0
  numberOfMipsStripped: 0
  m_StackTraceTypes: 010000000100000001000000010000000100000001000000
  iosShowActivityIndicatorOnLoading: -1
  androidShowActivityIndicatorOnLoading: -1
  iosUseCustomAppBackgroundBehavior: 0
  iosAllowHTTPDownload: 1
  allowedAutorotateToPortrait: 1
  allowedAutorotateToPortraitUpsideDown: 1
  allowedAutorotateToLandscapeRight: 1
  allowedAutorotateToLandscapeLeft: 1
  useOSAutorotation: 1
  use32BitDisplayBuffer: 1
  preserveFramebufferAlpha: 0
  disableDepthAndStencilBuffers: 0
  androidStartInFullscreen: 1
  androidRenderOutsideSafeArea: 1
  androidUseSwappy: 1
  androidBlitType: 0
  androidResizableWindow: 0
  androidDefaultWindowWidth: 1920
  androidDefaultWindowHeight: 1080
  androidMinimumWindowWidth: 400
  androidMinimumWindowHeight: 300
  androidFullscreenMode: 1
  defaultIsNativeResolution: 1
  macRetinaSupport: 1
  runInBackground: 0
  captureSingleScreen: 0
  muteOtherAudioSources: 0
  Prepare IOS For Recording: 0
  Force IOS Speakers When Recording: 0
  deferSystemGesturesMode: 0
  hideHomeButton: 0
  submitAnalytics: 1
  usePlayerLog: 1
  bakeCollisionMeshes: 0
  forceSingleInstance: 0
  useFlipModelSwapchain: 1
  resizableWindow: 0
  useMacAppStoreValidation: 0
  macAppStoreCategory: public.app-category.games
  gpuSkinning: 0
  xboxPIXTextureCapture: 0
  xboxEnableAvatar: 0
  xboxEnableKinect: 0
  xboxEnableKinectAutoTracking: 0
  xboxEnableFitness: 0
  visibleInBackground: 1
  allowFullscreenSwitch: 1
  fullscreenMode: 1
  xboxSpeechDB: 0
  xboxEnableHeadOrientation: 0
  xboxEnableGuest: 0
  xboxEnablePIXSampling: 0
  metalFramebufferOnly: 0
  xboxOneResolution: 0
  xboxOneSResolution: 0
  xboxOneXResolution: 3
  xboxOneMonoLoggingLevel: 0
  xboxOneLoggingLevel: 1
  xboxOneDisableEsram: 0
  xboxOneEnableTypeOptimization: 0
  xboxOnePresentImmediateThreshold: 0
  switchQueueCommandMemory: 1048576
  switchQueueControlMemory: 16384
  switchQueueComputeMemory: 262144
  switchNVNShaderPoolsGranularity: 33554432
  switchNVNDefaultPoolsGranularity: 16777216
  switchNVNOtherPoolsGranularity: 16777216
  switchNVNMaxPublicTextureIDCount: 0
  switchNVNMaxPublicSamplerIDCount: 0
  stadiaPresentMode: 0
  stadiaTargetFramerate: 0
  vulkanNumSwapchainBuffers: 3
  vulkanEnableSetSRGBWrite: 0
  vulkanEnablePreTransform: 0
  vulkanEnableLateAcquireNextImage: 0
  vulkanEnableCommandBufferRecycling: 1
  m_SupportedAspectRatios:
    4:3: 1
    5:4: 1
    16:10: 1
    16:9: 1
    Others: 1
  bundleVersion: 1.0
  preloadedAssets: []
  metroInputSource: 0
  wsaTransparentSwapchain: 0
  m_HolographicPauseOnTrackingLoss: 1
  xboxOneDisableKinectGpuReservation: 1
  xboxOneEnable7thCore: 1
  vrSettings:
    enable360StereoCapture: 0
  isWsaHolographicRemotingEnabled: 0
  enableFrameTimingStats: 0
  enableOpenGLProfilerGPURecorders: 1
  useHDRDisplay: 0
  D3DHDRBitDepth: 0
  m_ColorGamuts: 00000000
  targetPixelDensity: 30
  resolutionScalingMode: 0
  resetResolutionOnWindowResize: 0
  androidSupportedAspectRatio: 1
  androidMaxAspectRatio: 2.1
  applicationIdentifier: {}
  buildNumber:
    Standalone: 0
    iPhone: 0
    tvOS: 0
  overrideDefaultApplicationIdentifier: 0
  AndroidBundleVersionCode: 1
  AndroidMinSdkVersion: 22
  AndroidTargetSdkVersion: 0
  AndroidPreferredInstallLocation: 1
  aotOptions: 
  stripEngineCode: 1
  iPhoneStrippingLevel: 0
  iPhoneScriptCallOptimization: 0
  ForceInternetPermission: 0
  ForceSDCardPermission: 0
  CreateWallpaper: 0
  APKExpansionFiles: 0
  keepLoadedShadersAlive: 0
  StripUnusedMeshComponents: 0
  VertexChannelCompressionMask: 4054
  iPhoneSdkVersion: 988
  iOSTargetOSVersionString: 11.0
  tvOSSdkVersion: 0
  tvOSRequireExtendedGameController: 0
  tvOSTargetOSVersionString: 11.0
  uIPrerenderedIcon: 0
  uIRequiresPersistentWiFi: 0
  uIRequiresFullScreen: 1
  uIStatusBarHidden: 1
  uIExitOnSuspend: 0
  uIStatusBarStyle: 0
  appleTVSplashScreen: {fileID: 0}
  appleTVSplashScreen2x: {fileID: 0}
  tvOSSmallIconLayers: []
  tvOSSmallIconLayers2x: []
  tvOSLargeIconLayers: []
  tvOSLargeIconLayers2x: []
  tvOSTopShelfImageLayers: []
  tvOSTopShelfImageLayers2x: []
  tvOSTopShelfImageWideLayers: []
  tvOSTopShelfImageWideLayers2x: []
  iOSLaunchScreenType: 0
  iOSLaunchScreenPortrait: {fileID: 0}
  iOSLaunchScreenLandscape: {fileID: 0}
  iOSLaunchScreenBackgroundColor:
    serializedVersion: 2
    rgba: 0
  iOSLaunchScreenFillPct: 100
  iOSLaunchScreenSize: 100
  iOSLaunchScreenCustomXibPath: 
  iOSLaunchScreeniPadType: 0
  iOSLaunchScreeniPadImage: {fileID: 0}
  iOSLaunchScreeniPadBackgroundColor:
    serializedVersion: 2
    rgba: 0
  iOSLaunchScreeniPadFillPct: 100
  iOSLaunchScreeniPadSize: 100
  iOSLaunchScreeniPadCustomXibPath: 
  iOSLaunchScreenCustomStoryboardPath: 
  iOSLaunchScreeniPadCustomStoryboardPath: 
  iOSDeviceRequirements: []
  iOSURLSchemes: []
  macOSURLSchemes: []
  iOSBackgroundModes: 0
  iOSMetalForceHardShadows: 0
  metalEditorSupport: 1
  metalAPIValidation: 1
  iOSRenderExtraFrameOnPause: 0
  iosCopyPluginsCodeInsteadOfSymlink: 0
  appleDeveloperTeamID: 
  iOSManualSigningProvisioningProfileID: 
  tvOSManualSigningProvisioningProfileID: 
  iOSManualSigningProvisioningProfileType: 0
  tvOSManualSigningProvisioningProfileType: 0
  appleEnableAutomaticSigning: 0
  iOSRequireARKit: 0
  iOSAutomaticallyDetectAndAddCapabilities: 1
  appleEnableProMotion: 0
  shaderPrecisionModel: 0
  clonedFromGUID: 00000000000000000000000000000000
  templatePackageId: 
  templateDefaultScene: 
  useCustomMainManifest: 0
  useCustomLauncherManifest: 0
  useCustomMainGradleTemplate: 0
  useCustomLauncherGradleManifest: 0
  useCustomBaseGradleTemplate: 0
  useCustomGradlePropertiesTemplate: 0
  useCustomProguardFile: 0
  AndroidTargetArchitectures: 1
  AndroidTargetDevices: 0
  AndroidSplashScreenScale: 0
  androidSplashScreen: {fileID: 0}
  AndroidKeystoreName: 
  AndroidKeyaliasName: 
  AndroidBuildApkPerCpuArchitecture: 0
  AndroidTVCompatibility: 0
  AndroidIsGame: 1
  AndroidEnableTango: 0
  androidEnableBanner: 1
  androidUseLowAccuracyLocation: 0
  androidUseCustomKeystore: 0
  m_AndroidBanners:
  - width: 320
    height: 180
    banner: {fileID: 0}
  androidGamepadSupportLevel: 0
  chromeosInputEmulation: 1
  AndroidMinifyWithR8: 0
  AndroidMinifyRelease: 0
  AndroidMinifyDebug: 0
  AndroidValidateAppBundleSize: 1
  AndroidAppBundleSizeToValidate: 150
  m_BuildTargetIcons: []
  m_BuildTargetPlatformIcons:
  - m_BuildTarget: Android
    m_Icons:
    - m_Textures: []
      m_Width: 432
      m_Height: 432
      m_Kind: 2
      m_SubKind: 
    - m_Textures: []
      m_Width: 324
      m_Height: 324
      m_Kind: 2
      m_SubKind: 
    - m_Textures: []
      m_Width: 216
      m_Height: 216
      m_Kind: 2
      m_SubKind: 
    - m_Textures: []
      m_Width: 162
      m_Height: 162
      m_Kind: 2
      m_SubKind: 
    - m_Textures: []
      m_Width: 108
      m_Height: 108
      m_Kind: 2
      m_SubKind: 
    - m_Textures: []
      m_Width: 81
      m_Height: 81
      m_Kind: 2
      m_SubKind: 
    - m_Textures: []
      m_Width: 192
      m_Height: 192
      m_Kind: 1
      m_SubKind: 
    - m_Textures: []
      m_Width: 144
      m_Height: 144
      m_Kind: 1
      m_SubKind: 
    - m_Textures: []
      m_Width: 96
      m_Height: 96
      m_Kind: 1
      m_SubKind: 
    - m_Textures: []
      m_Width: 72
      m_Height: 72
      m_Kind: 1
      m_SubKind: 
    - m_Textures: []
      m_Width: 48
      m_Height: 48
      m_Kind: 1
      m_SubKind: 
    - m_Textures: []
      m_Width: 36
      m_Height: 36
      m_Kind: 1
      m_SubKind: 
    - m_Textures: []
      m_Width: 192
      m_Height: 192
      m_Kind: 0
      m_SubKind: 
    - m_Textures: []
      m_Width: 144
      m_Height: 144
      m_Kind: 0
      m_SubKind: 
    - m_Textures: []
      m_Width: 96
      m_Height: 96
      m_Kind: 0
      m_SubKind: 
    - m_Textures: []
      m_Width: 72
      m_Height: 72
      m_Kind: 0
      m_SubKind: 
    - m_Textures: []
      m_Width: 48
      m_Height: 48
      m_Kind: 0
      m_SubKind: 
    - m_Textures: []
      m_Width: 36
      m_Height: 36
      m_Kind: 0
      m_SubKind: 
  m_BuildTargetBatching: []
  m_BuildTargetGraphicsJobs: []
  m_BuildTargetGraphicsJobMode: []
  m_BuildTargetGraphicsAPIs: []
  m_BuildTargetVRSettings: []
  openGLRequireES31: 0
  openGLRequireES31AEP: 0
  openGLRequireES32: 0
  m_TemplateCustomTags: {}
  mobileMTRendering:
    Android: 1
    iPhone: 1
    tvOS: 1
  m_BuildTargetGroupLightmapEncodingQuality: []
  m_BuildTargetGroupLightmapSettings: []
  m_BuildTargetNormalMapEncoding: []
  m_BuildTargetDefaultTextureCompressionFormat: []
  playModeTestRunnerEnabled: 0
  runPlayModeTestAsEditModeTest: 0
  actionOnDotNetUnhandledException: 1
  enableInternalProfiler: 0
  logObjCUncaughtExceptions: 1
  enableCrashReportAPI: 0
  cameraUsageDescription: 
  locationUsageDescription: 
  microphoneUsageDescription: 
  bluetoothUsageDescription: 
  switchNMETAOverride: 
  switchNetLibKey: 
  switchSocketMemoryPoolSize: 6144
  switchSocketAllocatorPoolSize: 128
  switchSocketConcurrencyLimit: 14
  switchScreenResolutionBehavior: 2
  switchUseCPUProfiler: 0
  switchUseGOLDLinker: 0
  switchLTOSetting: 0
  switchApplicationID: 0x01004b9000490000
  switchNSODependencies: 
  switchTitleNames_0: 
  switchTitleNames_1: 
  switchTitleNames_2: 
  switchTitleNames_3: 
  switchTitleNames_4: 
  switchTitleNames_5: 
  switchTitleNames_6: 
  switchTitleNames_7: 
  switchTitleNames_8: 
  switchTitleNames_9: 
  switchTitleNames_10: 
  switchTitleNames_11: 
  switchTitleNames_12: 
  switchTitleNames_13: 
  switchTitleNames_14: 
  switchTitleNames_15: 
  switchPublisherNames_0: 
  switchPublisherNames_1: 
  switchPublisherNames_2: 
  switchPublisherNames_3: 
  switchPublisherNames_4: 
  switchPublisherNames_5: 
  switchPublisherNames_6: 
  switchPublisherNames_7: 
  switchPublisherNames_8: 
  switchPublisherNames_9: 
  switchPublisherNames_10: 
  switchPublisherNames_11: 
  switchPublisherNames_12: 
  switchPublisherNames_13: 
  switchPublisherNames_14: 
  switchPublisherNames_15: 
  switchIcons_0: {fileID: 0}
  switchIcons_1: {fileID: 0}
  switchIcons_2: {fileID: 0}
  switchIcons_3: {fileID: 0}
  switchIcons_4: {fileID: 0}
  switchIcons_5: {fileID: 0}
  switchIcons_6: {fileID: 0}
  switchIcons_7: {fileID: 0}
  switchIcons_8: {fileID: 0}
  switchIcons_9: {fileID: 0}
  switchIcons_10: {fileID: 0}
  switchIcons_11: {fileID: 0}
  switchIcons_12: {fileID: 0}
  switchIcons_13: {fileID: 0}
  switchIcons_14: {fileID: 0}
  switchIcons_15: {fileID: 0}
  switchSmallIcons_0: {fileID: 0}
  switchSmallIcons_1: {fileID: 0}
  switchSmallIcons_2: {fileID: 0}
  switchSmallIcons_3: {fileID: 0}
  switchSmallIcons_4: {fileID: 0}
  switchSmallIcons_5: {fileID: 0}
  switchSmallIcons_6: {fileID: 0}
  switchSmallIcons_7: {fileID: 0}
  switchSmallIcons_8: {fileID: 0}
  switchSmallIcons_9: {fileID: 0}
  switchSmallIcons_10: {fileID: 0}
  switchSmallIcons_11: {fileID: 0}
  switchSmallIcons_12: {fileID: 0}
  switchSmallIcons_13: {fileID: 0}
  switchSmallIcons_14: {fileID: 0}
  switchSmallIcons_15: {fileID: 0}
  switchManualHTML: 
  switchAccessibleURLs: 
  switchLegalInformation: 
  switchMainThreadStackSize: 1048576
  switchPresenceGroupId: 
  switchLogoHandling: 0
  switchReleaseVersion: 0
  switchDisplayVersion: 1.0.0
  switchStartupUserAccount: 0
  switchTouchScreenUsage: 0
  switchSupportedLanguagesMask: 0
  switchLogoType: 0
  switchApplicationErrorCodeCategory: 
  switchUserAccountSaveDataSize: 0
  switchUserAccountSaveDataJournalSize: 0
  switchApplicationAttribute: 0
  switchCardSpecSize: -1
  switchCardSpecClock: -1
  switchRatingsMask: 0
  switchRatingsInt_0: 0
  switchRatingsInt_1: 0
  switchRatingsInt_2: 0
  switchRatingsInt_3: 0
  switchRatingsInt_4: 0
  switchRatingsInt_5: 0
  switchRatingsInt_6: 0
  switchRatingsInt_7: 0
  switchRatingsInt_8: 0
  switchRatingsInt_9: 0
  switchRatingsInt_10: 0
  switchRatingsInt_11: 0
  switchRatingsInt_12: 0
  switchLocalCommunicationIds_0: 
  switchLocalCommunicationIds_1: 
  switchLocalCommunicationIds_2: 
  switchLocalCommunicationIds_3: 
  switchLocalCommunicationIds_4: 
  switchLocalCommunicationIds_5: 
  switchLocalCommunicationIds_6: 
  switchLocalCommunicationIds_7: 
  switchParentalControl: 0
  switchAllowsScreenshot: 1
  switchAllowsVideoCapturing: 1
  switchAllowsRuntimeAddOnContentInstall: 0
  switchDataLossConfirmation: 0
  switchUserAccountLockEnabled: 0
  switchSystemResourceMemory: 16777216
  switchSupportedNpadStyles: 22
  switchNativeFsCacheSize: 32
  switchIsHoldTypeHorizontal: 0
  switchSupportedNpadCount: 8
  switchSocketConfigEnabled: 0
  switchTcpInitialSendBufferSize: 32
  switchTcpInitialReceiveBufferSize: 64
  switchTcpAutoSendBufferSizeMax: 256
  switchTcpAutoReceiveBufferSizeMax: 256
  switchUdpSendBufferSize: 9
  switchUdpReceiveBufferSize: 42
  switchSocketBufferEfficiency: 4
  switchSocketInitializeEnabled: 1
  switchNetworkInterfaceManagerInitializeEnabled: 1
  switchPlayerConnectionEnabled: 1
  switchUseNewStyleFilepaths: 0
  switchUseMicroSleepForYield: 1
  switchEnableRamDiskSupport: 0
  switchMicroSleepForYieldTime: 25
  switchRamDiskSpaceSize: 12
  ps4NPAgeRating: 12
  ps4NPTitleSecret: 
  ps4NPTrophyPackPath: 
  ps4ParentalLevel: 11
  ps4ContentID: ED1633-NPXX51362_00-0000000000000000
  ps4Category: 0
  ps4MasterVersion: 01.00
  ps4AppVersion: 01.00
  ps4AppType: 0
  ps4ParamSfxPath: 
  ps4VideoOutPixelFormat: 0
  ps4VideoOutInitialWidth: 1920
  ps4VideoOutBaseModeInitialWidth: 1920
  ps4VideoOutReprojectionRate: 60
  ps4PronunciationXMLPath: 
  ps4PronunciationSIGPath: 
  ps4BackgroundImagePath: 
  ps4StartupImagePath: 
  ps4StartupImagesFolder: 
  ps4IconImagesFolder: 
  ps4SaveDataImagePath: 
  ps4SdkOverride: 
  ps4BGMPath: 
  ps4ShareFilePath: 
  ps4ShareOverlayImagePath: 
  ps4PrivacyGuardImagePath: 
  ps4ExtraSceSysFile: 
  ps4NPtitleDatPath: 
  ps4RemotePlayKeyAssignment: -1
  ps4RemotePlayKeyMappingDir: 
  ps4PlayTogetherPlayerCount: 0
  ps4EnterButtonAssignment: 2
  ps4ApplicationParam1: 0
  ps4ApplicationParam2: 0
  ps4ApplicationParam3: 0
  ps4ApplicationParam4: 0
  ps4DownloadDataSize: 0
  ps4GarlicHeapSize: 2048
  ps4ProGarlicHeapSize: 2560
  playerPrefsMaxSize: 32768
  ps4Passcode: frAQBc8Wsa1xVPfvJcrgRYwTiizs2trQ
  ps4pnSessions: 1
  ps4pnPresence: 1
  ps4pnFriends: 1
  ps4pnGameCustomData: 1
  playerPrefsSupport: 0
  enableApplicationExit: 0
  resetTempFolder: 1
  restrictedAudioUsageRights: 0
  ps4UseResolutionFallback: 0
  ps4ReprojectionSupport: 0
  ps4UseAudio3dBackend: 0
  ps4UseLowGarlicFragmentationMode: 1
  ps4SocialScreenEnabled: 0
  ps4ScriptOptimizationLevel: 2
  ps4Audio3dVirtualSpeakerCount: 14
  ps4attribCpuUsage: 0
  ps4PatchPkgPath: 
  ps4PatchLatestPkgPath: 
  ps4PatchChangeinfoPath: 
  ps4PatchDayOne: 0
  ps4attribUserManagement: 0
  ps4attribMoveSupport: 0
  ps4attrib3DSupport: 0
  ps4attribShareSupport: 0
  ps4attribExclusiveVR: 0
  ps4disableAutoHideSplash: 0
  ps4videoRecordingFeaturesUsed: 0
  ps4contentSearchFeaturesUsed: 0
  ps4CompatibilityPS5: 0
  ps4GPU800MHz: 1
  ps4attribEyeToEyeDistanceSettingVR: 0
  ps4IncludedModules: []
  ps4attribVROutputEnabled: 0
  monoEnv: 
  splashScreenBackgroundSourceLandscape: {fileID: 0}
  splashScreenBackgroundSourcePortrait: {fileID: 0}
  blurSplashScreenBackground: 1
  spritePackerPolicy: 
  webGLMemorySize: 32
  webGLExceptionSupport: 1
  webGLNameFilesAsHashes: 0
  webGLDataCaching: 1
  webGLDebugSymbols: 0
  webGLEmscriptenArgs: 
  webGLModulesDirectory: 
  webGLTemplate: APPLICATION:Default
  webGLAnalyzeBuildSize: 0
  webGLUseEmbeddedResources: 0
  webGLCompressionFormat: 0
  webGLWasmArithmeticExceptions: 0
  webGLLinkerTarget: 1
  webGLThreadsSupport: 0
  webGLDecompressionFallback: 0
  scriptingDefineSymbols: {}
  additionalCompilerArguments: {}
  platformArchitecture: {}
  scriptingBackend: {}
  il2cppCompilerConfiguration: {}
  managedStrippingLevel: {}
  incrementalIl2cppBuild: {}
  suppressCommonWarnings: 1
  allowUnsafeCode: 0
  useDeterministicCompilation: 1
  enableRoslynAnalyzers: 1
  additionalIl2CppArgs: 
  scriptingRuntimeVersion: 1
  gcIncremental: 1
  assemblyVersionValidation: 1
  gcWBarrierValidation: 0
  apiCompatibilityLevelPerPlatform: {}
  m_RenderingPath: 1
  m_MobileRenderingPath: 1
  metroPackageName: FMP
  metroPackageVersion: 
  metroCertificatePath: 
  metroCertificatePassword: 
  metroCertificateSubject: 
  metroCertificateIssuer: 
  metroCertificateNotAfter: 0000000000000000
  metroApplicationDescription: FMP
  wsaImages: {}
  metroTileShortName: 
  metroTileShowName: 0
  metroMediumTileShowName: 0
  metroLargeTileShowName: 0
  metroWideTileShowName: 0
  metroSupportStreamingInstall: 0
  metroLastRequiredScene: 0
  metroDefaultTileSize: 1
  metroTileForegroundText: 2
  metroTileBackgroundColor: {r: 0.13333334, g: 0.17254902, b: 0.21568628, a: 0}
  metroSplashScreenBackgroundColor: {r: 0.12941177, g: 0.17254902, b: 0.21568628, a: 1}
  metroSplashScreenUseBackgroundColor: 0
  platformCapabilities: {}
  metroTargetDeviceFamilies: {}
  metroFTAName: 
  metroFTAFileTypes: []
  metroProtocolName: 
  vcxProjDefaultLanguage: 
  XboxOneProductId: 
  XboxOneUpdateKey: 
  XboxOneSandboxId: 
  XboxOneContentId: 
  XboxOneTitleId: 
  XboxOneSCId: 
  XboxOneGameOsOverridePath: 
  XboxOnePackagingOverridePath: 
  XboxOneAppManifestOverridePath: 
  XboxOneVersion: 1.0.0.0
  XboxOnePackageEncryption: 0
  XboxOnePackageUpdateGranularity: 2
  XboxOneDescription: 
  XboxOneLanguage:
  - enus
  XboxOneCapability: []
  XboxOneGameRating: {}
  XboxOneIsContentPackage: 0
  XboxOneEnhancedXboxCompatibilityMode: 0
  XboxOneEnableGPUVariability: 1
  XboxOneSockets: {}
  XboxOneSplashScreen: {fileID: 0}
  XboxOneAllowedProductIds: []
  XboxOnePersistentLocalStorageSize: 0
  XboxOneXTitleMemory: 8
  XboxOneOverrideIdentityName: 
  XboxOneOverrideIdentityPublisher: 
  vrEditorSettings: {}
  cloudServicesEnabled: {}
  luminIcon:
    m_Name: 
    m_ModelFolderPath: 
    m_PortalFolderPath: 
  luminCert:
    m_CertPath: 
    m_SignPackage: 1
  luminIsChannelApp: 0
  luminVersion:
    m_VersionCode: 1
    m_VersionName: 
  apiCompatibilityLevel: 6
  activeInputHandler: 0
  cloudProjectId: 
  framebufferDepthMemorylessMode: 0
  qualitySettingsNames: []
  projectName: 
  organizationId: 
  cloudEnabled: 0
  legacyClampBlendShapeWeights: 0
  playerDataPath: 
  forceSRGBBlit: 1
  virtualTexturingSupportEnabled: 0 
"""


def generate(_options, _outputdir: str):
    output_dir = os.path.join(_outputdir, "ProjectSettings")
    os.makedirs(output_dir, exist_ok=True)

    contents = template
    output_path = os.path.join(output_dir, "ProjectSettings.asset")
    writer.write(output_path, contents, False)
