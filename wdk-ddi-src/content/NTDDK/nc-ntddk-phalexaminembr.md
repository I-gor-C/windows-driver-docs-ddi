---
UID: NC.ntddk.pHalExamineMBR
title: pHalExamineMBR
author: windows-driver-content
description: 
ms.assetid: 649fdabe-62a5-41f7-a548-165259239ef3
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

# pHalExamineMBR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

pHalExamineMBR Phalexaminembr; 

// Definition

VOID Phalexaminembr 
(
	PDEVICE_OBJECT DeviceObject
	ULONG SectorSize
	ULONG MBRTypeIdentifier
	PVOID *Buffer
)
{...}

pHalExamineMBR 


```

## -parameters

### -param DeviceObject: 
### -param SectorSize: 
### -param MBRTypeIdentifier: 
### -param *Buffer: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also