---
UID: NS:ata._IDENTIFY_DEVICE_DATA
title: "_IDENTIFY_DEVICE_DATA"
author: windows-driver-content
description: The IDENTIFY_DEVICE_DATA structure contains the data retrieved by an ATA identify device data command (0xEC).Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\identify_device_data.htm
old-project: storage
ms.assetid: 7f2edd6f-16bf-47a6-8546-7871435a56ac
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: "*PIDENTIFY_DEVICE_DATA, IDENTIFY_DEVICE_DATA, IDENTIFY_DEVICE_DATA structure [Storage Devices], PIDENTIFY_DEVICE_DATA, PIDENTIFY_DEVICE_DATA structure pointer [Storage Devices], _IDENTIFY_DEVICE_DATA, ata/IDENTIFY_DEVICE_DATA, ata/PIDENTIFY_DEVICE_DATA, storage.identify_device_data, structs-ATA_904f6e71-4dd9-4ecb-9928-0d7ce44b83ef.xml"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ata.h
req.include-header: Irb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ata.h
api_name:
-	IDENTIFY_DEVICE_DATA
product: Windows
targetos: Windows
req.typenames: IDENTIFY_DEVICE_DATA, *PIDENTIFY_DEVICE_DATA
---

# _IDENTIFY_DEVICE_DATA structure
The IDENTIFY_DEVICE_DATA structure contains the data retrieved by an ATA identify device data command (0xEC).
<div class="alert"><b>Note</b>  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/storage/storport-driver">Storport driver</a> and <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/storage/storport-miniport-drivers">Storport miniport</a> driver models.</div><div> </div>

