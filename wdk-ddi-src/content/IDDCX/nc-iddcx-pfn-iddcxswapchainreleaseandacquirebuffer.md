---
UID: NC.iddcx.PFN_IDDCXSWAPCHAINRELEASEANDACQUIREBUFFER
title: *PFN_IDDCXSWAPCHAINRELEASEANDACQUIREBUFFER
author: windows-driver-content
description: 
ms.assetid: cbfd1c48-53b5-41fb-b9e6-dfc437c74647
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

# *PFN_IDDCXSWAPCHAINRELEASEANDACQUIREBUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_IDDCXSWAPCHAINRELEASEANDACQUIREBUFFER *PfnIddcxswapchainreleaseandacquirebuffer; 

// Definition

HRESULT *PfnIddcxswapchainreleaseandacquirebuffer 
(
	PIDD_DRIVER_GLOBALS DriverGlobals
	IDDCX_SWAPCHAIN SwapChainObject
	IDARG_OUT_RELEASEANDACQUIREBUFFER *pOutArgs
)
{...}

*PFN_IDDCXSWAPCHAINRELEASEANDACQUIREBUFFER 


```

## -parameters

### -param DriverGlobals: 
### -param SwapChainObject: 
### -param *pOutArgs: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also