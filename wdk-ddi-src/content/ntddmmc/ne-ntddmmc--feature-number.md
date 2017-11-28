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

### -field <a id="FeatureProfileList"></a><a id="featureprofilelist"></a><a id="FEATUREPROFILELIST"></a><b>FeatureProfileList</b>

<dd>
<p>Indicates the feature named "Profile List" by the <i>MMC-3 </i>specification. This feature provides a list of all profiles supported by the device. </p>
</dd>

### -field <a id="FeatureCore"></a><a id="featurecore"></a><a id="FEATURECORE"></a><b>FeatureCore</b>

<dd>
<p>Indicates the feature named "Core" by the <i>MMC-3 </i>specification. This feature encompasses the basic functionality which is mandatory for all devices that support the <i>MMC-3</i> standard. See the <i>MMC-3</i> specification for a description of the capabilities included in the Core feature. </p>
</dd>

### -field <a id="FeatureMorphing"></a><a id="featuremorphing"></a><a id="FEATUREMORPHING"></a><b>FeatureMorphing</b>

<dd>
<p>Indicates the feature named "Morphing" by the <i>MMC-3 </i>specification. Devices that support this feature can notify the initiator of operational changes and allow the initiator to prevent operational changes. </p>
</dd>

### -field <a id="FeatureRemovableMedium"></a><a id="featureremovablemedium"></a><a id="FEATUREREMOVABLEMEDIUM"></a><b>FeatureRemovableMedium</b>

<dd>
<p>Indicates the feature named "Removable Medium" by the <i>MMC-3 </i>specification. Devices that support this feature allow the medium to be removed from the device. They also can communicate to the initiator that the user wants to eject the medium or has inserted a new medium. </p>
</dd>

### -field <a id="FeatureWriteProtect"></a><a id="featurewriteprotect"></a><a id="FEATUREWRITEPROTECT"></a><b>FeatureWriteProtect</b>

<dd>
<p>Indicates the feature named "Write Protect" by the <i>MMC-3 </i>specification. Devices that support this feature allow the initiator to change the write-protection state of the media programmatically. </p>
</dd>

### -field <a id="FeatureRandomReadable"></a><a id="featurerandomreadable"></a><a id="FEATURERANDOMREADABLE"></a><b>FeatureRandomReadable</b>

<dd>
<p>Indicates the feature named "Random Readable" by the <i>MMC-3 </i>specification. Devices that support this feature allow the initiator to read blocks of data on the disk at random locations. These devices do not require that the initiator address disk locations in any particular order. </p>
</dd>

### -field <a id="FeatureMultiRead"></a><a id="featuremultiread"></a><a id="FEATUREMULTIREAD"></a><b>FeatureMultiRead</b>

<dd>
<p>Indicates the feature named "MultiRead," originally defined by the Optical Storage Technology Association (OSTA) and incorporated into the <i>MMC-3 </i>specification. Devices that support this feature can read all CD media types. </p>
</dd>

### -field <a id="FeatureCdRead"></a><a id="featurecdread"></a><a id="FEATURECDREAD"></a><b>FeatureCdRead</b>

<dd>
<p>Indicates the feature named "CD Read" by the <i>MMC-3 </i>specification. Devices that support this feature can read CD-specific information from the media and can read user data from all types of CD blocks. </p>
</dd>

### -field <a id="FeatureDvdRead"></a><a id="featuredvdread"></a><a id="FEATUREDVDREAD"></a><b>FeatureDvdRead</b>

<dd>
<p>Indicates the feature named "DVD Read" by the <i>MMC-3 </i>specification. Devices that support this feature can read DVD-specific information from the media.</p>
</dd>

### -field <a id="FeatureRandomWritable"></a><a id="featurerandomwritable"></a><a id="FEATURERANDOMWRITABLE"></a><b>FeatureRandomWritable</b>

<dd>
<p>Indicates the feature named "Random Writable" by the <i>MMC-3 </i>specification. Devices that support this feature can write blocks of data to random locations on the disk. These devices do not require that the initiator address disk locations in any particular order. </p>
</dd>

### -field <a id="FeatureIncrementalStreamingWritable"></a><a id="featureincrementalstreamingwritable"></a><a id="FEATUREINCREMENTALSTREAMINGWRITABLE"></a><b>FeatureIncrementalStreamingWritable</b>

<dd>
<p>Indicates the feature named "Incremental Streaming Writable" by the <i>MMC-3 </i>specification. Devices that support this feature can append data to a limited number of locations on the media. </p>
</dd>

### -field <a id="FeatureSectorErasable"></a><a id="featuresectorerasable"></a><a id="FEATURESECTORERASABLE"></a><b>FeatureSectorErasable</b>

