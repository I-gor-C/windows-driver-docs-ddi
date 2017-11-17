---
UID: NC.sercx.PFN_SERCX2COMPLETEWAIT
title: PFN_SERCX2COMPLETEWAIT
author: windows-driver-content
description: 
ms.assetid: 0c28df6a-6b21-42bc-b8aa-ecd697553719
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

# PFN_SERCX2COMPLETEWAIT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2COMPLETEWAIT PfnSercx2completewait; 

// Definition

WDFAPI PfnSercx2completewait 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	ULONG Event
)
{...}

PFN_SERCX2COMPLETEWAIT 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Event: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also