---
UID: NC.wsk.PFN_WSK_SEND_MESSAGES
title: PFN_WSK_SEND_MESSAGES
author: windows-driver-content
description: 
ms.assetid: 2ccbb47c-d687-4c4a-8419-3bf377646309
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wsk.h
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

# PFN_WSK_SEND_MESSAGES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WSK_SEND_MESSAGES PfnWskSendMessages; 

// Definition

NTSTATUS PfnWskSendMessages 
(
	PWSK_SOCKET Socket
	PWSK_BUF_LIST BufferList
	ULONG Flags
	PSOCKADDR RemoteAddress
	ULONG ControlInfoLength
	PCMSGHDR ControlInfo
	PIRP Irp
)
{...}

PFN_WSK_SEND_MESSAGES 


```

## -parameters

### -param Socket: 
### -param BufferList: 
### -param Flags: 
### -param RemoteAddress: 
### -param ControlInfoLength: 
### -param ControlInfo: 
### -param Irp: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also