## Syntax
```
typedef struct _IDENTIFY_DEVICE_DATA {
  struct {
    USHORT  : 1 DeviceType;
    USHORT  : 1 FixedDevice;
    USHORT  : 1 RemovableMedia;
    USHORT  : 1 Reserved1;
    USHORT  : 1 ResponseIncomplete;
    USHORT  : 7 Retired1;
    USHORT  : 3 Retired2;
    USHORT  : 1 Retired3;
  } GeneralConfiguration;
  USHORT       NumCylinders;
  USHORT       SpecificConfiguration;
  USHORT       NumHeads;
  USHORT       Retired1[2];
  USHORT       NumSectorsPerTrack;
  USHORT       VendorUnique1[3];
  UCHAR        SerialNumber[20];
  USHORT       Retired2[2];
  USHORT       Obsolete1;
  UCHAR        FirmwareRevision[8];
  UCHAR        ModelNumber[40];
  UCHAR        MaximumBlockTransfer;
  UCHAR        VendorUnique2;
  struct {
    USHORT  : 1  FeatureSupported;
    USHORT  : 15 Reserved;
  } TrustedComputing;
  struct {
    UCHAR  : 2 CurrentLongPhysicalSectorAlignment;
    UCHAR  : 1 DmaSupported;
    UCHAR  : 1 IordyDisable;
    UCHAR  : 1 IordySupported;
    UCHAR  : 1 LbaSupported;
    UCHAR  : 1 Reserved1;
    UCHAR  : 2 Reserved2;
    UCHAR  : 6 ReservedByte49;
    USHORT     ReservedWord50;
    UCHAR  : 1 StandybyTimerSupport;
  } Capabilities;
  USHORT       ObsoleteWords51[2];
  USHORT  : 3  TranslationFieldsValid;
  USHORT  : 5  Reserved3;
  USHORT  : 8  FreeFallControlSensitivity;
  USHORT       NumberOfCurrentCylinders;
  USHORT       NumberOfCurrentHeads;
  USHORT       CurrentSectorsPerTrack;
  ULONG        CurrentSectorCapacity;
  UCHAR        CurrentMultiSectorSetting;
  UCHAR  : 1   MultiSectorSettingValid;
  UCHAR  : 3   ReservedByte59;
  UCHAR  : 1   SanitizeFeatureSupported;
  UCHAR  : 1   CryptoScrambleExtCommandSupported;
  UCHAR  : 1   OverwriteExtCommandSupported;
  UCHAR  : 1   BlockEraseExtCommandSupported;
  ULONG        UserAddressableSectors;
  USHORT       ObsoleteWord62;
  USHORT  : 8  MultiWordDMASupport;
  USHORT  : 8  MultiWordDMAActive;
  USHORT  : 8  AdvancedPIOModes;
  USHORT  : 8  ReservedByte64;
  USHORT       MinimumMWXferCycleTime;
  USHORT       RecommendedMWXferCycleTime;
  USHORT       MinimumPIOCycleTime;
  USHORT       MinimumPIOCycleTimeIORDY;
  struct {
    USHORT  : 1 CFastSpecSupported;
    USHORT  : 1 DeterministicReadAfterTrimSupported;
    USHORT  : 1 DeviceConfigIdentifySetDmaSupported;
    USHORT  : 1 DeviceEncryptsAllUserData;
    USHORT  : 1 DownloadMicrocodeDmaSupported;
    USHORT  : 1 ExtendedUserAddressableSectorsSupported;
    USHORT  : 1 IEEE1667;
    USHORT  : 1 LPSAERCSupported;
    USHORT  : 1 NonVolatileWriteCache;
    USHORT  : 1 Optional28BitCommandsSupported;
    USHORT  : 1 ReadBufferDmaSupported;
    USHORT  : 1 ReadZeroAfterTrimSupported;
    USHORT  : 1 SetMaxSetPasswordUnlockDmaSupported;
    USHORT  : 1 WriteBufferDmaSupported;
    USHORT  : 2 ZonedCapabilities;
  } AdditionalSupported;
  USHORT       ReservedWords70[5];
  USHORT  : 5  QueueDepth;
  USHORT  : 11 ReservedWord75;
  struct {
    USHORT  : 3 CurrentSpeed;
    USHORT  : 1 DeviceAutoPS;
    USHORT  : 1 DEVSLPtoReducedPwrState;
    USHORT  : 1 HIPM;
    USHORT  : 1 HostAutoPS;
    USHORT  : 1 NCQ;
    USHORT  : 1 NcqPriority;
    USHORT  : 1 NcqQueueMgmt;
    USHORT  : 1 NcqReceiveSend;
    USHORT  : 1 NcqStreaming;
    USHORT  : 1 NcqUnload;
    USHORT  : 1 PhyEvents;
    USHORT  : 1 ReadLogDMA;
    USHORT  : 1 Reserved0;
    USHORT  : 4 Reserved1;
    USHORT  : 1 Reserved2;
    USHORT  : 8 Reserved3;
    USHORT  : 1 SataGen1;
    USHORT  : 1 SataGen2;
    USHORT  : 1 SataGen3;
  } SerialAtaCapabilities;
  struct {
    USHORT  : 1 DEVSLP;
    USHORT  : 1 DIPM;
    USHORT  : 1 DmaSetupAutoActivate;
    USHORT  : 1 HardwareFeatureControl;
    USHORT  : 1 HybridInformation;
    USHORT  : 1 InOrderData;
    USHORT  : 1 NCQAutosense;
    USHORT  : 1 NonZeroOffsets;
    USHORT  : 1 Reserved0;
    USHORT  : 6 Reserved1;
    USHORT  : 1 SoftwareSettingsPreservation;
  } SerialAtaFeaturesSupported;
  struct {
    USHORT  : 1 DeviceAutoPS;
    USHORT  : 1 DEVSLP;
    USHORT  : 1 DIPM;
    USHORT  : 1 DmaSetupAutoActivate;
    USHORT  : 1 HardwareFeatureControl;
    USHORT  : 1 HybridInformation;
    USHORT  : 1 InOrderData;
    USHORT  : 1 NonZeroOffsets;
    USHORT  : 1 Reserved0;
    USHORT  : 6 Reserved1;
    USHORT  : 1 SoftwareSettingsPreservation;
  } SerialAtaFeaturesEnabled;
  USHORT       MajorRevision;
  USHORT       MinorRevision;
  struct {
    USHORT  : 1 Acoustics;
    USHORT  : 1 AdvancedPm;
    USHORT  : 1 BigLba;
    USHORT  : 1 Cfa;
    USHORT  : 1 DeviceConfigOverlay;
    USHORT  : 1 DeviceReset;
    USHORT  : 1 DmaQueued;
    USHORT  : 1 DownloadMicrocode;
    USHORT  : 1 FlushCache;
    USHORT  : 1 FlushCacheExt;
    USHORT  : 1 GpLogging;
    USHORT  : 1 HostProtectedArea;
    USHORT  : 1 IdleWithUnloadFeature;
    USHORT  : 1 LookAhead;
    USHORT  : 1 ManualPowerUp;
    USHORT  : 1 MediaCardPassThrough;
    USHORT  : 1 MediaSerialNumber;
    USHORT  : 1 Msn;
    USHORT  : 1 Nop;
    USHORT  : 1 Obsolete1;
    USHORT  : 1 Obsolete2;
    USHORT  : 1 PowerManagement;
    USHORT  : 1 PowerUpInStandby;
    USHORT  : 1 ReadBuffer;
    USHORT  : 1 ReleaseInterrupt;
    USHORT  : 1 RemovableMediaFeature;
    USHORT  : 1 Reserved1;
    USHORT  : 1 Reserved2;
    USHORT  : 2 ReservedForTechReport;
    USHORT  : 1 SecurityMode;
    USHORT  : 1 ServiceInterrupt;
    USHORT  : 1 SetMax;
    USHORT  : 1 SmartCommands;
    USHORT  : 1 SmartErrorLog;
    USHORT  : 1 SmartSelfTest;
    USHORT  : 1 StreamingFeature;
    USHORT  : 1 URGReadStream;
    USHORT  : 1 URGWriteStream;
    USHORT  : 2 WordValid;
    USHORT  : 2 WordValid83;
    USHORT  : 1 WriteBuffer;
    USHORT  : 1 WriteCache;
    USHORT  : 1 WriteFua;
    USHORT  : 1 WriteQueuedFua;
    USHORT  : 1 WWN64Bit;
  } CommandSetSupport;
  struct {
    USHORT  : 1 Acoustics;
    USHORT  : 1 AdvancedPm;
    USHORT  : 1 BigLba;
    USHORT  : 1 Cfa;
    USHORT  : 1 DeviceConfigOverlay;
    USHORT  : 1 DeviceReset;
    USHORT  : 1 DmaQueued;
    USHORT  : 1 DownloadMicrocode;
    USHORT  : 1 FlushCache;
    USHORT  : 1 FlushCacheExt;
    USHORT  : 1 GpLogging;
    USHORT  : 1 HostProtectedArea;
    USHORT  : 1 IdleWithUnloadFeature;
    USHORT  : 1 LookAhead;
    USHORT  : 1 ManualPowerUp;
    USHORT  : 1 MediaCardPassThrough;
    USHORT  : 1 MediaSerialNumber;
    USHORT  : 1 Msn;
    USHORT  : 1 Nop;
    USHORT  : 1 Obsolete1;
    USHORT  : 1 Obsolete2;
    USHORT  : 1 PowerManagement;
    USHORT  : 1 PowerUpInStandby;
    USHORT  : 1 ReadBuffer;
    USHORT  : 1 ReleaseInterrupt;
    USHORT  : 1 RemovableMediaFeature;
    USHORT  : 1 Reserved1;
    USHORT  : 1 Reserved2;
    USHORT  : 2 Reserved4;
    USHORT  : 2 ReservedForTechReport;
    USHORT  : 1 Resrved3;
    USHORT  : 1 SecurityMode;
    USHORT  : 1 ServiceInterrupt;
    USHORT  : 1 SetMax;
    USHORT  : 1 SmartCommands;
    USHORT  : 1 SmartErrorLog;
    USHORT  : 1 SmartSelfTest;
    USHORT  : 1 StreamingFeature;
    USHORT  : 1 URGReadStream;
    USHORT  : 1 URGWriteStream;
    USHORT  : 1 Words119_120Valid;
    USHORT  : 1 WriteBuffer;
    USHORT  : 1 WriteCache;
    USHORT  : 1 WriteFua;
    USHORT  : 1 WriteQueuedFua;
    USHORT  : 1 WWN64Bit;
  } CommandSetActive;
  USHORT  : 8  UltraDMASupport;
  USHORT  : 8  UltraDMAActive;
  struct {
    USHORT  : 1  ExtendedTimeReported;
    USHORT  : 15 TimeRequired;
  } NormalSecurityEraseUnit;
  struct {
    USHORT  : 1  ExtendedTimeReported;
    USHORT  : 15 TimeRequired;
  } EnhancedSecurityEraseUnit;
  USHORT  : 8  CurrentAPMLevel;
  USHORT  : 8  ReservedWord91;
  USHORT       MasterPasswordID;
  USHORT       HardwareResetResult;
  USHORT  : 8  CurrentAcousticValue;
  USHORT  : 8  RecommendedAcousticValue;
  USHORT       StreamMinRequestSize;
  USHORT       StreamingTransferTimeDMA;
  USHORT       StreamingAccessLatencyDMAPIO;
  ULONG        StreamingPerfGranularity;
  ULONG        Max48BitLBA[2];
  USHORT       StreamingTransferTime;
  USHORT       DsmCap;
  struct {
    USHORT  : 1 LogicalSectorLongerThan256Words;
    USHORT  : 4 LogicalSectorsPerPhysicalSector;
    USHORT  : 1 MultipleLogicalSectorsPerPhysicalSector;
    USHORT  : 8 Reserved0;
    USHORT  : 2 Reserved1;
  } PhysicalLogicalSectorSize;
  USHORT       InterSeekDelay;
  USHORT       WorldWideName[4];
  USHORT       ReservedForWorldWideName128[4];
  USHORT       ReservedForTlcTechnicalReport;
  USHORT       WordsPerLogicalSector[2];
  struct {
    USHORT  : 1 DownloadMicrocodeMode3;
    USHORT  : 1 ExtendedPowerConditions;
    USHORT  : 1 FreefallControl;
    USHORT  : 1 ReadWriteLogDmaExt;
    USHORT  : 6 Reserved0;
    USHORT  : 1 ReservedForDrqTechnicalReport;
    USHORT  : 1 SenseDataReporting;
    USHORT  : 2 WordValid;
    USHORT  : 1 WriteReadVerify;
    USHORT  : 1 WriteUncorrectableExt;
  } CommandSetSupportExt;
  struct {
    USHORT  : 1 DownloadMicrocodeMode3;
    USHORT  : 1 ExtendedPowerConditions;
    USHORT  : 1 FreefallControl;
    USHORT  : 1 ReadWriteLogDmaExt;
    USHORT  : 6 Reserved0;
    USHORT  : 2 Reserved1;
    USHORT  : 1 ReservedForDrqTechnicalReport;
    USHORT  : 1 SenseDataReporting;
    USHORT  : 1 WriteReadVerify;
    USHORT  : 1 WriteUncorrectableExt;
  } CommandSetActiveExt;
  USHORT       ReservedForExpandedSupportandActive[6];
  USHORT  : 2  MsnSupport;
  USHORT  : 14 ReservedWord127;
  struct {
    USHORT  : 1 EnhancedSecurityEraseSupported;
    USHORT  : 2 Reserved0;
    USHORT  : 7 Reserved1;
    USHORT  : 1 SecurityCountExpired;
    USHORT  : 1 SecurityEnabled;
    USHORT  : 1 SecurityFrozen;
    USHORT  : 1 SecurityLevel;
    USHORT  : 1 SecurityLocked;
    USHORT  : 1 SecuritySupported;
  } SecurityStatus;
  USHORT       ReservedWord129[31];
  struct {
    USHORT  : 1  CfaPowerMode1Disabled;
    USHORT  : 1  CfaPowerMode1Required;
    USHORT  : 12 MaximumCurrentInMA;
    USHORT  : 1  Reserved0;
    USHORT  : 1  Word160Supported;
  } CfaPowerMode1;
  USHORT       ReservedForCfaWord161[7];
  USHORT  : 4  NominalFormFactor;
  USHORT  : 12 ReservedWord168;
  struct {
    USHORT  : 15 Reserved0;
    USHORT  : 1  SupportsTrim;
  } DataSetManagementFeature;
  USHORT       AdditionalProductID[4];
  USHORT       ReservedForCfaWord174[2];
  USHORT       CurrentMediaSerialNumber[30];
  struct {
    USHORT  : 1 DataTablesSuported;
    USHORT  : 1 ErrorRecoveryControlSupported;
    USHORT  : 1 FeatureControlSuported;
    USHORT  : 1 Reserved0;
    USHORT  : 6 Reserved1;
    USHORT  : 1 Supported;
    USHORT  : 4 VendorSpecific;
    USHORT  : 1 WriteSameSuported;
  } SCTCommandTransport;
  USHORT       ReservedWord207[2];
  struct {
    USHORT  : 14 AlignmentOfLogicalWithinPhysical;
    USHORT  : 1  Reserved0;
    USHORT  : 1  Word209Supported;
  } BlockAlignment;
  USHORT       WriteReadVerifySectorCountMode3Only[2];
  USHORT       WriteReadVerifySectorCountMode2Only[2];
  struct {
    USHORT  : 1 NVCacheFeatureSetEnabled;
    USHORT  : 4 NVCacheFeatureSetVersion;
    USHORT  : 1 NVCachePowerModeEnabled;
    USHORT  : 4 NVCachePowerModeVersion;
    USHORT  : 3 Reserved0;
    USHORT  : 3 Reserved1;
  } NVCacheCapabilities;
  USHORT       NVCacheSizeLSW;
  USHORT       NVCacheSizeMSW;
  USHORT       NominalMediaRotationRate;
  USHORT       ReservedWord218;
  struct {
    UCHAR NVCacheEstimatedTimeToSpinUpInSeconds;
    UCHAR Reserved;
  } NVCacheOptions;
  USHORT  : 8  WriteReadVerifySectorCountMode;
  USHORT  : 8  ReservedWord220;
  USHORT       ReservedWord221;
  struct {
    USHORT  : 12 MajorVersion;
    USHORT  : 4  TransportType;
  } TransportMajorVersion;
  USHORT       TransportMinorVersion;
  USHORT       ReservedWord224[6];
  ULONG        ExtendedNumberOfUserAddressableSectors[2];
  USHORT       MinBlocksPerDownloadMicrocodeMode03;
  USHORT       MaxBlocksPerDownloadMicrocodeMode03;
  USHORT       ReservedWord236[19];
  USHORT  : 8  Signature;
  USHORT  : 8  CheckSum;
} IDENTIFY_DEVICE_DATA, *PIDENTIFY_DEVICE_DATA;
```

