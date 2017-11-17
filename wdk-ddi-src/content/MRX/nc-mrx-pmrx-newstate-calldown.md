---
UID: NC.mrx.PMRX_NEWSTATE_CALLDOWN
title: PMRX_NEWSTATE_CALLDOWN
author: windows-driver-content
description: 
ms.assetid: ccf158ec-7c00-4d11-a042-95b01dfe8127
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: mrx.h
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

# PMRX_NEWSTATE_CALLDOWN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMRX_NEWSTATE_CALLDOWN PmrxNewstateCalldown; 

// Definition

VOID PmrxNewstateCalldown 
(
	IN OUT PVOID Context
)
{...}

PMRX_NEWSTATE_CALLDOWN 


```

## -parameters

### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also