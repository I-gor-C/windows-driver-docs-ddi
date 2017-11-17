---
UID: NC.fltkernel.PFLT_GENERIC_WORKITEM_ROUTINE
title: PFLT_GENERIC_WORKITEM_ROUTINE
author: windows-driver-content
description: 
ms.assetid: dca80385-c772-4589-ac91-2567fe9206e4
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

# PFLT_GENERIC_WORKITEM_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFLT_GENERIC_WORKITEM_ROUTINE PfltGenericWorkitemRoutine; 

// Definition

VOID PfltGenericWorkitemRoutine 
(
	PFLT_GENERIC_WORKITEM FltWorkItem
	PVOID FltObject
	PVOID Context
)
{...}

PFLT_GENERIC_WORKITEM_ROUTINE 


```

## -parameters

### -param FltWorkItem: 
### -param FltObject: 
### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also