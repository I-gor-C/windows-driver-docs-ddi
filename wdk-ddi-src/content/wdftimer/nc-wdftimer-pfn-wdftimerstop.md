---
UID: NC.wdftimer.PFN_WDFTIMERSTOP
title: *PFN_WDFTIMERSTOP
author: windows-driver-content
description: 
ms.assetid: 18a8994b-3d56-4c29-af7b-db3f36a86267
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdftimer.h
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

# *PFN_WDFTIMERSTOP callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_WDFTIMERSTOP *PfnWdftimerstop; 

// Definition

BOOLEAN *PfnWdftimerstop 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFTIMER Timer
	BOOLEAN Wait
)
{...}

*PFN_WDFTIMERSTOP 


```

## -parameters

### -param DriverGlobals: 
### -param Timer: 
### -param Wait: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also