## Members


`GeneralConfiguration`

#### Reserved1

Reserved.



#### Retired3

This member is no longer used.



#### ResponseIncomplete

Indicates that the response was incomplete.



#### Retired2

This member is no longer used.



#### FixedDevice

Indicates when set to 1 that the device is fixed.



#### RemovableMedia

Indicates when set to 1 that the media is removable.



#### Retired1

This member is no longer used.



#### DeviceType

Indicates when set to 1 that the device is an ATA device.

`NumCylinders`

Indicates the number of cylinders on the device.

`SpecificConfiguration`



`NumHeads`

Number of logical heads on the device.

`Retired1`

This member is no longer used.

`NumSectorsPerTrack`

Indicates the number of sectors per track.

`VendorUnique1`

Contains the first ID of the device's vendor.

`SerialNumber`

Contains the serial number of the device.

`Retired2`

This member is no longer used.

`Obsolete1`

This member is obsolete. Do not use.

`FirmwareRevision`

Contains the revision number of the device's firmware.

`ModelNumber`

Contains the device's model number.

`MaximumBlockTransfer`

Contains the maximum number of blocks allowed in a single transfer.

`VendorUnique2`

Contains the second ID of the device's vendor.

`TrustedComputing`



`Capabilities`

#### ReservedByte49

