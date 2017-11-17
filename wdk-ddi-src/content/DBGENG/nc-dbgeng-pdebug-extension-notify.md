---
UID: NC.dbgeng.PDEBUG_EXTENSION_NOTIFY
title: PDEBUG_EXTENSION_NOTIFY
author: windows-driver-content
description: 
ms.assetid: 07c98efa-61bd-4191-b556-7ff75f2ca51f
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

# PDEBUG_EXTENSION_NOTIFY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDEBUG_EXTENSION_NOTIFY PdebugExtensionNotify; 

// Definition

void PdebugExtensionNotify 
(
	ULONG Notify
	ULONG64 Argument
)
{...}

PDEBUG_EXTENSION_NOTIFY 


```

## -parameters

### -param Notify: 
### -param Argument: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also