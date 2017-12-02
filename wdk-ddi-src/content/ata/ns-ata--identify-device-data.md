---
UID: NS.ata._IDENTIFY_DEVICE_DATA
title: IDENTIFY_DEVICE_DATA
author: windows-driver-content
description: The IDENTIFY_DEVICE_DATA structure contains the data retrieved by an ATA identify device data command (0xEC).Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\identify_device_data.htm
old-project: storage
ms.assetid: 7f2edd6f-16bf-47a6-8546-7871435a56ac
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDENTIFY_DEVICE_DATA, IDENTIFY_DEVICE_DATA, *PIDENTIFY_DEVICE_DATA
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

### -field GeneralConfiguration

<dd>
<dl>

### -field Reserved1

<dd>
<p>Reserved.</p>
</dd>

### -field Retired3

<dd>
<p>This member is no longer used.</p>
</dd>

### -field ResponseIncomplete

<dd>
<p>Indicates that the response was incomplete.</p>
</dd>

### -field Retired2

<dd>
<p>This member is no longer used.</p>
</dd>

### -field FixedDevice

<dd>
<p>Indicates when set to 1 that the device is fixed.</p>
</dd>

### -field RemovableMedia

<dd>
<p>Indicates when set to 1 that the media is removable.</p>
</dd>

### -field Retired1

<dd>
<p>This member is no longer used.</p>
</dd>

### -field DeviceType

<dd>
<p>Indicates when set to 1 that the device is an ATA device.</p>
</dd>
</dl>
</dd>

### -field NumCylinders

<dd>
<p>Indicates the number of cylinders on the device.</p>
</dd>

### -field ReservedWord2

<dd>
<p>Reserved.</p>
</dd>

### -field NumHeads

<dd>
<p>Number of logical heads on the device.</p>
</dd>

### -field Retired1

<dd>
<p>This member is no longer used.</p>
</dd>

### -field NumSectorsPerTrack

<dd>
<p>Indicates the number of sectors per track.</p>
</dd>

### -field VendorUnique1

<dd>
<p>Contains the first ID of the device's vendor.</p>
</dd>

### -field SerialNumber

<dd>
<p>Contains the serial number of the device.</p>
</dd>

### -field Retired2

<dd>
<p>This member is no longer used.</p>
</dd>

### -field Obsolete1

<dd>
<p>This member is obsolete. Do not use.</p>
</dd>

### -field FirmwareRevision

<dd>
<p>Contains the revision number of the device's firmware.</p>
</dd>

### -field ModelNumber

<dd>
<p>Contains the device's model number.</p>
</dd>

### -field MaximumBlockTransfer

<dd>
<p>Contains the maximum number of blocks allowed in a single transfer.</p>
</dd>

### -field VendorUnique2

<dd>
<p>Contains the second ID of the device's vendor.</p>
</dd>

### -field ReservedWord48

<dd>
<p>Reserved.</p>
</dd>

### -field Capabilities

<dd>
<dl>

### -field ReservedByte49

<dd>
<p>Reserved.</p>
</dd>

### -field DmaSupported

<dd>
<p>Indicates that the device supports DMA operations.</p>
</dd>

### -field LbaSupported

<dd>
<p>Indicates that the device supports logical block addressing.</p>
</dd>

### -field IordyDisable

<dd>
<p>Indicates when set to 1 that I/O channel ready is disabled for the device.</p>
</dd>

### -field IordySupported

<dd>
<p>Indicates when set to 1 that I/O channel ready is supported by the device.</p>
</dd>

### -field Reserved1

<dd>
<p>Reserved.</p>
</dd>

### -field StandybyTimerSupport

<dd>
<p>Indicates when set to 1 that the device supports standby timers.</p>
</dd>

### -field Reserved2

<dd>
<p>Reserved.</p>
</dd>

### -field ReservedWord50

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>

### -field ObsoleteWords51

