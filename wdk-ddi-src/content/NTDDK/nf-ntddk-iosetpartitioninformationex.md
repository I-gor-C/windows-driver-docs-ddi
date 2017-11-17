---
UID: NF.ntddk.IoSetPartitionInformationEx
title: IoSetPartitionInformationEx
author: windows-driver-content
description: For the disk represented by DeviceObject, the IoSetPartitionInformationEx routine initializes a partition table entry with the information specified in the SET_PARTITION_INFORMATION_EX structure.
old-location: storage\iosetpartitioninformationex.htm
ms.assetid: e663a9aa-ed83-4d85-b110-390f0c03a724
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
req.alt-api: IoSetPartitionInformationEx
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
ms.keywords: IoSetPartitionInformationEx
req.iface: 
---

# IoSetPartitionInformationEx function



## -description
<p>For the disk represented by <i>DeviceObject</i>, the <b>IoSetPartitionInformationEx</b> routine initializes a partition table entry with the information specified in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff566194">SET_PARTITION_INFORMATION_EX</a> structure.</p>


## -syntax

````
NTSTATUS IoSetPartitionInformationEx(
  _In_ PDEVICE_OBJECT                       DeviceObject,
  _In_ ULONG                                PartitionNumber,
  _In_ struct _SET_PARTITION_INFORMATION_EX *PartitionInfo
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the device object representing the device on which the partition type is to be set.</p>
</dd>

### -param <i>PartitionNumber</i> [in]

<dd>
<p>Specifies the partition number on the device whose partition type is to be set.</p>
</dd>

### -param <i>PartitionInfo</i> [in]

<dd>
<p>A structure whose <i>PartitionType</i> member specifies the type for the partition. For the currently defined <i>PartitionType</i> values <a href="https://msdn.microsoft.com/library/windows/hardware/ff563751">PARTITION_INFORMATION</a>.</p>
</dd>
</dl>

## -returns
<p>If <b>IoSetPartitionInformationEx</b> returns STATUS_SUCCESS, the disk driver updates its notion of the partition type for this partition in its device extension.</p>

## -remarks
<p><b>IoSetPartitionInformationEx</b> must only be used by disk drivers. Other drivers should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560417">IOCTL_DISK_SET_PARTITION_INFO_EX</a> disk I/O request instead.</p>

<p>This routine is called when a disk device driver is requested to set partition information in a partition table entry by an IRP_MJ_DEVICE_CONTROL request. This request is generally issued by the format utility, which performs I/O control functions on the partition. The driver passes a pointer to the device object representing the physical disk and the number of the partition associated with the device object that the format utility has open. Since the HAL routines that underlie <b>IoSetPartitionInformationEx</b> were developed before support for dynamic partitioning was implemented, they do not distinguish between the <i>partitionordinal</i> (that is the order of a partition on a disk) and the <i>partition number</i> (the partition number assigned to a partition in order to identify it to the system). Drivers must call <b>IoSetPartitionInformationEx</b> using the <i>ordinal</i> number of the partition and not the actual partition number.</p>

<p>If the partition is a Master Boot Record (MBR) type partition, <b>IoSetPartitionInformationEx</b> is limited to setting the partition style, and the partition style, which is represented as an unsigned character. See SET_PARTITION_INFORMATION_MBR for further information about these values.</p>

<p>If the partition is a GUID Partition Table (GPT) partition, <b>IoSetPartitionInformationEx</b> sets the following values: the partition style, the partition type, represented by a GUID instead of an integer as was the case with MBR partitions; a partition ID, also represented by a GUID; a set of attributes (see the Extensible Firmware Interface for a description of these attributes); and a Unicode name for the partition. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff566196">SET_PARTITION_INFORMATION_GPT</a> for further information about these values.</p>

<p>This routine is synchronous and must be called by the disk driver's Dispatch routine or by a driver thread. Thus, all user and file system threads must be prepared to enter a wait state when issuing the device control request to set the partition type for the device.</p>

<p>This routine operates under the assumption that the partition number passed in by the disk driver actually exists.</p>

<p>This routine must be called at IRQL = PASSIVE_LEVEL because it uses a kernel event object to synchronize I/O completion on the device. The event cannot be set to the Signaled state without queuing and executing the I/O system's special kernel APC routine for I/O completion.</p>

<p><b>IoSetPartitionInformationEx</b> must only be used by disk drivers. Other drivers should use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560417">IOCTL_DISK_SET_PARTITION_INFO_EX</a> disk I/O request instead.</p>

<p>This routine is called when a disk device driver is requested to set partition information in a partition table entry by an IRP_MJ_DEVICE_CONTROL request. This request is generally issued by the format utility, which performs I/O control functions on the partition. The driver passes a pointer to the device object representing the physical disk and the number of the partition associated with the device object that the format utility has open. Since the HAL routines that underlie <b>IoSetPartitionInformationEx</b> were developed before support for dynamic partitioning was implemented, they do not distinguish between the <i>partitionordinal</i> (that is the order of a partition on a disk) and the <i>partition number</i> (the partition number assigned to a partition in order to identify it to the system). Drivers must call <b>IoSetPartitionInformationEx</b> using the <i>ordinal</i> number of the partition and not the actual partition number.</p>

<p>If the partition is a Master Boot Record (MBR) type partition, <b>IoSetPartitionInformationEx</b> is limited to setting the partition style, and the partition style, which is represented as an unsigned character. See SET_PARTITION_INFORMATION_MBR for further information about these values.</p>

<p>If the partition is a GUID Partition Table (GPT) partition, <b>IoSetPartitionInformationEx</b> sets the following values: the partition style, the partition type, represented by a GUID instead of an integer as was the case with MBR partitions; a partition ID, also represented by a GUID; a set of attributes (see the Extensible Firmware Interface for a description of these attributes); and a Unicode name for the partition. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff566196">SET_PARTITION_INFORMATION_GPT</a> for further information about these values.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561452">IoReadPartitionTable</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561464">IoWritePartitionTable</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561456">IoSetPartitionInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566192">SET_PARTITION_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566194">SET_PARTITION_INFORMATION_EX</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20IoSetPartitionInformationEx routine%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
