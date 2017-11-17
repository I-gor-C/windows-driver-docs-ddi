---
UID: NC.tdikrnl.PTDI_IND_RECEIVE_DATAGRAM
title: PTDI_IND_RECEIVE_DATAGRAM
author: windows-driver-content
description: 
ms.assetid: b68721f6-bc00-465d-aff2-22049ce95f4a
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

# PTDI_IND_RECEIVE_DATAGRAM callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PTDI_IND_RECEIVE_DATAGRAM PtdiIndReceiveDatagram; 

// Definition

NTSTATUS PtdiIndReceiveDatagram 
(
	PVOID TdiEventContext
	LONG SourceAddressLength
	PVOID SourceAddress
	LONG OptionsLength
	PVOID Options
	ULONG ReceiveDatagramFlags
	ULONG BytesIndicated
	ULONG BytesAvailable
	ULONG *BytesTaken
	PVOID Tsdu
	PIRP *IoRequestPacket
)
{...}

PTDI_IND_RECEIVE_DATAGRAM 


```

## -parameters

### -param TdiEventContext: 
### -param SourceAddressLength: 
### -param SourceAddress: 
### -param OptionsLength: 
### -param Options: 
### -param ReceiveDatagramFlags: 
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