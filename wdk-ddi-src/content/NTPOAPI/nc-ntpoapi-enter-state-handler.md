---
UID: NC.ntpoapi.ENTER_STATE_HANDLER
title: ENTER_STATE_HANDLER
author: windows-driver-content
description: 
ms.assetid: 5f1697c8-288e-4723-a8a9-bc9b80c791c0
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntpoapi.h
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

# ENTER_STATE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

ENTER_STATE_HANDLER EnterStateHandler; 

// Definition

NTSTATUS EnterStateHandler 
(
	PVOID Context
	PENTER_STATE_SYSTEM_HANDLER SystemHandler
	PVOID SystemContext
	LONG NumberProcessors
	LONG *Number
)
{...}

ENTER_STATE_HANDLER 


```

## -parameters

### -param Context: 
### -param SystemHandler: 
### -param SystemContext: 
### -param NumberProcessors: 
### -param *Number: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also