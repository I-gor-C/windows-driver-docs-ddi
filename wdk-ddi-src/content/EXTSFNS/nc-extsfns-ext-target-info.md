---
UID: NC.extsfns.EXT_TARGET_INFO
title: EXT_TARGET_INFO
author: windows-driver-content
description: 
ms.assetid: a95d5ac8-6bd9-4449-b5f1-8a705f2e564c
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

# EXT_TARGET_INFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EXT_TARGET_INFO ExtTargetInfo; 

// Definition

HRESULT ExtTargetInfo 
(
	PDEBUG_CLIENT4 Client
	PTARGET_DEBUG_INFO pTargetInfo
)
{...}

EXT_TARGET_INFO 


```

## -parameters

### -param Client: 
### -param pTargetInfo: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also