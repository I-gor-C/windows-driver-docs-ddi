---
UID: NC.ucxendpoint.PFN_UCXENDPOINTABORTCOMPLETE
title: PFN_UCXENDPOINTABORTCOMPLETE
author: windows-driver-content
description: 
ms.assetid: 4ef834e3-31d1-4afb-bb6a-088636c92871
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucxendpoint.h
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

# PFN_UCXENDPOINTABORTCOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCXENDPOINTABORTCOMPLETE PfnUcxendpointabortcomplete; 

// Definition

WDFAPI PfnUcxendpointabortcomplete 
(
	PUCX_DRIVER_GLOBALS DriverGlobals
	UCXENDPOINT Endpoint
)
{...}

PFN_UCXENDPOINTABORTCOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param Endpoint: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also