---
UID: NC.fltkernel.PFLT_DEFERRED_IO_WORKITEM_ROUTINE
title: PFLT_DEFERRED_IO_WORKITEM_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 9f8c940e-cea4-4244-ab92-437e77364dfa
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: fltkernel.h
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

# PFLT_DEFERRED_IO_WORKITEM_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFLT_DEFERRED_IO_WORKITEM_ROUTINE PfltDeferredIoWorkitemRoutine; 

// Definition

VOID PfltDeferredIoWorkitemRoutine 
(
	PFLT_DEFERRED_IO_WORKITEM FltWorkItem
	PFLT_CALLBACK_DATA CallbackData
	PVOID Context
)
{...}

PFLT_DEFERRED_IO_WORKITEM_ROUTINE 


```

## -parameters

### -param FltWorkItem: 
### -param CallbackData: 
### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also