Reserved.



#### DmaSupported

Indicates that the device supports DMA operations.



#### LbaSupported

Indicates that the device supports logical block addressing.



#### IordyDisable

Indicates when set to 1 that I/O channel ready is disabled for the device.



#### IordySupported

Indicates when set to 1 that I/O channel ready is supported by the device.



#### Reserved1

Reserved.



#### StandybyTimerSupport

Indicates when set to 1 that the device supports standby timers.



#### Reserved2

Reserved.



#### ReservedWord50

Reserved.

`ObsoleteWords51`

This member is obsolete. Do not use.

`TranslationFieldsValid`

Contains a bitfield whose bits indicate which of the bytes in the identify data package contain valid address translation information. For more information about how this bitfield is defined, see the <i>ATA/ATAPI specification</i>.

`Reserved3`

Reserved.

`FreeFallControlSensitivity`



`NumberOfCurrentCylinders`

Indicates the number of cylinders on the device.

`NumberOfCurrentHeads`

Indicates the number of heads on the device.

`CurrentSectorsPerTrack`

Indicates the number of sectors per track.

`CurrentSectorCapacity`

Indicates the number of sectors on the device.

`CurrentMultiSectorSetting`

Indicates the multisector setting.

`MultiSectorSettingValid`

Indicates when <b>TRUE</b> that the multisector setting is valid.

