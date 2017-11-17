---
UID: NC.extsfns.PGET_FULL_IMAGE_NAME
title: PGET_FULL_IMAGE_NAME
author: windows-driver-content
description: 
ms.assetid: e4fda34d-0a47-47aa-ba55-ed1fd83183e2
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

# PGET_FULL_IMAGE_NAME callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGET_FULL_IMAGE_NAME PgetFullImageName; 

// Definition

HRESULT PgetFullImageName 
(
	PDEBUG_CLIENT Client
	ULONG64 Process
	LPSTR *FullImageName
)
{...}

PGET_FULL_IMAGE_NAME 


```

## -parameters

### -param Client: 
### -param Process: 
### -param *FullImageName: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also