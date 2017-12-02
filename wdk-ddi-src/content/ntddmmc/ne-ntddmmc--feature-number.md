---
UID: NE.ntddmmc._FEATURE_NUMBER
title: FEATURE_NUMBER
author: windows-driver-content
description: The FEATURE_NUMBER enumeration provides a list of the features that are defined by the SCSI Multimedia - 4 (MMC-4) specification.
old-location: storage\feature_number.htm
old-project: storage
ms.assetid: f139da57-1527-476d-8e9f-0b96876adecf
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: WHEA_XPF_PROCESSOR_ERROR_SECTION,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddmmc.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FEATURE_NUMBER
req.alt-loc: ntddmmc.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FEATURE_NUMBER enumeration



## -description
<p>The FEATURE_NUMBER enumeration provides a list of the features that are defined by the <i>SCSI Multimedia - 4 (MMC-4)</i> specification. </p>


## -syntax

````
typedef enum _FEATURE_NUMBER { 
  FeatureProfileList                   = 0x0000,
  FeatureCore                          = 0x0001,
  FeatureMorphing                      = 0x0002,
  FeatureRemovableMedium               = 0x0003,
  FeatureWriteProtect                  = 0x0004,
  FeatureRandomReadable                = 0x0010,
  FeatureMultiRead                     = 0x001D,
  FeatureCdRead                        = 0x001E,
  FeatureDvdRead                       = 0x001F,
  FeatureRandomWritable                = 0x0020,
  FeatureIncrementalStreamingWritable  = 0x0021,
  FeatureSectorErasable                = 0x0022,
  FeatureFormattable                   = 0x0023,
  FeatureDefectManagement              = 0x0024,
  FeatureWriteOnce                     = 0x0025,
  FeatureRestrictedOverwrite           = 0x0026,
  FeatureCdrwCAVWrite                  = 0x0027,
  FeatureMrw                           = 0x0028,
  FeatureEnhancedDefectReporting       = 0x0029,
  FeatureDvdPlusRW                     = 0x002A,
  FeatureDvdPlusR                      = 0x002B,
  FeatureRigidRestrictedOverwrite      = 0x002C,
  FeatureCdTrackAtOnce                 = 0x002D,
  FeatureCdMastering                   = 0x002E,
  FeatureDvdRecordableWrite            = 0x002F,
  FeatureDDCDRead                      = 0x0030,
  FeatureDDCDRWrite                    = 0x0031,
  FeatureDDCDRWWrite                   = 0x0032,
  FeatureLayerJumpRecording            = 0x0033,
  FeatureCDRWMediaWriteSupport         = 0x0037,
  FeatureBDRPseudoOverwrite            = 0x0038,
  FeatureDvdPlusRWDualLayer            = 0x003A,
  FeatureDvdPlusRDualLayer             = 0x003B,
  FeatureBDRead                        = 0x0040,
  FeatureBDWrite                       = 0x0041,
  FeatureTSR                           = 0x0042,
  FeatureHDDVDRead                     = 0x0050,
  FeatureHDDVDWrite                    = 0x0051,
  FeatureHybridDisc                    = 0x0080,
  FeaturePowerManagement               = 0x0100,
  FeatureSMART                         = 0x0101,
  FeatureEmbeddedChanger               = 0x0102,
  FeatureCDAudioAnalogPlay             = 0x0103,
  FeatureMicrocodeUpgrade              = 0x0104,
  FeatureTimeout                       = 0x0105,
  FeatureDvdCSS                        = 0x0106,
  FeatureRealTimeStreaming             = 0x0107,
  FeatureLogicalUnitSerialNumber       = 0x0108,
  FeatureMediaSerialNumber             = 0x0109,
  FeatureDiscControlBlocks             = 0x010A,
  FeatureDvdCPRM                       = 0x010B,
  FeatureFirmwareDate                  = 0x010C,
  FeatureAACS                          = 0x010D,
  FeatureVCPS                          = 0x0110
} FEATURE_NUMBER, *PFEATURE_NUMBER;
````


## -enum-fields
<dl>

### -field FeatureProfileList

<dd>
<p>Indicates the feature named "Profile List" by the <i>MMC-3 </i>specification. This feature provides a list of all profiles supported by the device. </p>
</dd>

### -field FeatureCore

<dd>
<p>Indicates the feature named "Core" by the <i>MMC-3 </i>specification. This feature encompasses the basic functionality which is mandatory for all devices that support the <i>MMC-3</i> standard. See the <i>MMC-3</i> specification for a description of the capabilities included in the Core feature. </p>
</dd>

### -field FeatureMorphing

<dd>
<p>Indicates the feature named "Morphing" by the <i>MMC-3 </i>specification. Devices that support this feature can notify the initiator of operational changes and allow the initiator to prevent operational changes. </p>
</dd>

### -field FeatureRemovableMedium

