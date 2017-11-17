---
UID: NC.ks.PFNKSDEFAULTALLOCATE
title: PFNKSDEFAULTALLOCATE
author: windows-driver-content
description: 
ms.assetid: 8e44c646-808a-441b-b484-71403e17b394
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNKSDEFAULTALLOCATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSDEFAULTALLOCATE Pfnksdefaultallocate; 

// Definition

PVOID Pfnksdefaultallocate 
(
	PVOID Context
)
{...}

PFNKSDEFAULTALLOCATE 


```

## -parameters

### -param Context: 



## -returns

Returns PVOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also