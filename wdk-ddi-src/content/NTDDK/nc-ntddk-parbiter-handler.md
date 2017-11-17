---
UID: NC.ntddk.PARBITER_HANDLER
title: PARBITER_HANDLER
author: windows-driver-content
description: 
ms.assetid: d0fb4953-d391-4440-ae6c-35303358f189
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddk.h
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

# PARBITER_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PARBITER_HANDLER ParbiterHandler; 

// Definition

NTSTATUS ParbiterHandler 
(
	PVOID Context
	ARBITER_ACTION Action
	PARBITER_PARAMETERS Parameters
)
{...}

PARBITER_HANDLER 


```

## -parameters

### -param Context: 
### -param Action: 
### -param Parameters: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also