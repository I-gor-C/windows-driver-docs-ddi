---
UID: NC.tdikrnl.PTDI_IND_RECEIVE
title: PTDI_IND_RECEIVE
author: windows-driver-content
description: 
ms.assetid: d860edb0-eee9-42c1-9028-42566732f389
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

# PTDI_IND_RECEIVE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PTDI_IND_RECEIVE PtdiIndReceive; 

// Definition

NTSTATUS PtdiIndReceive 
(
	PVOID TdiEventContext
	CONNECTION_CONTEXT ConnectionContext
	ULONG ReceiveFlags
	ULONG BytesIndicated
	ULONG BytesAvailable
	ULONG *BytesTaken
	PVOID Tsdu
	PIRP *IoRequestPacket
)
{...}

PTDI_IND_RECEIVE 


```

## -parameters

### -param TdiEventContext: 
### -param ConnectionContext: 
### -param ReceiveFlags: 
### -param BytesIndicated: 
### -param BytesAvailable: 
### -param *BytesTaken: 
### -param Tsdu: 
### -param *IoRequestPacket: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also