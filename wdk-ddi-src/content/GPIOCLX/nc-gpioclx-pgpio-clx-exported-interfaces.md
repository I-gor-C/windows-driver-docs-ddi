---
UID: NC.gpioclx.PGPIO_CLX_EXPORTED_INTERFACES
title: PGPIO_CLX_EXPORTED_INTERFACES
author: windows-driver-content
description: 
ms.assetid: 08ebe0c2-0ea9-41e5-a579-128a348d63f5
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: gpioclx.h
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

# PGPIO_CLX_EXPORTED_INTERFACES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGPIO_CLX_EXPORTED_INTERFACES PgpioClxExportedInterfaces; 

// Definition

VOID PgpioClxExportedInterfaces 
(
	 VOID
)
{...}

PGPIO_CLX_EXPORTED_INTERFACES 


```

## -parameters

### -param VOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also