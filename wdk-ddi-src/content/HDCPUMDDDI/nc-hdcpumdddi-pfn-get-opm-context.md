---
UID: NC.hdcpumdddi.PFN_GET_OPM_CONTEXT
title: PFN_GET_OPM_CONTEXT
author: windows-driver-content
description: 
ms.assetid: 8add7f56-d31a-4d96-b534-5f72854f2c7e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: hdcpumdddi.h
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

# PFN_GET_OPM_CONTEXT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_GET_OPM_CONTEXT PfnGetOpmContext; 

// Definition

VOID PfnGetOpmContext 
(
	PVOID pDriverContext
	PVOID *pOPMContext
)
{...}

PFN_GET_OPM_CONTEXT 


```

## -parameters

### -param pDriverContext: 
### -param *pOPMContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also