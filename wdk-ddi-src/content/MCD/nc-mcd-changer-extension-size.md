---
UID: NC.mcd.CHANGER_EXTENSION_SIZE
title: CHANGER_EXTENSION_SIZE
author: windows-driver-content
description: 
ms.assetid: fa0ad24e-bbc5-4f63-afec-9e97b7851e58
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: mcd.h
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

# CHANGER_EXTENSION_SIZE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

CHANGER_EXTENSION_SIZE ChangerExtensionSize; 

// Definition

ULONG ChangerExtensionSize 
(
	 VOID
)
{...}

CHANGER_EXTENSION_SIZE 


```

## -parameters

### -param VOID: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also