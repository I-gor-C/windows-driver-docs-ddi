---
UID: NC.ws2san.LPFN_WSPREGISTERMEMORY
title: LPFN_WSPREGISTERMEMORY
author: windows-driver-content
description: 
ms.assetid: 3befedc4-4cd5-49f5-b74e-5b93b3326495
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ws2san.h
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

# LPFN_WSPREGISTERMEMORY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPFN_WSPREGISTERMEMORY LpfnWspregistermemory; 

// Definition

HANDLE LpfnWspregistermemory 
(
	SOCKET s
	PVOID lpBuffer
	DWORD dwBufferLength
	DWORD dwFlags
	LPINT lpErrno
)
{...}

LPFN_WSPREGISTERMEMORY 


```

## -parameters

### -param s: 
### -param lpBuffer: 
### -param dwBufferLength: 
### -param dwFlags: 
### -param lpErrno: 



## -returns

Returns HANDLE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also