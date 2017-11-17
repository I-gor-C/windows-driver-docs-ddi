---
UID: NC.bthsdpddi.PADDATTRIBUTETOTREEE
title: PADDATTRIBUTETOTREEE
author: windows-driver-content
description: 
ms.assetid: cc183a64-0f5f-458b-af1b-861b1eb049b5
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

# PADDATTRIBUTETOTREEE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PADDATTRIBUTETOTREEE Paddattributetotreee; 

// Definition

NTSTATUS Paddattributetotreee 
(
	PSDP_TREE_ROOT_NODE Root
	USHORT AttribId
	__drv_aliasesMem PSDP_NODE AttribValueNode
	ULONG tag
)
{...}

PADDATTRIBUTETOTREEE 


```

## -parameters

### -param Root: 
### -param AttribId: 
### -param AttribValueNode: 
### -param tag: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also