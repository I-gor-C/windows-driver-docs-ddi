---
UID: NC.printoem.PFN_DrvGetDriverSetting
title: PFN_DrvGetDriverSetting
author: windows-driver-content
description: 
ms.assetid: 6053411b-adc9-4be0-925f-c9c117f5f9e0
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

# PFN_DrvGetDriverSetting callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_DrvGetDriverSetting PfnDrvgetdriversetting; 

// Definition

BOOL PfnDrvgetdriversetting 
(
	PVOID pdriverobj
	PCSTR Feature
	PVOID pOutput
	DWORD cbSize
	PDWORD pcbNeeded
	PDWORD pdwOptionsReturned
)
{...}

PFN_DrvGetDriverSetting 


```

## -parameters

### -param pdriverobj: 
### -param Feature: 
### -param pOutput: 
### -param cbSize: 
### -param pcbNeeded: 
### -param pdwOptionsReturned: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also