---
UID: NC.poscx.PPOSCX_EXPORTED_INTERFACES
title: PPOSCX_EXPORTED_INTERFACES
author: windows-driver-content
description: 
ms.assetid: 842727fd-a5cc-42e3-a3eb-87a92ce69b0b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: poscx.h
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

# PPOSCX_EXPORTED_INTERFACES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PPOSCX_EXPORTED_INTERFACES PposcxExportedInterfaces; 

// Definition

VOID PposcxExportedInterfaces 
(
	 VOID
)
{...}

PPOSCX_EXPORTED_INTERFACES 


```

## -parameters

### -param VOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also