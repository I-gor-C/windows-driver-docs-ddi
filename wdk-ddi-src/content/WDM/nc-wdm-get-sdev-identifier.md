---
UID: NC.wdm.GET_SDEV_IDENTIFIER
title: GET_SDEV_IDENTIFIER
author: windows-driver-content
description: 
ms.assetid: 58ffbdd9-dcb2-49c2-ac0e-8cbbd91f1f26
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# GET_SDEV_IDENTIFIER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GET_SDEV_IDENTIFIER GetSdevIdentifier; 

// Definition

ULONGLONG GetSdevIdentifier 
(
	PVOID InterfaceContext
)
{...}

GET_SDEV_IDENTIFIER PGET_SDEV_IDENTIFIER


```

## -parameters

### -param InterfaceContext: 



## -returns

Returns ULONGLONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also