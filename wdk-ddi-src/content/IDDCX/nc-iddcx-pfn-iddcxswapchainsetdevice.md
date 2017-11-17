---
UID: NC.iddcx.PFN_IDDCXSWAPCHAINSETDEVICE
title: *PFN_IDDCXSWAPCHAINSETDEVICE
author: windows-driver-content
description: 
ms.assetid: e04e0660-91a2-4a1a-b002-3653f6b3914e
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

# *PFN_IDDCXSWAPCHAINSETDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_IDDCXSWAPCHAINSETDEVICE *PfnIddcxswapchainsetdevice; 

// Definition

HRESULT *PfnIddcxswapchainsetdevice 
(
	PIDD_DRIVER_GLOBALS DriverGlobals
	IDDCX_SWAPCHAIN SwapChainObject
	IDARG_IN_SWAPCHAINSETDEVICE *pInArgs
)
{...}

*PFN_IDDCXSWAPCHAINSETDEVICE 


```

## -parameters

### -param DriverGlobals: 
### -param SwapChainObject: 
### -param *pInArgs: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also