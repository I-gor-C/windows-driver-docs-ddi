---
UID: NC.wdfchildlist.PFN_WDFCHILDLISTBEGINSCAN
title: PFN_WDFCHILDLISTBEGINSCAN
author: windows-driver-content
description: 
ms.assetid: adaf447c-0f12-498c-92c8-51ac7826063d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfchildlist.h
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

# PFN_WDFCHILDLISTBEGINSCAN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCHILDLISTBEGINSCAN PfnWdfchildlistbeginscan; 

// Definition

WDFAPI PfnWdfchildlistbeginscan 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCHILDLIST ChildList
)
{...}

PFN_WDFCHILDLISTBEGINSCAN 


```

## -parameters

### -param DriverGlobals: 
### -param ChildList: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also