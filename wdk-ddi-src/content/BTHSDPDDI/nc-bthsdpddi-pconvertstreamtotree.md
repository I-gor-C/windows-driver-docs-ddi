---
UID: NC.bthsdpddi.PCONVERTSTREAMTOTREE
title: PCONVERTSTREAMTOTREE
author: windows-driver-content
description: 
ms.assetid: da49e1e3-c8e2-4bb8-8318-d461726486be
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

# PCONVERTSTREAMTOTREE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCONVERTSTREAMTOTREE Pconvertstreamtotree; 

// Definition

NTSTATUS Pconvertstreamtotree 
(
	PUCHAR Stream
	ULONG Size
	PSDP_TREE_ROOT_NODE *Node
	ULONG tag
)
{...}

PCONVERTSTREAMTOTREE 


```

## -parameters

### -param Stream: 
### -param Size: 
### -param *Node: 
### -param tag: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also