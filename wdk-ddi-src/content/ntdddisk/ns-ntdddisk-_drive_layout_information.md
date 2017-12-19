---
UID: NS.NTDDDISK._DRIVE_LAYOUT_INFORMATION
title: _DRIVE_LAYOUT_INFORMATION
author: windows-driver-content
description: The DRIVE_LAYOUT_INFORMATION structure is obsolete and is provided only to support existing drivers.
old-location: storage\drive_layout_information.htm
old-project: storage
ms.assetid: 980cd307-9048-4054-be8e-967d15862a14
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _DRIVE_LAYOUT_INFORMATION, PDRIVE_LAYOUT_INFORMATION, DRIVE_LAYOUT_INFORMATION, *PDRIVE_LAYOUT_INFORMATION
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
req.alt-api: DRIVE_LAYOUT_INFORMATION
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
---

# _DRIVE_LAYOUT_INFORMATION structure



## -description
The DRIVE_LAYOUT_INFORMATION structure is obsolete and is provided only to support existing drivers. New drivers must use <a href="storage.drive_layout_information_ex">DRIVE_LAYOUT_INFORMATION_EX</a>. 

The DRIVE_LAYOUT_INFORMATION structure is used to report information about a disk drive and its partitions. It is also used to write new drive layout information to the disk. 



## -syntax

````
typedef struct _DRIVE_LAYOUT_INFORMATION {
  ULONG                 PartitionCount;
  ULONG                 Signature;
  PARTITION_INFORMATION PartitionEntry[1];
} DRIVE_LAYOUT_INFORMATION, *PDRIVE_LAYOUT_INFORMATION;
````


## -struct-fields

### -field PartitionCount

Contains the number of partitions on the drive. 


### -field Signature

Contains the disk signature.


### -field PartitionEntry

Contains a variable-length array of <a href="storage.partition_information">PARTITION_INFORMATION</a> structures, one for each partition on the drive. 


## -remarks
In Windows 2000 and later operating systems, disk drivers should use structures <a href="storage.drive_layout_information_ex">DRIVE_LAYOUT_INFORMATION_EX</a> and <a href="storage.partition_information_ex">PARTITION_INFORMATION_EX</a> along with routines <b>IoReadPartitionTableEx</b> and <a href="storage.iosetpartitioninformationex">IoSetPartitionInformationEx</a> to read and alter partition information on the disk. 


## -requirements
<table>
<tr>
<th width="30%">
Header

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
<a href="..\ntdddisk\ni-ntdddisk-ioctl_disk_get_partition_info.md">IOCTL_DISK_GET_PARTITION_INFO</a>
</dt>
<dt>
<a href="..\ntdddisk\ni-ntdddisk-ioctl_disk_get_drive_layout.md">IOCTL_DISK_GET_DRIVE_LAYOUT</a>
</dt>
<dt>
<a href="..\ntdddisk\ni-ntdddisk-ioctl_disk_set_drive_layout.md">IOCTL_DISK_SET_DRIVE_LAYOUT</a>
</dt>
<dt>
<a href="storage.ioreadpartitiontable">IoReadPartitionTable</a>
</dt>
<dt>
<a href="storage.ioreadpartitiontableex">IoReadPartitionTableEx</a>
</dt>
<dt>
<a href="storage.iosetpartitioninformation">IoSetPartitionInformation</a>
</dt>
<dt>
<a href="storage.iowritepartitiontable">IoWritePartitionTable</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20DRIVE_LAYOUT_INFORMATION structure%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

