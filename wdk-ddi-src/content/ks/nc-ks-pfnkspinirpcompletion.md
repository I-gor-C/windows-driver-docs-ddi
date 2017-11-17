---
UID: NC.ks.PFNKSPINIRPCOMPLETION
title: PFNKSPINIRPCOMPLETION
author: windows-driver-content
description: 
ms.assetid: 265bda7e-8759-4ef2-8c47-44de65bc7256
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

# PFNKSPINIRPCOMPLETION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSPINIRPCOMPLETION Pfnkspinirpcompletion; 

// Definition

void Pfnkspinirpcompletion 
(
	PKSPIN Pin
	PIRP Irp
)
{...}

PFNKSPINIRPCOMPLETION 


```

## -parameters

### -param Pin: 
### -param Irp: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also