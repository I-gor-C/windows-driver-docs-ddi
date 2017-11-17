---
UID: NC.ntifs.PCC_POST_DEFERRED_WRITE
title: PCC_POST_DEFERRED_WRITE
author: windows-driver-content
description: 
ms.assetid: 056fbcce-f384-49aa-96c6-1c1ef979edfe
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntifs.h
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

# PCC_POST_DEFERRED_WRITE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCC_POST_DEFERRED_WRITE PccPostDeferredWrite; 

// Definition

VOID PccPostDeferredWrite 
(
	PVOID Context1
	PVOID Context2
)
{...}

PCC_POST_DEFERRED_WRITE 


```

## -parameters

### -param Context1: 
### -param Context2: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also