---
UID: NS.ntddstor._STORAGE_ADAPTER_DESCRIPTOR
title: STORAGE_ADAPTER_DESCRIPTOR
author: windows-driver-content
description: The STORAGE_ADAPTER_DESCRIPTOR structure is used in conjunction with the IOCTL_STORAGE_QUERY_PROPERTY request to retrieve the storage adapter descriptor data for a device.
old-location: storage\storage_adapter_descriptor.htm
old-project: storage
ms.assetid: 83ef2a1a-f95e-4b05-8911-e5e900192630
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORAGE_ADAPTER_DESCRIPTOR, STORAGE_ADAPTER_DESCRIPTOR, *PSTORAGE_ADAPTER_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_ADAPTER_DESCRIPTOR
req.alt-loc: ntddstor.h
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

# STORAGE_ADAPTER_DESCRIPTOR structure



## -description
<p>The <b>STORAGE_ADAPTER_DESCRIPTOR</b> structure is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a> request to retrieve the storage adapter descriptor data for a device. </p>


## -syntax

````
typedef struct _STORAGE_ADAPTER_DESCRIPTOR {
  ULONG   Version;
  ULONG   Size;
  ULONG   MaximumTransferLength;
  ULONG   MaximumPhysicalPages;
  ULONG   AlignmentMask;
  BOOLEAN AdapterUsesPio;
  BOOLEAN AdapterScansDown;
  BOOLEAN CommandQueueing;
  BOOLEAN AcceleratedTransfer;
  UCHAR   BusType;
  USHORT  BusMajorVersion;
  USHORT  BusMinorVersion;
  UCHAR   SrbType;
  UCHAR   AddressType;
} STORAGE_ADAPTER_DESCRIPTOR, *PSTORAGE_ADAPTER_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>Contains the version of the structure <b>STORAGE_ADAPTER_DESCRIPTOR</b>. The value of this member will change as members are added to the structure.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>Specifies the total size of the descriptor, in bytes.</p>
</dd>

### -field <b>MaximumTransferLength</b>

<dd>
<p>Specifies the maximum number of bytes the host bus adapter (HBA) can transfer in a single operation.</p>
</dd>

### -field <b>MaximumPhysicalPages</b>

<dd>
<p>Specifies the maximum number of discontinuous physical pages the HBA can manage in a single transfer (in other words, the extent of its scatter/gather support).</p>
</dd>

### -field <b>AlignmentMask</b>

<dd>
<p>Specifies the HBA's alignment requirements for transfers. A storage class driver sets the <b>AlignmentRequirement</b> field in its device objects to this value. The alignment mask indicates alignment restrictions for buffers required by the HBA for transfer operations. The valid mask values are 0 (byte aligned), 1 (word aligned), 3 (DWORD aligned), and 7 (double DWORD aligned). </p>
</dd>

### -field <b>AdapterUsesPio</b>

<dd>
<p>Indicates when <b>TRUE</b> that the HBA uses Programmed Input/Output (PIO) and requires the use of system-space virtual addresses mapped to physical memory for data buffers. When <b>FALSE</b>, the HBA does not use PIO.</p>
</dd>

### -field <b>AdapterScansDown</b>

<dd>
<p>Indicates when <b>TRUE</b> that the HBA scans down for BIOS devices, that is, the HBA begins scanning with the highest device number rather than the lowest. When <b>FALSE</b>, the HBA begins scanning with the lowest device number. This member is reserved for legacy miniport drivers.</p>
</dd>

### -field <b>CommandQueueing</b>

<dd>
<p>Indicates when <b>TRUE</b> that the HBA supports SCSI-tagged queuing and/or per-logical-unit internal queues, or the non-SCSI equivalent. When <b>FALSE</b>, the HBA neither supports SCSI-tagged queuing nor per-logical-unit internal queues. </p>
</dd>

### -field <b>AcceleratedTransfer</b>

<dd>
<p>Indicates when <b>TRUE</b> that the HBA supports synchronous transfers as a way of speeding up I/O. When <b>FALSE</b>, the HBA does not support synchronous transfers as a way of speeding up I/O. </p>
</dd>

### -field <b>BusType</b>

<dd>
<p>Specifies a value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff566356">STORAGE_BUS_TYPE</a> that indicates the type of bus to which the device is connected.</p>
</dd>

### -field <b>BusMajorVersion</b>

<dd>
<p>Specifies the major version number, if any, of the HBA. </p>
</dd>

### -field <b>BusMinorVersion</b>

<dd>
<p>Specifies the minor version number, if any, of the HBA.</p>
</dd>

### -field <b>SrbType</b>

<dd>
<p>Specifies the SCSI request block (SRB) type used by the HBA.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="SRB_TYPE_SCSI_REQUEST_BLOCK"></a><a id="srb_type_scsi_request_block"></a><dl>

### -field <b>SRB_TYPE_SCSI_REQUEST_BLOCK</b>

</dl>
</td>
<td width="60%">
<p>The HBA uses SCSI request blocks.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="SRB_TYPE_STORAGE_REQUEST_BLOCK"></a><a id="srb_type_storage_request_block"></a><dl>

### -field <b>SRB_TYPE_STORAGE_REQUEST_BLOCK</b>

</dl>
</td>
<td width="60%">
<p>The HBA uses extended SCSI request blocks.</p>
</td>
</tr>
</table>
<p> </p>
<p>This member is valid starting with Windows 8.</p>
</dd>

### -field <b>AddressType</b>

<dd>
<p>Specifies the address type of the HBA.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="STORAGE_ADDRESS_TYPE_BTL8"></a><a id="storage_address_type_btl8"></a><dl>

### -field <b>STORAGE_ADDRESS_TYPE_BTL8</b>

</dl>
</td>
<td width="60%">
<p>The HBA uses 8-bit bus, target, and LUN addressing.</p>
</td>
</tr>
</table>
<p> </p>
<p>This member is valid starting with Windows 8.</p>
</dd>
</dl>

## -remarks
<p>Storage class drivers issue a device-control request with the I/O control code <a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a> to retrieve this structure, which contains configuration information from the HBA for data transfer operations. The structure can be retrieved either from the device object for the bus or from a functional device object (FDO), which forwards the request to the underlying bus.</p>

<p>If excessive protocol errors occur on an HBA that supports synchronous transfers (<b>AcceleratedTransfer</b> is <b>TRUE</b>), the storage class driver can disable synchronous transfers by setting SRB_FLAGS_DISABLE_SYNCH_TRANSFER in SRBs.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddstor.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548318">IoBuildDeviceIoControlRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566971">STORAGE_DEVICE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566968">STORAGE_DESCRIPTOR_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566972">STORAGE_DEVICE_ID_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566346">STORAGE_ADAPTER_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20STORAGE_ADAPTER_DESCRIPTOR structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
