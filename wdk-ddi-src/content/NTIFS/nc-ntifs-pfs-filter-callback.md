---
UID: NC.ntifs.PFS_FILTER_CALLBACK
title: PFS_FILTER_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 194e1a2d-9952-4892-8cf1-72b5ed28018f
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

# PFS_FILTER_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFS_FILTER_CALLBACK PfsFilterCallback; 

// Definition

NTSTATUS PfsFilterCallback 
(
	PFS_FILTER_CALLBACK_DATA Data
	PVOID *CompletionContext
)
{...}

PFS_FILTER_CALLBACK 


```

## -parameters

### -param Data: 
### -param *CompletionContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also