---
UID: NC.wdfmemory.PFN_WDFMEMORYCREATE
title: *PFN_WDFMEMORYCREATE
author: windows-driver-content
description: 
ms.assetid: 712c46ad-0726-49f6-b335-6d13fce7a895
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

# *PFN_WDFMEMORYCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_WDFMEMORYCREATE *PfnWdfmemorycreate; 

// Definition

NTSTATUS *PfnWdfmemorycreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDF_OBJECT_ATTRIBUTES Attributes
	_Strict_type_match_ POOL_TYPE PoolType
	ULONG PoolTag
	size_t BufferSize
	WDFMEMORY *Memory
	PVOID *Buffer
)
{...}

*PFN_WDFMEMORYCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Attributes: 
### -param PoolType: 
### -param PoolTag: 
### -param BufferSize: 
### -param *Memory: 
### -param *Buffer: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also