<dd>
<p>This member is obsolete. Do not use.</p>
</dd>

### -field TranslationFieldsValid

<dd>
<p>Contains a bitfield whose bits indicate which of the bytes in the identify data package contain valid address translation information. For more information about how this bitfield is defined, see the <i>ATA/ATAPI specification</i>.</p>
</dd>

### -field Reserved3

<dd>
<p>Reserved.</p>
</dd>

### -field NumberOfCurrentCylinders

<dd>
<p>Indicates the number of cylinders on the device.</p>
</dd>

### -field NumberOfCurrentHeads

<dd>
<p>Indicates the number of heads on the device.</p>
</dd>

### -field CurrentSectorsPerTrack

<dd>
<p>Indicates the number of sectors per track.</p>
</dd>

### -field CurrentSectorCapacity

<dd>
<p>Indicates the number of sectors on the device.</p>
</dd>

### -field CurrentMultiSectorSetting

<dd>
<p>Indicates the multisector setting.</p>
</dd>

### -field MultiSectorSettingValid

<dd>
<p>Indicates when <b>TRUE</b> that the multisector setting is valid.</p>
</dd>

### -field ReservedByte59

<dd>
<p>Reserved.</p>
</dd>

### -field UserAddressableSectors

<dd>
<p>Indicates the total number of user-addressable sectors.</p>
</dd>

### -field ObsoleteWord62

<dd>
<p>This member is obsolete. Do not use.</p>
</dd>

### -field MultiWordDMASupport

<dd>
<p>Indicates which DMA modes the device supports.</p>
</dd>

### -field MultiWordDMAActive

<dd>
<p>Indicates which DMA modes are currently selected.</p>
</dd>

### -field AdvancedPIOModes

<dd></dd>

### -field ReservedByte64

<dd>
<p>Reserved.</p>
</dd>

### -field MinimumMWXferCycleTime

<dd>
<p>Indicates the minimum multiword DMA transfer cycle time per word.</p>
</dd>

### -field RecommendedMWXferCycleTime

<dd>
<p>Indicates the recommended multiword DMA transfer cycle time per word.</p>
</dd>

### -field MinimumPIOCycleTime

<dd>
<p>Indicates the minimum PIO transfer cycle time without flow control.</p>
</dd>

### -field MinimumPIOCycleTimeIORDY

<dd>
<p>Indicates the minimum PIO transfer cycle time with IORDY flow control.</p>
</dd>

### -field ReservedWords69

<dd>
<p>Reserved.</p>
</dd>

### -field QueueDepth

<dd>
<p>Indicates the maximum queue depth.</p>
</dd>

### -field ReservedWord75

<dd>
<p>Reserved.</p>
</dd>

### -field ReservedWords76

<dd>
<p>Reserved.</p>
</dd>

### -field MajorRevision

<dd>
<p>Indicates the device's major revision number.</p>
</dd>

### -field MinorRevision

<dd>
<p>Indicates the device's minor revision number.</p>
</dd>

### -field CommandSetSupport

<dd>
<dl>

### -field SmartCommands

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the SMART feature set.</p>
</dd>

### -field SecurityMode

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the security mode feature set.</p>
</dd>

### -field PowerManagement

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the mandatory power management feature set.</p>
</dd>

### -field Reserved1

<dd>
<p>Reserved.</p>
</dd>

### -field WriteCache

<dd>
<p>Indicates when <b>TRUE</b> that the device supports a write cache.</p>
</dd>

### -field LookAhead

<dd>
<p>Indicates when <b>TRUE</b> that the device supports lookahead.</p>
</dd>

### -field ReleaseInterrupt

<dd>
<p>Indicates when <b>TRUE</b> that the device supports release interrupt.</p>
</dd>

### -field ServiceInterrupt

<dd>
<p>Indicates when <b>TRUE</b> that the device supports service interrupt.</p>
</dd>

### -field DeviceReset

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the device reset command.</p>
</dd>

