---
UID: NC.miniport.PINTERFACE_REFERENCE
title: PINTERFACE_REFERENCE
author: windows-driver-content
description: 
ms.assetid: 0cec43c0-ef2c-4f62-b83d-84d1848c15e5
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: miniport.h
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