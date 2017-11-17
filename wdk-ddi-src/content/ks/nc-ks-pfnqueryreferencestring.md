---
UID: NC.ks.PFNQUERYREFERENCESTRING
title: PFNQUERYREFERENCESTRING
author: windows-driver-content
description: 
ms.assetid: d8d1883e-c28e-4d8c-bb3e-923ac59e0a03
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNQUERYREFERENCESTRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNQUERYREFERENCESTRING Pfnqueryreferencestring; 

// Definition

NTSTATUS Pfnqueryreferencestring 
(
	PVOID Context
	PWCHAR *String
)
{...}

PFNQUERYREFERENCESTRING 


```

## -parameters

### -param Context: 
### -param *String: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also