---
UID: NC.wdm.PREPLACE_SET_PROCESSOR_ID
title: PREPLACE_SET_PROCESSOR_ID
author: windows-driver-content
description: 
ms.assetid: 87dfe6f5-ce12-466c-9cae-76d20b6d0053
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# PREPLACE_SET_PROCESSOR_ID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PREPLACE_SET_PROCESSOR_ID PreplaceSetProcessorId; 

// Definition

NTSTATUS PreplaceSetProcessorId 
(
	PVOID Context
	ULONG ApicId
	BOOLEAN Target
)
{...}

PREPLACE_SET_PROCESSOR_ID 


```

## -parameters

### -param Context: 
### -param ApicId: 
### -param Target: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also