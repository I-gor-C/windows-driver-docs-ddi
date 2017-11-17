---
UID: NC.umdprovider.PFNUMDETW_RUNDOWN
title: PFNUMDETW_RUNDOWN
author: windows-driver-content
description: 
ms.assetid: 59037281-7b90-4677-9b34-b76a8f8e0962
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: umdprovider.h
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

# PFNUMDETW_RUNDOWN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNUMDETW_RUNDOWN PfnumdetwRundown; 

// Definition

void PfnumdetwRundown 
(
	 
)
{...}

PFNUMDETW_RUNDOWN 


```

## -parameters

### -param : 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also