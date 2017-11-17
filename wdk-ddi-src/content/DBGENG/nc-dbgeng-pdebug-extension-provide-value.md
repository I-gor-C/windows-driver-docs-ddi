---
UID: NC.dbgeng.PDEBUG_EXTENSION_PROVIDE_VALUE
title: PDEBUG_EXTENSION_PROVIDE_VALUE
author: windows-driver-content
description: 
ms.assetid: 176c084d-ff33-4c29-904c-faef3e561632
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

# PDEBUG_EXTENSION_PROVIDE_VALUE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDEBUG_EXTENSION_PROVIDE_VALUE PdebugExtensionProvideValue; 

// Definition

HRESULT PdebugExtensionProvideValue 
(
	PDEBUG_CLIENT Client
	ULONG Flags
	PCWSTR Name
	PULONG64 Value
	PULONG64 TypeModBase
	PULONG TypeId
	PULONG TypeFlags
)
{...}

PDEBUG_EXTENSION_PROVIDE_VALUE 


```

## -parameters

### -param Client: 
### -param Flags: 
### -param Name: 
### -param Value: 
### -param TypeModBase: 
### -param TypeId: 
### -param TypeFlags: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also