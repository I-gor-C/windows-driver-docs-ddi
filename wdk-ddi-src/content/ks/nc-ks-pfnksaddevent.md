---
UID: NC.ks.PFNKSADDEVENT
title: PFNKSADDEVENT
author: windows-driver-content
description: 
ms.assetid: 3b1003f1-0b73-4eb6-a6c7-e208ff6df076
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

# PFNKSADDEVENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSADDEVENT Pfnksaddevent; 

// Definition

NTSTATUS Pfnksaddevent 
(
	PIRP Irp
	PKSEVENTDATA EventData
	_KSEVENT_ENTRY *EventEntry
)
{...}

PFNKSADDEVENT 


```

## -parameters

### -param Irp: 
### -param EventData: 
### -param *EventEntry: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also