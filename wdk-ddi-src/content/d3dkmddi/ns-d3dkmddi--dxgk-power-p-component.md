---
UID: NS.d3dkmddi._DXGK_POWER_P_COMPONENT
title: DXGK_POWER_P_COMPONENT
author: windows-driver-content
description: Reserved for system use. Do not use it in your driver.
old-location: display\dxgk_power_p_component.htm
old-project: display
ms.assetid: 31D76B3B-E939-404B-9EE4-FFCDFCD304C8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_POWER_P_COMPONENT, DXGK_POWER_P_COMPONENT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_POWER_P_COMPONENT
req.alt-loc: D3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DXGK_POWER_P_COMPONENT structure



## -description
<p>Reserved for system use. Do not use it in your driver.</p>


## -syntax

````
typedef struct _DXGK_POWER_P_COMPONENT {
  ULONG                        StateCount;
  DXGK_POWER_P_STATE           States[DXGK_MAX_P_STATES];
  DXGK_POWER_COMPONENT_P_FLAGS Flags;
} DXGK_POWER_P_COMPONENT;
````


## -struct-fields
<dl>

### -field <b>StateCount</b>

<dd></dd>

### -field <b>States</b>

<dd></dd>

### -field <b>Flags</b>

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>