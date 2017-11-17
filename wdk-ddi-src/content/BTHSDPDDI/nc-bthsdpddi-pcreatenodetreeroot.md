---
UID: NC.bthsdpddi.PCREATENODETREEROOT
title: PCREATENODETREEROOT
author: windows-driver-content
description: 
ms.assetid: 93deae2a-1f77-4c2f-9034-3e02b9dae14b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: bthsdpddi.h
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

# PCREATENODETREEROOT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCREATENODETREEROOT Pcreatenodetreeroot; 

// Definition

PSDP_TREE_ROOT_NODE Pcreatenodetreeroot 
(
	ULONG tag
)
{...}

PCREATENODETREEROOT 


```

## -parameters

### -param tag: 



## -returns

Returns PSDP_TREE_ROOT_NODE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also