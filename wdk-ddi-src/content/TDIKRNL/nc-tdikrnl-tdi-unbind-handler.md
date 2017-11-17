---
UID: NC.tdikrnl.TDI_UNBIND_HANDLER
title: TDI_UNBIND_HANDLER
author: windows-driver-content
description: 
ms.assetid: e5fd79b6-a204-4185-998d-1159526a37ad
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: tdikrnl.h
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

# TDI_UNBIND_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

TDI_UNBIND_HANDLER TdiUnbindHandler; 

// Definition

VOID TdiUnbindHandler 
(
	PUNICODE_STRING DeviceName
)
{...}

TDI_UNBIND_HANDLER 


```

## -parameters

### -param DeviceName: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also