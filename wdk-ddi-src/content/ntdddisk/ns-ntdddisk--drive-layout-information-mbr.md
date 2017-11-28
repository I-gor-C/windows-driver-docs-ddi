---
UID: NS.ntdddisk._DRIVE_LAYOUT_INFORMATION_MBR
title: DRIVE_LAYOUT_INFORMATION_MBR
author: windows-driver-content
description: The DRIVE_LAYOUT_INFORMATION_MBR structure reports the drive signature for a Master Boot Record partition.
old-location: storage\drive_layout_information_mbr.htm
old-project: storage
ms.assetid: 41df2847-7cfa-4746-82bd-d0b8b482a0d4
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DRIVE_LAYOUT_INFORMATION_MBR, DRIVE_LAYOUT_INFORMATION_MBR, *PDRIVE_LAYOUT_INFORMATION_MBR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntdddisk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DRIVE_LAYOUT_INFORMATION_MBR
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

# DRIVE_LAYOUT_INFORMATION_MBR structure



## -description
<p>The DRIVE_LAYOUT_INFORMATION_MBR structure reports the drive signature for a Master Boot Record partition. </p>


## -syntax

````
typedef struct _DRIVE_LAYOUT_INFORMATION_MBR {
  ULONG Signature;
} DRIVE_LAYOUT_INFORMATION_MBR, *PDRIVE_LAYOUT_INFORMATION_MBR;
````


## -struct-fields
<dl>

### -field <b>Signature</b>

<dd>
<p>Specifies the disk signature value, which uniquely identifies the disk. </p>
</dd>
</dl>

## -remarks
<p>This structure contains the drive layout information that is specific to a drive with a Master Boot Record partition. It is contained within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552662">DRIVE_LAYOUT_INFORMATION_EX</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntdddisk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552662">DRIVE_LAYOUT_INFORMATION_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561452">IoReadPartitionTable</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561464">IoWritePartitionTable</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20DRIVE_LAYOUT_INFORMATION_MBR structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
