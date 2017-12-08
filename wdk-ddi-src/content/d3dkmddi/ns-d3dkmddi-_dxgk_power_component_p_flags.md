---
UID: NS.D3DKMDDI._DXGK_POWER_COMPONENT_P_FLAGS
title: _DXGK_POWER_COMPONENT_P_FLAGS
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\dxgk_power_component_p_flags.htm
old-project: display
ms.assetid: 9A3C9821-7E98-4F9E-94EE-AF2C09C2A881
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _DXGK_POWER_COMPONENT_P_FLAGS, DXGK_POWER_COMPONENT_P_FLAGS
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
---

# _DXGK_POWER_COMPONENT_P_FLAGS structure



## -description
Reserved for system use. Do not use in your driver.


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

### -field Reserved


### -field Value


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8.1
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012 R2
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>