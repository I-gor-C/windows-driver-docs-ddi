---
UID: NS:ata._IDENTIFY_DEVICE_DATA
title: "_IDENTIFY_DEVICE_DATA"
author: windows-driver-content
description: The IDENTIFY_DEVICE_DATA structure contains the data retrieved by an ATA identify device data command (0xEC).Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\identify_device_data.htm
old-project: storage
ms.assetid: 7f2edd6f-16bf-47a6-8546-7871435a56ac
ms.author: windowsdriverdev
ms.date: 1/10/2018
ms.keywords: PIDENTIFY_DEVICE_DATA, structs-ATA_904f6e71-4dd9-4ecb-9928-0d7ce44b83ef.xml, IDENTIFY_DEVICE_DATA, PIDENTIFY_DEVICE_DATA structure pointer [Storage Devices], *PIDENTIFY_DEVICE_DATA, IDENTIFY_DEVICE_DATA structure [Storage Devices], _IDENTIFY_DEVICE_DATA, ata/PIDENTIFY_DEVICE_DATA, ata/IDENTIFY_DEVICE_DATA, storage.identify_device_data
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	ata.h
apiname:
-	IDENTIFY_DEVICE_DATA
product: Windows
targetos: Windows
req.typenames: "*PIDENTIFY_DEVICE_DATA, IDENTIFY_DEVICE_DATA"
---

# _IDENTIFY_DEVICE_DATA structure
The IDENTIFY_DEVICE_DATA structure contains the data retrieved by an ATA identify device data command (0xEC).
<div class="alert"><b>Note</b>  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/storage/storport-driver">Storport driver</a> and <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/storage/storport-miniport-drivers">Storport miniport</a> driver models.</div><div> </div>

