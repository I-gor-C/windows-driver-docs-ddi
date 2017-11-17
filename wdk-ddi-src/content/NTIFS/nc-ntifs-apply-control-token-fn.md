---
UID: NC.ntifs.APPLY_CONTROL_TOKEN_FN
title: APPLY_CONTROL_TOKEN_FN
author: windows-driver-content
description: 
ms.assetid: 3b966a1e-27a0-40b1-ac1b-c2cc92e19916
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

# APPLY_CONTROL_TOKEN_FN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

APPLY_CONTROL_TOKEN_FN ApplyControlTokenFn; 

// Definition

SECURITY_STATUS ApplyControlTokenFn 
(
	PCtxtHandle 
	PSecBufferDesc 
)
{...}

APPLY_CONTROL_TOKEN_FN 


```

## -parameters

### -param : 
### -param : 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also