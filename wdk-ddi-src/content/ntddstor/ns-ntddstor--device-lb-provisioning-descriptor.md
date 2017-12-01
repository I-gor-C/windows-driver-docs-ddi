---
UID: NS.ntddstor._DEVICE_LB_PROVISIONING_DESCRIPTOR
title: DEVICE_LB_PROVISIONING_DESCRIPTOR
author: windows-driver-content
description: The DEVICE_LB_PROVISIONING_DESCRIPTOR structure is one of the query result structures returned from an IOCTL_STORAGE_QUERY_PROPERTY request. This structure contains the thin provisioning capabilities for a storage device.
old-location: storage\device_lb_provisioning_descriptor.htm
old-project: storage
ms.assetid: E7287A50-2BB8-4D11-AB9B-6E65EEDD698D
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DEVICE_LB_PROVISIONING_DESCRIPTOR, DEVICE_LB_PROVISIONING_DESCRIPTOR, *PDEVICE_LB_PROVISIONING_DESCRIPTOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DEVICE_LB_PROVISIONING_DESCRIPTOR
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

# DEVICE_LB_PROVISIONING_DESCRIPTOR structure



## -description
<p>The <b>DEVICE_LB_PROVISIONING_DESCRIPTOR</b> structure is one of the query result structures returned from an <a href="..\ntddstor\ni-ntddstor-ioctl-storage-query-property.md">IOCTL_STORAGE_QUERY_PROPERTY</a> request. This structure contains the thin provisioning capabilities for a storage device.</p>


## -syntax

````
typedef struct _DEVICE_LB_PROVISIONING_DESCRIPTOR {
  ULONG     Version;
  ULONG     Size;
  UCHAR     ThinProvisioningEnabled  :1;
  UCHAR     ThinProvisioningReadZeros  :1;
  UCHAR     AnchorSupported  :3;
  UCHAR     UnmapGranularityAlignmentValid  :1;
  UCHAR     Reserverd0  :2;
  UCHAR     Reserverd1[7];
  ULONGLONG OptimalUnmapGranularity;
  ULONGLONG UnmapGranularityAlignment;
  ULONG     MaxUnmapLbaCount;
  ULONG     MaxUnmapBlockDescriptorCount;
} DEVICE_LB_PROVISIONING_DESCRIPTOR, *PDEVICE_LB_PROVISIONING_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of this structure.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size of this structure. This is set to <b>sizeof</b>(DEVICE_LB_PROVISIONING_DESCRIPTOR).</p>
</dd>

### -field <b>ThinProvisioningEnabled</b>

<dd>
<p>The thin provisioning–enabled status.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0

</dl>
</td>
<td width="60%">
<p>Thin provisioning is disabled.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 1

</dl>
</td>
<td width="60%">
<p>Thin provisioning is enabled.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ThinProvisioningReadZeros</b>

<dd>
<p>Reads to unmapped regions return zeros.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0

</dl>
</td>
<td width="60%">
<p>Data read from unmapped regions is undefined.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 1

</dl>
</td>
<td width="60%">
<p>Reads return zeros.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>AnchorSupported</b>

<dd>
<p>Support for the anchored LBA mapping state.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0

</dl>
</td>
<td width="60%">
<p>The anchored LBA mapping state is not supported.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 1

</dl>
</td>
<td width="60%">
<p>The anchored LBA mapping state is supported.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>UnmapGranularityAlignmentValid</b>

<dd>
<p>The validity of unmap granularity alignment for the device.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -field 0

</dl>
</td>
<td width="60%">
<p>Unmap granularity alignment is not valid.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field 1

</dl>
</td>
<td width="60%">
<p>Unmap granularity alignment is valid.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Reserverd0</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>Reserverd1</b>

<dd>
<p>Reserved.</p>
</dd>

### -field <b>OptimalUnmapGranularity</b>

<dd>
<p>The optimal number of blocks for unmap granularity for the device.</p>
</dd>

### -field <b>UnmapGranularityAlignment</b>

<dd>
<p>The current value, in blocks, set for unmap granularity alignment on the device.   The value <b>UnmapGranularityAlignmentValid</b> indicates the validity of this member.</p>
</dd>

### -field <b>MaxUnmapLbaCount</b>

<dd>
<p>Maximum amount of LBAs that can be unmapped in a single UNMAP command, in units of logical blocks. This is valid only in Windows 10 and above.</p>
</dd>

### -field <b>MaxUnmapBlockDescriptorCount</b>

<dd>
<p>Maximum number of descriptors allowed in a single UNMAP command. This is valid only in Windows 10 and above.</p>
</dd>
</dl>

## -remarks
<p>This structure is returned in the system buffer from a <a href="..\ntddstor\ni-ntddstor-ioctl-storage-query-property.md">IOCTL_STORAGE_QUERY_PROPERTY</a> request when the <b>PropertyId</b> member of <a href="..\ntddstor\ns-ntddstor--storage-property-query.md">STORAGE_PROPERTY_QUERY</a> is set to <b>StorageDeviceLBProvisioningProperty</b>. </p>

<p>The <b>DEVICE_LB_PROVISIONING_DESCRIPTOR</b> structure is written to the system buffer, <i>Irp-&gt;AssociatedIrp.SystemBuffer</i>, with a value of <b>sizeof</b>(DEVICE_LB_PROVISIONING_DESCRIPTOR) set in <i>Parameters.DeviceIoControl.OutputBufferLength</i> for the current IRP stack location.</p>

<p>If <b>UnmapGranularityAlignmentValid</b> = 0,  then any code using <b>UnmapGranularityAlignment</b> should assume it has a value of 0.</p>

<p>If the underlying storage device is a SCSI device, unmapping capability can be queried. If the <b>TrimEnabled</b> member of the <a href="..\ntddstor\ns-ntddstor--device-trim-descriptor.md">DEVICE_TRIM_DESCRIPTOR</a> structure is TRUE, UNMAP is supported. The <b>DEVICE_TRIM_DESCRIPTOR</b> structure is returned in the system buffer from a <a href="..\ntddstor\ni-ntddstor-ioctl-storage-query-property.md">IOCTL_STORAGE_QUERY_PROPERTY</a> request when the <b>PropertyId</b> member of <a href="..\ntddstor\ns-ntddstor--storage-property-query.md">STORAGE_PROPERTY_QUERY</a> is set to <b>StorageDeviceTrimProperty</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 8.</p>
</td>
</tr>
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
<a href="..\ntddstor\ni-ntddstor-ioctl-storage-query-property.md">IOCTL_STORAGE_QUERY_PROPERTY</a>
</dt>
<dt>
<a href="..\ntddstor\ns-ntddstor--storage-property-query.md">STORAGE_PROPERTY_QUERY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20DEVICE_LB_PROVISIONING_DESCRIPTOR structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
