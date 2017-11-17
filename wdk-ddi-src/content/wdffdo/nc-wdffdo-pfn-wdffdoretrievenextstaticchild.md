---
UID: NC.wdffdo.PFN_WDFFDORETRIEVENEXTSTATICCHILD
title: PFN_WDFFDORETRIEVENEXTSTATICCHILD
author: windows-driver-content
description: 
ms.assetid: b87a42bb-6ae1-4e01-b932-c5647a6e038f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdffdo.h
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

# PFN_WDFFDORETRIEVENEXTSTATICCHILD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFFDORETRIEVENEXTSTATICCHILD PfnWdffdoretrievenextstaticchild; 

// Definition

WDFAPI PfnWdffdoretrievenextstaticchild 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Fdo
	WDFDEVICE PreviousChild
	ULONG Flags
)
{...}

PFN_WDFFDORETRIEVENEXTSTATICCHILD 


```

## -parameters

### -param DriverGlobals: 
### -param Fdo: 
### -param PreviousChild: 
### -param Flags: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also