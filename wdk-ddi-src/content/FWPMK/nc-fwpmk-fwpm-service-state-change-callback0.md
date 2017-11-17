---
UID: NC.fwpmk.FWPM_SERVICE_STATE_CHANGE_CALLBACK0
title: FWPM_SERVICE_STATE_CHANGE_CALLBACK0
author: windows-driver-content
description: 
ms.assetid: 50c401c3-652f-4638-91f7-66187d8092ab
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: fwpmk.h
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

# FWPM_SERVICE_STATE_CHANGE_CALLBACK0 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

FWPM_SERVICE_STATE_CHANGE_CALLBACK0 FwpmServiceStateChangeCallback0; 

// Definition

void FwpmServiceStateChangeCallback0 
(
	void *context
	FWPM_SERVICE_STATE newState
)
{...}

FWPM_SERVICE_STATE_CHANGE_CALLBACK0 


```

## -parameters

### -param *context: 
### -param newState: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also