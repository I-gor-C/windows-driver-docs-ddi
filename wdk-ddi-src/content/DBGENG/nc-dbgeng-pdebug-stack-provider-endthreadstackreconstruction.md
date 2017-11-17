---
UID: NC.dbgeng.PDEBUG_STACK_PROVIDER_ENDTHREADSTACKRECONSTRUCTION
title: PDEBUG_STACK_PROVIDER_ENDTHREADSTACKRECONSTRUCTION
author: windows-driver-content
description: 
ms.assetid: d13fb2e4-eddf-4d4e-9bd5-57e85d894803
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dbgeng.h
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

# PDEBUG_STACK_PROVIDER_ENDTHREADSTACKRECONSTRUCTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDEBUG_STACK_PROVIDER_ENDTHREADSTACKRECONSTRUCTION PdebugStackProviderEndthreadstackreconstruction; 

// Definition

HRESULT PdebugStackProviderEndthreadstackreconstruction 
(
	 void
)
{...}

PDEBUG_STACK_PROVIDER_ENDTHREADSTACKRECONSTRUCTION 


```

## -parameters

### -param void: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also