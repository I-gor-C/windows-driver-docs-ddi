---
UID: NC.wdfregistry.PFN_WDFREGISTRYREMOVEKEY
title: PFN_WDFREGISTRYREMOVEKEY
author: windows-driver-content
description: 
ms.assetid: d1eef382-4824-4d0b-a27e-24333ddc1723
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfregistry.h
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

# PFN_WDFREGISTRYREMOVEKEY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREGISTRYREMOVEKEY PfnWdfregistryremovekey; 

// Definition

WDFAPI PfnWdfregistryremovekey 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFKEY Key
)
{...}

PFN_WDFREGISTRYREMOVEKEY 


```

## -parameters

### -param DriverGlobals: 
### -param Key: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also