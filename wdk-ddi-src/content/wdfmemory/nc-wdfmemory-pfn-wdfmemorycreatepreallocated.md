---
UID: NC.wdfmemory.PFN_WDFMEMORYCREATEPREALLOCATED
title: PFN_WDFMEMORYCREATEPREALLOCATED
author: windows-driver-content
description: 
ms.assetid: 68611247-b6f1-48a3-afc5-fac8161c45db
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfmemory.h
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

# PFN_WDFMEMORYCREATEPREALLOCATED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFMEMORYCREATEPREALLOCATED PfnWdfmemorycreatepreallocated; 

// Definition

WDFAPI PfnWdfmemorycreatepreallocated 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDF_OBJECT_ATTRIBUTES Attributes
	__drv_aliasesMem PVOID
	size_t BufferSize
	WDFMEMORY *Memory
)
{...}

PFN_WDFMEMORYCREATEPREALLOCATED 


```

## -parameters

### -param DriverGlobals: 
### -param Attributes: 
### -param PVOID: 
### -param BufferSize: 
### -param *Memory: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also