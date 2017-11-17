---
UID: NC.sercx.PFN_SERCX2PIORECEIVEREADY
title: PFN_SERCX2PIORECEIVEREADY
author: windows-driver-content
description: 
ms.assetid: 7503f2b1-8dff-47b4-8474-ee36e3d3acdd
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: sercx.h
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

# PFN_SERCX2PIORECEIVEREADY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2PIORECEIVEREADY PfnSercx2pioreceiveready; 

// Definition

WDFAPI PfnSercx2pioreceiveready 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2PIORECEIVE PioReceive
)
{...}

PFN_SERCX2PIORECEIVEREADY 


```

## -parameters

### -param DriverGlobals: 
### -param PioReceive: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also