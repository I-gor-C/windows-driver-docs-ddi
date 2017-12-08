---
UID: NS.d3dkmddi._DXGK_POWER_COMPONENT_P_FLAGS
title: DXGK_POWER_COMPONENT_P_FLAGS
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\dxgk_power_component_p_flags.htm
old-project: display
ms.assetid: 9A3C9821-7E98-4F9E-94EE-AF2C09C2A881
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_POWER_COMPONENT_P_FLAGS, DXGK_POWER_COMPONENT_P_FLAGS
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
req.alt-api: DXGK_POWER_COMPONENT_P_FLAGS
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

# DXGK_POWER_COMPONENT_P_FLAGS structure



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef struct _DXGK_POWER_COMPONENT_P_FLAGS {
  union {
    struct {
      UINT Reserved  :32;
    };
    UINT Value;
  };
} DXGK_POWER_COMPONENT_P_FLAGS;
````


## -struct-fields
<dl>

### -field Reserved

<dd></dd>

### -field Value

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