---
UID: NC.ndis.W_CHECK_FOR_HANG_HANDLER
title: W_CHECK_FOR_HANG_HANDLER
author: windows-driver-content
description: 
ms.assetid: d1fb8b25-7a6e-4ee9-ae82-bdaf83b2dc2e
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

# W_CHECK_FOR_HANG_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

W_CHECK_FOR_HANG_HANDLER WCheckForHangHandler; 

// Definition

BOOLEAN WCheckForHangHandler 
(
	NDIS_HANDLE MiniportAdapterContext
)
{...}

W_CHECK_FOR_HANG_HANDLER 


```

## -parameters

### -param MiniportAdapterContext: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also