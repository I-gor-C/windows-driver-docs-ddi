---
UID: NC.ntifs.MAKE_SIGNATURE_FN
title: MAKE_SIGNATURE_FN
author: windows-driver-content
description: 
ms.assetid: 85729509-dbd1-4495-a08e-4127288f404b
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

# MAKE_SIGNATURE_FN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

MAKE_SIGNATURE_FN MakeSignatureFn; 

// Definition

SECURITY_STATUS MakeSignatureFn 
(
	PCtxtHandle 
	 unsigned long
	PSecBufferDesc 
	 unsigned long
)
{...}

MAKE_SIGNATURE_FN 


```

## -parameters

### -param : 
### -param long: 
### -param : 
### -param long: 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also