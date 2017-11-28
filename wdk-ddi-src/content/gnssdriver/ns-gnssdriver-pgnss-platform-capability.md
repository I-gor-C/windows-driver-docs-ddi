---
UID: NS.gnssdriver.PGNSS_PLATFORM_CAPABILITY
title: PGNSS_PLATFORM_CAPABILITY
author: windows-driver-content
description: This structure is used to communicate the platform/HLOS capabilities to the underlying GNSS driver.
old-location: sensors\gnss_platform_capability.htm
old-project: sensors
ms.assetid: A97DE517-26ED-452F-9066-94F73BC47BDE
ms.author: windowsdriverdev
ms.date: 11/26/2017
ms.keywords: PGNSS_PLATFORM_CAPABILITY, GNSS_PLATFORM_CAPABILITY, *PGNSS_PLATFORM_CAPABILITY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_PLATFORM_CAPABILITY
req.alt-loc: gnssdriver.h
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

# PGNSS_PLATFORM_CAPABILITY structure



## -description
<p>This structure is used to communicate the platform/HLOS capabilities to the underlying GNSS driver.</p>


## -syntax

````
typedef struct {
  ULONG Size;
  ULONG Version;
  BOOL  SupportAgnssInjection;
  ULONG AgnssFormatSupported;
  BOOL  Reserved;
  BYTE  Unused[512];
} GNSS_PLATFORM_CAPABILITY, *PGNSS_PLATFORM_CAPABILITY;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Structure size.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Version number.</p>
</dd>

### -field <b>SupportAgnssInjection</b>

<dd>
<p>Indicates that the platform supports AGNSS injection via the location platform.</p>
</dd>

### -field <b>AgnssFormatSupported</b>

<dd>
<p>Specifies a bitmask containing the different AGNSS formats (GNSS_AGNSSFORMAT_*) that the GNSS driver or device supports.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>Unused[512]</b>

<dd>
<p>Padding buffer.</p>
</dd>
</dl>

## -remarks
<p> This is a list of individual capability support of the GNSS adapter. The platform capability is represented in the same way as the device capabilities are represented.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Gnssdriver.h</dt>
</dl>
</td>
</tr>
</table>