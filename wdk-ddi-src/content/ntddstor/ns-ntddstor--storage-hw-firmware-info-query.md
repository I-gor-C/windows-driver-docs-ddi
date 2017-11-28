---
UID: NS.ntddstor._STORAGE_HW_FIRMWARE_INFO_QUERY
title: STORAGE_HW_FIRMWARE_INFO_QUERY
author: windows-driver-content
description: This structure contains information about the device firmware.
old-location: storage\storage_hw_firmware_info_query.htm
old-project: storage
ms.assetid: 7B58F050-2AF4-4BD5-95AB-254BCAA865F6
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORAGE_HW_FIRMWARE_INFO_QUERY, STORAGE_HW_FIRMWARE_INFO_QUERY, *PSTORAGE_HW_FIRMWARE_INFO_QUERY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_HW_FIRMWARE_INFO_QUERY
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

# STORAGE_HW_FIRMWARE_INFO_QUERY structure



## -description
<p>This structure contains information about the device firmware.</p>


## -syntax

````
typedef struct _STORAGE_HW_FIRMWARE_INFO_QUERY {
  ULONG Version;
  ULONG Size;
  ULONG Flags;
  ULONG Reserved;
} STORAGE_HW_FIRMWARE_INFO_QUERY, *PSTORAGE_HW_FIRMWARE_INFO_QUERY;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of this structure. This should be set to sizeof(STORAGE_HW_FIRMWARE_INFO_QUERY)</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size of this structure as a buffer.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>The flags associated with the query. The following are flags that can be set in this member.</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>STORAGE_HW_FIRMWARE_REQUEST_FLAG_CONTROLLER</td>
<td>Indicates that the target of the request is different than the device handle or object itself.</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Server</p>
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
<dt>Ntddstor.h</dt>
</dl>
</td>
</tr>
</table>