### -field HostProtectedArea

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the host protected area feature set.</p>
</dd>

### -field Obsolete1

<dd>
<p>This member is obsolete. Do not use.</p>
</dd>

### -field WriteBuffer

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the write buffer command.</p>
</dd>

### -field ReadBuffer

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the read buffer command.</p>
</dd>

### -field Nop

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the NOP command.</p>
</dd>

### -field Obsolete2

<dd>
<p>Obsolete. Do not use.</p>
</dd>

### -field DownloadMicrocode

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the DOWNLOAD MICROCODE command.</p>
</dd>

### -field DmaQueued

<dd>
<p>Indicates when <b>TRUE</b> that the device supports READ/WRITE DMA QUEUED command.</p>
</dd>

### -field Cfa

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the CFA feature set.</p>
</dd>

### -field AdvancedPm

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the advanced power management feature set.</p>
</dd>

### -field Msn

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the media status notification feature set.</p>
</dd>

### -field PowerUpInStandby

<dd>
<p>Indicates when <b>TRUE</b> that the device supports power-up in standby feature set.</p>
</dd>

### -field ManualPowerUp

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the SET FEATURES subcommand required to spin up the device after power-up.</p>
</dd>

### -field Reserved2

<dd>
<p>Reserved.</p>
</dd>

### -field SetMax

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the SET MAX security extension command.</p>
</dd>

### -field Acoustics

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the automatic acoustic management feature set.</p>
</dd>

### -field BigLba

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the 48-bit address feature set.</p>
</dd>

### -field Resrved3

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>

### -field CommandSetActive

<dd>
<dl>


</dl>
<dl>

### -field SmartCommands

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the SMART feature set.</p>
</dd>

### -field SecurityMode

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the security mode feature set.</p>
</dd>

### -field PowerManagement

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the mandatory power management feature set.</p>
</dd>

### -field Reserved1

<dd>
<p>Reserved.</p>
</dd>

### -field WriteCache

<dd>
<p>Indicates when <b>TRUE</b> that the device supports a write cache.</p>
</dd>

### -field LookAhead

<dd>
<p>Indicates when <b>TRUE</b> that the device supports lookahead.</p>
</dd>

### -field ReleaseInterrupt

<dd>
<p>Indicates when <b>TRUE</b> that the device supports release interrupt.</p>
</dd>

### -field ServiceInterrupt

<dd>
<p>Indicates when <b>TRUE</b> that the device supports service interrupt.</p>
</dd>

### -field DeviceReset

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the device reset command.</p>
</dd>

### -field HostProtectedArea

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the host protected area feature set.</p>
</dd>

### -field Obsolete1

<dd>
<p>This member is obsolete. Do not use.</p>
</dd>

### -field WriteBuffer

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the write buffer command.</p>
</dd>

### -field ReadBuffer

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the read buffer command.</p>
</dd>

### -field Nop

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the NOP command.</p>
</dd>

### -field Obsolete2

<dd>
<p>Obsolete. Do not use.</p>
</dd>

### -field DownloadMicrocode

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the DOWNLOAD MICROCODE command.</p>
</dd>

### -field DmaQueued

<dd>
<p>Indicates when <b>TRUE</b> that the device supports READ/WRITE DMA QUEUED command.</p>
</dd>

### -field Cfa

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the CFA feature set.</p>
</dd>

### -field AdvancedPm

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the advanced power management feature set.</p>
</dd>

### -field Msn

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the media status notification feature set.</p>
</dd>

### -field PowerUpInStandby

<dd>
<p>Indicates when <b>TRUE</b> that the device supports power-up in standby feature set.</p>
</dd>

### -field ManualPowerUp

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the SET FEATURES subcommand required to spin up the device after power-up.</p>
</dd>

### -field Reserved2

<dd>
<p>Reserved.</p>
</dd>

### -field SetMax

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the SET MAX security extension command.</p>
</dd>

