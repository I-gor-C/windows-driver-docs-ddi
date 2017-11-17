---
UID: NS.wdm._POWER_PLATFORM_INFORMATION
title: POWER_PLATFORM_INFORMATION
author: windows-driver-content
description: The POWER_PLATFORM_INFORMATION structure contains information about the power capabilities of the system.
old-location: kernel\power_platform_information.htm
ms.assetid: 0E62B57D-F9B1-4B01-A19E-9E2DBC387578
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: POWER_PLATFORM_INFORMATION
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
ms.keywords: POWER_PLATFORM_INFORMATION, POWER_PLATFORM_INFORMATION, *PPOWER_PLATFORM_INFORMATION
req.iface: 
req.product: Windows 10 or later.
---

# POWER_PLATFORM_INFORMATION structure



## -description
<p>The <b>POWER_PLATFORM_INFORMATION</b> structure contains information about  the power capabilities of the system.</p>


## -syntax

````
typedef struct _POWER_PLATFORM_INFORMATION {
  BOOLEAN AoAc;
} POWER_PLATFORM_INFORMATION, *PPOWER_PLATFORM_INFORMATION;
````


## -struct-fields
<dl>

### -field <b>AoAc</b>

<dd>
<p>Indicates whether the system supports the connected standby power model.</p>
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
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
</table>