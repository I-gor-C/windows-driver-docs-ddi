---
UID: NC.ntifs.PFN_FSRTLTEARDOWNPERSTREAMCONTEXTS
title: PFN_FSRTLTEARDOWNPERSTREAMCONTEXTS
author: windows-driver-content
description: 
ms.assetid: 60c55176-14d8-4b48-898b-855a8e57f999
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntifs.h
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

# PFN_FSRTLTEARDOWNPERSTREAMCONTEXTS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_FSRTLTEARDOWNPERSTREAMCONTEXTS PfnFsrtlteardownperstreamcontexts; 

// Definition

VOID PfnFsrtlteardownperstreamcontexts 
(
	PFSRTL_ADVANCED_FCB_HEADER AdvancedHeader
)
{...}

PFN_FSRTLTEARDOWNPERSTREAMCONTEXTS 


```

## -parameters

### -param AdvancedHeader: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also