<dd>
<p>Indicates the feature named "Removable Medium" by the <i>MMC-3 </i>specification. Devices that support this feature allow the medium to be removed from the device. They also can communicate to the initiator that the user wants to eject the medium or has inserted a new medium. </p>
</dd>

### -field FeatureWriteProtect

<dd>
<p>Indicates the feature named "Write Protect" by the <i>MMC-3 </i>specification. Devices that support this feature allow the initiator to change the write-protection state of the media programmatically. </p>
</dd>

### -field FeatureRandomReadable

<dd>
<p>Indicates the feature named "Random Readable" by the <i>MMC-3 </i>specification. Devices that support this feature allow the initiator to read blocks of data on the disk at random locations. These devices do not require that the initiator address disk locations in any particular order. </p>
</dd>

### -field FeatureMultiRead

<dd>
<p>Indicates the feature named "MultiRead," originally defined by the Optical Storage Technology Association (OSTA) and incorporated into the <i>MMC-3 </i>specification. Devices that support this feature can read all CD media types. </p>
</dd>

### -field FeatureCdRead

<dd>
<p>Indicates the feature named "CD Read" by the <i>MMC-3 </i>specification. Devices that support this feature can read CD-specific information from the media and can read user data from all types of CD blocks. </p>
</dd>

### -field FeatureDvdRead

<dd>
<p>Indicates the feature named "DVD Read" by the <i>MMC-3 </i>specification. Devices that support this feature can read DVD-specific information from the media.</p>
</dd>

### -field FeatureRandomWritable

<dd>
<p>Indicates the feature named "Random Writable" by the <i>MMC-3 </i>specification. Devices that support this feature can write blocks of data to random locations on the disk. These devices do not require that the initiator address disk locations in any particular order. </p>
</dd>

### -field FeatureIncrementalStreamingWritable

<dd>
<p>Indicates the feature named "Incremental Streaming Writable" by the <i>MMC-3 </i>specification. Devices that support this feature can append data to a limited number of locations on the media. </p>
</dd>

### -field FeatureSectorErasable

<dd>
<p>Indicates the feature named "Sector Erasable" by the <i>MMC-3 </i>specification. Devices that support this feature require an erase pass before overwriting existing data.</p>
</dd>

### -field FeatureFormattable

<dd>
<p>Indicates the feature named "Formattable" by the <i>MMC-3 </i>specification. Devices that support this feature can format media into logical blocks. </p>
</dd>

### -field FeatureDefectManagement

<dd>
<p>Indicates the feature named "Defect Management" by the <i>MMC-3 </i>specification. Devices that support this feature are able to provide contiguous address space that is guaranteed to be defect free. </p>
</dd>

### -field FeatureWriteOnce

<dd>
<p>Indicates the feature named "Write Once" by the <i>MMC-3 </i>specification. Devices that support this feature can write to any previously unused logical block. </p>
</dd>

### -field FeatureRestrictedOverwrite

<dd>
<p>Indicates the feature named "Restricted Overwrite" by the <i>MMC-3 </i>specification. Devices that support this feature are limited in regard to which logical blocks they can overwrite at any given time. </p>
</dd>

### -field FeatureCdrwCAVWrite

<dd>
<p>Indicates the feature named "CD-RW CAV Write" by the <i>MMC-3 </i>specification. Devices that support this feature can perform writes on CD-RW media in CAV mode. </p>
</dd>

### -field FeatureMrw

<dd>
<p>Indicates the feature named "MRW" by the <i>MMC-3 </i>specification. Devices that support this feature can recognize, read and optionally write MRW formatted media. </p>
</dd>

### -field FeatureEnhancedDefectReporting

<dd></dd>

### -field FeatureDvdPlusRW

<dd>
<p>Indicates the feature named "DVD+RW" by the <i>MMC-3 </i>specification. Devices that support this feature can recognize, read and optionally write DVD+RW media. </p>
</dd>

### -field FeatureDvdPlusR

<dd></dd>

### -field FeatureRigidRestrictedOverwrite

<dd>
<p>Indicates the feature named "DVD-RW Restricted Overwrite" by the <i>MMC-3 </i>specification. Devices that support this feature can only write on block boundaries. These devices cannot perform read or write operations that transfer less than a block of data. </p>
</dd>

### -field FeatureCdTrackAtOnce

<dd>
<p>Indicates the feature named "CD Track at Once" by the <i>MMC-3 </i>specification. Devices that support this feature can write data to a CD track. </p>
</dd>

### -field FeatureCdMastering

<dd>
<p>Indicates the feature named "CD Mastering" by the <i>MMC-3 </i>specification. Devices that support this feature can write to a CD in either "Session-at-Once" mode or raw mode. </p>
</dd>

### -field FeatureDvdRecordableWrite

<dd>
<p>Indicates the feature named "DVD-R Write" by the <i>MMC-3 </i>specification. Devices that support this feature can write data to a write-once DVD media in "Disc-at-Once" mode.</p>
</dd>

### -field FeatureDDCDRead

