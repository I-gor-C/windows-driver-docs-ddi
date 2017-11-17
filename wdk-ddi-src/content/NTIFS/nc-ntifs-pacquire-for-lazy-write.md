---
UID: NC.ntifs.PACQUIRE_FOR_LAZY_WRITE
title: PACQUIRE_FOR_LAZY_WRITE
author: windows-driver-content
description: 
ms.assetid: 6932fb88-8157-40dc-80d0-5aa115db5f01
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

# PACQUIRE_FOR_LAZY_WRITE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PACQUIRE_FOR_LAZY_WRITE PacquireForLazyWrite; 

// Definition

BOOLEAN PacquireForLazyWrite 
(
	PVOID Context
	BOOLEAN Wait
)
{...}

PACQUIRE_FOR_LAZY_WRITE 


```

## -parameters

### -param Context: 
### -param Wait: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also