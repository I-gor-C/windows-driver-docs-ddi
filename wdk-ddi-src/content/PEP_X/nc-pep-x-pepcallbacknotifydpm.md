---
UID: NC.pep_x.PEPCALLBACKNOTIFYDPM
title: PEPCALLBACKNOTIFYDPM
author: windows-driver-content
description: 
ms.assetid: 2d6a83b8-e7b6-4ea6-8c96-a9b8cbeb2aa8
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: pep_x.h
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

# PEPCALLBACKNOTIFYDPM callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PEPCALLBACKNOTIFYDPM Pepcallbacknotifydpm; 

// Definition

BOOLEAN Pepcallbacknotifydpm 
(
	ULONG Notification
	PVOID Data
)
{...}

PEPCALLBACKNOTIFYDPM PPEPCALLBACKNOTIFYDPM


```

## -parameters

### -param Notification: 
### -param Data: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also