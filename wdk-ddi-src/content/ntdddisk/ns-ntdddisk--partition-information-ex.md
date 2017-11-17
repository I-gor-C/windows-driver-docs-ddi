---
UID: NS.ntdddisk._PARTITION_INFORMATION_EX
title: PARTITION_INFORMATION_EX
author: windows-driver-content
description: PARTITION_INFORMATION_EX is the extended version of the PARTITION_INFORMATION structure. It holds information both for partitions with a Master Boot Record and for partitions with a GUID Partition Table.
old-location: storage\partition_information_ex.htm
ms.assetid: de44fe5a-5d47-4b2e-ab94-52cadfdbc345
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntdddisk.h
req.include-header: Ntdddisk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PARTITION_INFORMATION_EX
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
ms.keywords: PARTITION_INFORMATION_EX, PARTITION_INFORMATION_EX, *PPARTITION_INFORMATION_EX
req.iface: 
---

# PARTITION_INFORMATION_EX structure



## -description
<p>PARTITION_INFORMATION_EX is the extended version of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563751">PARTITION_INFORMATION</a> structure. It holds information both for partitions with a Master Boot Record and for partitions with a GUID Partition Table.</p>


## -syntax

````
typedef struct _PARTITION_INFORMATION_EX {
  PARTITION_STYLE PartitionStyle;
  LARGE_INTEGER   StartingOffset;
  LARGE_INTEGER   PartitionLength;
  ULONG           PartitionNumber;
  BOOLEAN         RewritePartition;
  union {
    PARTITION_INFORMATION_MBR Mbr;
    PARTITION_INFORMATION_GPT Gpt;
  };
} PARTITION_INFORMATION_EX, *PPARTITION_INFORMATION_EX;
````


## -struct-fields
<dl>

### -field <b>PartitionStyle</b>

<dd>
<p>Takes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563773">PARTITION_STYLE</a> enumerated value that specifies the type of partition table that contains the partition.</p>
</dd>

### -field <b>StartingOffset</b>

<dd>
<p>Specifies the offset in bytes on drive where the partition begins.</p>
</dd>

### -field <b>PartitionLength</b>

<dd>
<p>Specifies the length in bytes of the partition.</p>
</dd>

### -field <b>PartitionNumber</b>

<dd>
<p>Specifies the number of the partition.</p>
</dd>

### -field <b>RewritePartition</b>

<dd>
<p>Indicates, when <b>TRUE</b>, that the partition information has changed. When <b>FALSE</b>, the information has not changed. This member has a value of <b>TRUE</b> when the partition has changed as a result of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff560408">IOCTL_DISK_SET_DRIVE_LAYOUT</a> IOCTL. This informs the system that the partition information needs to be rewritten.</p>
</dd>

### -field <b>Mbr</b>

<dd>
<p>Contains a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff563767">PARTITION_INFORMATION_MBR</a> containing information specific to a partition with a <b>PartitionStyle</b> member of PARTITION_STYLE_MBR.</p>
</dd>

### -field <b>Gpt</b>

<dd>
<p>Contains a structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff563763">PARTITION_INFORMATION_GPT</a> containing information specific to a partition with a <b>PartitionStyle</b> member of PARTITION_STYLE_GPT.</p>
</dd>
</dl>

## -remarks
<p>This is the extended version of the partition information structure, PARTITION_INFORMATION. <a href="https://msdn.microsoft.com/library/windows/hardware/ff561454">IoReadPartitionTableEx</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff561470">IoWritePartitionTableEx</a> operate on an array of PARTITON_INFORMATION_EX structures contained within the extended drive layout structure, <a href="https://msdn.microsoft.com/library/windows/hardware/ff552662">DRIVE_LAYOUT_INFORMATION_EX</a>. PARTITION_INFORMATION_EX replaces the structure PARTITION_INFORMATION that was used with <a href="https://msdn.microsoft.com/library/windows/hardware/ff561452">IoReadPartitionTable</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff561464">IoWritePartitionTable</a>. The principal difference is that the new structures and routines support both Master Boot Record (MBR) partitions and GUID Partition Table (GPT) partitions, whereas the older routines and structures are only used with MBR partitions.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563767">PARTITION_INFORMATION_MBR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563763">PARTITION_INFORMATION_GPT</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20PARTITION_INFORMATION_EX structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
