---
UID: NF.ntddk.IoReadPartitionTable
title: IoReadPartitionTable
author: windows-driver-content
description: The IoReadPartitionTable routine is obsolete and is provided only to support existing drivers.
old-location: storage\ioreadpartitiontable.htm
ms.assetid: f87c74c3-fcb1-4358-ade6-6c0afc0020e2
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoReadPartitionTable
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
req.irql: PASSIVE_LEVEL
ms.keywords: IoReadPartitionTable
req.iface: 
---

# IoReadPartitionTable function



## -description
<p>The <b>IoReadPartitionTable</b> routine is <b>obsolete</b> and is provided only to support existing drivers. New drivers must use <a href="https://msdn.microsoft.com/library/windows/hardware/ff561454">IoReadPartitionTableEx</a>. <b>IoReadPartitionTable</b> reads a list of partitions on a disk having a specified sector size and creates an entry in the partition list for each recognized partition. </p>


## -syntax

````
NTSTATUS FASTCALL IoReadPartitionTable(
  _In_  PDEVICE_OBJECT                   DeviceObject,
  _In_  ULONG                            SectorSize,
  _In_  BOOLEAN                          ReturnRecognizedPartitions,
  _Out_ struct _DRIVE_LAYOUT_INFORMATION **PartitionBuffer
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the device object for the disk whose partitions are to be read.</p>
</dd>

### -param <i>SectorSize</i> [in]

<dd>
<p>Specifies the size of the sectors on the disk.</p>
</dd>

### -param <i>ReturnRecognizedPartitions</i> [in]

<dd>
<p>Indicates whether only recognized partitions or all partition entries should be returned.</p>
</dd>

### -param <i>PartitionBuffer</i> [out]

<dd>
<p>Pointer to an uninitialized address. If successful, <b>IoReadPartitionTable</b> allocates the memory for this buffer from nonpaged pool and returns the drive layout information in it.</p>
</dd>
</dl>

## -returns
<p>This routine returns a value of STATUS_SUCCESS if at least one sector table was read. Otherwise, it returns an error status and sets the pointer at <i>PartitionBuffer</i> to <b>NULL</b>.</p>

## -remarks
<p><b>IoReadPartitionTable</b> must only be used by disk drivers. Other drivers should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560361">IOCTL_DISK_GET_DRIVE_LAYOUT</a> disk I/O request instead.</p>

<p>Disk device drivers call this routine during driver initialization.</p>

<p>It is the responsibility of the caller to deallocate the <i>PartitionBuffer</i> that was allocated by this routine with <b>ExFreePool</b>.</p>

<p>The algorithm used by this routine is determined by the Boolean value <i>ReturnRecognizedPartitions</i>:</p>

<p>Read each partition table and, for each valid and recognized partition found, fill in an element in an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff563751">PARTITION_INFORMATION</a> entries. The array of partition information entries is pointed to by the <b>PartitionEntry</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552659">DRIVE_LAYOUT_INFORMATION</a> structure. The DRIVE_LAYOUT_INFORMATION structure is found at the location pointed to by <i>PartitionBuffer</i>. Extended partitions are located in order to find other partition tables, but no entries are built for them.</p>

<p>Read each partition table and, for each and every entry, fill in a partition information entry. Extended partitions are located to find each partition on the disk; entries are built for these as well.</p>

<p><b>IoReadPartitionTable</b> must only be used by disk drivers. Other drivers should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560361">IOCTL_DISK_GET_DRIVE_LAYOUT</a> disk I/O request instead.</p>

<p>Disk device drivers call this routine during driver initialization.</p>

<p>It is the responsibility of the caller to deallocate the <i>PartitionBuffer</i> that was allocated by this routine with <b>ExFreePool</b>.</p>

<p>The algorithm used by this routine is determined by the Boolean value <i>ReturnRecognizedPartitions</i>:</p>

<p>Read each partition table and, for each valid and recognized partition found, fill in an element in an array of <a href="https://msdn.microsoft.com/library/windows/hardware/ff563751">PARTITION_INFORMATION</a> entries. The array of partition information entries is pointed to by the <b>PartitionEntry</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552659">DRIVE_LAYOUT_INFORMATION</a> structure. The DRIVE_LAYOUT_INFORMATION structure is found at the location pointed to by <i>PartitionBuffer</i>. Extended partitions are located in order to find other partition tables, but no entries are built for them.</p>

<p>Read each partition table and, for each and every entry, fill in a partition information entry. Extended partitions are located to find each partition on the disk; entries are built for these as well.</p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560373">IOCTL_DISK_GET_PARTITION_INFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560361">IOCTL_DISK_GET_DRIVE_LAYOUT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560408">IOCTL_DISK_SET_DRIVE_LAYOUT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561456">IoSetPartitionInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561464">IoWritePartitionTable</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20IoReadPartitionTable routine%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
