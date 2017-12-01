---
UID: NS.ntdddisk._SET_PARTITION_INFORMATION
title: SET_PARTITION_INFORMATION
author: windows-driver-content
description: SET_PARTITION_INFORMATION is used with IOCTL_DISK_SET_PARTITION_INFO to change the partition type of a specified Master Boot Record (MBR) disk partition.
old-location: storage\set_partition_information.htm
old-project: storage
ms.assetid: 882aedda-5ed5-43e0-a370-59a7c7e4c802
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SET_PARTITION_INFORMATION, SET_PARTITION_INFORMATION, *PSET_PARTITION_INFORMATION
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
req.alt-api: SET_PARTITION_INFORMATION
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

# SET_PARTITION_INFORMATION structure



## -description
<p>SET_PARTITION_INFORMATION is used with IOCTL_DISK_SET_PARTITION_INFO to change the partition type of a specified Master Boot Record (MBR) disk partition.</p>


## -syntax

````
typedef struct _SET_PARTITION_INFORMATION {
  UCHAR PartitionType;
} SET_PARTITION_INFORMATION, *PSET_PARTITION_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>PartitionType</b>

<dd>
<p>Indicates the partition type. IOCTL_DISK_SET_PARTITION_INFO uses this value to set the partition type. See <a href="..\ntdddisk\ns-ntdddisk--partition-information.md">PARTITION_INFORMATION</a> for a list of system-defined GPT partition types.</p>
</dd>
</dl>

## -remarks
<p>The single byte unsigned value, <i>PartitionType</i>, contained in this structure defines a traditional AT Master Boot Record style of partition and cannot be used to define an Extensible Firmware Interface partition (also known as a GUID Partition Table partition). GPT partitions use a GUID to indicate the partition type.</p>

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
<a href="..\ntdddisk\ns-ntdddisk--set-partition-information-ex.md">SET_PARTITION_INFORMATION_EX</a>
</dt>
<dt>
<a href="storage.set_partition_information_mbr">SET_PARTITION_INFORMATION_MBR</a>
</dt>
<dt>
<a href="storage.set_partition_information_gpt">SET_PARTITION_INFORMATION_GPT</a>
</dt>
<dt>
<a href="..\ntdddisk\ni-ntdddisk-ioctl-disk-set-partition-info.md">IOCTL_DISK_SET_PARTITION_INFO</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-ioreadpartitiontable.md">IoReadPartitionTable</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20SET_PARTITION_INFORMATION structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
