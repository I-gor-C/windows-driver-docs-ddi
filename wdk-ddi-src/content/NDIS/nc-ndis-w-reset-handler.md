---
UID: NC.ndis.W_RESET_HANDLER
title: W_RESET_HANDLER
author: windows-driver-content
description: 
ms.assetid: 633ae0a4-eee0-4fcb-a747-e84aa9165f72
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

# W_RESET_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

W_RESET_HANDLER WResetHandler; 

// Definition

NDIS_STATUS WResetHandler 
(
	PBOOLEAN AddressingReset
	NDIS_HANDLE MiniportAdapterContext
)
{...}

W_RESET_HANDLER 


```

## -parameters

### -param AddressingReset: 
### -param MiniportAdapterContext: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also