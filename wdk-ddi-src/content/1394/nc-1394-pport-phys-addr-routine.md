---
UID: NC.1394.PPORT_PHYS_ADDR_ROUTINE
title: PPORT_PHYS_ADDR_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 49a1a24a-a005-4a63-b483-358aebebcbd2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: 1394.h
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

# PPORT_PHYS_ADDR_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PPORT_PHYS_ADDR_ROUTINE PportPhysAddrRoutine; 

// Definition

NTSTATUS PportPhysAddrRoutine 
(
	PVOID Context
	PIRB Irb
)
{...}

PPORT_PHYS_ADDR_ROUTINE 


```

## -parameters

### -param Context: 
### -param Irb: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also