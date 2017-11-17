---
UID: NC.wsk.PFN_WSK_CONNECT_EX
title: PFN_WSK_CONNECT_EX
author: windows-driver-content
description: 
ms.assetid: d10b16e1-244c-4439-906f-fe9aad0d015b
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

# PFN_WSK_CONNECT_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WSK_CONNECT_EX PfnWskConnectEx; 

// Definition

NTSTATUS PfnWskConnectEx 
(
	PWSK_SOCKET Socket
	PSOCKADDR RemoteAddress
	PWSK_BUF Buffer
	ULONG Flags
	PIRP Irp
)
{...}

PFN_WSK_CONNECT_EX 


```

## -parameters

### -param Socket: 
### -param RemoteAddress: 
### -param Buffer: 
### -param Flags: 
### -param Irp: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also