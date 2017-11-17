---
UID: NC.extsfns.ENTRY_CALLBACK
title: ENTRY_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 423d597b-0a77-4071-8a56-f2a491239868
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: extsfns.h
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

# ENTRY_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

ENTRY_CALLBACK EntryCallback; 

// Definition

HRESULT EntryCallback 
(
	ULONG64 EntryAddress
	PVOID Context
)
{...}

ENTRY_CALLBACK 


```

## -parameters

### -param EntryAddress: 
### -param Context: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also