---
UID: NC.mrx.PMRX_CREATE_V_NET_ROOT
title: PMRX_CREATE_V_NET_ROOT
author: windows-driver-content
description: 
ms.assetid: bf0d3f97-316f-43f7-904b-42b8af0ded09
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

# PMRX_CREATE_V_NET_ROOT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMRX_CREATE_V_NET_ROOT PmrxCreateVNetRoot; 

// Definition

NTSTATUS PmrxCreateVNetRoot 
(
	IN OUT PMRX_CREATENETROOT_CONTEXT Context
)
{...}

PMRX_CREATE_V_NET_ROOT 


```

## -parameters

### -param Context: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also