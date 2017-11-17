---
UID: NC.miniport.PINTERFACE_DEREFERENCE
title: PINTERFACE_DEREFERENCE
author: windows-driver-content
description: 
ms.assetid: a6400095-35e7-44b2-82e0-6a79d84a15cf
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: miniport.h
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

# PINTERFACE_DEREFERENCE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PINTERFACE_DEREFERENCE PinterfaceDereference; 

// Definition

VOID PinterfaceDereference 
(
	PVOID Context
)
{...}

PINTERFACE_DEREFERENCE 


```

## -parameters

### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also