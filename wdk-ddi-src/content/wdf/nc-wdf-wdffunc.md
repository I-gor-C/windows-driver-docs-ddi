---
UID: NC.wdf.WDFFUNC
title: WDFFUNC
author: windows-driver-content
description: 
ms.assetid: 75bcc14e-54ed-4f76-82ca-ebe9f64eeac2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdf.h
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

# WDFFUNC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

WDFFUNC Wdffunc; 

// Definition

VOID Wdffunc 
(
	 VOID
)
{...}

WDFFUNC 


```

## -parameters

### -param VOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also