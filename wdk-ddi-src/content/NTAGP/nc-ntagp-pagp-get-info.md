---
UID: NC.ntagp.PAGP_GET_INFO
title: PAGP_GET_INFO
author: windows-driver-content
description: 
ms.assetid: f78a0d75-b38b-4584-93eb-8782e4c39f0e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntagp.h
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

# PAGP_GET_INFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PAGP_GET_INFO PagpGetInfo; 

// Definition

VOID PagpGetInfo 
(
	IN PVOID AgpContext
	OUT PAGP_INFO AgpInfo
)
{...}

PAGP_GET_INFO 


```

## -parameters

### -param AgpContext: 
### -param AgpInfo: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also