---
UID: NC.hidclass.PHIDP_GETCAPS
title: PHIDP_GETCAPS
author: windows-driver-content
description: 
ms.assetid: 36828804-d0c8-4e39-8aeb-71a7b29f38af
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: hidclass.h
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

# PHIDP_GETCAPS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PHIDP_GETCAPS PhidpGetcaps; 

// Definition

NTSTATUS PhidpGetcaps 
(
	PHIDP_PREPARSED_DATA PreparsedData
	PHIDP_CAPS Capabilities
)
{...}

PHIDP_GETCAPS 


```

## -parameters

### -param PreparsedData: 
### -param Capabilities: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also