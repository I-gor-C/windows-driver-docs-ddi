---
UID: NC.ntddk.pKdMapPhysicalMemory64
title: pKdMapPhysicalMemory64
author: windows-driver-content
description: 
ms.assetid: 681acb5e-bbb4-47aa-ac6f-8b054680acd4
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

# pKdMapPhysicalMemory64 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pKdMapPhysicalMemory64 Pkdmapphysicalmemory64; 

// Definition

PVOID Pkdmapphysicalmemory64 
(
	PHYSICAL_ADDRESS PhysicalAddress
	ULONG NumberPages
	BOOLEAN FlushCurrentTLB
)
{...}

pKdMapPhysicalMemory64 


```

## -parameters

### -param PhysicalAddress: 
### -param NumberPages: 
### -param FlushCurrentTLB: 



## -returns

Returns PVOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also