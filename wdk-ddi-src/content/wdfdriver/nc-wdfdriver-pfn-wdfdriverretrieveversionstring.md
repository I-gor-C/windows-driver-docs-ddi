---
UID: NC.wdfdriver.PFN_WDFDRIVERRETRIEVEVERSIONSTRING
title: PFN_WDFDRIVERRETRIEVEVERSIONSTRING
author: windows-driver-content
description: 
ms.assetid: 3d7e7814-4f24-4c57-afc4-808568e36672
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdriver.h
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

# PFN_WDFDRIVERRETRIEVEVERSIONSTRING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDRIVERRETRIEVEVERSIONSTRING PfnWdfdriverretrieveversionstring; 

// Definition

WDFAPI PfnWdfdriverretrieveversionstring 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDRIVER Driver
	WDFSTRING String
)
{...}

PFN_WDFDRIVERRETRIEVEVERSIONSTRING 


```

## -parameters

### -param DriverGlobals: 
### -param Driver: 
### -param String: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also