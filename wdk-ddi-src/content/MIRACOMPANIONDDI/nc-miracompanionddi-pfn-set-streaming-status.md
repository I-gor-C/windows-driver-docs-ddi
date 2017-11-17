---
UID: NC.miracompanionddi.PFN_SET_STREAMING_STATUS
title: PFN_SET_STREAMING_STATUS
author: windows-driver-content
description: 
ms.assetid: 0458332c-c71d-43c4-9e94-123e170a1818
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: miracompanionddi.h
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

# PFN_SET_STREAMING_STATUS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SET_STREAMING_STATUS PfnSetStreamingStatus; 

// Definition

VOID PfnSetStreamingStatus 
(
	void const *pOSContext
	COMPANION_STREAMING_STATUS eStatus
)
{...}

PFN_SET_STREAMING_STATUS 


```

## -parameters

### -param *pOSContext: 
### -param eStatus: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also