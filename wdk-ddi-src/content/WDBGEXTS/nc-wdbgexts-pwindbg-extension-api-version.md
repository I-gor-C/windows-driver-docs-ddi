---
UID: NC.wdbgexts.PWINDBG_EXTENSION_API_VERSION
title: PWINDBG_EXTENSION_API_VERSION
author: windows-driver-content
description: 
ms.assetid: b1afc342-655d-45e3-9c26-9015ae4625b2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdbgexts.h
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

# PWINDBG_EXTENSION_API_VERSION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_EXTENSION_API_VERSION PwindbgExtensionApiVersion; 

// Definition

LPEXT_API_VERSION PwindbgExtensionApiVersion 
(
	VOID 
)
{...}

PWINDBG_EXTENSION_API_VERSION 


```

## -parameters

### -param : 



## -returns

Returns LPEXT_API_VERSION that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also