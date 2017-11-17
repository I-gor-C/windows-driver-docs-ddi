---
UID: NC.tlvgeneratorparser.TlvDumperCallback
title: TlvDumperCallback
author: windows-driver-content
description: 
ms.assetid: c6750c5f-ed49-43ec-9c22-d2e45c40f1fa
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: tlvgeneratorparser.hpp
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

# TlvDumperCallback callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

TlvDumperCallback Tlvdumpercallback; 

// Definition

_Function_class_(TlvDumperCallback) void Tlvdumpercallback 
(
	UINT_PTR Context
	PCSTR Format
	 ...
)
{...}

TlvDumperCallback 


```

## -parameters

### -param Context: 
### -param Format: 
### -param ...: 



## -returns

Returns _Function_class_(TlvDumperCallback) void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also