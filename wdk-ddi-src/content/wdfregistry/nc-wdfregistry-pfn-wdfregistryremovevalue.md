---
UID: NC.wdfregistry.PFN_WDFREGISTRYREMOVEVALUE
title: PFN_WDFREGISTRYREMOVEVALUE
author: windows-driver-content
description: 
ms.assetid: 68e11c4b-313e-4411-aac4-e759c25afe2b
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

# PFN_WDFREGISTRYREMOVEVALUE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFREGISTRYREMOVEVALUE PfnWdfregistryremovevalue; 

// Definition

WDFAPI PfnWdfregistryremovevalue 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFKEY Key
	PCUNICODE_STRING ValueName
)
{...}

PFN_WDFREGISTRYREMOVEVALUE 


```

## -parameters

### -param DriverGlobals: 
### -param Key: 
### -param ValueName: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also