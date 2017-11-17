---
UID: NF.ntddk.IoWritePartitionTableEx
title: IoWritePartitionTableEx
author: windows-driver-content
description: The IoWritePartitionTableEx routine writes partition tables from the entries in the partition list buffer for each partition on the disk represented by the given device object.
old-location: storage\iowritepartitiontableex.htm
ms.assetid: b49ea2db-bb1e-4293-bfac-cbb3e62bca91
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
req.alt-api: IoWritePartitionTableEx
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
ms.keywords: IoWritePartitionTableEx
req.iface: 
---

# IoWritePartitionTableEx function



## -description
<p>The <b>IoWritePartitionTableEx</b> routine writes partition tables from the entries in the partition list buffer for each partition on the disk represented by the given device object.</p>


## -syntax

````
NTSTATUS IoWritePartitionTableEx(
  _In_ PDEVICE_OBJECT                      DeviceObject,
  _In_ struct _DRIVE_LAYOUT_INFORMATION_EX *PartitionBuffer
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the device object representing the disk whose partition tables are to be written.</p>
</dd>

### -param <i>PartitionBuffer</i> [in]

<dd>
<p>Pointer to the drive layout buffer that contains the partition list entries. For more detailed information see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552662">DRIVE_LAYOUT_INFORMATION_EX</a>.</p>
</dd>
</dl>

## -returns
<p><b>IoWritePartitionTabloEx</b> returns a status code of STATUS_SUCCESS if all writes were completed without error. In case of failure, the error codes returned by <b>IoWritePartitionTableEx</b> might include, but are not limited to, the following list:</p><dl>
<dt><b>STATUS_DEVICE_NOT_READY</b></dt>
</dl><p>Indicates a failure read the correct disk geometry.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Indicates a failure to allocate necessary resources (for example, heap memory, IRPs, and so on).</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>Indicates that sector zero did not have the expected MBR disk signature.</p>

<p> </p>

## -remarks
<p><b>IoWritePartitionTableEx</b> replaces the obsolete routine <a href="https://msdn.microsoft.com/library/windows/hardware/ff561464">IoWritePartitionTable</a>. Unlike the older routine, it can write to GUID Partition Tables as well as Master Boot Record Partition Tables. </p>

<p><b>IoWritePartitionTableEx</b> must only be used by disk drivers. Other drivers should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560411">IOCTL_DISK_SET_DRIVE_LAYOUT_EX</a> disk I/O request instead.</p>

<p>When a disk device driver receives an IRP_MJ_DEVICE_CONTROL request to set the partition type in a partition table entry, or to repartition the disk, it should call <b>IoWritePartionTableEx</b>. The device control request is generally issued by the format utility, which performs I/O control functions on the partitions and disks in the machine.</p>

<p>To reset a partition type, the driver passes a pointer to the device object, representing the physical disk, and the number of the partition associated with the device object that the format utility has open. When a disk is to be repartitioned dynamically, the disk driver must tear down its set of device objects representing the current disk partitions and create a new set of device objects representing the new partitions on the disk.</p>

<p>In order tot create or delete partitions a full description of the system must be obtained by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff561454">IoReadPartitionTableEx</a>. The drive layout structure can be modified by the system format utility to reflect a new configuration of the disk.</p>

<p><b>IoWritePartitionTableEx</b> is synchronous. It must be called by the disk driver's Dispatch routine or by a driver thread. Thus, all user and file system threads must be prepared to enter a wait state when issuing the device control request to reset partition types for the device.</p>

<p><b>IoWritePartitionTableEx</b> replaces the obsolete routine <a href="https://msdn.microsoft.com/library/windows/hardware/ff561464">IoWritePartitionTable</a>. Unlike the older routine, it can write to GUID Partition Tables as well as Master Boot Record Partition Tables. </p>

<p><b>IoWritePartitionTableEx</b> must only be used by disk drivers. Other drivers should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560411">IOCTL_DISK_SET_DRIVE_LAYOUT_EX</a> disk I/O request instead.</p>

<p>When a disk device driver receives an IRP_MJ_DEVICE_CONTROL request to set the partition type in a partition table entry, or to repartition the disk, it should call <b>IoWritePartionTableEx</b>. The device control request is generally issued by the format utility, which performs I/O control functions on the partitions and disks in the machine.</p>

<p>To reset a partition type, the driver passes a pointer to the device object, representing the physical disk, and the number of the partition associated with the device object that the format utility has open. When a disk is to be repartitioned dynamically, the disk driver must tear down its set of device objects representing the current disk partitions and create a new set of device objects representing the new partitions on the disk.</p>

<p>In order tot create or delete partitions a full description of the system must be obtained by a call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff561454">IoReadPartitionTableEx</a>. The drive layout structure can be modified by the system format utility to reflect a new configuration of the disk.</p>

<p><b>IoWritePartitionTableEx</b> is synchronous. It must be called by the disk driver's Dispatch routine or by a driver thread. Thus, all user and file system threads must be prepared to enter a wait state when issuing the device control request to reset partition types for the device.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548397">IoCreateDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561454">IoReadPartitionTableEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561461">IoSetPartitionInformationEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20IoWritePartitionTableEx routine%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
