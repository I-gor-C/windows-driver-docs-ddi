---
UID: NC.ntddk.pHalSetSystemInformation
title: pHalSetSystemInformation
author: windows-driver-content
description: 
ms.assetid: 6127636c-6787-4953-8815-3b5cc9cbaf99
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

# pHalSetSystemInformation callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pHalSetSystemInformation Phalsetsysteminformation; 

// Definition

NTSTATUS Phalsetsysteminformation 
(
	HAL_SET_INFORMATION_CLASS InformationClass
	ULONG BufferSize
	PVOID Buffer
)
{...}

pHalSetSystemInformation 


```

## -parameters

### -param InformationClass: 
### -param BufferSize: 
### -param Buffer: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also