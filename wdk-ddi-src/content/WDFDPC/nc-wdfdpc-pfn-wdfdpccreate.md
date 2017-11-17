---
UID: NC.wdfdpc.PFN_WDFDPCCREATE
title: PFN_WDFDPCCREATE
author: windows-driver-content
description: 
ms.assetid: 1441c221-dd2d-4232-8b25-ad8724d0aae9
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdpc.h
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

# PFN_WDFDPCCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDPCCREATE PfnWdfdpccreate; 

// Definition

WDFAPI PfnWdfdpccreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDF_DPC_CONFIG Config
	PWDF_OBJECT_ATTRIBUTES Attributes
	WDFDPC *Dpc
)
{...}

PFN_WDFDPCCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Config: 
### -param Attributes: 
### -param *Dpc: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also