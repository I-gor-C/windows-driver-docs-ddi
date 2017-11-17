---
UID: NC.rxcehdlr.PRXCE_IND_RECEIVE_DATAGRAM
title: PRXCE_IND_RECEIVE_DATAGRAM
author: windows-driver-content
description: 
ms.assetid: a23d6aaf-4911-4595-abc8-cd9fb5f056df
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: rxcehdlr.h
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

# PRXCE_IND_RECEIVE_DATAGRAM callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PRXCE_IND_RECEIVE_DATAGRAM PrxceIndReceiveDatagram; 

// Definition

NTSTATUS PrxceIndReceiveDatagram 
(
	IN PVOID pRxCeEventContext
	IN int SourceAddressLength
	IN PVOID SourceAddress
	IN int OptionsLength
	IN PVOID Options
	IN ULONG ReceiveDatagramFlags
	IN ULONG BytesIndicated
	IN ULONG BytesAvailable
	OUT ULONG *BytesTaken
	IN PVOID Tsdu
	OUT PMDL *pDataBufferPointer
	OUT PULONG pDataBufferSize
)
{...}

PRXCE_IND_RECEIVE_DATAGRAM 


```

## -parameters

### -param pRxCeEventContext: 
### -param SourceAddressLength: 
### -param SourceAddress: 
### -param OptionsLength: 
### -param Options: 
### -param ReceiveDatagramFlags: 
### -param BytesIndicated: 
### -param BytesAvailable: 
### -param *BytesTaken: 
### -param Tsdu: 
### -param *pDataBufferPointer: 
### -param pDataBufferSize: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also