---
UID: NC.ntifs.DECRYPT_MESSAGE_FN
title: DECRYPT_MESSAGE_FN
author: windows-driver-content
description: 
ms.assetid: e858d468-871c-4905-9fe9-8b195f797b4e
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

# DECRYPT_MESSAGE_FN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DECRYPT_MESSAGE_FN DecryptMessageFn; 

// Definition

SECURITY_STATUS DecryptMessageFn 
(
	PCtxtHandle 
	PSecBufferDesc 
	 unsigned long
	 unsigned long *
)
{...}

DECRYPT_MESSAGE_FN 


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