---
UID: NC.ntifs.VERIFY_SIGNATURE_FN
title: VERIFY_SIGNATURE_FN
author: windows-driver-content
description: 
ms.assetid: 8b00f3c2-296c-42c6-b7fc-ff4b9529a090
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

# VERIFY_SIGNATURE_FN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

VERIFY_SIGNATURE_FN VerifySignatureFn; 

// Definition

SECURITY_STATUS VerifySignatureFn 
(
	PCtxtHandle 
	PSecBufferDesc 
	 unsigned long
	 unsigned long *
)
{...}

VERIFY_SIGNATURE_FN 


```

## -parameters

### -param : 
### -param : 
### -param long: 
### -param *: 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also