---
UID: NC.wdfcommonbuffer.PFN_WDFCOMMONBUFFERGETLENGTH
title: PFN_WDFCOMMONBUFFERGETLENGTH
author: windows-driver-content
description: 
ms.assetid: 8c061a46-98db-476d-bbbc-d9ee9a9bf7a4
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfcommonbuffer.h
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

# PFN_WDFCOMMONBUFFERGETLENGTH callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCOMMONBUFFERGETLENGTH PfnWdfcommonbuffergetlength; 

// Definition

WDFAPI PfnWdfcommonbuffergetlength 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCOMMONBUFFER CommonBuffer
)
{...}

PFN_WDFCOMMONBUFFERGETLENGTH 


```

## -parameters

### -param DriverGlobals: 
### -param CommonBuffer: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also