---
UID: NS.ata._IDENTIFY_DEVICE_DATA
title: IDENTIFY_DEVICE_DATA
author: windows-driver-content
description: The IDENTIFY_DEVICE_DATA structure contains the data retrieved by an ATA identify device data command (0xEC).Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\identify_device_data.htm
ms.assetid: 7f2edd6f-16bf-47a6-8546-7871435a56ac
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ata.h
req.include-header: Irb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDENTIFY_DEVICE_DATA
req.alt-loc: ata.h
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
ms.keywords: IDENTIFY_DEVICE_DATA, IDENTIFY_DEVICE_DATA, *PIDENTIFY_DEVICE_DATA
---

# IDENTIFY_DEVICE_DATA structure



## -description
<p>The IDENTIFY_DEVICE_DATA structure contains the data retrieved by an ATA identify device data command (0xEC).</p>


## -syntax

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


## -struct-fields
<dl>

### -field <b>GeneralConfiguration</b>

<dd>
<dl>

### -field <b>Reserved1</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Retired3</b>

<dd>
<p>This member is no longer used.</p>
</dd>

### -field <b>ResponseIncomplete</b>

<dd>
<p>Indicates that the response was incomplete.</p>
</dd>

### -field <b>Retired2</b>

<dd>
<p>This member is no longer used.</p>
</dd>

### -field <b>FixedDevice</b>

<dd>
<p>Indicates when set to 1 that the device is fixed.</p>
</dd>

### -field <b>RemovableMedia</b>

<dd>
<p>Indicates when set to 1 that the media is removable.</p>
</dd>

### -field <b>Retired1</b>

<dd>
<p>This member is no longer used.</p>
</dd>

### -field <b>DeviceType</b>

<dd>
<p>Indicates when set to 1 that the device is an ATA device.</p>
</dd>
</dl>
</dd>

### -field <b>NumCylinders</b>

<dd>
<p>Indicates the number of cylinders on the device.</p>
</dd>

### -field <b>ReservedWord2</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>NumHeads</b>

<dd>
<p>Number of logical heads on the device.</p>
</dd>

### -field <b>Retired1</b>

<dd>
<p>This member is no longer used.</p>
</dd>

### -field <b>NumSectorsPerTrack</b>

<dd>
<p>Indicates the number of sectors per track.</p>
</dd>

### -field <b>VendorUnique1</b>

<dd>
<p>Contains the first ID of the device's vendor.</p>
</dd>

### -field <b>SerialNumber</b>

<dd>
<p>Contains the serial number of the device.</p>
</dd>

### -field <b>Retired2</b>

<dd>
<p>This member is no longer used.</p>
</dd>

### -field <b>Obsolete1</b>

<dd>
<p>This member is obsolete. Do not use.</p>
</dd>

### -field <b>FirmwareRevision</b>

<dd>
<p>Contains the revision number of the device's firmware.</p>
</dd>

### -field <b>ModelNumber</b>

<dd>
<p>Contains the device's model number.</p>
</dd>

### -field <b>MaximumBlockTransfer</b>

<dd>
<p>Contains the maximum number of blocks allowed in a single transfer.</p>
</dd>

### -field <b>VendorUnique2</b>

<dd>
<p>Contains the second ID of the device's vendor.</p>
</dd>

### -field <b>ReservedWord48</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Capabilities</b>

<dd>
<dl>

### -field <b>ReservedByte49</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>DmaSupported</b>

<dd>
<p>Indicates that the device supports DMA operations.</p>
</dd>

### -field <b>LbaSupported</b>

<dd>
<p>Indicates that the device supports logical block addressing.</p>
</dd>

### -field <b>IordyDisable</b>

<dd>
<p>Indicates when set to 1 that I/O channel ready is disabled for the device.</p>
</dd>

### -field <b>IordySupported</b>

<dd>
<p>Indicates when set to 1 that I/O channel ready is supported by the device.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>StandybyTimerSupport</b>

<dd>
<p>Indicates when set to 1 that the device supports standby timers.</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>ReservedWord50</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>

### -field <b>ObsoleteWords51</b>

<dd>
<p>This member is obsolete. Do not use.</p>
</dd>

### -field <b>TranslationFieldsValid</b>

<dd>
<p>Contains a bitfield whose bits indicate which of the bytes in the identify data package contain valid address translation information. For more information about how this bitfield is defined, see the <i>ATA/ATAPI specification</i>.</p>
</dd>

### -field <b>Reserved3</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>NumberOfCurrentCylinders</b>

<dd>
<p>Indicates the number of cylinders on the device.</p>
</dd>

### -field <b>NumberOfCurrentHeads</b>

<dd>
<p>Indicates the number of heads on the device.</p>
</dd>

### -field <b>CurrentSectorsPerTrack</b>

<dd>
<p>Indicates the number of sectors per track.</p>
</dd>

### -field <b>CurrentSectorCapacity</b>

<dd>
<p>Indicates the number of sectors on the device.</p>
</dd>

### -field <b>CurrentMultiSectorSetting</b>

<dd>
<p>Indicates the multisector setting.</p>
</dd>

### -field <b>MultiSectorSettingValid</b>