`ReservedByte59`

Reserved.

`SanitizeFeatureSupported`



`CryptoScrambleExtCommandSupported`



`OverwriteExtCommandSupported`



`BlockEraseExtCommandSupported`



`UserAddressableSectors`

Indicates the total number of user-addressable sectors.

`ObsoleteWord62`

This member is obsolete. Do not use.

`MultiWordDMASupport`

Indicates which DMA modes the device supports.

`MultiWordDMAActive`

Indicates which DMA modes are currently selected.

`AdvancedPIOModes`



`ReservedByte64`

Reserved.

`MinimumMWXferCycleTime`

Indicates the minimum multiword DMA transfer cycle time per word.

`RecommendedMWXferCycleTime`

Indicates the recommended multiword DMA transfer cycle time per word.

`MinimumPIOCycleTime`

Indicates the minimum PIO transfer cycle time without flow control.

`MinimumPIOCycleTimeIORDY`

Indicates the minimum PIO transfer cycle time with IORDY flow control.

`AdditionalSupported`



`ReservedWords70`



`QueueDepth`

Indicates the maximum queue depth.

`ReservedWord75`

Reserved.

`SerialAtaCapabilities`



`SerialAtaFeaturesSupported`



`SerialAtaFeaturesEnabled`



`MajorRevision`

