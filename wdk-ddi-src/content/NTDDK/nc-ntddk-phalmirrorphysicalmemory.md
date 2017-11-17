---
UID: NC.ntddk.pHalMirrorPhysicalMemory
title: pHalMirrorPhysicalMemory
author: windows-driver-content
description: 
ms.assetid: 35f42d79-ce4d-4345-982c-46e0484f13f9
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddk.h
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

# pHalMirrorPhysicalMemory callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pHalMirrorPhysicalMemory Phalmirrorphysicalmemory; 

// Definition

NTSTATUS Phalmirrorphysicalmemory 
(
	PHYSICAL_ADDRESS PhysicalAddress
	LARGE_INTEGER NumberOfBytes
)
{...}

pHalMirrorPhysicalMemory 


```

## -parameters

### -param PhysicalAddress: 
### -param NumberOfBytes: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also