---
UID: NS.ntddstor._STORAGE_HW_FIRMWARE_SLOT_INFO
title: STORAGE_HW_FIRMWARE_SLOT_INFO
author: windows-driver-content
description: This structure contains information about a slot on a device.
old-location: storage\storage_hw_firmware_slot_info.htm
old-project: storage
ms.assetid: D5DF9785-83E0-4137-8E5F-357F94721CAD
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORAGE_HW_FIRMWARE_SLOT_INFO, STORAGE_HW_FIRMWARE_SLOT_INFO, *PSTORAGE_HW_FIRMWARE_SLOT_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_HW_FIRMWARE_SLOT_INFO
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

# STORAGE_HW_FIRMWARE_SLOT_INFO structure



## -description
<p>This structure contains information about a slot on a device.</p>


## -syntax

````
typedef struct _STORAGE_HW_FIRMWARE_SLOT_INFO {
  ULONG Version;
  ULONG Size;
  UCHAR SlotNumber;
  UCHAR ReadOnly  :1;
  UCHAR Reserved0  :7;
  UCHAR Reserved1[6];
  UCHAR Revision[STORAGE_HW_FIRMWARE_REVISION_LENGTH];
} STORAGE_HW_FIRMWARE_SLOT_INFO, *PSTORAGE_HW_FIRMWARE_SLOT_INFO;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of this structure. This should be set to sizeof(STORAGE_HW_FIRMWARE_SLOT_INFO)</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size of this structure.</p>
</dd>

### -field <b>SlotNumber</b>

<dd>
<p>The slot number of this slot.</p>
</dd>

### -field <b>ReadOnly</b>

<dd>
<p>Indicates whether this slot is read-only or not.</p>
</dd>

### -field <b>Reserved0</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>Reserved1</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>Revision</b>

<dd>
<p>The revision of the firmware on this slot.</p>
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
<dt>Ntddstor.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>