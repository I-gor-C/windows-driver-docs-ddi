---
UID: NC.parallel.PPARALLEL_DESELECT_DEVICE
title: PPARALLEL_DESELECT_DEVICE
author: windows-driver-content
description: 
ms.assetid: 54fe1c16-740a-4703-ad03-5ce2b9acbff2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: parallel.h
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

# PPARALLEL_DESELECT_DEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PPARALLEL_DESELECT_DEVICE PparallelDeselectDevice; 

// Definition

NTSTATUS PparallelDeselectDevice 
(
	PVOID Context
	PARALLEL_1284_COMMAND Command
)
{...}

PPARALLEL_DESELECT_DEVICE 


```

## -parameters

### -param Context: 
### -param Command: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also