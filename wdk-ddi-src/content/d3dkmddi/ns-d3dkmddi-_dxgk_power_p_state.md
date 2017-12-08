---
UID: NS.D3DKMDDI._DXGK_POWER_P_STATE
title: _DXGK_POWER_P_STATE
author: windows-driver-content
description: Reserved for system use. Do not use it in your driver.
old-location: display\dxgk_power_p_state.htm
old-project: display
ms.assetid: F4612284-36C8-49C4-914D-43C32489EABD
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _DXGK_POWER_P_STATE, DXGK_POWER_P_STATE
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
req.alt-api: DXGK_POWER_P_STATE
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

# _DXGK_POWER_P_STATE structure



## -description
Reserved for system use. Do not use it in your driver.


## -syntax

````
typedef struct _DXGK_POWER_P_STATE {
  ULONG     NominalPower;
  ULONG     OperatingFrequency;
  ULONGLONG TransitionLatencies[DXGK_MAX_P_STATES];
  ULONGLONG ResidencyRequirement;
} DXGK_POWER_P_STATE, *PDXGK_POWER_P_STATE;
````


## -struct-fields

### -field NominalPower


### -field OperatingFrequency


### -field TransitionLatencies


### -field ResidencyRequirement


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