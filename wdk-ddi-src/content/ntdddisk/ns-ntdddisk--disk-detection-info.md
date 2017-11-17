---
UID: NS.ntdddisk._DISK_DETECTION_INFO
title: DISK_DETECTION_INFO
author: windows-driver-content
description: The DISK_DETECTION_INFO structure contains the detected drive parameters that are supplied by an x86 PC BIOS on boot.
old-location: storage\disk_detection_info.htm
ms.assetid: 67a508cf-79c4-4c86-9ad3-fa7cca99cf5f
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntdddisk.h
req.include-header: Ntdddisk.h, Ntddk.h, Ntdddisk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DISK_DETECTION_INFO
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
ms.keywords: DISK_DETECTION_INFO, DISK_DETECTION_INFO, *PDISK_DETECTION_INFO
req.iface: 
---

# DISK_DETECTION_INFO structure



## -description
<p>The DISK_DETECTION_INFO structure contains the detected drive parameters that are supplied by an x86 PC BIOS on boot.</p>


## -syntax

````
typedef struct _DISK_DETECTION_INFO {
  ULONG          SizeOfDetectInfo;
  DETECTION_TYPE DetectionType;
  union {
    struct {
      DISK_INT13_INFO    Int13;
      DISK_EX_INT13_INFO ExInt13;
    };
  };
} DISK_DETECTION_INFO, *PDISK_DETECTION_INFO;
````


## -struct-fields
<dl>

### -field <b>SizeOfDetectInfo</b>

<dd>
<p>Contains the quantity, in bytes, of retrieved detect information.</p>
</dd>

### -field <b>DetectionType</b>

<dd>
<p>Indicates one of three possible detection types:</p>
<ol>
<li>
<p><b>DetectNone</b></p>
</li>
<li>
<p><b>DetectInt13</b></p>
</li>
<li>
<p><b>DetectExInt13</b></p>
</li>
</ol>
<p>See the structure <a href="https://msdn.microsoft.com/library/windows/hardware/ff552516">DETECTION_TYPE</a> for further information.</p>
</dd>

### -field ( <i>unnamed struct</i> )

<dd>
<p>Contains the quantity, in bytes, of retrieved detect information.</p>
<dl>

### -field <b>Int13</b>

<dd>
<p>Contains <a href="https://msdn.microsoft.com/library/windows/hardware/ff552624">DISK_INT13_INFO</a> structure with the disk parameters for INT 13 type partitions. This member is used if <b>DetectionType </b>== <b>DetectInt13</b>.</p>
</dd>

### -field <b>ExInt13</b>

<dd>
<p>Contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552610">DISK_EX_INT13_INFO</a> structure with the disk parameters for extended INT 13 type partitions. This member is used if <b>DetectionType</b> == <b>DetectExInt13</b>.</p>
</dd>
</dl>
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
<dt>Ntdddisk.h (include Ntdddisk.h, Ntddk.h, or Ntdddisk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552618">DISK_GEOMETRY_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552624">DISK_INT13_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552610">DISK_EX_INT13_INFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20DISK_DETECTION_INFO structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
