---
UID: NC.ntifs.ENCRYPT_MESSAGE_FN
title: ENCRYPT_MESSAGE_FN
author: windows-driver-content
description: 
ms.assetid: 02d5a74b-11fd-48c2-9f39-a31f4c4e5205
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

# ENCRYPT_MESSAGE_FN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

ENCRYPT_MESSAGE_FN EncryptMessageFn; 

// Definition

SECURITY_STATUS EncryptMessageFn 
(
	PCtxtHandle 
	 unsigned long
	PSecBufferDesc 
	 unsigned long
)
{...}

ENCRYPT_MESSAGE_FN 


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