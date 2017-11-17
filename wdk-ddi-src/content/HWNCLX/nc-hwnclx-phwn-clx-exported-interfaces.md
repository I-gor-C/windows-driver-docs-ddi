---
UID: NC.hwnclx.PHWN_CLX_EXPORTED_INTERFACES
title: PHWN_CLX_EXPORTED_INTERFACES
author: windows-driver-content
description: 
ms.assetid: f44b65d0-cc89-4610-8496-883cc8bcc3e6
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: hwnclx.h
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

# PHWN_CLX_EXPORTED_INTERFACES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PHWN_CLX_EXPORTED_INTERFACES PhwnClxExportedInterfaces; 

// Definition

VOID PhwnClxExportedInterfaces 
(
	 VOID
)
{...}

PHWN_CLX_EXPORTED_INTERFACES 


```

## -parameters

### -param VOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also