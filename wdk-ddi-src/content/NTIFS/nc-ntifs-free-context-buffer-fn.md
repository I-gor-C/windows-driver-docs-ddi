---
UID: NC.ntifs.FREE_CONTEXT_BUFFER_FN
title: FREE_CONTEXT_BUFFER_FN
author: windows-driver-content
description: 
ms.assetid: e3e84458-a57e-4d1b-9cc3-9c792c86352d
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

# FREE_CONTEXT_BUFFER_FN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

FREE_CONTEXT_BUFFER_FN FreeContextBufferFn; 

// Definition

SECURITY_STATUS FreeContextBufferFn 
(
	PVOID 
)
{...}

FREE_CONTEXT_BUFFER_FN 


```

## -parameters

### -param : 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also