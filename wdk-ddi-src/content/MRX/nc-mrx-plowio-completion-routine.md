---
UID: NC.mrx.PLOWIO_COMPLETION_ROUTINE
title: PLOWIO_COMPLETION_ROUTINE
author: windows-driver-content
description: 
ms.assetid: dadabd4e-b5a4-4c02-9bd9-621821eaab7f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: mrx.h
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

# PLOWIO_COMPLETION_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PLOWIO_COMPLETION_ROUTINE PlowioCompletionRoutine; 

// Definition

NTSTATUS PlowioCompletionRoutine 
(
	IN PRX_CONTEXT RxContext
)
{...}

PLOWIO_COMPLETION_ROUTINE 


```

## -parameters

### -param RxContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also