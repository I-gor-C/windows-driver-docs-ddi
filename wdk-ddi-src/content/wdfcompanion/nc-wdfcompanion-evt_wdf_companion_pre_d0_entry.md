---
UID: NC.wdfcompanion.EVT_WDF_COMPANION_PRE_D0_ENTRY
title: EVT_WDF_COMPANION_PRE_D0_ENTRY
author: windows-driver-content
description: For internal use only.
old-location: wdf\evt_wdf_companion_pre_d0_entry.htm
old-project: wdf
ms.assetid: 18d55cf3-62c3-42e8-8c33-f61ea80ff680
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: _WDF_COMMON_BUFFER_CONFIG, WDF_COMMON_BUFFER_CONFIG, PWDF_COMMON_BUFFER_CONFIG, *PWDF_COMMON_BUFFER_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdfcompanion.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.23
req.alt-api: EVT_WDF_COMPANION_PRE_D0_ENTRY
req.alt-loc: wdfcompanion.h
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
req.product: Windows 10 or later.
---

# EVT_WDF_COMPANION_PRE_D0_ENTRY callback



## -description

			For internal use only.



## -prototype

````
EVT_WDF_COMPANION_PRE_D0_ENTRY EVT_WDF_COMPANION_PRE_D0_ENTRY;

NTSTATUS EVT_WDF_COMPANION_PRE_D0_ENTRY(
  _In_ WDFCOMPANION           Companion,
  _In_ WDF_POWER_DEVICE_STATE PreviousState
)
{ ... }
````


## -parameters

### -param Companion [in]


### -param PreviousState [in]


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.23

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfcompanion.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>