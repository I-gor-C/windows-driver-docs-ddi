---
UID: NC.d3dkmddi.DXGKDDI_CREATEPERIODICFRAMENOTIFICATION
title: DXGKDDI_CREATEPERIODICFRAMENOTIFICATION
author: windows-driver-content
description: Used to create a periodic frame notification.
old-location: display\dxgkddi_createperiodicframenotification.htm
old-project: display
ms.assetid: EE11227A-E576-49C6-AEF1-CBE0AD788275
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
req.alt-api: DXGKDDI_CREATEPERIODICFRAMENOTIFICATION
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
req.irql: requires_max_(PASSIVE_LEVEL)
req.iface: 
---

# DXGKDDI_CREATEPERIODICFRAMENOTIFICATION callback



## -description
<p>Used to create a periodic frame notification.</p>


## -prototype

````
NTSTATUS APIENTRY DXGKDDI_CREATEPERIODICFRAMENOTIFICATION(
  _In_ const PDXGKARG_CREATEPERIODICFRAMENOTIFICATION pCreatePeriodicFrameNotification
);
````


## -parameters
<dl>

### -param <i>pCreatePeriodicFrameNotification</i> [in]

<dd>
<p>A structure of type <i>PDXGKARG_CREATEPERIODICFRAMENOTIFICATION</i> containing the arguments needed to create a periodic frame notification.</p>
</dd>
</dl>

## -returns
<p>DXGKDDI_CREATEPERIODICFRAMENOTIFICATION returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>When a periodic frame notification has been successfully created.</p><dl>
<dt><b>STATUS_NO_MEMORY</b></dt>
</dl><p>When a periodic frame notification does not have enough memory to be allocated.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Indicates that there was an invalid parameter passed to the call.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>When a periodic frame notification has not been successfully created.</p>

<p> </p>

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
<p>requires_max_(PASSIVE_LEVEL)</p>
</td>
</tr>
</table>