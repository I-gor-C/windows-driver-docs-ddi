---
UID: NS.ntddstor._STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR
title: STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR
author: windows-driver-content
description: The STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR structure is used to retrieve the attributes information for a device.
old-location: storage\storage_device_attributes_descriptor.htm
ms.assetid: DA8434EF-6163-4D07-A81D-D1AC2D55BFB4
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR
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
ms.keywords: STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR, STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR, *PSTORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR
req.iface: 
---

# STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR structure



## -description
<p>The STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR structure is used to retrieve the attributes information for a  device.</p>


## -syntax

````
typedef struct _STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR {
  ULONG   Version;
  ULONG   Size;
  ULONG64 Attributes;
} STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR, *PSTORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>Contains the version of the data reported. </p>
</dd>

### -field <b>Size</b>

<dd>
<p>Indicates the quantity of data reported, in bytes. This is the <code>sizeof(STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR)</code>.</p>
</dd>

### -field <b>Attributes</b>

<dd>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="STORAGE_ATTRIBUTE_BYTE_ADDRESSABLE_IO"></a><a id="storage_attribute_byte_addressable_io"></a><dl>

### -field <b>STORAGE_ATTRIBUTE_BYTE_ADDRESSABLE_IO</b>


### -field 0x01

</dl>
</td>
<td width="60%">
<p>Attribute that indicates a storage device supports byte addressable IO.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="STORAGE_ATTRIBUTE_BLOCK_IO"></a><a id="storage_attribute_block_io"></a><dl>

### -field <b>STORAGE_ATTRIBUTE_BLOCK_IO</b>


### -field 0x02

</dl>
</td>
<td width="60%">
<p>Attribute that indicates a storage device supports block IO.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="STORAGE_ATTRIBUTE_DYNAMIC_PERSISTENCE"></a><a id="storage_attribute_dynamic_persistence"></a><dl>

### -field <b>STORAGE_ATTRIBUTE_DYNAMIC_PERSISTENCE</b>


### -field 0x04

</dl>
</td>
<td width="60%">
<p>Attribute that indicates that persistence of data on storage device may change.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="STORAGE_ATTRIBUTE_VOLATILE"></a><a id="storage_attribute_volatile"></a><dl>

### -field <b>STORAGE_ATTRIBUTE_VOLATILE</b>


### -field 0x08

</dl>
</td>
<td width="60%">
<p>Attribute that indicates a storage device is volatile and does not support persistence of data.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="STORAGE_ATTRIBUTE_ASYNC_EVENT_NOTIFICATION"></a><a id="storage_attribute_async_event_notification"></a><dl>

### -field <b>STORAGE_ATTRIBUTE_ASYNC_EVENT_NOTIFICATION</b>


### -field 0x10

</dl>
</td>
<td width="60%">
<p>Reserved</p>
</td>
</tr>
<tr>
<td width="40%"><a id="STORAGE_ATTRIBUTE_PERF_SIZE_INDEPENDENT"></a><a id="storage_attribute_perf_size_independent"></a><dl>

### -field <b>STORAGE_ATTRIBUTE_PERF_SIZE_INDEPENDENT</b>


### -field 0x20

</dl>
</td>
<td width="60%">
<p>Attribute that indicates a storage device has IO performance independent of IO sizes.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
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