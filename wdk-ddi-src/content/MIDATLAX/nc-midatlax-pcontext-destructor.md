---
UID: NC.midatlax.PCONTEXT_DESTRUCTOR
title: PCONTEXT_DESTRUCTOR
author: windows-driver-content
description: 
ms.assetid: 8415dd37-c9e9-466a-9db7-53dc1136bb3d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: midatlax.h
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

# PCONTEXT_DESTRUCTOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCONTEXT_DESTRUCTOR PcontextDestructor; 

// Definition

VOID PcontextDestructor 
(
	PVOID Context
)
{...}

PCONTEXT_DESTRUCTOR 


```

## -parameters

### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also