<dd>
<p>Indicates when <b>TRUE</b> that the multisector setting is valid.</p>
</dd>

### -field <b>ReservedByte59</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>UserAddressableSectors</b>

<dd>
<p>Indicates the total number of user-addressable sectors.</p>
</dd>

### -field <b>ObsoleteWord62</b>

<dd>
<p>This member is obsolete. Do not use.</p>
</dd>

### -field <b>MultiWordDMASupport</b>

<dd>
<p>Indicates which DMA modes the device supports.</p>
</dd>

### -field <b>MultiWordDMAActive</b>

<dd>
<p>Indicates which DMA modes are currently selected.</p>
</dd>

### -field <b>AdvancedPIOModes</b>

<dd></dd>

### -field <b>ReservedByte64</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>MinimumMWXferCycleTime</b>

<dd>
<p>Indicates the minimum multiword DMA transfer cycle time per word.</p>
</dd>

### -field <b>RecommendedMWXferCycleTime</b>

<dd>
<p>Indicates the recommended multiword DMA transfer cycle time per word.</p>
</dd>

### -field <b>MinimumPIOCycleTime</b>

<dd>
<p>Indicates the minimum PIO transfer cycle time without flow control.</p>
</dd>

### -field <b>MinimumPIOCycleTimeIORDY</b>

<dd>
<p>Indicates the minimum PIO transfer cycle time with IORDY flow control.</p>
</dd>

### -field <b>ReservedWords69</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>QueueDepth</b>

<dd>
<p>Indicates the maximum queue depth.</p>
</dd>

### -field <b>ReservedWord75</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>ReservedWords76</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>MajorRevision</b>

<dd>
<p>Indicates the device's major revision number.</p>
</dd>

### -field <b>MinorRevision</b>

<dd>
<p>Indicates the device's minor revision number.</p>
</dd>

### -field <b>CommandSetSupport</b>

<dd>
<dl>

### -field <b>SmartCommands</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the SMART feature set.</p>
</dd>

### -field <b>SecurityMode</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the security mode feature set.</p>
</dd>

### -field <b>PowerManagement</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the mandatory power management feature set.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>WriteCache</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports a write cache.</p>
</dd>

### -field <b>LookAhead</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports lookahead.</p>
</dd>

### -field <b>ReleaseInterrupt</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports release interrupt.</p>
</dd>

### -field <b>ServiceInterrupt</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports service interrupt.</p>
</dd>

### -field <b>DeviceReset</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the device reset command.</p>
</dd>

### -field <b>HostProtectedArea</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the host protected area feature set.</p>
</dd>

### -field <b>Obsolete1</b>

<dd>
<p>This member is obsolete. Do not use.</p>
</dd>

### -field <b>WriteBuffer</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the write buffer command.</p>
</dd>

### -field <b>ReadBuffer</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the read buffer command.</p>
</dd>

### -field <b>Nop</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the NOP command.</p>
</dd>

### -field <b>Obsolete2</b>

<dd>
<p>Obsolete. Do not use.</p>
</dd>

### -field <b>DownloadMicrocode</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the DOWNLOAD MICROCODE command.</p>
</dd>

### -field <b>DmaQueued</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports READ/WRITE DMA QUEUED command.</p>
</dd>

### -field <b>Cfa</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the CFA feature set.</p>
</dd>

### -field <b>AdvancedPm</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the advanced power management feature set.</p>
</dd>

### -field <b>Msn</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the media status notification feature set.</p>
</dd>

### -field <b>PowerUpInStandby</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports power-up in standby feature set.</p>
</dd>

### -field <b>ManualPowerUp</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the SET FEATURES subcommand required to spin up the device after power-up.</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>SetMax</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the SET MAX security extension command.</p>
</dd>

### -field <b>Acoustics</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the automatic acoustic management feature set.</p>
</dd>

### -field <b>BigLba</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the 48-bit address feature set.</p>
</dd>

### -field <b>Resrved3</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>

### -field <b>CommandSetActive</b>

<dd>
<dl>


</dl>
<dl>

### -field <b>SmartCommands</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the SMART feature set.</p>
</dd>

### -field <b>SecurityMode</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the security mode feature set.</p>
</dd>

### -field <b>PowerManagement</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the mandatory power management feature set.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>WriteCache</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports a write cache.</p>
</dd>

### -field <b>LookAhead</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports lookahead.</p>
</dd>

### -field <b>ReleaseInterrupt</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports release interrupt.</p>
</dd>

### -field <b>ServiceInterrupt</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports service interrupt.</p>
</dd>

### -field <b>DeviceReset</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the device reset command.</p>
</dd>

### -field <b>HostProtectedArea</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the host protected area feature set.</p>
</dd>

### -field <b>Obsolete1</b>

<dd>
<p>This member is obsolete. Do not use.</p>
</dd>

### -field <b>WriteBuffer</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the write buffer command.</p>
</dd>

### -field <b>ReadBuffer</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the read buffer command.</p>
</dd>

### -field <b>Nop</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the NOP command.</p>
</dd>

### -field <b>Obsolete2</b>

<dd>
<p>Obsolete. Do not use.</p>
</dd>

