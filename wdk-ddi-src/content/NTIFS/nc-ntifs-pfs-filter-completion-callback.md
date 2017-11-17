---
UID: NC.ntifs.PFS_FILTER_COMPLETION_CALLBACK
title: PFS_FILTER_COMPLETION_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 6e452faf-6856-4f56-84b8-4df1e71c242a
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntifs.h
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

# PFS_FILTER_COMPLETION_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFS_FILTER_COMPLETION_CALLBACK PfsFilterCompletionCallback; 

// Definition

VOID PfsFilterCompletionCallback 
(
	PFS_FILTER_CALLBACK_DATA Data
	NTSTATUS OperationStatus
	PVOID CompletionContext
)
{...}

PFS_FILTER_COMPLETION_CALLBACK 


```

## -parameters

### -param Data: 
### -param OperationStatus: 
### -param CompletionContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also