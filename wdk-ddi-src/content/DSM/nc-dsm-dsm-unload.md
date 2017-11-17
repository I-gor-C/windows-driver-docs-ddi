---
UID: NC.dsm.DSM_UNLOAD
title: DSM_UNLOAD
author: windows-driver-content
description: 
ms.assetid: e2fd033e-7d1d-47c3-910a-97ab2223aa25
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

# DSM_UNLOAD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_UNLOAD DsmUnload; 

// Definition

NTSTATUS DsmUnload 
(
	IN PVOID DsmContext
)
{...}

DSM_UNLOAD 


```

## -parameters

### -param DsmContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also