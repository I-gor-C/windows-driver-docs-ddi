---
UID: NC.d3dkmddi.DXGKDDI_SETPOINTERSHAPE
title: DXGKDDI_SETPOINTERSHAPE
author: windows-driver-content
description: 
ms.assetid: 2e933496-c5b2-4924-af52-faef30bb0171
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

# DXGKDDI_SETPOINTERSHAPE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_SETPOINTERSHAPE DxgkddiSetpointershape; 

// Definition

NTSTATUS DxgkddiSetpointershape 
(
	IN_CONST_HANDLE hAdapter
	IN_CONST_PDXGKARG_SETPOINTERSHAPE pSetPointerShape
)
{...}

DXGKDDI_SETPOINTERSHAPE PDXGKDDI_SETPOINTERSHAPE


```

## -parameters

### -param hAdapter: 
### -param pSetPointerShape: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also