---
UID: NC.mf.MF_ENUMERATE_CHILD
title: MF_ENUMERATE_CHILD
author: windows-driver-content
description: 
ms.assetid: 260302ad-a237-44b4-9b84-8794444e9ea2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: mf.h
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

# MF_ENUMERATE_CHILD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

MF_ENUMERATE_CHILD MfEnumerateChild; 

// Definition

NTSTATUS MfEnumerateChild 
(
	PVOID Context
	ULONG Index
	PMF_DEVICE_INFO ChildInfo
)
{...}

MF_ENUMERATE_CHILD PMF_ENUMERATE_CHILD


```

## -parameters

### -param Context: 
### -param Index: 
### -param ChildInfo: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also