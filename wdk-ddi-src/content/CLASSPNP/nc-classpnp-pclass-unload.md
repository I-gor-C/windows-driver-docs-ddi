---
UID: NC.classpnp.PCLASS_UNLOAD
title: PCLASS_UNLOAD
author: windows-driver-content
description: 
ms.assetid: 432cd3d4-1238-413c-8738-d06f4a19eaab
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: classpnp.h
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

# PCLASS_UNLOAD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLASS_UNLOAD PclassUnload; 

// Definition

VOID PclassUnload 
(
	PDRIVER_OBJECT DriverObject
)
{...}

PCLASS_UNLOAD 


```

## -parameters

### -param DriverObject: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also