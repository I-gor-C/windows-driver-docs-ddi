---
UID: NC.rilapi.RILRESULTCALLBACK
title: RILRESULTCALLBACK
author: windows-driver-content
description: 
ms.assetid: 4c21985f-f951-4a09-877d-6ab18c309fe0
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

# RILRESULTCALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

RILRESULTCALLBACK Rilresultcallback; 

// Definition

void Rilresultcallback 
(
	HRIL hRil
	DWORD dwCode
	LPVOID usersContext
	 const void *lpData
	DWORD cbData
	LPVOID lpParam
)
{...}

RILRESULTCALLBACK 


```

## -parameters

### -param hRil: 
### -param dwCode: 
### -param usersContext: 
### -param *lpData: 
### -param cbData: 
### -param lpParam: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also