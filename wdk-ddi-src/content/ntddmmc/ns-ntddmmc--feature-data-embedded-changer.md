---
UID: NS.ntddmmc._FEATURE_DATA_EMBEDDED_CHANGER
title: FEATURE_DATA_EMBEDDED_CHANGER
author: windows-driver-content
description: The FEATURE_DATA_EMBEDDED_CHANGER structure holds data for the Embedded Changer feature.
old-location: storage\feature_data_embedded_changer.htm
old-project: storage
ms.assetid: 1335d1fa-af96-4a31-a1cf-266f7a3325ef
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: FEATURE_DATA_EMBEDDED_CHANGER, FEATURE_DATA_EMBEDDED_CHANGER, *PFEATURE_DATA_EMBEDDED_CHANGER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddmmc.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FEATURE_DATA_EMBEDDED_CHANGER
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

# FEATURE_DATA_EMBEDDED_CHANGER structure



## -description
<p>The FEATURE_DATA_EMBEDDED_CHANGER structure holds data for the Embedded Changer feature. </p>


## -syntax

````
typedef struct _FEATURE_DATA_EMBEDDED_CHANGER {
  FEATURE_HEADER Header;
  UCHAR          Reserved1  :2;
  UCHAR          SupportsDiscPresent  :1;
  UCHAR          Reserved2  :1;
  UCHAR          SideChangeCapable  :1;
  UCHAR          Reserved3  :3;
  UCHAR          Reserved4[2];
  UCHAR          HighestSlotNumber  :5;
  UCHAR          Reserved  :3;
} FEATURE_DATA_EMBEDDED_CHANGER, *PFEATURE_DATA_EMBEDDED_CHANGER;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>Contains a <a href="..\ntddmmc\ns-ntddmmc--feature-header.md">FEATURE_HEADER</a> structure with header information for this feature descriptor. </p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>SupportsDiscPresent</b>

<dd>
<p>Indicates, when set to 1, that the device can report the contents of the slots after a reset or magazine change. When set to zero, this bit indicates that the device can report the contents of the slots after reset or magazine change. </p>
</dd>

### -field <b>Reserved2</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>SideChangeCapable</b>

<dd>
<p>Indicates, when set to 1, that the device is capable of selecting both sides of the media. When set to zero, this bit indicates that the device is not capable of selecting both sides of the media. </p>
</dd>

### -field <b>Reserved3</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserved4</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>HighestSlotNumber</b>

<dd>
<p>Indicates the number of slots minus 1. </p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>

## -remarks
<p>This structure holds data for the feature named "Embedded Changer" by the <i>SCSI Multimedia - 4 (MMC-4) </i>specification. Devices that support this feature can move media back and forth between a media storage area and the mechanism that actually accesses the media.</p>

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
<dt>
<a href="..\ntddmmc\ne-ntddmmc--feature-number.md">FEATURE_NUMBER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20FEATURE_DATA_EMBEDDED_CHANGER structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
