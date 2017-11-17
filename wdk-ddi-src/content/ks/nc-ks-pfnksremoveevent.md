---
UID: NC.ks.PFNKSREMOVEEVENT
title: PFNKSREMOVEEVENT
author: windows-driver-content
description: 
ms.assetid: 83357ccb-33f9-49dd-8cef-5b95ab5d165b
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

# PFNKSREMOVEEVENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSREMOVEEVENT Pfnksremoveevent; 

// Definition

VOID Pfnksremoveevent 
(
	PFILE_OBJECT FileObject
	_KSEVENT_ENTRY *EventEntry
)
{...}

PFNKSREMOVEEVENT 


```

## -parameters

### -param FileObject: 
### -param *EventEntry: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also