<dd>
<p>Indicates the feature named "Sector Erasable" by the <i>MMC-3 </i>specification. Devices that support this feature require an erase pass before overwriting existing data.</p>
</dd>

### -field <a id="FeatureFormattable"></a><a id="featureformattable"></a><a id="FEATUREFORMATTABLE"></a><b>FeatureFormattable</b>

<dd>
<p>Indicates the feature named "Formattable" by the <i>MMC-3 </i>specification. Devices that support this feature can format media into logical blocks. </p>
</dd>

### -field <a id="FeatureDefectManagement"></a><a id="featuredefectmanagement"></a><a id="FEATUREDEFECTMANAGEMENT"></a><b>FeatureDefectManagement</b>

<dd>
<p>Indicates the feature named "Defect Management" by the <i>MMC-3 </i>specification. Devices that support this feature are able to provide contiguous address space that is guaranteed to be defect free. </p>
</dd>

### -field <a id="FeatureWriteOnce"></a><a id="featurewriteonce"></a><a id="FEATUREWRITEONCE"></a><b>FeatureWriteOnce</b>

<dd>
<p>Indicates the feature named "Write Once" by the <i>MMC-3 </i>specification. Devices that support this feature can write to any previously unused logical block. </p>
</dd>

### -field <a id="FeatureRestrictedOverwrite"></a><a id="featurerestrictedoverwrite"></a><a id="FEATURERESTRICTEDOVERWRITE"></a><b>FeatureRestrictedOverwrite</b>

<dd>
<p>Indicates the feature named "Restricted Overwrite" by the <i>MMC-3 </i>specification. Devices that support this feature are limited in regard to which logical blocks they can overwrite at any given time. </p>
</dd>

### -field <a id="FeatureCdrwCAVWrite"></a><a id="featurecdrwcavwrite"></a><a id="FEATURECDRWCAVWRITE"></a><b>FeatureCdrwCAVWrite</b>

<dd>
<p>Indicates the feature named "CD-RW CAV Write" by the <i>MMC-3 </i>specification. Devices that support this feature can perform writes on CD-RW media in CAV mode. </p>
</dd>

### -field <a id="FeatureMrw"></a><a id="featuremrw"></a><a id="FEATUREMRW"></a><b>FeatureMrw</b>

<dd>
<p>Indicates the feature named "MRW" by the <i>MMC-3 </i>specification. Devices that support this feature can recognize, read and optionally write MRW formatted media. </p>
</dd>

### -field <a id="FeatureEnhancedDefectReporting"></a><a id="featureenhanceddefectreporting"></a><a id="FEATUREENHANCEDDEFECTREPORTING"></a><b>FeatureEnhancedDefectReporting</b>

<dd></dd>

### -field <a id="FeatureDvdPlusRW"></a><a id="featuredvdplusrw"></a><a id="FEATUREDVDPLUSRW"></a><b>FeatureDvdPlusRW</b>

<dd>
<p>Indicates the feature named "DVD+RW" by the <i>MMC-3 </i>specification. Devices that support this feature can recognize, read and optionally write DVD+RW media. </p>
</dd>

### -field <a id="FeatureDvdPlusR"></a><a id="featuredvdplusr"></a><a id="FEATUREDVDPLUSR"></a><b>FeatureDvdPlusR</b>

<dd></dd>

### -field <a id="FeatureRigidRestrictedOverwrite"></a><a id="featurerigidrestrictedoverwrite"></a><a id="FEATURERIGIDRESTRICTEDOVERWRITE"></a><b>FeatureRigidRestrictedOverwrite</b>

<dd>
<p>Indicates the feature named "DVD-RW Restricted Overwrite" by the <i>MMC-3 </i>specification. Devices that support this feature can only write on block boundaries. These devices cannot perform read or write operations that transfer less than a block of data. </p>
</dd>

### -field <a id="FeatureCdTrackAtOnce"></a><a id="featurecdtrackatonce"></a><a id="FEATURECDTRACKATONCE"></a><b>FeatureCdTrackAtOnce</b>

<dd>
<p>Indicates the feature named "CD Track at Once" by the <i>MMC-3 </i>specification. Devices that support this feature can write data to a CD track. </p>
</dd>

### -field <a id="FeatureCdMastering"></a><a id="featurecdmastering"></a><a id="FEATURECDMASTERING"></a><b>FeatureCdMastering</b>

<dd>
<p>Indicates the feature named "CD Mastering" by the <i>MMC-3 </i>specification. Devices that support this feature can write to a CD in either "Session-at-Once" mode or raw mode. </p>
</dd>

### -field <a id="FeatureDvdRecordableWrite"></a><a id="featuredvdrecordablewrite"></a><a id="FEATUREDVDRECORDABLEWRITE"></a><b>FeatureDvdRecordableWrite</b>

