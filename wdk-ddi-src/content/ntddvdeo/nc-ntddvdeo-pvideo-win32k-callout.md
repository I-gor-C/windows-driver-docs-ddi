---
UID: NC.ntddvdeo.PVIDEO_WIN32K_CALLOUT
title: PVIDEO_WIN32K_CALLOUT
author: windows-driver-content
description: 
ms.assetid: ccb87f5d-7ab2-47e8-a455-6967770f2050
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddvdeo.h
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

# PVIDEO_WIN32K_CALLOUT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PVIDEO_WIN32K_CALLOUT PvideoWin32kCallout; 

// Definition

VOID PvideoWin32kCallout 
(
	IN PVOID Params
)
{...}

PVIDEO_WIN32K_CALLOUT 


```

## -parameters

### -param Params: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also