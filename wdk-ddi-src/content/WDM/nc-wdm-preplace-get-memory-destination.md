---
UID: NC.wdm.PREPLACE_GET_MEMORY_DESTINATION
title: PREPLACE_GET_MEMORY_DESTINATION
author: windows-driver-content
description: 
ms.assetid: 7e8d5650-2c62-48a3-95bd-5cf1664429b3
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# PREPLACE_GET_MEMORY_DESTINATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PREPLACE_GET_MEMORY_DESTINATION PreplaceGetMemoryDestination; 

// Definition

NTSTATUS PreplaceGetMemoryDestination 
(
	PVOID Context
	PHYSICAL_ADDRESS SourceAddress
	PPHYSICAL_ADDRESS DestinationAddress
)
{...}

PREPLACE_GET_MEMORY_DESTINATION 


```

## -parameters

### -param Context: 
### -param SourceAddress: 
### -param DestinationAddress: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also