---
UID: NC.printoem.PFN_DrvWriteSpoolBuf
title: PFN_DrvWriteSpoolBuf
author: windows-driver-content
description: 
ms.assetid: 714f386a-f133-4748-acec-3913ce32fce9
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

# PFN_DrvWriteSpoolBuf callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_DrvWriteSpoolBuf PfnDrvwritespoolbuf; 

// Definition

DWORD PfnDrvwritespoolbuf 
(
	PDEVOBJ pdevobj
	PVOID pBuffer
	DWORD cbSize
)
{...}

PFN_DrvWriteSpoolBuf 


```

## -parameters

### -param pdevobj: 
### -param pBuffer: 
### -param cbSize: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also