---
UID: NC.d3dkmthk.PFND3DKMT_GETPOSTCOMPOSITIONCAPS
title: PFND3DKMT_GETPOSTCOMPOSITIONCAPS
author: windows-driver-content
description: 
ms.assetid: 0a6207b4-1b32-43d6-9201-c7769dde5fca
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dkmthk.h
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

# PFND3DKMT_GETPOSTCOMPOSITIONCAPS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_GETPOSTCOMPOSITIONCAPS Pfnd3dkmtGetpostcompositioncaps; 

// Definition

NTSTATUS Pfnd3dkmtGetpostcompositioncaps 
(
	D3DKMT_GET_POST_COMPOSITION_CAPS *
)
{...}

PFND3DKMT_GETPOSTCOMPOSITIONCAPS 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also