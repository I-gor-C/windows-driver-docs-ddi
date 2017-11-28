---
UID: NC.d3dkmddi.DXGKDDISETPOWERPSTATE
title: DXGKDDISETPOWERPSTATE
author: windows-driver-content
description: Reserved for system use. Do not use it in your driver.
old-location: display\dxgkddisetpowerpstate.htm
old-project: display
ms.assetid: 58DB4615-BD52-4003-8D60-0881E87C7BD3
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkDdiSetPowerPState
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

# DXGKDDISETPOWERPSTATE callback



## -description
<p>Reserved for system use. Do not use it in your driver.</p>


## -prototype

````
PDXGKDDISETPOWERPSTATE DxgkDdiSetPowerPState;

NTSTATUS APIENTRY DxgkDdiSetPowerPState(
  _In_ const HANDLE DriverContext,
  _In_       UINT   ComponentIndex,
  _In_       UINT   RequestedComponentPState
)
{ ... }
````


## -parameters
<dl>

### -param <i>DriverContext</i> [in]

<dd></dd>

### -param <i>ComponentIndex</i> [in]

<dd></dd>

### -param <i>RequestedComponentPState</i> [in]

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
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>