---
UID: NC.rxdata.RxTeardownPerStreamContexts
title: RxTeardownPerStreamContexts
author: windows-driver-content
description: 
ms.assetid: 996373fd-a6bf-4d3b-b06b-0d7da1c69cd9
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: rxdata.h
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

# RxTeardownPerStreamContexts callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

RxTeardownPerStreamContexts Rxteardownperstreamcontexts; 

// Definition

VOID Rxteardownperstreamcontexts 
(
	IN PFSRTL_ADVANCED_FCB_HEADER
)
{...}

RxTeardownPerStreamContexts 


```

## -parameters

### -param PFSRTL_ADVANCED_FCB_HEADER: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also