## Syntax
````
typedef struct _IDENTIFY_DEVICE_DATA {
  struct {
    USHORT Reserved1  :1;
    USHORT Retired3  :1;
    USHORT ResponseIncomplete  :1;
    USHORT Retired2  :3;
    USHORT FixedDevice  :1;
    USHORT RemovableMedia  :1;
    USHORT Retired1  :7;
    USHORT DeviceType  :1;
  } GeneralConfiguration;
  USHORT NumCylinders;
  USHORT ReservedWord2;
  USHORT NumHeads;
  USHORT Retired1[2];
  USHORT NumSectorsPerTrack;
  USHORT VendorUnique1[3];
  UCHAR  SerialNumber[20];
  USHORT Retired2[2];
  USHORT Obsolete1;
  UCHAR  FirmwareRevision[8];
  UCHAR  ModelNumber[40];
  UCHAR  MaximumBlockTransfer;
  UCHAR  VendorUnique2;
  USHORT ReservedWord48;
  struct {
    UCHAR  ReservedByte49;
    UCHAR  DmaSupported  :1;
    UCHAR  LbaSupported  :1;
    UCHAR  IordyDisable  :1;
    UCHAR  IordySupported  :1;
    UCHAR  Reserved1  :1;
    UCHAR  StandybyTimerSupport  :1;
    UCHAR  Reserved2  :2;
    USHORT ReservedWord50;
  } Capabilities;
  USHORT ObsoleteWords51[2];
  USHORT TranslationFieldsValid  :3;
  USHORT Reserved3  :13;
  USHORT NumberOfCurrentCylinders;
  USHORT NumberOfCurrentHeads;
  USHORT CurrentSectorsPerTrack;
  ULONG  CurrentSectorCapacity;
  UCHAR  CurrentMultiSectorSetting;
  UCHAR  MultiSectorSettingValid  :1;
  UCHAR  ReservedByte59  :7;
  ULONG  UserAddressableSectors;
  USHORT ObsoleteWord62;
  USHORT MultiWordDMASupport  :8;
  USHORT MultiWordDMAActive  :8;
  USHORT AdvancedPIOModes  :8;
  USHORT ReservedByte64  :8;
  USHORT MinimumMWXferCycleTime;
  USHORT RecommendedMWXferCycleTime;
  USHORT MinimumPIOCycleTime;
  USHORT MinimumPIOCycleTimeIORDY;
  USHORT ReservedWords69[6];
  USHORT QueueDepth  :5;
  USHORT ReservedWord75  :11;
  USHORT ReservedWords76[4];
  USHORT MajorRevision;
  USHORT MinorRevision;
  struct {
    USHORT SmartCommands  :1;
    USHORT SecurityMode  :1;
    USHORT RemovableMediaFeature  :1;
    USHORT PowerManagement  :1;
    USHORT Reserved1  :1;
    USHORT WriteCache  :1;
    USHORT LookAhead  :1;
    USHORT ReleaseInterrupt  :1;
    USHORT ServiceInterrupt  :1;
    USHORT DeviceReset  :1;
    USHORT HostProtectedArea  :1;
    USHORT Obsolete1  :1;
    USHORT WriteBuffer  :1;
    USHORT ReadBuffer  :1;
    USHORT Nop  :1;
    USHORT Obsolete2  :1;
    USHORT DownloadMicrocode  :1;
    USHORT DmaQueued  :1;
    USHORT Cfa  :1;
    USHORT AdvancedPm  :1;
    USHORT Msn  :1;
    USHORT PowerUpInStandby  :1;
    USHORT ManualPowerUp  :1;
    USHORT Reserved2  :1;
    USHORT SetMax  :1;
    USHORT Acoustics  :1;
    USHORT BigLba  :1;
    USHORT DeviceConfigOverlay  :1;
    USHORT FlushCache  :1;
    USHORT FlushCacheExt  :1;
    USHORT Resrved3  :2;
    USHORT SmartErrorLog  :1;
    USHORT SmartSelfTest  :1;
    USHORT MediaSerialNumber  :1;
    USHORT MediaCardPassThrough  :1;
    USHORT StreamingFeature  :1;
    USHORT GpLogging  :1;
    USHORT WriteFua  :1;
    USHORT WriteQueuedFua  :1;
    USHORT WWN64Bit  :1;
    USHORT URGReadStream  :1;
    USHORT URGWriteStream  :1;
    USHORT ReservedForTechReport  :2;
    USHORT IdleWithUnloadFeature  :1;
    USHORT Reserved4  :2;
  } CommandSetSupport;
  struct {
    USHORT SmartCommands  :1;
    USHORT SecurityMode  :1;
    USHORT RemovableMediaFeature  :1;
    USHORT PowerManagement  :1;
    USHORT Reserved1  :1;
    USHORT WriteCache  :1;
    USHORT LookAhead  :1;
    USHORT ReleaseInterrupt  :1;
    USHORT ServiceInterrupt  :1;
    USHORT DeviceReset  :1;
    USHORT HostProtectedArea  :1;
    USHORT Obsolete1  :1;
    USHORT WriteBuffer  :1;
    USHORT ReadBuffer  :1;
    USHORT Nop  :1;
    USHORT Obsolete2  :1;
    USHORT DownloadMicrocode  :1;
    USHORT DmaQueued  :1;
    USHORT Cfa  :1;
    USHORT AdvancedPm  :1;
    USHORT Msn  :1;
    USHORT PowerUpInStandby  :1;
    USHORT ManualPowerUp  :1;
    USHORT Reserved2  :1;
    USHORT SetMax  :1;
    USHORT Acoustics  :1;
    USHORT BigLba  :1;
    USHORT DeviceConfigOverlay  :1;
    USHORT FlushCache  :1;
    USHORT FlushCacheExt  :1;
    USHORT Resrved3  :2;
    USHORT SmartErrorLog  :1;
    USHORT SmartSelfTest  :1;
    USHORT MediaSerialNumber  :1;
    USHORT MediaCardPassThrough  :1;
    USHORT StreamingFeature  :1;
    USHORT GpLogging  :1;
    USHORT WriteFua  :1;
    USHORT WriteQueuedFua  :1;
    USHORT WWN64Bit  :1;
    USHORT URGReadStream  :1;
    USHORT URGWriteStream  :1;
    USHORT ReservedForTechReport  :2;
    USHORT IdleWithUnloadFeature  :1;
    USHORT Reserved4  :2;
  } CommandSetActive;
  USHORT UltraDMASupport  :8;
  USHORT UltraDMAActive  :8;
  USHORT ReservedWord89[4];
  USHORT HardwareResetResult;
  USHORT CurrentAcousticValue  :8;
  USHORT RecommendedAcousticValue  :8;
  USHORT ReservedWord95[5];
  ULONG  Max48BitLBA[2];
  USHORT StreamingTransferTime;
  USHORT ReservedWord105;
  struct {
    USHORT LogicalSectorsPerPhysicalSector  :4;
    USHORT Reserved0  :8;
    USHORT LogicalSectorLongerThan256Words  :1;
    USHORT MultipleLogicalSectorsPerPhysicalSector  :1;
    USHORT Reserved1  :2;
  } PhysicalLogicalSectorSize;
  USHORT InterSeekDelay;
  USHORT WorldWideName[4];
  USHORT ReservedForWorldWideName128[4];
  USHORT ReservedForTlcTechnicalReport;
  USHORT WordsPerLogicalSector[2];
  struct {
    USHORT ReservedForDrqTechnicalReport  :1;
    USHORT WriteReadVerifySupported  :1;
    USHORT Reserved01  :11;
    USHORT Reserved1  :2;
  } CommandSetSupportExt;
  struct {
    USHORT ReservedForDrqTechnicalReport  :1;
    USHORT WriteReadVerifyEnabled  :1;
    USHORT Reserved01  :11;
    USHORT Reserved1  :2;
  } CommandSetActiveExt;
  USHORT ReservedForExpandedSupportandActive[6];
  USHORT MsnSupport  :2;
  USHORT ReservedWord1274  :14;
  struct {
    USHORT SecuritySupported  :1;
    USHORT SecurityEnabled  :1;
    USHORT SecurityLocked  :1;
    USHORT SecurityFrozen  :1;
    USHORT SecurityCountExpired  :1;
    USHORT EnhancedSecurityEraseSupported  :1;
    USHORT Reserved0  :2;
    USHORT SecurityLevel  :1;
    USHORT Reserved1  :7;
  } SecurityStatus;
  USHORT ReservedWord129[31];
  struct {
    USHORT MaximumCurrentInMA2  :12;
    USHORT CfaPowerMode1Disabled  :1;
    USHORT CfaPowerMode1Required  :1;
    USHORT Reserved0  :1;
    USHORT Word160Supported  :1;
  } CfaPowerModel;
  USHORT ReservedForCfaWord161[8];
  struct {
    USHORT SupportsTrim  :1;
    USHORT Reserved0  :15;
  } DataSetManagementFeature;
  USHORT ReservedForCfaWord170[6];
  USHORT CurrentMediaSerialNumber[30];
  USHORT ReservedWord206;
  USHORT ReservedWord207[2];
  struct {
    USHORT AlignmentOfLogicalWithinPhysical  :14;
    USHORT Word209Supported  :1;
    USHORT Reserved0  :1;
  } BlockAlignment;
  USHORT WriteReadVerifySectorCountMode3Only[2];
  USHORT WriteReadVerifySectorCountMode2Only[2];
  struct {
    USHORT NVCachePowerModeEnabled  :1;
    USHORT Reserved0  :3;
    USHORT NVCacheFeatureSetEnabled  :1;
    USHORT Reserved1  :3;
    USHORT NVCachePowerModeVersion  :4;
    USHORT NVCacheFeatureSetVersion  :4;
  } NVCacheCapabilities;
  USHORT NVCacheSizeLSW;
  USHORT NVCacheSizeMSW;
  USHORT NominalMediaRotationRate;
  USHORT ReservedWord218;
  struct {
    UCHAR NVCacheEstimatedTimeToSpinUpInSeconds;
    UCHAR Reserved;
  } NVCacheOptions;
  USHORT ReservedWord220[35];
  USHORT Signature  :8;
  USHORT CheckSum  :8;
} IDENTIFY_DEVICE_DATA, *PIDENTIFY_DEVICE_DATA;
````