Indicates the device's major revision number.

`MinorRevision`

Indicates the device's minor revision number.

`CommandSetSupport`

#### SmartCommands

Indicates when <b>TRUE</b> that the device supports the SMART feature set.



#### SecurityMode

Indicates when <b>TRUE</b> that the device supports the security mode feature set.



#### PowerManagement

Indicates when <b>TRUE</b> that the device supports the mandatory power management feature set.



#### Reserved1

Reserved.



#### WriteCache

Indicates when <b>TRUE</b> that the device supports a write cache.



#### LookAhead

Indicates when <b>TRUE</b> that the device supports lookahead.



#### ReleaseInterrupt

Indicates when <b>TRUE</b> that the device supports release interrupt.



#### ServiceInterrupt

Indicates when <b>TRUE</b> that the device supports service interrupt.



#### DeviceReset

Indicates when <b>TRUE</b> that the device supports the device reset command.



#### HostProtectedArea

Indicates when <b>TRUE</b> that the device supports the host protected area feature set.



#### Obsolete1

This member is obsolete. Do not use.



#### WriteBuffer

Indicates when <b>TRUE</b> that the device supports the write buffer command.



#### ReadBuffer

Indicates when <b>TRUE</b> that the device supports the read buffer command.



#### Nop

Indicates when <b>TRUE</b> that the device supports the NOP command.



