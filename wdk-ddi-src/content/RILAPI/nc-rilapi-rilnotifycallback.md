---
UID: NC.rilapi.RILNOTIFYCALLBACK
title: RILNOTIFYCALLBACK
author: windows-driver-content
description: 
ms.assetid: eb4a8c99-6e7c-4372-bee3-0f0d97e3e8e0
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: rilapi.h
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

# RILNOTIFYCALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

RILNOTIFYCALLBACK Rilnotifycallback; 

// Definition

void Rilnotifycallback 
(
	HRIL hRil
	DWORD dwCode
	 const void *lpData
	DWORD cbData
	LPVOID lpParam
)
{...}

RILNOTIFYCALLBACK 


```

## -parameters

### -param hRil: 
### -param dwCode: 
### -param *lpData: 
### -param cbData: 
### -param lpParam: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also