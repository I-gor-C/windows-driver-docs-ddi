---
UID: NC.ntagp.PAGP_CHECK_INTEGRITY
title: PAGP_CHECK_INTEGRITY
author: windows-driver-content
description: 
ms.assetid: df974ea6-864d-4620-8cc4-d353c02c404b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntagp.h
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

# PAGP_CHECK_INTEGRITY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PAGP_CHECK_INTEGRITY PagpCheckIntegrity; 

// Definition

NTSTATUS PagpCheckIntegrity 
(
	IN PVOID AgpContext
)
{...}

PAGP_CHECK_INTEGRITY 


```

## -parameters

### -param AgpContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also