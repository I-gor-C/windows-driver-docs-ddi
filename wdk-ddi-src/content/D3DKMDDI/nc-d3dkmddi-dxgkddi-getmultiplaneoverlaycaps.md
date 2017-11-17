---
UID: NC.d3dkmddi.DXGKDDI_GETMULTIPLANEOVERLAYCAPS
title: DXGKDDI_GETMULTIPLANEOVERLAYCAPS
author: windows-driver-content
description: 
ms.assetid: a8563030-de8c-44dc-9855-b736b1528ead
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dkmddi.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# DXGKDDI_GETMULTIPLANEOVERLAYCAPS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_GETMULTIPLANEOVERLAYCAPS DxgkddiGetmultiplaneoverlaycaps; 

// Definition

NTSTATUS DxgkddiGetmultiplaneoverlaycaps 
(
	IN_CONST_HANDLE hAdapter
	IN_OUT_PDXGKARG_GETMULTIPLANEOVERLAYCAPS pGetMultiPlaneOverlayCaps
)
{...}

DXGKDDI_GETMULTIPLANEOVERLAYCAPS PDXGKDDI_GETMULTIPLANEOVERLAYCAPS


```

## -parameters

### -param hAdapter: 
### -param pGetMultiPlaneOverlayCaps: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also