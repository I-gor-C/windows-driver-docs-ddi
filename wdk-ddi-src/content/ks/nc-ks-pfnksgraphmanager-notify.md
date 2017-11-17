---
UID: NC.ks.PFNKSGRAPHMANAGER_NOTIFY
title: PFNKSGRAPHMANAGER_NOTIFY
author: windows-driver-content
description: 
ms.assetid: fa3236ef-2c3c-4902-9ee2-15148386e204
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNKSGRAPHMANAGER_NOTIFY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSGRAPHMANAGER_NOTIFY PfnksgraphmanagerNotify; 

// Definition

VOID PfnksgraphmanagerNotify 
(
	PFILE_OBJECT GraphManager
	ULONG EventId
	PVOID Filter
	PVOID Pin
	PVOID Frame
	ULONG Duration
)
{...}

PFNKSGRAPHMANAGER_NOTIFY 


```

## -parameters

### -param GraphManager: 
### -param EventId: 
### -param Filter: 
### -param Pin: 
### -param Frame: 
### -param Duration: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also