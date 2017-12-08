---
UID: NS.ntddstor._DEVICE_DATA_SET_LB_PROVISIONING_STATE
title: DEVICE_DATA_SET_LB_PROVISIONING_STATE
author: windows-driver-content
description: The DEVICE_DATA_SET_LB_PROVISIONING_STATE structure is returned by an IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES request when requesting logical block provisioning information for a data set range.
old-location: storage\device_data_set_lb_provisioning_state.htm
old-project: storage
ms.assetid: 99FBD363-0999-4AEE-A222-69C0FB71D248
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DEVICE_DATA_SET_LB_PROVISIONING_STATE, DEVICE_DATA_SET_LB_PROVISIONING_STATE, *PDEVICE_DATA_SET_LB_PROVISIONING_STATE
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
req.alt-api: DEVICE_DATA_SET_LB_PROVISIONING_STATE
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

# DEVICE_DATA_SET_LB_PROVISIONING_STATE structure



## -description
<p>The <b>DEVICE_DATA_SET_LB_PROVISIONING_STATE</b> structure is returned by an  <a href="..\ntddstor\ni-ntddstor-ioctl-storage-manage-data-set-attributes.md">IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES</a> request when requesting logical block  provisioning information for a data set range.</p>


## -syntax

````
typedef struct _DEVICE_DATA_SET_LB_PROVISIONING_STATE {
  ULONG     Size;
  ULONG     Version;
  ULONGLONG SlabSizeInBytes;
  ULONG     SlabOffsetDeltaInBytes;
  ULONG     SlabAllocationBitMapBitCount;
  ULONG     SlabAllocationBitMapLength;
  ULONG     SlabAllocationBitMap[ANYSIZE_ARRAY];
} DEVICE_DATA_SET_LB_PROVISIONING_STATE, *PDEVICE_DATA_SET_LB_PROVISIONING_STATE;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>The size of this structure, including the slab allocation bitmap, in bytes.</p>
</dd>

### -field Version

<dd>
<p>The version of this structure.</p>
</dd>

### -field SlabSizeInBytes

<dd>
<p>The size, in bytes, of a slab.</p>
</dd>

### -field SlabOffsetDeltaInBytes

<dd>
<p>The difference, in bytes, from the offset specified in the data set range to the starting slab position.</p>
</dd>

### -field SlabAllocationBitMapBitCount

<dd>
<p>The number of bits  in the allocation bitmap mapping  slabs for the data set range.</p>
</dd>

### -field SlabAllocationBitMapLength

<dd>
<p>The number of <b>ULONG</b> array values containing the slab allocation bitmap.</p>
</dd>

### -field SlabAllocationBitMap

<dd>
<p>A bitmap of slab allocations.</p>
</dd>
</dl>

## -remarks
<p>Provisioning state information is returned when the <b>Action</b> member of <a href="..\ntddstor\ns-ntddstor--device-manage-data-set-attributes.md">DEVICE_MANAGE_DATA_SET_ATTRIBUTES</a> is set to <b>DeviceDsmAction_Allocation</b>. The caller should include only one data set range in the system buffer at <b>DataSetRangesOffset</b>.</p>

<p>On return, the system buffer contains a <a href="..\ntddstor\ns-ntddstor--device-manage-data-set-attributes-output.md">DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUPUT</a> structure followed by the <b>DEVICE_DATA_SET_LB_PROVISIONING_STATE</b> structure. The <b>DEVICE_DATA_SET_LB_PROVISIONING_STATE</b> structure begins at an offset from the beginning of the system buffer specified by <b>OutputBlockOffset</b> in <b>DEVICE_MANAGE_DATA_SET_ATTRIBUTES_OUPUT</b>.</p>

<p>Each bit in the allocation bitmap represents a slab mapping within the data set range requested. The bits correspond directly to the slabs in the data set range. This means that bit 0 in the bitmap marks the first slab in the range. A slab is mapped if the bit value = 1 and unmapped if the bit value = 0.</p>

<p>Space for <b>SlabAllocationBitMap</b> should be allocated based on the number of possible slabs  in the requested data set range. The <b>SlabAllocationBitMapLength</b> of the bitmap returned is (<i>number of slabs</i> / 32) + ((<i>number of slabs</i> MOD 32) &gt; 0 ? 1 : 0).</p>

<p>Slab size is determined by the <b>OptimalUnmapGranularity</b> member of <a href="..\ntddstor\ns-ntddstor--device-lb-provisioning-descriptor.md">DEVICE_LB_PROVISIONING_DESCRIPTOR</a> returned from an <a href="..\ntddstor\ni-ntddstor-ioctl-storage-query-property.md">IOCTL_STORAGE_QUERY_PROPERTY</a> request. The length of the data set range provided should be a multiple of <b>OptimalUnmapGranularity</b>. When the range length is not a multiple of <b>OptimalUnmapGranularity</b>, it is reduced to be a multiple.</p>

<p>If the starting offset in the data set range is not aligned on a slab boundary, a multiple of <b>OptimalUnmapGranularity</b>, the offset will be adjusted to the next boundary. The difference between the requested offset and the adjusted offset is returned in <b>SlabOffsetDeltaInBytes</b>.</p>

<p>If the slab allocation total returned in <b>SlabAllocationBitMapBitCount</b> is not as expected because of data set range alignment or length adjustments, an additional request may be submitted with a data set range modified according to the values in both <b>SlabAllocationBitMapBitCount</b> and <b>SlabOffsetDeltaInBytes</b>. The new range will properly select the slabs left out of the bitmap returned by the previous request.</p>

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
<a href="storage.device_data_management_set_action">DEVICE_DATA_MANAGEMENT_SET_ACTION</a>
</dt>
<dt>
<a href="..\ntddstor\ns-ntddstor--device-manage-data-set-attributes.md">DEVICE_MANAGE_DATA_SET_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\ntddstor\ni-ntddstor-ioctl-storage-manage-data-set-attributes.md">IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\ntddstor\ni-ntddstor-ioctl-storage-query-property.md">IOCTL_STORAGE_QUERY_PROPERTY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20DEVICE_DATA_SET_LB_PROVISIONING_STATE structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
