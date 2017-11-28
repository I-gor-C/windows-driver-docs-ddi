---
UID: NE.ntddmmc._FEATURE_PROFILE_TYPE
title: FEATURE_PROFILE_TYPE
author: windows-driver-content
description: The FEATURE_PROFILE_TYPE enumeration provides a list of the profile names that are defined by the SCSI Multimedia - 4 (MMC-4) specification.
old-location: storage\feature_profile_type.htm
old-project: storage
ms.assetid: 60cce78f-1025-41a7-861d-150ef28376cb
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
req.alt-api: FEATURE_PROFILE_TYPE
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

# FEATURE_PROFILE_TYPE enumeration



## -description
<p>The FEATURE_PROFILE_TYPE enumeration provides a list of the profile names that are defined by the <i>SCSI Multimedia - 4 (MMC-4)</i> specification. </p>


## -syntax

````
typedef enum _FEATURE_PROFILE_TYPE { 
  ProfileInvalid                = 0x0000,
  ProfileNonRemovableDisk       = 0x0001,
  ProfileRemovableDisk          = 0x0002,
  ProfileMOErasable             = 0x0003,
  ProfileMOWriteOnce            = 0x0004,
  ProfileAS_MO                  = 0x0005,
  ProfileCdrom                  = 0x0008,
  ProfileCdRecordable           = 0x0009,
  ProfileCdRewritable           = 0x000a,
  ProfileDvdRom                 = 0x0010,
  ProfileDvdRecordable          = 0x0011,
  ProfileDvdRam                 = 0x0012,
  ProfileDvdRewritable          = 0x0013,
  ProfileDvdRWSequential        = 0x0014,
  ProfileDvdDashRDualLayer      = 0x0015,
  ProfileDvdDashRLayerJump      = 0x0016,
  ProfileDvdPlusRW              = 0x001A,
  ProfileDvdPlusR               = 0x001B,
  ProfileDDCdrom                = 0x0020,
  ProfileDDCdRecordable         = 0x0021,
  ProfileDDCdRewritable         = 0x0022,
  ProfileDvdPlusRWDualLayer     = 0x002A,
  ProfileDvdPlusRDualLayer      = 0x002B,
  ProfileBDRom                  = 0x0040,
  ProfileBDRSequentialWritable  = 0x0041,
  ProfileBDRRandomWritable      = 0x0042,
  ProfileBDRewritable           = 0x0043,
  ProfileHDDVDRom               = 0x0050,
  ProfileHDDVDRecordable        = 0x0051,
  ProfileHDDVDRam               = 0x0052,
  ProfileHDDVDRewritable        = 0x0053,
  ProfileHDDVDRDualLayer        = 0x0058,
  ProfileHDDVDRWDualLayer       = 0x005A,
  ProfileNonStandard            = 0xffff
} FEATURE_PROFILE_TYPE, *PFEATURE_PROFILE_TYPE;
````


## -enum-fields
<dl>

### -field <a id="ProfileInvalid"></a><a id="profileinvalid"></a><a id="PROFILEINVALID"></a><b>ProfileInvalid</b>

<dd>
<p>Does not indicate a valid profile. </p>
</dd>

### -field <a id="ProfileNonRemovableDisk"></a><a id="profilenonremovabledisk"></a><a id="PROFILENONREMOVABLEDISK"></a><b>ProfileNonRemovableDisk</b>

<dd>
<p>Indicates the profile named "Nonremovable disk" by the <i>SCSI-3 Multimedia (MMC-3)</i> specification. This profile is used with devices that manage rewritable media and are capable of changing behavior. </p>
</dd>

### -field <a id="ProfileRemovableDisk"></a><a id="profileremovabledisk"></a><a id="PROFILEREMOVABLEDISK"></a><b>ProfileRemovableDisk</b>

<dd>
<p>Indicates the profile named "Removable disk" by the <i>MMC-3</i> specification. This profile is used with devices that manage rewritable, removable media. </p>
</dd>

### -field <a id="ProfileMOErasable"></a><a id="profilemoerasable"></a><a id="PROFILEMOERASABLE"></a><b>ProfileMOErasable</b>

<dd>
<p>Indicates the profile named "MO Erasable" by the <i>MMC-3</i> specification. This profile is used with devices that manage magneto-optical media and that have a sector-erase capability. </p>
</dd>

### -field <a id="ProfileMOWriteOnce"></a><a id="profilemowriteonce"></a><a id="PROFILEMOWRITEONCE"></a><b>ProfileMOWriteOnce</b>

<dd>
<p>Indicates the profile named "MO Write Once" by the <i>MMC-3</i> specification. This profile is used with devices that manage magneto-optical write-once media.</p>
</dd>

### -field <a id="ProfileAS_MO"></a><a id="profileas_mo"></a><a id="PROFILEAS_MO"></a><b>ProfileAS_MO</b>

