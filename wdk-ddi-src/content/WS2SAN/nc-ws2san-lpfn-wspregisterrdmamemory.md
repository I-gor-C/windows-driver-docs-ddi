---
UID: NC.ws2san.LPFN_WSPREGISTERRDMAMEMORY
title: LPFN_WSPREGISTERRDMAMEMORY
author: windows-driver-content
description: 
ms.assetid: a7deb2c4-ce40-46bd-b735-8ccac9d65e8b
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

# LPFN_WSPREGISTERRDMAMEMORY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPFN_WSPREGISTERRDMAMEMORY LpfnWspregisterrdmamemory; 

// Definition

BOOL LpfnWspregisterrdmamemory 
(
	SOCKET s
	PVOID lpBuffer
	DWORD dwBufferLength
	DWORD dwFlags
	LPVOID lpRdmaBufferDescriptor
	LPDWORD lpdwDescriptorLength
	LPINT lpErrno
)
{...}

LPFN_WSPREGISTERRDMAMEMORY 


```

## -parameters

### -param s: 
### -param lpBuffer: 
### -param dwBufferLength: 
### -param dwFlags: 
### -param lpRdmaBufferDescriptor: 
### -param lpdwDescriptorLength: 
### -param lpErrno: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also