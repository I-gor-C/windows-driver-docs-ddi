---
UID: NC.netadaptercxtypes.NETFUNC
title: NETFUNC
author: windows-driver-content
description: 
ms.assetid: e39bb976-98bf-4dcd-a771-0315bc502fac
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: netadaptercxtypes.h
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

# NETFUNC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NETFUNC Netfunc; 

// Definition

VOID Netfunc 
(
	 VOID
)
{...}

NETFUNC 


```

## -parameters

### -param VOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also