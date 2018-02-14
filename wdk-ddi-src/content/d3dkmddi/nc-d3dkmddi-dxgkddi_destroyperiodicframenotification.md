---
UID: NC:d3dkmddi.DXGKDDI_DESTROYPERIODICFRAMENOTIFICATION
title: DXGKDDI_DESTROYPERIODICFRAMENOTIFICATION
author: windows-driver-content
description: Used to destroy a periodic frame notification.
old-location: display\dxgkddi_destroyperiodicframenotification.htm
old-project: display
ms.assetid: 4C6B6FB2-A699-40F5-ACA3-62E8620E99AB
ms.author: windowsdriverdev
ms.date: 12/29/2017
ms.keywords: display.dxgkddi_destroyperiodicframenotification, DXGKDDI_DESTROYPERIODICFRAMENOTIFICATION callback function [Display Devices], DXGKDDI_DESTROYPERIODICFRAMENOTIFICATION, d3dkmddi/DXGKDDI_DESTROYPERIODICFRAMENOTIFICATION
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	UserDefined
apilocation:
-	d3dkmddi.h
apiname:
-	DXGKDDI_DESTROYPERIODICFRAMENOTIFICATION
product: Windows
targetos: Windows
req.typenames: DD_MULTISAMPLEQUALITYLEVELSDATA
---


# DXGKDDI_DESTROYPERIODICFRAMENOTIFICATION function
Used to destroy a periodic frame notification.

## Syntax

```
DXGKDDI_DESTROYPERIODICFRAMENOTIFICATION DxgkddiDestroyperiodicframenotification;

NTSTATUS DxgkddiDestroyperiodicframenotification(
  IN_CONST_PDXGKARG_DESTROYPERIODICFRAMENOTIFICATION pDestroyPeriodicFrameNotification
)
{...}
```

## Parameters

`pDestroyPeriodicFrameNotification`

A structure of type <i>PDXGKARG_DESTROYPERIODICFRAMENOTIFICATION</i> containing the arguments needed to destroy a periodic frame notification.


## Return Value

DXGKDDI_DESTROYPERIODICFRAMENOTIFICATION returns one of the following values:

<table>
<tr>
<th>Return code</th>
<th>Description</th>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>
</td>
<td width="60%">
When a periodic frame notification has been successfully created.

</td>
</tr>
<tr>
<td width="40%">
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>
</td>
<td width="60%">
Indicates that there was an invalid parameter passed to the call.

</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | d3dkmddi.h |