<dd>
<p>Indicates the feature named "DVD-R Write" by the <i>MMC-3 </i>specification. Devices that support this feature can write data to a write-once DVD media in "Disc-at-Once" mode.</p>
</dd>

### -field <a id="FeatureDDCDRead"></a><a id="featureddcdread"></a><a id="FEATUREDDCDREAD"></a><b>FeatureDDCDRead</b>

<dd>
<p>Indicates the feature named "DDCD Read" by the <i>MMC-3 </i>specification. Devices that support this feature can read user data from DDCD blocks. </p>
</dd>

### -field <a id="FeatureDDCDRWrite"></a><a id="featureddcdrwrite"></a><a id="FEATUREDDCDRWRITE"></a><b>FeatureDDCDRWrite</b>

<dd>
<p>Indicates the feature named "DDCD-R Write" by the <i>MMC-3 </i>specification. Devices that support this feature can read and write DDCD-R media. </p>
</dd>

### -field <a id="FeatureDDCDRWWrite"></a><a id="featureddcdrwwrite"></a><a id="FEATUREDDCDRWWRITE"></a><b>FeatureDDCDRWWrite</b>

<dd>
<p>Indicates the feature named "DDCD-RW Write" by the <i>MMC-3 </i>specification. Devices that support this feature can read and write DDCD-RW media. </p>
</dd>

### -field <a id="FeatureLayerJumpRecording"></a><a id="featurelayerjumprecording"></a><a id="FEATURELAYERJUMPRECORDING"></a><b>FeatureLayerJumpRecording</b>

<dd>
<p>Reserved 0x0034 - 0x0036</p>
</dd>

### -field <a id="FeatureCDRWMediaWriteSupport"></a><a id="featurecdrwmediawritesupport"></a><a id="FEATURECDRWMEDIAWRITESUPPORT"></a><b>FeatureCDRWMediaWriteSupport</b>

<dd></dd>

### -field <a id="FeatureBDRPseudoOverwrite"></a><a id="featurebdrpseudooverwrite"></a><a id="FEATUREBDRPSEUDOOVERWRITE"></a><b>FeatureBDRPseudoOverwrite</b>

<dd>
<p>Reserved 0x0039</p>
</dd>

### -field <a id="FeatureDvdPlusRWDualLayer"></a><a id="featuredvdplusrwduallayer"></a><a id="FEATUREDVDPLUSRWDUALLAYER"></a><b>FeatureDvdPlusRWDualLayer</b>

<dd></dd>

### -field <a id="FeatureDvdPlusRDualLayer"></a><a id="featuredvdplusrduallayer"></a><a id="FEATUREDVDPLUSRDUALLAYER"></a><b>FeatureDvdPlusRDualLayer</b>

<dd>
<p>Reserved 0x003c - 0x003f</p>
</dd>

### -field <a id="FeatureBDRead"></a><a id="featurebdread"></a><a id="FEATUREBDREAD"></a><b>FeatureBDRead</b>

<dd></dd>

### -field <a id="FeatureBDWrite"></a><a id="featurebdwrite"></a><a id="FEATUREBDWRITE"></a><b>FeatureBDWrite</b>

<dd></dd>

### -field <a id="FeatureTSR"></a><a id="featuretsr"></a><a id="FEATURETSR"></a><b>FeatureTSR</b>

<dd>
<p>Reserved 0x0043 - 0x004f</p>
</dd>

### -field <a id="FeatureHDDVDRead"></a><a id="featurehddvdread"></a><a id="FEATUREHDDVDREAD"></a><b>FeatureHDDVDRead</b>

<dd></dd>

### -field <a id="FeatureHDDVDWrite"></a><a id="featurehddvdwrite"></a><a id="FEATUREHDDVDWRITE"></a><b>FeatureHDDVDWrite</b>

<dd>
<p>Reserved 0x0052 - 0x007f</p>
</dd>

### -field <a id="FeatureHybridDisc"></a><a id="featurehybriddisc"></a><a id="FEATUREHYBRIDDISC"></a><b>FeatureHybridDisc</b>

<dd>
<p>Reserved 0x0081 - 0x00ff</p>
</dd>

### -field <a id="FeaturePowerManagement"></a><a id="featurepowermanagement"></a><a id="FEATUREPOWERMANAGEMENT"></a><b>FeaturePowerManagement</b>

<dd>
<p>Indicates the feature named "Power Management" by the <i>MMC-3 </i>specification. Devices that support this feature can perform both initiator and logical-unit directed power management. </p>
</dd>

### -field <a id="FeatureSMART"></a><a id="featuresmart"></a><a id="FEATURESMART"></a><b>FeatureSMART</b>

<dd>
<p>Indicates the feature named "S.M.A.R.T." by the <i>MMC-3 </i>specification. Devices that support this feature support Self-Monitoring Analysis and Reporting Technology (SMART). </p>
</dd>

