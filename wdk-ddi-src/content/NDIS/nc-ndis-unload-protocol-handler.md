---
UID: NC.ndis.UNLOAD_PROTOCOL_HANDLER
title: UNLOAD_PROTOCOL_HANDLER
author: windows-driver-content
description: 
ms.assetid: 4f7665e4-b059-4df2-81af-c5de59dd5375
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

# UNLOAD_PROTOCOL_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

UNLOAD_PROTOCOL_HANDLER UnloadProtocolHandler; 

// Definition

VOID UnloadProtocolHandler 
(
	 VOID
)
{...}

UNLOAD_PROTOCOL_HANDLER 


```

## -parameters

### -param VOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also