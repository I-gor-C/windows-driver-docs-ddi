---
UID: NC.iddcx.PFN_IDDCXSWAPCHAINGETDIRTYRECTS
title: *PFN_IDDCXSWAPCHAINGETDIRTYRECTS
author: windows-driver-content
description: 
ms.assetid: 858a662a-c83b-46c8-bc1f-cd8cc500aef6
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: iddcx.h
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

# *PFN_IDDCXSWAPCHAINGETDIRTYRECTS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_IDDCXSWAPCHAINGETDIRTYRECTS *PfnIddcxswapchaingetdirtyrects; 

// Definition

HRESULT *PfnIddcxswapchaingetdirtyrects 
(
	PIDD_DRIVER_GLOBALS DriverGlobals
	IDDCX_SWAPCHAIN SwapChainObject
	CONST IDARG_IN_GETDIRTYRECTS *pInArgs
	IDARG_OUT_GETDIRTYRECTS *pOutArgs
)
{...}

*PFN_IDDCXSWAPCHAINGETDIRTYRECTS 


```

## -parameters

### -param DriverGlobals: 
### -param SwapChainObject: 
### -param *pInArgs: 
### -param *pOutArgs: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also