---
UID: NC.ntimage.PIMAGE_TLS_CALLBACK
title: PIMAGE_TLS_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 8c1b1022-e01d-496e-8597-b05d0d422301
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntimage.h
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

# PIMAGE_TLS_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PIMAGE_TLS_CALLBACK PimageTlsCallback; 

// Definition

VOID PimageTlsCallback 
(
	PVOID DllHandle
	ULONG Reason
	PVOID Reserved
)
{...}

PIMAGE_TLS_CALLBACK 


```

## -parameters

### -param DllHandle: 
### -param Reason: 
### -param Reserved: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also