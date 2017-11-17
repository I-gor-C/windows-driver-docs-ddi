---
UID: NC.ntddk.pHalGetAcpiTable
title: pHalGetAcpiTable
author: windows-driver-content
description: 
ms.assetid: cbd8ee52-9e46-4590-8bb8-20a6489e61fb
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

# pHalGetAcpiTable callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pHalGetAcpiTable Phalgetacpitable; 

// Definition

PVOID Phalgetacpitable 
(
	ULONG Signature
	PCSTR OemId
	PCSTR OemTableId
)
{...}

pHalGetAcpiTable 


```

## -parameters

### -param Signature: 
### -param OemId: 
### -param OemTableId: 



## -returns

Returns PVOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also