## Members


`AdditionalProductID`



`AdditionalSupported`



`AdvancedPIOModes`



`BlockAlignment`



`BlockEraseExtCommandSupported`



`Capabilities`



`CfaPowerMode1`



`CheckSum`

Indicates the checksum.

`CommandSetActive`

####

`CommandSetActiveExt`



`CommandSetSupport`

#### Resrved3

Reserved.

`CommandSetSupportExt`

#### Reserved1

Reserved.

`CryptoScrambleExtCommandSupported`



`CurrentAcousticValue`

Indicates the current acoustic management value.

`CurrentAPMLevel`



`CurrentMediaSerialNumber`

Words 176-205

`CurrentMultiSectorSetting`

Indicates the multisector setting.

`CurrentSectorCapacity`

Indicates the number of sectors on the device.

`CurrentSectorsPerTrack`

Indicates the number of sectors per track.

`DataSetManagementFeature`



`DsmCap`



`EnhancedSecurityEraseUnit`



`ExtendedNumberOfUserAddressableSectors`



`FirmwareRevision`

Contains the revision number of the device's firmware.

`FreeFallControlSensitivity`



`GeneralConfiguration`



`HardwareResetResult`

Indicates the result of a hardware reset. For more information about the values assigned to this member, see the <i>ATA/ATAP specification</i>.

`InterSeekDelay`



`MajorRevision`

Indicates the device's major revision number.

`MasterPasswordID`



`Max48BitLBA`

