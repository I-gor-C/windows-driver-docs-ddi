---
UID: NC.wdfcompanion.EVT_WDF_COMPANION_PRE_D0_ENTRY
title: EVT_WDF_COMPANION_PRE_D0_ENTRY
author: windows-driver-content
description: For internal use only.
old-location: wdf\evt_wdf_companion_pre_d0_entry.htm
ms.assetid: 18d55cf3-62c3-42e8-8c33-f61ea80ff680
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: wdf
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
ms.keywords: WDF_COMMON_BUFFER_CONFIG, WDF_COMMON_BUFFER_CONFIG, *PWDF_COMMON_BUFFER_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# EVT_WDF_COMPANION_PRE_D0_ENTRY callback



## -description
<p>
			For internal use only.</p>


## -prototype

````
NTSTATUS EVT_WDF_COMPANION_PRE_D0_ENTRY(
  _In_ WDFCOMPANION           Companion,
  _In_ WDF_POWER_DEVICE_STATE PreviousState
);
````


## -parameters
<dl>

### -param <i>Companion</i> [in]

<dd></dd>

### -param <i>PreviousState</i> [in]

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.23</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfcompanion.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>