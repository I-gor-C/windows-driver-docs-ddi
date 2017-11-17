---
UID: NC.ndis.UNBIND_HANDLER
title: UNBIND_HANDLER
author: windows-driver-content
description: 
ms.assetid: c59eddaa-97df-416d-9d76-dedd4f087ee3
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

# UNBIND_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

UNBIND_HANDLER UnbindHandler; 

// Definition

VOID UnbindHandler 
(
	PNDIS_STATUS Status
	NDIS_HANDLE ProtocolBindingContext
	NDIS_HANDLE UnbindContext
)
{...}

UNBIND_HANDLER 


```

## -parameters

### -param Status: 
### -param ProtocolBindingContext: 
### -param UnbindContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also