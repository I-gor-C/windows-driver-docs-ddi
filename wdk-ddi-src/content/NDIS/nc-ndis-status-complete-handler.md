---
UID: NC.ndis.STATUS_COMPLETE_HANDLER
title: STATUS_COMPLETE_HANDLER
author: windows-driver-content
description: 
ms.assetid: e0d3ea7a-c3b3-44c0-ab5c-16bca58472cd
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

# STATUS_COMPLETE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

STATUS_COMPLETE_HANDLER StatusCompleteHandler; 

// Definition

VOID StatusCompleteHandler 
(
	NDIS_HANDLE ProtocolBindingContext
)
{...}

STATUS_COMPLETE_HANDLER 


```

## -parameters

### -param ProtocolBindingContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also