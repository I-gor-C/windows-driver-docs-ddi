---
UID: NC.wdfrequest.PFN_WDFREQUESTREUSE
title: PFN_WDFREQUESTREUSE
author: windows-driver-content
description: 
ms.assetid: 02394f89-5dce-47ee-b73e-8aab4cff6e25
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfrequest.h
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

# PFN_WDFREQUESTREUSE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREQUESTREUSE PfnWdfrequestreuse; 

// Definition

WDFAPI PfnWdfrequestreuse 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	PWDF_REQUEST_REUSE_PARAMS ReuseParams
)
{...}

PFN_WDFREQUESTREUSE 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param ReuseParams: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also