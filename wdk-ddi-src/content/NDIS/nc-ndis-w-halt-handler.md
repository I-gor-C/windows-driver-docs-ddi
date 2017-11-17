---
UID: NC.ndis.W_HALT_HANDLER
title: W_HALT_HANDLER
author: windows-driver-content
description: 
ms.assetid: e8425b08-5e33-4d8a-b3a3-a67ffa1de938
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ndis.h
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

# W_HALT_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

W_HALT_HANDLER WHaltHandler; 

// Definition

VOID WHaltHandler 
(
	NDIS_HANDLE MiniportAdapterContext
)
{...}

W_HALT_HANDLER 


```

## -parameters

### -param MiniportAdapterContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also