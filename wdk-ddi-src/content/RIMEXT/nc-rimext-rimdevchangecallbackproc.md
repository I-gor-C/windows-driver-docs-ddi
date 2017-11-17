---
UID: NC.rimext.RIMDEVCHANGECALLBACKPROC
title: RIMDEVCHANGECALLBACKPROC
author: windows-driver-content
description: 
ms.assetid: f5a516e1-69d1-4441-8f2c-bc7e864f1492
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: rimext.h
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

# RIMDEVCHANGECALLBACKPROC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

RIMDEVCHANGECALLBACKPROC Rimdevchangecallbackproc; 

// Definition

BOOL Rimdevchangecallbackproc 
(
	HANDLE hRim
	HANDLE hRimDev
	DWORD dwCode
	DWORD dwDeviceType
	DWORD dwRimInputType
	USHORT usage
	USHORT usagePage
	PVOID pvContext
)
{...}

RIMDEVCHANGECALLBACKPROC 


```

## -parameters

### -param hRim: 
### -param hRimDev: 
### -param dwCode: 
### -param dwDeviceType: 
### -param dwRimInputType: 
### -param usage: 
### -param usagePage: 
### -param pvContext: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also