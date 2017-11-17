---
UID: NC.1394.PPORT_ALLOC_COMPLETE_NOTIFICATION
title: PPORT_ALLOC_COMPLETE_NOTIFICATION
author: windows-driver-content
description: 
ms.assetid: 0f02d730-1929-4900-8ff1-5a626a9a2458
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: 1394.h
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

# PPORT_ALLOC_COMPLETE_NOTIFICATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PPORT_ALLOC_COMPLETE_NOTIFICATION PportAllocCompleteNotification; 

// Definition

void PportAllocCompleteNotification 
(
	PVOID Context
)
{...}

PPORT_ALLOC_COMPLETE_NOTIFICATION 


```

## -parameters

### -param Context: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also