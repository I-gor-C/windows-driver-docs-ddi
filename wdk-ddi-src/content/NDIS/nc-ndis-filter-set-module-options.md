---
UID: NC.ndis.FILTER_SET_MODULE_OPTIONS
title: FILTER_SET_MODULE_OPTIONS
author: windows-driver-content
description: 
ms.assetid: 467643b2-7851-490a-90a4-f43680a634bf
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ndis.h
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

# FILTER_SET_MODULE_OPTIONS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

FILTER_SET_MODULE_OPTIONS FilterSetModuleOptions; 

// Definition

NDIS_STATUS FilterSetModuleOptions 
(
	NDIS_HANDLE FilterModuleContext
)
{...}

FILTER_SET_MODULE_OPTIONS PFILTER_SET_MODULE_OPTIONS


```

## -parameters

### -param FilterModuleContext: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also