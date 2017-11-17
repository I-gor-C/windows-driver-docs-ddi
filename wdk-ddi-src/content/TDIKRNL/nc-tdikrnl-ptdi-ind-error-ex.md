---
UID: NC.tdikrnl.PTDI_IND_ERROR_EX
title: PTDI_IND_ERROR_EX
author: windows-driver-content
description: 
ms.assetid: 9b2f6a83-c859-4d6a-b5ba-d116a765a7d5
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: tdikrnl.h
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

# PTDI_IND_ERROR_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PTDI_IND_ERROR_EX PtdiIndErrorEx; 

// Definition

NTSTATUS PtdiIndErrorEx 
(
	PVOID TdiEventContext
	NTSTATUS Status
	PVOID Buffer
)
{...}

PTDI_IND_ERROR_EX 


```

## -parameters

### -param TdiEventContext: 
### -param Status: 
### -param Buffer: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also