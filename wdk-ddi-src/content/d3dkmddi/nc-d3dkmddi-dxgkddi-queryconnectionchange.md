---
UID: NC.d3dkmddi.DXGKDDI_QUERYCONNECTIONCHANGE
title: DXGKDDI_QUERYCONNECTIONCHANGE
author: windows-driver-content
description: The OS calls this in response to a status change reported through DxgkCbIndicateConnectorChange or when the OutputFlags.ConnectorStatusChanges field indicates that a call to SetTimingsFromVidPn has detected connector status changes.
old-location: display\dxgkddi_queryconnectionchange.htm
old-project: display
ms.assetid: 8C09B692-3439-4ACD-942D-F7A107E2B4DA
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
req.alt-api: DXGKDDI_QUERYCONNECTIONCHANGE
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
req.irql: 
req.iface: 
---

# DXGKDDI_QUERYCONNECTIONCHANGE callback



## -description
<p>The OS calls this in response to a status change reported through DxgkCbIndicateConnectorChange or when the OutputFlags.ConnectorStatusChanges field indicates that a call to SetTimingsFromVidPn has detected connector status changes.</p>


## -prototype

````
NTSTATUS APIENTRY DXGKDDI_QUERYCONNECTIONCHANGE(
  _In_ const HANDLE                         hAdapter,
  _In_       PDXGKARG_QUERYCONNECTIONCHANGE pQueryConnectionChange
);
````


## -parameters
<dl>

### -param <i>hAdapter</i> [in]

<dd>
<p>A handle that identifies the adapter.</p>
</dd>

### -param <i>pQueryConnectionChange</i> [in]

<dd>
<p>A pointer to a <a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-queryconnectionchange.md">DXGKARG_QUERYCONNECTIONCHANGE</a> structure that provides the OS allocated buffer into which the oldest change should be copied by the driver. The oldest change is judged by lowest ConnectionChangeId.</p>
</dd>
</dl>

## -returns
<dl>
<dt>STATUS_SUCCESS</dt>
</dl><p>Returned if the routine succeeds and returns the requested change.</p><dl>
<dt>STATUS_ALREADY_COMPLETE</dt>
</dl><p>Returned if the routine succeeds, but the changes have already been reported to the OS.</p>

<p> </p>

## -remarks
<p>This function is always called at PASSIVE level so the supporting code should be made pageable.</p>

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
</table>