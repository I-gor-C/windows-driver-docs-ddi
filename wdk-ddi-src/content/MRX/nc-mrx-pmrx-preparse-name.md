---
UID: NC.mrx.PMRX_PREPARSE_NAME
title: PMRX_PREPARSE_NAME
author: windows-driver-content
description: 
ms.assetid: c2b1736e-6caa-433f-8672-99604c884cd8
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

# PMRX_PREPARSE_NAME callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMRX_PREPARSE_NAME PmrxPreparseName; 

// Definition

NTSTATUS PmrxPreparseName 
(
	IN OUT PRX_CONTEXT RxContext
	IN PUNICODE_STRING Name
)
{...}

PMRX_PREPARSE_NAME 


```

## -parameters

### -param RxContext: 
### -param Name: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also