#### Obsolete2

Obsolete. Do not use.



#### DownloadMicrocode

Indicates when <b>TRUE</b> that the device supports the DOWNLOAD MICROCODE command.



#### DmaQueued

Indicates when <b>TRUE</b> that the device supports READ/WRITE DMA QUEUED command.



#### Cfa

Indicates when <b>TRUE</b> that the device supports the CFA feature set.



#### AdvancedPm

Indicates when <b>TRUE</b> that the device supports the advanced power management feature set.



#### Msn

Indicates when <b>TRUE</b> that the device supports the media status notification feature set.



#### PowerUpInStandby

Indicates when <b>TRUE</b> that the device supports power-up in standby feature set.



#### ManualPowerUp

Indicates when <b>TRUE</b> that the device supports the SET FEATURES subcommand required to spin up the device after power-up.



#### Reserved2

Reserved.



#### SetMax

Indicates when <b>TRUE</b> that the device supports the SET MAX security extension command.



#### Acoustics

Indicates when <b>TRUE</b> that the device supports the automatic acoustic management feature set.



#### BigLba

Indicates when <b>TRUE</b> that the device supports the 48-bit address feature set.



#### Resrved3

Reserved.

`CommandSetActive`

#### 



#### SmartCommands

Indicates when <b>TRUE</b> that the device supports the SMART feature set.



#### SecurityMode

Indicates when <b>TRUE</b> that the device supports the security mode feature set.



#### PowerManagement

Indicates when <b>TRUE</b> that the device supports the mandatory power management feature set.



#### Reserved1

Reserved.



#### WriteCache

Indicates when <b>TRUE</b> that the device supports a write cache.



#### LookAhead

Indicates when <b>TRUE</b> that the device supports lookahead.



#### ReleaseInterrupt

Indicates when <b>TRUE</b> that the device supports release interrupt.



#### ServiceInterrupt

Indicates when <b>TRUE</b> that the device supports service interrupt.



#### DeviceReset

Indicates when <b>TRUE</b> that the device supports the device reset command.



#### HostProtectedArea

Indicates when <b>TRUE</b> that the device supports the host protected area feature set.



#### Obsolete1

This member is obsolete. Do not use.



#### WriteBuffer

Indicates when <b>TRUE</b> that the device supports the write buffer command.



#### ReadBuffer

Indicates when <b>TRUE</b> that the device supports the read buffer command.



#### Nop

Indicates when <b>TRUE</b> that the device supports the NOP command.



#### Obsolete2

Obsolete. Do not use.



#### DownloadMicrocode

Indicates when <b>TRUE</b> that the device supports the DOWNLOAD MICROCODE command.



#### DmaQueued

Indicates when <b>TRUE</b> that the device supports READ/WRITE DMA QUEUED command.



#### Cfa

