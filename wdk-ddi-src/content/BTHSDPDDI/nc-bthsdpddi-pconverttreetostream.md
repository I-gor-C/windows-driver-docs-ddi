---
UID: NC.bthsdpddi.PCONVERTTREETOSTREAM
title: PCONVERTTREETOSTREAM
author: windows-driver-content
description: 
ms.assetid: bdc1a5fa-516a-4d4d-8b55-7d06e77bb697
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

# PCONVERTTREETOSTREAM callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCONVERTTREETOSTREAM Pconverttreetostream; 

// Definition

NTSTATUS Pconverttreetostream 
(
	PSDP_TREE_ROOT_NODE Root
	PUCHAR *Stream
	PULONG Size
	ULONG tag
)
{...}

PCONVERTTREETOSTREAM 


```

## -parameters

### -param Root: 
### -param *Stream: 
### -param Size: 
### -param tag: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also