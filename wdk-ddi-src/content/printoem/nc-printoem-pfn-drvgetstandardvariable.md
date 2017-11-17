---
UID: NC.printoem.PFN_DrvGetStandardVariable
title: PFN_DrvGetStandardVariable
author: windows-driver-content
description: 
ms.assetid: 9e037262-e6a2-441d-806c-b7cf04552d15
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

# PFN_DrvGetStandardVariable callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_DrvGetStandardVariable PfnDrvgetstandardvariable; 

// Definition

BOOL PfnDrvgetstandardvariable 
(
	PDEVOBJ pdevobj
	DWORD dwIndex
	PVOID pBuffer
	DWORD cbSize
	PDWORD pcbNeeded
)
{...}

PFN_DrvGetStandardVariable 


```

## -parameters

### -param pdevobj: 
### -param dwIndex: 
### -param pBuffer: 
### -param cbSize: 
### -param pcbNeeded: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also