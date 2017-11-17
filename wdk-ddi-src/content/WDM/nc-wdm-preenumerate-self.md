---
UID: NC.wdm.PREENUMERATE_SELF
title: PREENUMERATE_SELF
author: windows-driver-content
description: 
ms.assetid: 3ae57468-e510-45d0-85e6-fffb30e1e808
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# PREENUMERATE_SELF callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PREENUMERATE_SELF PreenumerateSelf; 

// Definition

VOID PreenumerateSelf 
(
	PVOID Context
)
{...}

PREENUMERATE_SELF 


```

## -parameters

### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also