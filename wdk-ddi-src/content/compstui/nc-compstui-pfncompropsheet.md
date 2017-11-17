---
UID: NC.compstui.PFNCOMPROPSHEET
title: PFNCOMPROPSHEET
author: windows-driver-content
description: 
ms.assetid: 12d2a530-2af9-440d-bb5b-3884970a0443
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: compstui.h
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

# PFNCOMPROPSHEET callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNCOMPROPSHEET Pfncompropsheet; 

// Definition

LONG_PTR Pfncompropsheet 
(
	HANDLE hComPropSheet
	UINT Function
	LPARAM lParam1
	LPARAM lParam2
)
{...}

PFNCOMPROPSHEET 


```

## -parameters

### -param hComPropSheet: 
### -param Function: 
### -param lParam1: 
### -param lParam2: 



## -returns

Returns LONG_PTR that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also