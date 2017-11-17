---
UID: NC.ntddk.pHalHaltSystem
title: pHalHaltSystem
author: windows-driver-content
description: 
ms.assetid: 29fc8aa4-17fe-4d0a-bda0-bfebdda0eff4
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddk.h
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

# pHalHaltSystem callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pHalHaltSystem Phalhaltsystem; 

// Definition

VOID Phalhaltsystem 
(
	 VOID
)
{...}

pHalHaltSystem 


```

## -parameters

### -param VOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also