### -field <b>DownloadMicrocode</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the DOWNLOAD MICROCODE command.</p>
</dd>

### -field <b>DmaQueued</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports READ/WRITE DMA QUEUED command.</p>
</dd>

### -field <b>Cfa</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the CFA feature set.</p>
</dd>

### -field <b>AdvancedPm</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the advanced power management feature set.</p>
</dd>

### -field <b>Msn</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the media status notification feature set.</p>
</dd>

### -field <b>PowerUpInStandby</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports power-up in standby feature set.</p>
</dd>

### -field <b>ManualPowerUp</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the SET FEATURES subcommand required to spin up the device after power-up.</p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>SetMax</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the SET MAX security extension command.</p>
</dd>

### -field <b>Acoustics</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the automatic acoustic management feature set.</p>
</dd>

### -field <b>BigLba</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the 48-bit address feature set.</p>
</dd>

### -field <b>Resrved3</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>

### -field <b>UltraDMASupport</b>

<dd>
<p>Contains a bitmap indicating which ultraDMA modes the device supports.</p>
</dd>

### -field <b>UltraDMAActive</b>

<dd>
<p>Contains a bitmap indicating which ultraDMA modes are selected.</p>
</dd>

### -field <b>ReservedWord89</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>HardwareResetResult</b>

<dd>
<p>Indicates the result of a hardware reset. For more information about the values assigned to this member, see the <i>ATA/ATAP specification</i>.</p>
</dd>

### -field <b>CurrentAcousticValue</b>

<dd>
<p>Indicates the current acoustic management value.</p>
</dd>

### -field <b>RecommendedAcousticValue</b>

<dd>
<p>Contain the device vendor's recommended acoustic management value.</p>
</dd>

### -field <b>ReservedWord95</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Max48BitLBA</b>

<dd>
<p>Contains the maximum user LBA for the 48-bit address feature set.</p>
</dd>

### -field <b>StreamingTransferTime</b>

<dd></dd>

### -field <b>ReservedWord105</b>

<dd></dd>

### -field <b>PhysicalLogicalSectorSize</b>

<dd>
<dl>

### -field <b>Reserved1</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>

### -field <b>InterSeekDelay</b>

<dd></dd>

### -field <b>WorldWideName</b>

<dd></dd>

### -field <b>ReservedForWorldWideName128</b>

<dd></dd>

### -field <b>ReservedForTlcTechnicalReport</b>

<dd></dd>

### -field <b>WordsPerLogicalSector</b>

<dd></dd>

### -field <b>CommandSetSupportExt</b>

<dd>
<dl>

### -field <b>Reserved1</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>

### -field <b>CommandSetActiveExt</b>

<dd>
<dl>

### -field <b>Reserved1</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>

### -field <b>ReservedForExpandedSupportandActive</b>

<dd></dd>

### -field <b>MsnSupport</b>

<dd>
<p>Indicates when <b>TRUE</b> that the device supports media status notification.</p>
</dd>

### -field <b>ReservedWord1274</b>

<dd></dd>

### -field <b>SecurityStatus</b>

<dd>
<p>Contains a bitmap that indicates the security status. For more information about the meaning of each individual bit, see the <i>ATA/ATAPI specification</i>.</p>
<dl>

### -field <b>Reserved1</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>

### -field <b>ReservedWord129</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>CfaPowerModel</b>

<dd>
</dd>

### -field <b>ReservedForCfaWord161</b>

<dd>
<p>Words 161-168</p>
</dd>

### -field <b>DataSetManagementFeature</b>

<dd>
</dd>

### -field <b>ReservedForCfaWord170</b>

<dd>
<p>Words 170-175</p>
</dd>

### -field <b>CurrentMediaSerialNumber</b>

<dd>
<p>Words 176-205</p>
</dd>

### -field <b>ReservedWord206</b>

<dd>
<p>Word 206</p>
</dd>

### -field <b>ReservedWord207</b>

<dd>
<p>Words 207-208</p>
</dd>

### -field <b>BlockAlignment</b>

<dd>
</dd>

### -field <b>WriteReadVerifySectorCountMode3Only</b>

<dd>
<p>Words 210-211</p>
</dd>

### -field <b>WriteReadVerifySectorCountMode2Only</b>

<dd>
<p>Words 212-213</p>
</dd>

### -field <b>NVCacheCapabilities</b>

<dd>
<dl>

### -field <b>Reserved1</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>

### -field <b>NVCacheSizeLSW</b>

<dd></dd>

### -field <b>NVCacheSizeMSW</b>

<dd></dd>

### -field <b>NominalMediaRotationRate</b>

<dd></dd>

### -field <b>ReservedWord218</b>

<dd></dd>

### -field <b>NVCacheOptions</b>

<dd>
</dd>

### -field <b>ReservedWord220</b>

<dd>
<p>Words 220-254</p>
</dd>

### -field <b>Signature</b>

<dd>
<p>Indicates the disk signature.</p>
</dd>

### -field <b>CheckSum</b>

<dd>
<p>Indicates the checksum.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ata.h (include Irb.h)</dt>
</dl>
</td>
</tr>
</table>