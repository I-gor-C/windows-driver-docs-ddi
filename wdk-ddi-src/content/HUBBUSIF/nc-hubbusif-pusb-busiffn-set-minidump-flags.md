---
UID: NC.hubbusif.PUSB_BUSIFFN_SET_MINIDUMP_FLAGS
title: PUSB_BUSIFFN_SET_MINIDUMP_FLAGS
author: windows-driver-content
description: 
ms.assetid: ed765b16-e1cc-47ab-9963-fcdf31a2f1e5
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: hubbusif.h
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

# PUSB_BUSIFFN_SET_MINIDUMP_FLAGS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PUSB_BUSIFFN_SET_MINIDUMP_FLAGS PusbBusiffnSetMinidumpFlags; 

// Definition

VOID PusbBusiffnSetMinidumpFlags 
(
	IN PVOID
)
{...}

PUSB_BUSIFFN_SET_MINIDUMP_FLAGS 


```

## -parameters

### -param PVOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also