<dd>
<p>Indicates the feature named "DDCD Read" by the <i>MMC-3 </i>specification. Devices that support this feature can read user data from DDCD blocks. </p>
</dd>

### -field FeatureDDCDRWrite

<dd>
<p>Indicates the feature named "DDCD-R Write" by the <i>MMC-3 </i>specification. Devices that support this feature can read and write DDCD-R media. </p>
</dd>

### -field FeatureDDCDRWWrite

<dd>
<p>Indicates the feature named "DDCD-RW Write" by the <i>MMC-3 </i>specification. Devices that support this feature can read and write DDCD-RW media. </p>
</dd>

### -field FeatureLayerJumpRecording

<dd>
<p>Reserved 0x0034 - 0x0036</p>
</dd>

### -field FeatureCDRWMediaWriteSupport

<dd></dd>

### -field FeatureBDRPseudoOverwrite

<dd>
<p>Reserved 0x0039</p>
</dd>

### -field FeatureDvdPlusRWDualLayer

<dd></dd>

### -field FeatureDvdPlusRDualLayer

<dd>
<p>Reserved 0x003c - 0x003f</p>
</dd>

### -field FeatureBDRead

<dd></dd>

### -field FeatureBDWrite

<dd></dd>

### -field FeatureTSR

<dd>
<p>Reserved 0x0043 - 0x004f</p>
</dd>

### -field FeatureHDDVDRead

<dd></dd>

### -field FeatureHDDVDWrite

<dd>
<p>Reserved 0x0052 - 0x007f</p>
</dd>

### -field FeatureHybridDisc

<dd>
<p>Reserved 0x0081 - 0x00ff</p>
</dd>

### -field FeaturePowerManagement

<dd>
<p>Indicates the feature named "Power Management" by the <i>MMC-3 </i>specification. Devices that support this feature can perform both initiator and logical-unit directed power management. </p>
</dd>

### -field FeatureSMART

<dd>
<p>Indicates the feature named "S.M.A.R.T." by the <i>MMC-3 </i>specification. Devices that support this feature support Self-Monitoring Analysis and Reporting Technology (SMART). </p>
</dd>

### -field FeatureEmbeddedChanger

<dd>
<p>Indicates the feature named "Embedded Changer" by the <i>MMC-3 </i>specification. Devices that support this feature can move media back and forth between a media storage area and the mechanism that actually accesses the media. </p>
</dd>

### -field FeatureCDAudioAnalogPlay

<dd>
<p>Indicates the feature named "CD Audio External Play" by the <i>MMC-3 </i>specification. Devices that support this feature can play CD audio data and channel it directly to an external output. </p>
</dd>

### -field FeatureMicrocodeUpgrade

<dd>
<p>Indicates the feature named "Microcode Upgrade" by the <i>MMC-3 </i>specification. Devices that support this feature can upgrade their internal microcode by means of a published interface. </p>
</dd>

### -field FeatureTimeout

<dd>
<p>Indicates the feature named "Time-Out" by the <i>MMC-3 </i>specification. Devices that have this feature must respond to commands within a set time period. When these devices cannot complete commands in the allotted time, they complete the commands with an error. </p>
</dd>

### -field FeatureDvdCSS

<dd>
<p>Indicates the feature named "DVD-CSS" by the <i>MMC-3 </i>specification. Devices that support this feature can perform DVD Content Scrambling System (DVD-CSS) authentication and key management. </p>
</dd>

### -field FeatureRealTimeStreaming

<dd>
<p>Indicates the feature named "Real Time Streaming" by the <i>MMC-3 </i>specification. Devices that support this feature allow the initiator to specify the performance level of the device within certain limits allowed by the device. These devices must also indicate to the initiator whether they support stream playback operations. </p>
</dd>

### -field FeatureLogicalUnitSerialNumber

<dd>
<p>Indicates the feature named "Device Serial Number" by the <i>MMC-3 </i>specification. Devices that support this feature can furnish the initiator with a serial number that uniquely identifies the device. </p>
</dd>

### -field FeatureMediaSerialNumber

<dd></dd>

### -field FeatureDiscControlBlocks

<dd>
<p>Indicates the feature named "Disc Control Blocks" by the <i>MMC-3 </i>specification. Devices that support this feature can read or write Disc Control Blocks. </p>
</dd>

### -field FeatureDvdCPRM

<dd>
<p>Indicates the feature named "DVD CPRM" by the <i>MMC-3 </i>specification. Devices that support this feature can perform DVD Content Protection for Recordable Media (CPRM) authentication and key management. </p>
</dd>

### -field FeatureFirmwareDate

<dd></dd>

### -field FeatureAACS

<dd>
<p>Reserved 0x010e - 0x010f</p>
</dd>

### -field FeatureVCPS

<dd>
<p>Reserved 0x0111 - 0xfeff</p>
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
<dt>Ntddmmc.h (include Ntddcdrm.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddmmc\ns-ntddmmc--feature-header.md">FEATURE_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20FEATURE_NUMBER enumeration%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
