---
UID: NC.tdikrnl.PTDI_IND_SEND_POSSIBLE
title: PTDI_IND_SEND_POSSIBLE
author: windows-driver-content
description: 
ms.assetid: 68eed069-4bb9-41a7-bbf7-f9d7411e5323
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

# PTDI_IND_SEND_POSSIBLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PTDI_IND_SEND_POSSIBLE PtdiIndSendPossible; 

// Definition

NTSTATUS PtdiIndSendPossible 
(
	PVOID TdiEventContext
	PVOID ConnectionContext
	ULONG BytesAvailable
)
{...}

PTDI_IND_SEND_POSSIBLE 


```

## -parameters

### -param TdiEventContext: 
### -param ConnectionContext: 
### -param BytesAvailable: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also