### -field Acoustics

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the automatic acoustic management feature set.</p>
</dd>

### -field BigLba

<dd>
<p>Indicates when <b>TRUE</b> that the device supports the 48-bit address feature set.</p>
</dd>

### -field Resrved3

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>

### -field UltraDMASupport

<dd>
<p>Contains a bitmap indicating which ultraDMA modes the device supports.</p>
</dd>

### -field UltraDMAActive

<dd>
<p>Contains a bitmap indicating which ultraDMA modes are selected.</p>
</dd>

### -field ReservedWord89

<dd>
<p>Reserved.</p>
</dd>

### -field HardwareResetResult

<dd>
<p>Indicates the result of a hardware reset. For more information about the values assigned to this member, see the <i>ATA/ATAP specification</i>.</p>
</dd>

### -field CurrentAcousticValue

<dd>
<p>Indicates the current acoustic management value.</p>
</dd>

### -field RecommendedAcousticValue

<dd>
<p>Contain the device vendor's recommended acoustic management value.</p>
</dd>

### -field ReservedWord95

<dd>
<p>Reserved.</p>
</dd>

### -field Max48BitLBA

<dd>
<p>Contains the maximum user LBA for the 48-bit address feature set.</p>
</dd>

### -field StreamingTransferTime

<dd></dd>

### -field ReservedWord105

<dd></dd>

### -field PhysicalLogicalSectorSize

<dd>
<dl>

### -field Reserved1

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>

### -field InterSeekDelay

<dd></dd>

### -field WorldWideName

<dd></dd>

### -field ReservedForWorldWideName128

<dd></dd>

### -field ReservedForTlcTechnicalReport

<dd></dd>

### -field WordsPerLogicalSector

<dd></dd>

### -field CommandSetSupportExt

<dd>
<dl>

### -field Reserved1

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>

### -field CommandSetActiveExt

<dd>
<dl>

### -field Reserved1

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>

### -field ReservedForExpandedSupportandActive

<dd></dd>

### -field MsnSupport

<dd>
<p>Indicates when <b>TRUE</b> that the device supports media status notification.</p>
</dd>

### -field ReservedWord1274

<dd></dd>

### -field SecurityStatus

<dd>
<p>Contains a bitmap that indicates the security status. For more information about the meaning of each individual bit, see the <i>ATA/ATAPI specification</i>.</p>
<dl>

### -field Reserved1

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>

### -field ReservedWord129

<dd>
<p>Reserved.</p>
</dd>

### -field CfaPowerModel

<dd>
</dd>

### -field ReservedForCfaWord161

<dd>
<p>Words 161-168</p>
</dd>

### -field DataSetManagementFeature

<dd>
</dd>

### -field ReservedForCfaWord170

<dd>
<p>Words 170-175</p>
</dd>

### -field CurrentMediaSerialNumber

<dd>
<p>Words 176-205</p>
</dd>

### -field ReservedWord206

<dd>
<p>Word 206</p>
</dd>

### -field ReservedWord207

<dd>
<p>Words 207-208</p>
</dd>

### -field BlockAlignment

<dd>
</dd>

### -field WriteReadVerifySectorCountMode3Only

<dd>
<p>Words 210-211</p>
</dd>

### -field WriteReadVerifySectorCountMode2Only

<dd>
<p>Words 212-213</p>
</dd>

### -field NVCacheCapabilities

<dd>
<dl>

### -field Reserved1

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>

### -field NVCacheSizeLSW

<dd></dd>

### -field NVCacheSizeMSW

<dd></dd>

### -field NominalMediaRotationRate

<dd></dd>

### -field ReservedWord218

<dd></dd>

### -field NVCacheOptions

<dd>
</dd>

### -field ReservedWord220

<dd>
<p>Words 220-254</p>
</dd>

### -field Signature

<dd>
<p>Indicates the disk signature.</p>
</dd>

### -field CheckSum

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