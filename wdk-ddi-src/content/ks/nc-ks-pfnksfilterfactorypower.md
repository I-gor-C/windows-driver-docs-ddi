---
UID: NC.ks.PFNKSFILTERFACTORYPOWER
title: PFNKSFILTERFACTORYPOWER
author: windows-driver-content
description: 
ms.assetid: 4d84e2ab-0281-442e-b0d1-790a9d5c18a2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNKSFILTERFACTORYPOWER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSFILTERFACTORYPOWER Pfnksfilterfactorypower; 

// Definition

void Pfnksfilterfactorypower 
(
	PKSFILTERFACTORY FilterFactory
	DEVICE_POWER_STATE State
)
{...}

PFNKSFILTERFACTORYPOWER 


```

## -parameters

### -param FilterFactory: 
### -param State: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also