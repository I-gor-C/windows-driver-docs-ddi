---
UID: NC.extsfns.PGET_CPU_MICROCODE_VERSION
title: PGET_CPU_MICROCODE_VERSION
author: windows-driver-content
description: 
ms.assetid: 00faa80f-5cfe-4bed-802d-9be7dff47759
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: extsfns.h
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

# PGET_CPU_MICROCODE_VERSION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGET_CPU_MICROCODE_VERSION PgetCpuMicrocodeVersion; 

// Definition

HRESULT PgetCpuMicrocodeVersion 
(
	IN PDEBUG_CLIENT Client
	OUT PDEBUG_CPU_MICROCODE_VERSION pCpuMicrocodeVersion
)
{...}

PGET_CPU_MICROCODE_VERSION 


```

## -parameters

### -param Client: 
### -param pCpuMicrocodeVersion: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also