### -field <a id="FeatureEmbeddedChanger"></a><a id="featureembeddedchanger"></a><a id="FEATUREEMBEDDEDCHANGER"></a><b>FeatureEmbeddedChanger</b>

<dd>
<p>Indicates the feature named "Embedded Changer" by the <i>MMC-3 </i>specification. Devices that support this feature can move media back and forth between a media storage area and the mechanism that actually accesses the media. </p>
</dd>

### -field <a id="FeatureCDAudioAnalogPlay"></a><a id="featurecdaudioanalogplay"></a><a id="FEATURECDAUDIOANALOGPLAY"></a><b>FeatureCDAudioAnalogPlay</b>

<dd>
<p>Indicates the feature named "CD Audio External Play" by the <i>MMC-3 </i>specification. Devices that support this feature can play CD audio data and channel it directly to an external output. </p>
</dd>

### -field <a id="FeatureMicrocodeUpgrade"></a><a id="featuremicrocodeupgrade"></a><a id="FEATUREMICROCODEUPGRADE"></a><b>FeatureMicrocodeUpgrade</b>

<dd>
<p>Indicates the feature named "Microcode Upgrade" by the <i>MMC-3 </i>specification. Devices that support this feature can upgrade their internal microcode by means of a published interface. </p>
</dd>

### -field <a id="FeatureTimeout"></a><a id="featuretimeout"></a><a id="FEATURETIMEOUT"></a><b>FeatureTimeout</b>

<dd>
<p>Indicates the feature named "Time-Out" by the <i>MMC-3 </i>specification. Devices that have this feature must respond to commands within a set time period. When these devices cannot complete commands in the allotted time, they complete the commands with an error. </p>
</dd>

### -field <a id="FeatureDvdCSS"></a><a id="featuredvdcss"></a><a id="FEATUREDVDCSS"></a><b>FeatureDvdCSS</b>

<dd>
<p>Indicates the feature named "DVD-CSS" by the <i>MMC-3 </i>specification. Devices that support this feature can perform DVD Content Scrambling System (DVD-CSS) authentication and key management. </p>
</dd>

### -field <a id="FeatureRealTimeStreaming"></a><a id="featurerealtimestreaming"></a><a id="FEATUREREALTIMESTREAMING"></a><b>FeatureRealTimeStreaming</b>

<dd>
<p>Indicates the feature named "Real Time Streaming" by the <i>MMC-3 </i>specification. Devices that support this feature allow the initiator to specify the performance level of the device within certain limits allowed by the device. These devices must also indicate to the initiator whether they support stream playback operations. </p>
</dd>

### -field <a id="FeatureLogicalUnitSerialNumber"></a><a id="featurelogicalunitserialnumber"></a><a id="FEATURELOGICALUNITSERIALNUMBER"></a><b>FeatureLogicalUnitSerialNumber</b>

<dd>
<p>Indicates the feature named "Device Serial Number" by the <i>MMC-3 </i>specification. Devices that support this feature can furnish the initiator with a serial number that uniquely identifies the device. </p>
</dd>

### -field <a id="FeatureMediaSerialNumber"></a><a id="featuremediaserialnumber"></a><a id="FEATUREMEDIASERIALNUMBER"></a><b>FeatureMediaSerialNumber</b>

<dd></dd>

### -field <a id="FeatureDiscControlBlocks"></a><a id="featuredisccontrolblocks"></a><a id="FEATUREDISCCONTROLBLOCKS"></a><b>FeatureDiscControlBlocks</b>

<dd>
<p>Indicates the feature named "Disc Control Blocks" by the <i>MMC-3 </i>specification. Devices that support this feature can read or write Disc Control Blocks. </p>
</dd>

### -field <a id="FeatureDvdCPRM"></a><a id="featuredvdcprm"></a><a id="FEATUREDVDCPRM"></a><b>FeatureDvdCPRM</b>

<dd>
<p>Indicates the feature named "DVD CPRM" by the <i>MMC-3 </i>specification. Devices that support this feature can perform DVD Content Protection for Recordable Media (CPRM) authentication and key management. </p>
</dd>

### -field <a id="FeatureFirmwareDate"></a><a id="featurefirmwaredate"></a><a id="FEATUREFIRMWAREDATE"></a><b>FeatureFirmwareDate</b>

<dd></dd>

### -field <a id="FeatureAACS"></a><a id="featureaacs"></a><a id="FEATUREAACS"></a><b>FeatureAACS</b>

<dd>
<p>Reserved 0x010e - 0x010f</p>
</dd>

### -field <a id="FeatureVCPS"></a><a id="featurevcps"></a><a id="FEATUREVCPS"></a><b>FeatureVCPS</b>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553848">FEATURE_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20FEATURE_NUMBER enumeration%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
