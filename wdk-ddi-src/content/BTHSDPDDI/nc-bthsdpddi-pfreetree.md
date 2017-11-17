---
UID: NC.bthsdpddi.PFREETREE
title: PFREETREE
author: windows-driver-content
description: 
ms.assetid: 0917a1f6-a11b-49f0-a2c4-b3f8684ba84d
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

# PFREETREE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFREETREE Pfreetree; 

// Definition

NTSTATUS Pfreetree 
(
	__drv_freesMem(Mem)PSDP_TREE_ROOT_NODE Tree
)
{...}

PFREETREE 


```

## -parameters

### -param Tree: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also