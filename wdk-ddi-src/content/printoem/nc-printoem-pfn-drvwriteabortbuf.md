---
UID: NC.printoem.PFN_DrvWriteAbortBuf
title: PFN_DrvWriteAbortBuf
author: windows-driver-content
description: 
ms.assetid: e5456e1c-07e6-4b09-a550-2ae66d1607b1
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: printoem.h
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

# PFN_DrvWriteAbortBuf callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_DrvWriteAbortBuf PfnDrvwriteabortbuf; 

// Definition

DWORD PfnDrvwriteabortbuf 
(
	PDEVOBJ pdevobj
	PVOID pBuffer
	DWORD cbSize
	DWORD dwWait
)
{...}

PFN_DrvWriteAbortBuf 


```

## -parameters

### -param pdevobj: 
### -param pBuffer: 
### -param cbSize: 
### -param dwWait: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also