<dd>
<p>Indicates the profile named "AS-MO" by the <i>MMC-3</i> specification. This profile is used with devices that implement Advance Storage technology and manage magneto-optical media. </p>
</dd>

### -field <a id="ProfileCdrom"></a><a id="profilecdrom"></a><a id="PROFILECDROM"></a><b>ProfileCdrom</b>

<dd>
<p>Indicates the profile named "CD-ROM" by the <i>MMC-3</i> specification. This profile is used with devices that manage read-only compact disc media.</p>
</dd>

### -field <a id="ProfileCdRecordable"></a><a id="profilecdrecordable"></a><a id="PROFILECDRECORDABLE"></a><b>ProfileCdRecordable</b>

<dd>
<p>Indicates the profile named "CD-R" by the <i>MMC-3</i> specification. This profile is used with devices that manage write-once compact disc media. </p>
</dd>

### -field <a id="ProfileCdRewritable"></a><a id="profilecdrewritable"></a><a id="PROFILECDREWRITABLE"></a><b>ProfileCdRewritable</b>

<dd>
<p>Indicates the profile named "CD-RW" by the <i>MMC-3</i> specification. This profile is used with devices that manage rewritable compact disc media. </p>
</dd>

### -field <a id="ProfileDvdRom"></a><a id="profiledvdrom"></a><a id="PROFILEDVDROM"></a><b>ProfileDvdRom</b>

<dd>
<p>Indicates the profile named "DVD-ROM" by the <i>MMC-3</i> specification. This profile is used with devices that manage read-only DVD media. </p>
</dd>

### -field <a id="ProfileDvdRecordable"></a><a id="profiledvdrecordable"></a><a id="PROFILEDVDRECORDABLE"></a><b>ProfileDvdRecordable</b>

<dd>
<p>Indicates the profile named "DVD-R" by the <i>MMC-3</i> specification. This profile is used with devices that manage write-once DVD media and operate in sequential recording mode. </p>
</dd>

### -field <a id="ProfileDvdRam"></a><a id="profiledvdram"></a><a id="PROFILEDVDRAM"></a><b>ProfileDvdRam</b>

<dd>
<p>Indicates the profile named "DVD-RAM or DVD+RW" by the <i>MMC-3</i> specification. This profile is used with devices that manage rewritable DVD media. </p>
</dd>

### -field <a id="ProfileDvdRewritable"></a><a id="profiledvdrewritable"></a><a id="PROFILEDVDREWRITABLE"></a><b>ProfileDvdRewritable</b>

<dd>
<p>Indicates the profile named "DVD-RW Restricted Overwrite" by the <i>MMC-3</i> specification. This profile is used with devices that manage rerecordable DVD media and operate in packet-writing mode. </p>
</dd>

### -field <a id="ProfileDvdRWSequential"></a><a id="profiledvdrwsequential"></a><a id="PROFILEDVDRWSEQUENTIAL"></a><b>ProfileDvdRWSequential</b>

<dd>
<p>Indicates the profile named "DVD-RW Sequential Recording" by the <i>MMC-3</i> specification. This profile is used with devices that implement a series of features associated with sequential recording, such as the features "Incremental Streaming Writable" and "Real-Time Streaming". For a full list of the features supported with this profile, see the <i>MMC-3</i> specification. </p>
</dd>

### -field <a id="ProfileDvdDashRDualLayer"></a><a id="profiledvddashrduallayer"></a><a id="PROFILEDVDDASHRDUALLAYER"></a><b>ProfileDvdDashRDualLayer</b>

<dd></dd>

### -field <a id="ProfileDvdDashRLayerJump"></a><a id="profiledvddashrlayerjump"></a><a id="PROFILEDVDDASHRLAYERJUMP"></a><b>ProfileDvdDashRLayerJump</b>

<dd>
<p>Reserved 0x0017 - 0x0019</p>
</dd>

### -field <a id="ProfileDvdPlusRW"></a><a id="profiledvdplusrw"></a><a id="PROFILEDVDPLUSRW"></a><b>ProfileDvdPlusRW</b>

<dd>
<p>Indicates the profile named "DVD+RW" by the <i>MMC-3</i> specification. This profile is used with devices that implement a series of features required to manage DVD media that is both readable and writable. For a full list of the features supported with this profile, see the <i>MMC-3</i> specification. </p>
</dd>

### -field <a id="ProfileDvdPlusR"></a><a id="profiledvdplusr"></a><a id="PROFILEDVDPLUSR"></a><b>ProfileDvdPlusR</b>

<dd>
<p>Reserved 0x001C - 001F</p>
</dd>

### -field <a id="ProfileDDCdrom"></a><a id="profileddcdrom"></a><a id="PROFILEDDCDROM"></a><b>ProfileDDCdrom</b>

