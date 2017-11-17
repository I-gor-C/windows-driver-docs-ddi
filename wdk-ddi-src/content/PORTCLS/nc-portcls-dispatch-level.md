---
UID: NC.portcls.DISPATCH_LEVEL
title: DISPATCH_LEVEL
author: windows-driver-content
description: 
ms.assetid: 10c452f3-7e64-4353-82ab-34d4259f100c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: portcls.h
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

# DISPATCH_LEVEL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DISPATCH_LEVEL DispatchLevel; 

// Definition

_IRQL_requires_max_ DispatchLevel 
(
	*PCPFNRUNTIME_POWER_CONTROL_CALLBACK 
)
{...}

DISPATCH_LEVEL 


```

## -parameters

### -param : 



## -returns

Returns _IRQL_requires_max_ that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also