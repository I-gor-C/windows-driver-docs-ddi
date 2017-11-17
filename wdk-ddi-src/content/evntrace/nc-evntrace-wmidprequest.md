---
UID: NC.evntrace.WMIDPREQUEST
title: WMIDPREQUEST
author: windows-driver-content
description: 
ms.assetid: a6da9642-1e72-47c5-be79-dc4b719ba8e9
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: evntrace.h
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

# WMIDPREQUEST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

WMIDPREQUEST Wmidprequest; 

// Definition

ULONG Wmidprequest 
(
	WMIDPREQUESTCODE RequestCode
	PVOID RequestContext
	ULONG *BufferSize
	PVOID Buffer
)
{...}

WMIDPREQUEST 


```

## -parameters

### -param RequestCode: 
### -param RequestContext: 
### -param *BufferSize: 
### -param Buffer: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also