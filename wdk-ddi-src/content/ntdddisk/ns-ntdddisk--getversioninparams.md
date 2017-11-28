---
UID: NS.ntdddisk._GETVERSIONINPARAMS
title: GETVERSIONINPARAMS
author: windows-driver-content
description: The GETVERSIONINPARAMS structure is used in conjunction with the SMART_GET_VERSION request to retrieve version information, a capabilities mask, and a bitmask for the indicated device.
old-location: storage\getversioninparams.htm
old-project: storage
ms.assetid: dcbfa8d2-c2ea-43ae-9d77-ce95a430a514
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: GETVERSIONINPARAMS, GETVERSIONINPARAMS, *PGETVERSIONINPARAMS, *LPGETVERSIONINPARAMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntdddisk.h
req.include-header: Ntdddisk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GETVERSIONINPARAMS
req.alt-loc: ntdddisk.h
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
req.iface: 
---

# GETVERSIONINPARAMS structure



## -description
<p>The GETVERSIONINPARAMS structure is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566202">SMART_GET_VERSION</a> request to retrieve version information, a capabilities mask, and a bitmask for the indicated device. </p>


## -syntax

````
typedef struct _GETVERSIONINPARAMS {
  UCHAR bVersion;
  UCHAR bRevision;
  UCHAR bReserved;
  UCHAR bIDEDeviceMap;
  ULONG fCapabilities;
  ULONG dwReserved[4];
} GETVERSIONINPARAMS, *PGETVERSIONINPARAMS, *LPGETVERSIONINPARAMS;
````


## -struct-fields
<dl>

### -field <b>bVersion</b>

<dd>
<p>Contains an integer that indicates the version number of the binary driver. </p>
</dd>

### -field <b>bRevision</b>

<dd>
<p>Contains an integer that indicates the revision number of the binary driver. </p>
</dd>

### -field <b>bReserved</b>

<dd>
<p>Reserved. </p>
</dd>

### -field <b>bIDEDeviceMap</b>

<dd>
<p>Contains the bitmap. The following table explains the meaning of the bitmap:</p>
<table>
<tr>
<th>Bitmap Flags</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>Bit 0 is set to 1.</p>
</td>
<td>
<p>The device is either a SATA drive or an IDE drive. If it is an IDE drive, it is the master device on the primary channel. </p>
</td>
</tr>
<tr>
<td>
<p>Bit 1 is set to 1.</p>
</td>
<td>
<p>The device is an IDE drive, and it is the subordinate device on the primary channel. </p>
</td>
</tr>
<tr>
<td>
<p>Bit 2 is set to 1.</p>
</td>
<td>
<p>The device is an IDE drive, and it is the master device on the secondary channel. </p>
</td>
</tr>
<tr>
<td>
<p>Bit 3 is set to 1.</p>
</td>
<td>
<p>The device is an IDE drive, and it is the subordinate device on the secondary channel. </p>
</td>
</tr>
<tr>
<td>
<p>Bit 4 is set to 1.</p>
</td>
<td>
<p>The device is an ATAPI drive, and it is the master device on the primary channel. </p>
</td>
</tr>
<tr>
<td>
<p>Bit 5 is set to 1.</p>
</td>
<td>
<p>The device is an ATAPI drive, and it is the subordinate device on the primary channel. </p>
</td>
</tr>
<tr>
<td>
<p>Bit 6 is set to 1.</p>
</td>
<td>
<p>The device is an ATAPI drive, and it is the master device on the secondary channel. </p>
</td>
</tr>
<tr>
<td>
<p>Bit 7 is set to 1.</p>
</td>
<td>
<p>The device is an ATAPI drive, and it is the subordinate device on the secondary channel. </p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>fCapabilities</b>

<dd>
<p>Contains the bitmask of driver capabilities. </p>
<table>
<tr>
<th>Bitmask Flags</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>CAP_ATA_ID_CMD</p>
</td>
<td>
<p>The device supports the ATA ID command. </p>
</td>
</tr>
<tr>
<td>
<p>CAP_ATAPI_ID_CMD</p>
</td>
<td>
<p>The device supports the ATAPI ID command. </p>
</td>
</tr>
<tr>
<td>
<p>CAP_SMART_CMD</p>
</td>
<td>
<p>The device supports SMART commands.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>dwReserved</b>

<dd>
<p>Reserved. </p>
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
<dt>Ntdddisk.h (include Ntdddisk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566202">SMART_GET_VERSION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20GETVERSIONINPARAMS structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
