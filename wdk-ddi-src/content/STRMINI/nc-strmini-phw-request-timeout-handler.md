---
UID: NC.strmini.PHW_REQUEST_TIMEOUT_HANDLER
title: PHW_REQUEST_TIMEOUT_HANDLER
author: windows-driver-content
description: 
ms.assetid: 2a4d23aa-72d1-41ab-99d6-f1e9aa7fdf2e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: strmini.h
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

# PHW_REQUEST_TIMEOUT_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PHW_REQUEST_TIMEOUT_HANDLER PhwRequestTimeoutHandler; 

// Definition

VOID PhwRequestTimeoutHandler 
(
	IN PHW_STREAM_REQUEST_BLOCK SRB
)
{...}

PHW_REQUEST_TIMEOUT_HANDLER 


```

## -parameters

### -param SRB: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also