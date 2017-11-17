---
UID: NC.printoem.PFN_DrvUpdateUISetting
title: PFN_DrvUpdateUISetting
author: windows-driver-content
description: 
ms.assetid: c8ba2109-8025-4f06-91ef-c07181d894d5
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

# PFN_DrvUpdateUISetting callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_DrvUpdateUISetting PfnDrvupdateuisetting; 

// Definition

BOOL PfnDrvupdateuisetting 
(
	PVOID pdriverobj
	PVOID pOptItem
	DWORD dwPreviousSelection
	DWORD dwMode
)
{...}

PFN_DrvUpdateUISetting 


```

## -parameters

### -param pdriverobj: 
### -param pOptItem: 
### -param dwPreviousSelection: 
### -param dwMode: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also