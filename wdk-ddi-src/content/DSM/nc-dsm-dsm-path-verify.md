---
UID: NC.dsm.DSM_PATH_VERIFY
title: DSM_PATH_VERIFY
author: windows-driver-content
description: 
ms.assetid: 8200af9f-ecaf-4a8a-a76f-7f8bd4111e35
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dsm.h
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

# DSM_PATH_VERIFY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_PATH_VERIFY DsmPathVerify; 

// Definition

NTSTATUS DsmPathVerify 
(
	IN PVOID DsmContext
	IN PVOID DsmId
	IN PVOID PathId
)
{...}

DSM_PATH_VERIFY 


```

## -parameters

### -param DsmContext: 
### -param DsmId: 
### -param PathId: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also