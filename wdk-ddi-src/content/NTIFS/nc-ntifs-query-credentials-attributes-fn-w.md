---
UID: NC.ntifs.QUERY_CREDENTIALS_ATTRIBUTES_FN_W
title: QUERY_CREDENTIALS_ATTRIBUTES_FN_W
author: windows-driver-content
description: 
ms.assetid: 6fb889d0-6686-4238-a0c1-9ff589513a34
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

# QUERY_CREDENTIALS_ATTRIBUTES_FN_W callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

QUERY_CREDENTIALS_ATTRIBUTES_FN_W QueryCredentialsAttributesFnW; 

// Definition

SECURITY_STATUS QueryCredentialsAttributesFnW 
(
	PCredHandle 
	 unsigned long
	 void *
)
{...}

QUERY_CREDENTIALS_ATTRIBUTES_FN_W 


```

## -parameters

### -param : 
### -param long: 
### -param *: 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also