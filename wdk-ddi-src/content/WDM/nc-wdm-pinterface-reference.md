---
UID: NC.wdm.PINTERFACE_REFERENCE
title: PINTERFACE_REFERENCE
author: windows-driver-content
description: 
ms.assetid: 24f5a189-d8e0-41c7-b71c-7f530054edcc
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

# PINTERFACE_REFERENCE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PINTERFACE_REFERENCE PinterfaceReference; 

// Definition

VOID PinterfaceReference 
(
	PVOID Context
)
{...}

PINTERFACE_REFERENCE 


```

## -parameters

### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also