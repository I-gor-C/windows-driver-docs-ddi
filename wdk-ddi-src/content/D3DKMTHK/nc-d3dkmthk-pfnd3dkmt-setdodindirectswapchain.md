---
UID: NC.d3dkmthk.PFND3DKMT_SETDODINDIRECTSWAPCHAIN
title: PFND3DKMT_SETDODINDIRECTSWAPCHAIN
author: windows-driver-content
description: 
ms.assetid: 56da3aef-bce4-403f-8e18-716838756603
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

# PFND3DKMT_SETDODINDIRECTSWAPCHAIN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_SETDODINDIRECTSWAPCHAIN Pfnd3dkmtSetdodindirectswapchain; 

// Definition

NTSTATUS Pfnd3dkmtSetdodindirectswapchain 
(
	D3DKMT_SETDODINDIRECTSWAPCHAIN *
)
{...}

PFND3DKMT_SETDODINDIRECTSWAPCHAIN 


```

## -parameters

### -param *: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also