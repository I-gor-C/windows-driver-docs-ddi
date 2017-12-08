---
UID: NC.d3dkmddi.DXGKDDI_DESTROYPERIODICFRAMENOTIFICATION
title: DXGKDDI_DESTROYPERIODICFRAMENOTIFICATION
author: windows-driver-content
description: Used to destroy a periodic frame notification.
old-location: display\dxgkddi_destroyperiodicframenotification.htm
old-project: display
ms.assetid: 4C6B6FB2-A699-40F5-ACA3-62E8620E99AB
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
req.alt-api: DXGKDDI_DESTROYPERIODICFRAMENOTIFICATION
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

# DXGKDDI_DESTROYPERIODICFRAMENOTIFICATION callback



## -description
<p>Used to destroy a periodic frame notification.</p>


## -prototype

````
NTSTATUS APIENTRY DXGKDDI_DESTROYPERIODICFRAMENOTIFICATION(
  _In_ const PDXGKARG_DESTROYPERIODICFRAMENOTIFICATION pDestroyPeriodicFrameNotification
);
````


## -parameters
<dl>

### -param pDestroyPeriodicFrameNotification [in]

<dd>
<p>A structure of type <i>PDXGKARG_DESTROYPERIODICFRAMENOTIFICATION</i> containing the arguments needed to destroy a periodic frame notification.</p>
</dd>
</dl>

## -returns
<p>DXGKDDI_DESTROYPERIODICFRAMENOTIFICATION returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>When a periodic frame notification has been successfully created.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Indicates that there was an invalid parameter passed to the call.</p>

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
</table>