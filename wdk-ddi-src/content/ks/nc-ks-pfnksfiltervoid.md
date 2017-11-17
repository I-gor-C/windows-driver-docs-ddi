---
UID: NC.ks.PFNKSFILTERVOID
title: PFNKSFILTERVOID
author: windows-driver-content
description: 
ms.assetid: 1c1b5627-0771-4706-a85a-31ec7313ed42
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

# PFNKSFILTERVOID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSFILTERVOID Pfnksfiltervoid; 

// Definition

NTSTATUS Pfnksfiltervoid 
(
	PKSFILTER Filter
)
{...}

PFNKSFILTERVOID 


```

## -parameters

### -param Filter: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also