---
UID: NE.ntdddisk._DETECTION_TYPE
title: DETECTION_TYPE
author: windows-driver-content
description: The DETECTION_TYPE enumeration type is used in conjunction with the IOCTL_DISK_GET_DRIVE_GEOMETRY_EX request and the DISK_GEOMETRY_EX structure to determine the type of formatting used by the BIOS to record the disk geometry.
old-location: storage\detection_type.htm
old-project: storage
ms.assetid: 3257a207-dd7e-4321-b037-95d62cea6f76
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: READ_ELEMENT_ADDRESS_INFO, READ_ELEMENT_ADDRESS_INFO, *PREAD_ELEMENT_ADDRESS_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntdddisk.h
req.include-header: Ntdddisk.h, Ntddk.h, Ntdddisk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DETECTION_TYPE
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

# DETECTION_TYPE enumeration



## -description
<p>The DETECTION_TYPE enumeration type is used in conjunction with the <a href="..\ntdddisk\ni-ntdddisk-ioctl-disk-get-drive-geometry-ex.md">IOCTL_DISK_GET_DRIVE_GEOMETRY_EX</a> request and the <a href="..\ntdddisk\ns-ntdddisk--disk-geometry-ex.md">DISK_GEOMETRY_EX</a> structure to determine the type of formatting used by the BIOS to record the disk geometry. </p>


## -syntax

````
typedef enum _DETECTION_TYPE { 
  DetectNone     = 0,
  DetectInt13    = 1,
  DetectExInt13  = 2
} DETECTION_TYPE;
````


## -enum-fields
<dl>

### -field <a id="DetectNone"></a><a id="detectnone"></a><a id="DETECTNONE"></a><b>DetectNone</b>

<dd>
<p>Indicates that the disk contains neither an INT 13h partition nor an extended INT 13h partition.</p>
</dd>

### -field <a id="DetectInt13"></a><a id="detectint13"></a><a id="DETECTINT13"></a><b>DetectInt13</b>

<dd>
<p>Indicates that the disk has a standard INT 13h partition.</p>
</dd>

### -field <a id="DetectExInt13"></a><a id="detectexint13"></a><a id="DETECTEXINT13"></a><b>DetectExInt13</b>

<dd>
<p>Indicates that the disk contains an extended INT 13h partition. </p>
</dd>
</dl>

## -remarks
<p>Possible formatting types are the standard INT 13h partition format or the extended INT 13h partition format. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntdddisk.h (include Ntdddisk.h, Ntddk.h, or Ntdddisk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntdddisk\ns-ntdddisk--disk-detection-info.md">DISK_DETECTION_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20DETECTION_TYPE enumeration%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
