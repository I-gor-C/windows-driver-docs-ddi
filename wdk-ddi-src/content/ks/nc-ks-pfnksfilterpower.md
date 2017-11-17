---
UID: NC.ks.PFNKSFILTERPOWER
title: PFNKSFILTERPOWER
author: windows-driver-content
description: 
ms.assetid: 0aaed2b6-12b9-4feb-a978-01ba30136e7f
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

# PFNKSFILTERPOWER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSFILTERPOWER Pfnksfilterpower; 

// Definition

void Pfnksfilterpower 
(
	PKSFILTER Filter
	DEVICE_POWER_STATE State
)
{...}

PFNKSFILTERPOWER 


```

## -parameters

### -param Filter: 
### -param State: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also