Indicates when <b>TRUE</b> that the device supports the CFA feature set.



#### AdvancedPm

Indicates when <b>TRUE</b> that the device supports the advanced power management feature set.



#### Msn

Indicates when <b>TRUE</b> that the device supports the media status notification feature set.



#### PowerUpInStandby

Indicates when <b>TRUE</b> that the device supports power-up in standby feature set.



#### ManualPowerUp

Indicates when <b>TRUE</b> that the device supports the SET FEATURES subcommand required to spin up the device after power-up.



#### Reserved2

Reserved.



#### SetMax

Indicates when <b>TRUE</b> that the device supports the SET MAX security extension command.



#### Acoustics

Indicates when <b>TRUE</b> that the device supports the automatic acoustic management feature set.



#### BigLba

Indicates when <b>TRUE</b> that the device supports the 48-bit address feature set.



#### Resrved3

Reserved.

`UltraDMASupport`

Contains a bitmap indicating which ultraDMA modes the device supports.

`UltraDMAActive`

Contains a bitmap indicating which ultraDMA modes are selected.

`NormalSecurityEraseUnit`



`EnhancedSecurityEraseUnit`



`CurrentAPMLevel`



`ReservedWord91`



`MasterPasswordID`



`HardwareResetResult`

Indicates the result of a hardware reset. For more information about the values assigned to this member, see the <i>ATA/ATAP specification</i>.

`CurrentAcousticValue`

Indicates the current acoustic management value.

`RecommendedAcousticValue`

Contain the device vendor's recommended acoustic management value.

`StreamMinRequestSize`



`StreamingTransferTimeDMA`



`StreamingAccessLatencyDMAPIO`



`StreamingPerfGranularity`



`Max48BitLBA`

Contains the maximum user LBA for the 48-bit address feature set.

`StreamingTransferTime`



`DsmCap`



`PhysicalLogicalSectorSize`

#### Reserved1

Reserved.

`InterSeekDelay`



`WorldWideName`



`ReservedForWorldWideName128`



`ReservedForTlcTechnicalReport`



`WordsPerLogicalSector`



`CommandSetSupportExt`

#### Reserved1

Reserved.

`CommandSetActiveExt`

#### Reserved1

Reserved.

`ReservedForExpandedSupportandActive`



`MsnSupport`

Indicates when <b>TRUE</b> that the device supports media status notification.

`ReservedWord127`



`SecurityStatus`

Contains a bitmap that indicates the security status. For more information about the meaning of each individual bit, see the <i>ATA/ATAPI specification</i>.



#### Reserved1

Reserved.

`ReservedWord129`

Reserved.

`CfaPowerMode1`



`ReservedForCfaWord161`

Words 161-168

`NominalFormFactor`



`ReservedWord168`



`DataSetManagementFeature`



`AdditionalProductID`



`ReservedForCfaWord174`



`CurrentMediaSerialNumber`

Words 176-205

`SCTCommandTransport`



`ReservedWord207`

Words 207-208

`BlockAlignment`



`WriteReadVerifySectorCountMode3Only`

Words 210-211

`WriteReadVerifySectorCountMode2Only`

Words 212-213

`NVCacheCapabilities`

#### Reserved1

Reserved.

`NVCacheSizeLSW`



`NVCacheSizeMSW`



`NominalMediaRotationRate`



`ReservedWord218`



`NVCacheOptions`



`WriteReadVerifySectorCountMode`



`ReservedWord220`

Words 220-254

`ReservedWord221`



`TransportMajorVersion`



`TransportMinorVersion`



`ReservedWord224`



`ExtendedNumberOfUserAddressableSectors`



`MinBlocksPerDownloadMicrocodeMode03`



`MaxBlocksPerDownloadMicrocodeMode03`



`ReservedWord236`



`Signature`

Indicates the disk signature.

`CheckSum`

Indicates the checksum.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ata.h (include Irb.h) |