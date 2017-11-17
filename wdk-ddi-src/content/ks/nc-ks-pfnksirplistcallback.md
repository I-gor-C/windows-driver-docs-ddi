---
UID: NC.ks.PFNKSIRPLISTCALLBACK
title: PFNKSIRPLISTCALLBACK
author: windows-driver-content
description: 
ms.assetid: b00902e7-6476-4b55-b583-690fcb81e50e
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

# PFNKSIRPLISTCALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSIRPLISTCALLBACK Pfnksirplistcallback; 

// Definition

NTSTATUS Pfnksirplistcallback 
(
	PIRP Irp
	PVOID Context
)
{...}

PFNKSIRPLISTCALLBACK 


```

## -parameters

### -param Irp: 
### -param Context: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also