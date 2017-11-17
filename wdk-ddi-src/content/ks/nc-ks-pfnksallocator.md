---
UID: NC.ks.PFNKSALLOCATOR
title: PFNKSALLOCATOR
author: windows-driver-content
description: 
ms.assetid: 2fc64452-e6d7-461a-ac39-1cc4c2f6a1c6
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNKSALLOCATOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSALLOCATOR Pfnksallocator; 

// Definition

NTSTATUS Pfnksallocator 
(
	PIRP Irp
	ULONG BufferSize
	BOOLEAN InputOperation
)
{...}

PFNKSALLOCATOR 


```

## -parameters

### -param Irp: 
### -param BufferSize: 
### -param InputOperation: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also