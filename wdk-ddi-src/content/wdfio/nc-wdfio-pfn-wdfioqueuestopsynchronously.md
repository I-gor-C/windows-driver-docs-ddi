---
UID: NC.wdfio.PFN_WDFIOQUEUESTOPSYNCHRONOUSLY
title: PFN_WDFIOQUEUESTOPSYNCHRONOUSLY
author: windows-driver-content
description: 
ms.assetid: 6dae62bf-9dd8-4928-b589-03103fd9160f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfio.h
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

# PFN_WDFIOQUEUESTOPSYNCHRONOUSLY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOQUEUESTOPSYNCHRONOUSLY PfnWdfioqueuestopsynchronously; 

// Definition

WDFAPI PfnWdfioqueuestopsynchronously 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFQUEUE Queue
)
{...}

PFN_WDFIOQUEUESTOPSYNCHRONOUSLY 


```

## -parameters

### -param DriverGlobals: 
### -param Queue: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also