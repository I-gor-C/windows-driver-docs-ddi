---
UID: NC.mrx.PMRX_FINALIZE_V_NET_ROOT_CALLDOWN
title: PMRX_FINALIZE_V_NET_ROOT_CALLDOWN
author: windows-driver-content
description: 
ms.assetid: 9d7bc4e9-fa08-4122-bc8c-530260471785
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: mrx.h
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

# PMRX_FINALIZE_V_NET_ROOT_CALLDOWN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMRX_FINALIZE_V_NET_ROOT_CALLDOWN PmrxFinalizeVNetRootCalldown; 

// Definition

NTSTATUS PmrxFinalizeVNetRootCalldown 
(
	IN OUT PMRX_V_NET_ROOT VirtualNetRoot
	IN PBOOLEAN Force
)
{...}

PMRX_FINALIZE_V_NET_ROOT_CALLDOWN 


```

## -parameters

### -param VirtualNetRoot: 
### -param Force: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also