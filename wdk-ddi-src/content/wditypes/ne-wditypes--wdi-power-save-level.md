---
UID: NE.wditypes._WDI_POWER_SAVE_LEVEL
title: WDI_POWER_SAVE_LEVEL
author: windows-driver-content
description: The WDI_POWER_SAVE_LEVEL enumeration defines the power save levels.
old-location: netvista\wdi_power_save_level.htm
old-project: netvista
ms.assetid: 3CB311C1-8FAE-44D5-896D-972F5DF1E88A
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_WORKITEM_CONFIG, WDF_WORKITEM_CONFIG, *PWDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wditypes.hpp
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WDI_POWER_SAVE_LEVEL
req.alt-loc: wditypes.hpp
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WDI_POWER_SAVE_LEVEL enumeration



## -description
<p>The WDI_POWER_SAVE_LEVEL enumeration defines the power save levels.</p>


## -syntax

````
typedef enum _WDI_POWER_SAVE_LEVEL { 
  WDI_POWER_SAVE_LEVEL_NO_POWER_SAVE  = 0,
  WDI_POWER_SAVE_LEVEL_FAST_PSP       = 8,
  WDI_POWER_SAVE_LEVEL_MAX_PSP        = 16,
  WDI_POWER_SAVE_LEVEL_MAXIMUM_LEVEL  = 24
} WDI_POWER_SAVE_LEVEL;
````


## -enum-fields
<dl>

### -field WDI_POWER_SAVE_LEVEL_NO_POWER_SAVE

<dd>
<p>No power saving.</p>
</dd>

### -field WDI_POWER_SAVE_LEVEL_FAST_PSP

<dd>
<p>Fast PSP.</p>
</dd>

### -field WDI_POWER_SAVE_LEVEL_MAX_PSP

<dd>
<p>Maximum PSP.</p>
</dd>

### -field WDI_POWER_SAVE_LEVEL_MAXIMUM_LEVEL

<dd>
<p>Maximum power saving level.</p>
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
<dt>Wditypes.hpp</dt>
</dl>
</td>
</tr>
</table>