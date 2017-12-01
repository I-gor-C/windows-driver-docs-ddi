---
UID: NF.ntddk.IoSetPartitionInformation
title: IoSetPartitionInformation
author: windows-driver-content
description: The IoSetPartitionInformation routine is obsolete and is provided only to support existing drivers.
old-location: storage\iosetpartitioninformation.htm
old-project: storage
ms.assetid: 3f1a6e3f-3bbc-4cc5-8efe-e3cf6ac3adf5
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IoSetPartitionInformation
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoSetPartitionInformation
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL (See Remarks section)
req.iface: 
---

# IoSetPartitionInformation function



## -description
<p>The <b>IoSetPartitionInformation</b> routine is <b>obsolete</b> and is provided only to support existing drivers. New drivers must use <a href="..\ntddk\nf-ntddk-iosetpartitioninformationex.md">IoSetPartitionInformationEx</a>. </p>
<p><b>IoSetPartitionInformation</b> sets the partition type and number in a partition table entry for the disk represented by <i>DeviceObject</i>.</p>


## -syntax

````
NTSTATUS FASTCALL IoSetPartitionInformation(
  _In_ PDEVICE_OBJECT DeviceObject,
  _In_ ULONG          SectorSize,
  _In_ ULONG          PartitionNumber,
  _In_ ULONG          PartitionType
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the device object representing the device on which the partition type is to be set.</p>
</dd>

### -param <i>SectorSize</i> [in]

<dd>
<p>Specifies the size, in bytes, of sectors on the disk.</p>
</dd>

### -param <i>PartitionNumber</i> [in]

<dd>
<p>Specifies the partition number on the device whose partition type is to be set.</p>
</dd>

### -param <i>PartitionType</i> [in]

<dd>
<p>Specifies the type for the partition. For a list of some of the key partition types see <a href="..\ntdddisk\ns-ntdddisk--partition-information.md">PARTITION_INFORMATION</a>. </p>
</dd>
</dl>

## -returns
<p>If <b>IoSetPartitionInformation</b> returns STATUS_SUCCESS, the disk driver updates its notion of the partition type for this partition in its device extension.</p>

## -remarks
<p><b>IoSetPartitionInformation</b> must only be used by disk drivers. Other drivers should use the <a href="..\ntdddisk\ni-ntdddisk-ioctl-disk-set-partition-info.md">IOCTL_DISK_SET_PARTITION_INFO</a> disk I/O request instead.</p>

<p>This routine is called when a disk device driver is asked to set the partition type in a partition table entry by an IRP_MJ_DEVICE_CONTROL request. This request is generally issued by the format utility, which performs I/O control functions on the partition. The driver passes a pointer to the device object representing the physical disk and the number of the partition associated with the device object that the format utility has open. Since the HAL routines that underlie <b>IoSetPartitionInformation</b> were developed before support of dynamic partitioning was implemented, they do not distinguish between the <i>partition ordinal</i> (that is the order of a partition on a disk) and the <i>partition number</i> (the partition number assigned to a partition in order to identify it to the system). Drivers must call <b>IoSetPartitionInformation</b> using the <i>ordinal</i> number of the partition and not the actual partition number.</p>

<p>This routine is synchronous and must be called by the disk driver's Dispatch routine or by a driver thread. Thus, all user and file system threads must be prepared to enter a wait state when issuing the device control request to set the partition type for the device.</p>

<p>This routine operates under the assumption that the partition number passed in by the disk driver actually exists.</p>

<p>This routine must be called at IRQL = PASSIVE_LEVEL because it uses a kernel event object to synchronize I/O completion on the device. The event cannot be set to the Signaled state without queuing and executing the I/O system's special kernel APC routine for I/O completion.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL (See Remarks section)</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddk\nf-ntddk-ioreadpartitiontable.md">IoReadPartitionTable</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-iowritepartitiontable.md">IoWritePartitionTable</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-iosetpartitioninformationex.md">IoSetPartitionInformationEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IoSetPartitionInformation routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
