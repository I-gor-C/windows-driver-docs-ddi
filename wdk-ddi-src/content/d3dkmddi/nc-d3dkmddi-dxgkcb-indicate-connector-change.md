---
UID: NC.d3dkmddi.DXGKCB_INDICATE_CONNECTOR_CHANGE
title: DXGKCB_INDICATE_CONNECTOR_CHANGE
author: windows-driver-content
description: DXGKCB_INDICATE_CONNECTOR_CHANGE is called by the KMD to indicate that it has added changes to its change queue which the OS should now query.
old-location: display\dxgkcb_indicate_connector_change.htm
old-project: display
ms.assetid: D3C76DC0-7A6B-4E1E-8277-F6410D4B474B
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: *DXGKCB_INDICATE_CONNECTOR_CHANGE
req.alt-loc: d3dkmddi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
req.iface: 
---

# DXGKCB_INDICATE_CONNECTOR_CHANGE callback



## -description
<p>DXGKCB_INDICATE_CONNECTOR_CHANGE is called by the KMD to indicate that it has added changes to its change queue which the OS should now query.</p>


## -prototype

````
NTSTATUS APIENTRY *DXGKCB_INDICATE_CONNECTOR_CHANGE(
  _In_ const HANDLE hAdapter
);
````


## -parameters
<dl>

### -param <i>hAdapter</i> [in]

<dd>
<p>A handle that identifies the adapter.</p>
</dd>
</dl>

## -returns
<p>If this routine succeeds, it returns STATUS_SUCCESS. </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>DISPATCH_LEVEL</p>
</td>
</tr>
</table>