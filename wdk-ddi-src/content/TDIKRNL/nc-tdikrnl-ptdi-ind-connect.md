---
UID: NC.tdikrnl.PTDI_IND_CONNECT
title: PTDI_IND_CONNECT
author: windows-driver-content
description: 
ms.assetid: 0d1a4c3d-2b43-4ad3-b085-c320c97b1191
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

# PTDI_IND_CONNECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PTDI_IND_CONNECT PtdiIndConnect; 

// Definition

NTSTATUS PtdiIndConnect 
(
	PVOID TdiEventContext
	LONG RemoteAddressLength
	PVOID RemoteAddress
	LONG UserDataLength
	PVOID UserData
	LONG OptionsLength
	PVOID Options
	CONNECTION_CONTEXT *ConnectionContext
	PIRP *AcceptIrp
)
{...}

PTDI_IND_CONNECT 


```

## -parameters

### -param TdiEventContext: 
### -param RemoteAddressLength: 
### -param RemoteAddress: 
### -param UserDataLength: 
### -param UserData: 
### -param OptionsLength: 
### -param Options: 
### -param *ConnectionContext: 
### -param *AcceptIrp: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also