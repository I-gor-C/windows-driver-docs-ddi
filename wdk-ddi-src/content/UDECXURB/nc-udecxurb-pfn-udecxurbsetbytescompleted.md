---
UID: NC.udecxurb.PFN_UDECXURBSETBYTESCOMPLETED
title: *PFN_UDECXURBSETBYTESCOMPLETED
author: windows-driver-content
description: 
ms.assetid: 7c14d20f-80ea-450e-8022-a2fcb1f2c5ea
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: udecxurb.h
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

# *PFN_UDECXURBSETBYTESCOMPLETED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_UDECXURBSETBYTESCOMPLETED *PfnUdecxurbsetbytescompleted; 

// Definition

VOID *PfnUdecxurbsetbytescompleted 
(
	PUDECX_DRIVER_GLOBALS DriverGlobals
	WDFREQUEST Request
	ULONG BytesCompleted
)
{...}

*PFN_UDECXURBSETBYTESCOMPLETED 


```

## -parameters

### -param DriverGlobals: 
### -param Request: 
### -param BytesCompleted: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also