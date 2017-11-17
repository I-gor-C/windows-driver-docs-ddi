---
UID: NC.portcls.PCPFNMETHOD_HANDLER
title: PCPFNMETHOD_HANDLER
author: windows-driver-content
description: 
ms.assetid: f1df7fa0-d54a-48d5-b2d2-49d6b3f0c5a4
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: portcls.h
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

# PCPFNMETHOD_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCPFNMETHOD_HANDLER PcpfnmethodHandler; 

// Definition

NTSTATUS PcpfnmethodHandler 
(
	PPCMETHOD_REQUEST MethodRequest
)
{...}

PCPFNMETHOD_HANDLER 


```

## -parameters

### -param MethodRequest: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also