Contains the maximum user LBA for the 48-bit address feature set.

`MaxBlocksPerDownloadMicrocodeMode03`



`MaximumBlockTransfer`

Contains the maximum number of blocks allowed in a single transfer.

`MinBlocksPerDownloadMicrocodeMode03`



`MinimumMWXferCycleTime`

Indicates the minimum multiword DMA transfer cycle time per word.

`MinimumPIOCycleTime`

Indicates the minimum PIO transfer cycle time without flow control.

`MinimumPIOCycleTimeIORDY`

Indicates the minimum PIO transfer cycle time with IORDY flow control.

`MinorRevision`

Indicates the device's minor revision number.

`ModelNumber`

Contains the device's model number.

`MsnSupport`

Indicates when <b>TRUE</b> that the device supports media status notification.

`MultiSectorSettingValid`

Indicates when <b>TRUE</b> that the multisector setting is valid.

`MultiWordDMAActive`

Indicates which DMA modes are currently selected.

`MultiWordDMASupport`

Indicates which DMA modes the device supports.

`NominalFormFactor`



`NominalMediaRotationRate`



`NormalSecurityEraseUnit`



`NumberOfCurrentCylinders`

Indicates the number of cylinders on the device.

`NumberOfCurrentHeads`

Indicates the number of heads on the device.

`NumCylinders`

Indicates the number of cylinders on the device.

`NumHeads`

Number of logical heads on the device.

`NumSectorsPerTrack`

Indicates the number of sectors per track.

`NVCacheCapabilities`



`NVCacheOptions`



`NVCacheSizeLSW`



`NVCacheSizeMSW`



`Obsolete1`

This member is obsolete. Do not use.

`ObsoleteWord62`

This member is obsolete. Do not use.

`ObsoleteWords51`

This member is obsolete. Do not use.

`OverwriteExtCommandSupported`



`PhysicalLogicalSectorSize`



`QueueDepth`

Indicates the maximum queue depth.

`RecommendedAcousticValue`

Contain the device vendor's recommended acoustic management value.

`RecommendedMWXferCycleTime`

Indicates the recommended multiword DMA transfer cycle time per word.

`Reserved3`

Reserved.

`ReservedByte59`

Reserved.

`ReservedByte64`

Reserved.

`ReservedForCfaWord161`

Words 161-168

`ReservedForCfaWord174`



`ReservedForExpandedSupportandActive`



`ReservedForTlcTechnicalReport`



`ReservedForWorldWideName128`



`ReservedWord127`



`ReservedWord129`

Reserved.

`ReservedWord168`



`ReservedWord207`

Words 207-208

`ReservedWord218`



`ReservedWord220`

Words 220-254

`ReservedWord221`



`ReservedWord224`



`ReservedWord236`



`ReservedWord75`

Reserved.

`ReservedWord91`



`ReservedWords70`



`Retired1`

This member is no longer used.

`Retired2`

This member is no longer used.

`SanitizeFeatureSupported`



`SCTCommandTransport`



`SecurityStatus`

Contains a bitmap that indicates the security status. For more information about the meaning of each individual bit, see the <i>ATA/ATAPI specification</i>.

`SerialAtaCapabilities`



`SerialAtaFeaturesEnabled`



`SerialAtaFeaturesSupported`



`SerialNumber`

Contains the serial number of the device.

`Signature`

Indicates the disk signature.

`SpecificConfiguration`



`StreamingAccessLatencyDMAPIO`



`StreamingPerfGranularity`



`StreamingTransferTime`



`StreamingTransferTimeDMA`



`StreamMinRequestSize`



`TranslationFieldsValid`

Contains a bitfield whose bits indicate which of the bytes in the identify data package contain valid address translation information. For more information about how this bitfield is defined, see the <i>ATA/ATAPI specification</i>.

`TransportMajorVersion`



`TransportMinorVersion`



`TrustedComputing`



`UltraDMAActive`

Contains a bitmap indicating which ultraDMA modes are selected.

`UltraDMASupport`

Contains a bitmap indicating which ultraDMA modes the device supports.

`UserAddressableSectors`

Indicates the total number of user-addressable sectors.

`VendorUnique1`

Contains the first ID of the device's vendor.

`VendorUnique2`

Contains the second ID of the device's vendor.

`WordsPerLogicalSector`



`WorldWideName`



`WriteReadVerifySectorCountMode`



`WriteReadVerifySectorCountMode2Only`

Words 212-213

`WriteReadVerifySectorCountMode3Only`

Words 210-211


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ata.h (include Irb.h) |