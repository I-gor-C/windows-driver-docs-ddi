---
UID: NS.ntddstor._STORAGE_DEVICE_POWER_CAP
title: STORAGE_DEVICE_POWER_CAP
author: windows-driver-content
description: This structure is used as an input and output buffer for the IOCTL_STORAGE_DEVICE_POWER_CAP.
old-location: storage\storage_device_power_cap.htm
old-project: storage
ms.assetid: B13D311F-FFC4-4A40-AF0C-6E7115174FD1
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: STORAGE_DEVICE_POWER_CAP, STORAGE_DEVICE_POWER_CAP, *PSTORAGE_DEVICE_POWER_CAP
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
req.alt-api: STORAGE_DEVICE_POWER_CAP
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

# STORAGE_DEVICE_POWER_CAP structure



## -description
<p>This structure is used as an input and output buffer for the <a href="https://msdn.microsoft.com/library/windows/hardware/dn932064">IOCTL_STORAGE_DEVICE_POWER_CAP</a>.</p>


## -syntax

````
typedef struct _STORAGE_DEVICE_POWER_CAP {
  ULONG                          Version;
  ULONG                          Size;
  STORAGE_DEVICE_POWER_CAP_UNITS Units;
  ULONG                          MaxPower;
} STORAGE_DEVICE_POWER_CAP, *PSTORAGE_DEVICE_POWER_CAP;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of this structure. This should be set to STORAGE_DEVICE_POWER_CAP_VERSION_V1.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>The size of this structure.</p>
</dd>

### -field <b>Units</b>

<dd>
<p>The units of the MaxPower value.</p>
</dd>

### -field <b>MaxPower</b>

<dd>
<p>Contains the value of the actual maximum power consumption level of the device. This may be equal to, less than, or greater than the desired threshold, depending on what the device supports.</p>
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