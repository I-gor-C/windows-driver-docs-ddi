---
UID: NS.ntddstor._STORAGE_HW_FIRMWARE_ACTIVATE
title: STORAGE_HW_FIRMWARE_ACTIVATE
author: windows-driver-content
description: This structure contains information about the downloaded firmware to activate.
old-location: storage\storage_hw_firmware_activate.htm
old-project: storage
ms.assetid: FCE1DE7B-CDFE-4533-90E7-A400EC236007
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORAGE_HW_FIRMWARE_ACTIVATE, STORAGE_HW_FIRMWARE_ACTIVATE, *PSTORAGE_HW_FIRMWARE_ACTIVATE
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
req.alt-api: STORAGE_HW_FIRMWARE_ACTIVATE
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

# STORAGE_HW_FIRMWARE_ACTIVATE structure



## -description
<p>This structure contains information about the downloaded firmware to activate.</p>


## -syntax

````
typedef struct _STORAGE_HW_FIRMWARE_ACTIVATE {
  ULONG Version;
  ULONG Size;
  ULONG Flags;
  UCHAR Slot;
  UCHAR Reserved0[3];
} STORAGE_HW_FIRMWARE_ACTIVATE, *PSTORAGE_HW_FIRMWARE_ACTIVATE;
````


## -struct-fields
<dl>

### -field Version

<dd>
<p>The version of this structure. This should be set to sizeof(STORAGE_HW_FIRMWARE_ACTIVATE).</p>
</dd>

### -field Size

<dd>
<p>The size of this structure. This should be set to sizeof(STORAGE_HW_FIRMWARE_ACTIVATE).</p>
</dd>

### -field Flags

<dd>
<p>The flags associated with the activation request. The following are valid flags that can be set in this member.</p>
<table>
<tr>
<th>Flag</th>
<th>Description</th>
</tr>
<tr>
<td>STORAGE_HW_FIRMWARE_REQUEST_FLAG_CONTROLLER</td>
<td>Indicates that the target of the request is a controller or adapter, different than the device handle or object itself (e.g. NVMe SSD or HBA).</td>
</tr>
<tr>
<td>STORAGE_HW_FIRMWARE_REQUEST_FLAG_SWITCH_TO_EXISTING_FIRMWARE  </td>
<td>Indicates that an existing firmware image in the specified slot should be activated. </td>
</tr>
</table>
<p> </p>
</dd>

### -field Slot

<dd>
<p>The slot with the firmware image that is to be activated.</p>
</dd>

### -field Reserved0

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