<dd>
<p>Indicates the profile named "DDCD-ROM" by the <i>MMC-3</i> specification. This profile is used with devices that can read "DDCD specific structure." For a full list of the features supported with this profile, see the <i>MMC-3</i> specification. </p>
</dd>

### -field <a id="ProfileDDCdRecordable"></a><a id="profileddcdrecordable"></a><a id="PROFILEDDCDRECORDABLE"></a><b>ProfileDDCdRecordable</b>

<dd>
<p>Indicates the profile named "DDCD-R" by the <i>MMC-3</i> specification. This profile is used with devices that can read "DDCD-R specific structure." For a full list of the features supported with this profile, see the <i>MMC-3</i> specification. </p>
</dd>

### -field <a id="ProfileDDCdRewritable"></a><a id="profileddcdrewritable"></a><a id="PROFILEDDCDREWRITABLE"></a><b>ProfileDDCdRewritable</b>

<dd>
<p>Indicates the profile named "DDCD-RW" by the <i>MMC-3</i> specification. This profile is used with devices that can read "DDCD-RW specific structure." For a full list of the features supported with this profile, see the <i>MMC-3</i> specification. </p>
</dd>

### -field <a id="ProfileDvdPlusRWDualLayer"></a><a id="profiledvdplusrwduallayer"></a><a id="PROFILEDVDPLUSRWDUALLAYER"></a><b>ProfileDvdPlusRWDualLayer</b>

<dd></dd>

### -field <a id="ProfileDvdPlusRDualLayer"></a><a id="profiledvdplusrduallayer"></a><a id="PROFILEDVDPLUSRDUALLAYER"></a><b>ProfileDvdPlusRDualLayer</b>

<dd>
<p>Reserved 0x002C - 0x003F</p>
</dd>

### -field <a id="ProfileBDRom"></a><a id="profilebdrom"></a><a id="PROFILEBDROM"></a><b>ProfileBDRom</b>

<dd></dd>

### -field <a id="ProfileBDRSequentialWritable"></a><a id="profilebdrsequentialwritable"></a><a id="PROFILEBDRSEQUENTIALWRITABLE"></a><b>ProfileBDRSequentialWritable</b>

<dd>
<p>BD-R 'SRM'</p>
</dd>

### -field <a id="ProfileBDRRandomWritable"></a><a id="profilebdrrandomwritable"></a><a id="PROFILEBDRRANDOMWRITABLE"></a><b>ProfileBDRRandomWritable</b>

<dd>
<p>BD-R 'RRM'</p>
</dd>

### -field <a id="ProfileBDRewritable"></a><a id="profilebdrewritable"></a><a id="PROFILEBDREWRITABLE"></a><b>ProfileBDRewritable</b>

<dd>
<p>Reserved 0x0044 - 0x004F</p>
</dd>

### -field <a id="ProfileHDDVDRom"></a><a id="profilehddvdrom"></a><a id="PROFILEHDDVDROM"></a><b>ProfileHDDVDRom</b>

<dd></dd>

### -field <a id="ProfileHDDVDRecordable"></a><a id="profilehddvdrecordable"></a><a id="PROFILEHDDVDRECORDABLE"></a><b>ProfileHDDVDRecordable</b>

<dd></dd>

### -field <a id="ProfileHDDVDRam"></a><a id="profilehddvdram"></a><a id="PROFILEHDDVDRAM"></a><b>ProfileHDDVDRam</b>

<dd></dd>

### -field <a id="ProfileHDDVDRewritable"></a><a id="profilehddvdrewritable"></a><a id="PROFILEHDDVDREWRITABLE"></a><b>ProfileHDDVDRewritable</b>

<dd>
<p>Reserved 0x0054 - 0x0057</p>
</dd>

### -field <a id="ProfileHDDVDRDualLayer"></a><a id="profilehddvdrduallayer"></a><a id="PROFILEHDDVDRDUALLAYER"></a><b>ProfileHDDVDRDualLayer</b>

<dd>
<p>Reserved 0x0059 - 0x0059</p>
</dd>

### -field <a id="ProfileHDDVDRWDualLayer"></a><a id="profilehddvdrwduallayer"></a><a id="PROFILEHDDVDRWDUALLAYER"></a><b>ProfileHDDVDRWDualLayer</b>

<dd>
<p>Reserved 0x005B - 0xfffe</p>
</dd>

### -field <a id="ProfileNonStandard"></a><a id="profilenonstandard"></a><a id="PROFILENONSTANDARD"></a><b>ProfileNonStandard</b>

<dd>
<p>Indicates that the device does not conform to any profile. </p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553816">FEATURE_DATA_PROFILE_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20FEATURE_PROFILE_TYPE enumeration%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
