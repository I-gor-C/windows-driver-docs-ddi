---
UID: NC.wdm.RTL_QUERY_REGISTRY_ROUTINE
title: RTL_QUERY_REGISTRY_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 845cbfb1-9c77-4d7f-8523-bb9cf423af89
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

# RTL_QUERY_REGISTRY_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

RTL_QUERY_REGISTRY_ROUTINE RtlQueryRegistryRoutine; 

// Definition

_IRQL_requires_same_ NTSTATUS RtlQueryRegistryRoutine 
(
	PWSTR ValueName
	ULONG ValueType
	PVOID ValueData
	ULONG ValueLength
	PVOID Context
	PVOID EntryContext
)
{...}

RTL_QUERY_REGISTRY_ROUTINE PRTL_QUERY_REGISTRY_ROUTINE


```

## -parameters

### -param ValueName: 
### -param ValueType: 
### -param ValueData: 
### -param ValueLength: 
### -param Context: 
### -param EntryContext: 



## -returns

Returns _IRQL_requires_same_ NTSTATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also