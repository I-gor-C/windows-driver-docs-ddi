---
UID: NC.d3dkmthk.PFND3DKMT_GETSETSWAPCHAINMETADATA
title: PFND3DKMT_GETSETSWAPCHAINMETADATA
author: windows-driver-content
description: 
ms.assetid: e6e4dbae-268e-4410-8a56-8d8bf557d282
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

# PFND3DKMT_GETSETSWAPCHAINMETADATA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_GETSETSWAPCHAINMETADATA Pfnd3dkmtGetsetswapchainmetadata; 

// Definition

NTSTATUS Pfnd3dkmtGetsetswapchainmetadata 
(
	D3DKMT_GETSETSWAPCHAINMETADATA *
)
{...}

PFND3DKMT_GETSETSWAPCHAINMETADATA 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also