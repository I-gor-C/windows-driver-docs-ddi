---
UID: NC.mrx.PMRX_EXTENDFILE_CALLDOWN
title: PMRX_EXTENDFILE_CALLDOWN
author: windows-driver-content
description: 
ms.assetid: d3e954b0-5a7e-4929-8f05-cc3155043c4b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: mrx.h
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

# PMRX_EXTENDFILE_CALLDOWN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMRX_EXTENDFILE_CALLDOWN PmrxExtendfileCalldown; 

// Definition

ULONG PmrxExtendfileCalldown 
(
	IN OUT PRX_CONTEXT RxContext
	IN OUT PLARGE_INTEGER NewFileSize
	OUT PLARGE_INTEGER NewAllocationSize
)
{...}

PMRX_EXTENDFILE_CALLDOWN 


```

## -parameters

### -param RxContext: 
### -param NewFileSize: 
### -param NewAllocationSize: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also