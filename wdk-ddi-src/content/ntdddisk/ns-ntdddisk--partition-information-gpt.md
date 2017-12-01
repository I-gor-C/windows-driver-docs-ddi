---
UID: NS.ntdddisk._PARTITION_INFORMATION_GPT
title: PARTITION_INFORMATION_GPT
author: windows-driver-content
description: PARTITION_INFORMATION_GPT contains information for a GUID Partition Table partition that is not held in common with a Master Boot Record partition.
old-location: storage\partition_information_gpt.htm
old-project: storage
ms.assetid: f2d76b4c-7acd-4701-b978-3d29dc8cde0b
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PARTITION_INFORMATION_GPT, PARTITION_INFORMATION_GPT, *PPARTITION_INFORMATION_GPT
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
req.alt-api: PARTITION_INFORMATION_GPT
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

# PARTITION_INFORMATION_GPT structure



## -description
<p>PARTITION_INFORMATION_GPT contains information for a GUID Partition Table partition that is not held in common with a Master Boot Record partition.</p>


## -syntax

````
typedef struct _PARTITION_INFORMATION_GPT {
  GUID    PartitionType;
  GUID    PartitionId;
  ULONG64 Attributes;
  WCHAR   Name[36];
} PARTITION_INFORMATION_GPT, *PPARTITION_INFORMATION_GPT;
````


## -struct-fields
<dl>

### -field <b>PartitionType</b>

<dd>
<p>Specifies a GUID that uniquely identifies the partition type. The GUID data type is described on the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565392">Using GUIDs in Drivers</a> reference page. </p>
</dd>

### -field <b>PartitionId</b>

<dd>
<p>Specifies a GUID that uniquely identifies the partition. The GUID data type is described on the <a href="https://msdn.microsoft.com/library/windows/hardware/ff565392">Using GUIDs in Drivers</a> reference page. </p>
</dd>

### -field <b>Attributes</b>

<dd>
<p>Specifies the partition entry attributes used for diagnostics, recovery tools, and other firmware essential to the operation of the device. See Intel's <i>Extensible Firmware Interface</i> specification for further information.</p>
</dd>

### -field <b>Name</b>

<dd>
<p>Specifies the partition name in Unicode.</p>
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
<a href="..\ntdddisk\ns-ntdddisk--partition-information-ex.md">PARTITION_INFORMATION_EX</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-ioreadpartitiontableex.md">IoReadPartitionTableEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20PARTITION_INFORMATION_GPT structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
