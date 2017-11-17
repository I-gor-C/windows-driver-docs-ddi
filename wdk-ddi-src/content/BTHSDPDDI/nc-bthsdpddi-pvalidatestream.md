---
UID: NC.bthsdpddi.PVALIDATESTREAM
title: PVALIDATESTREAM
author: windows-driver-content
description: 
ms.assetid: 93951e4f-b086-44d0-843c-e98826e7f7d8
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: bthsdpddi.h
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

# PVALIDATESTREAM callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PVALIDATESTREAM Pvalidatestream; 

// Definition

NTSTATUS Pvalidatestream 
(
	PUCHAR Stream
	ULONG Size
	PULONG_PTR ErrorByte
)
{...}

PVALIDATESTREAM 


```

## -parameters

### -param Stream: 
### -param Size: 
### -param ErrorByte: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also