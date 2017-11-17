---
UID: NC.wdfio.PFN_WDFIOQUEUESTOP
title: PFN_WDFIOQUEUESTOP
author: windows-driver-content
description: 
ms.assetid: 68356424-6baf-45e9-b47c-8e2386fb9878
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

# PFN_WDFIOQUEUESTOP callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOQUEUESTOP PfnWdfioqueuestop; 

// Definition

WDFAPI PfnWdfioqueuestop 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFQUEUE Queue
	PFN_WDF_IO_QUEUE_STATE StopComplete
	WDFCONTEXT Context
)
{...}

PFN_WDFIOQUEUESTOP 


```

## -parameters

### -param DriverGlobals: 
### -param Queue: 
### -param StopComplete: 
### -param Context: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also