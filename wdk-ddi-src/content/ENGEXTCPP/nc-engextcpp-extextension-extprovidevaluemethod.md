---
UID: NC.engextcpp.ExtExtension.ExtProvideValueMethod
title: ExtExtension::* ExtProvideValueMethod
author: windows-driver-content
description: 
ms.assetid: eb51b503-7c9d-4f7a-b35f-c4fc40ba77fc
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: engextcpp.hpp
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

# ExtExtension::* ExtProvideValueMethod callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

ExtExtension::* ExtProvideValueMethod Extextension::* Extprovidevaluemethod; 

// Definition

void Extextension::* Extprovidevaluemethod 
(
	ULONG Flags
	PCWSTR ValueName
	PULONG64 Value
	PULONG64 TypeModBase
	PULONG TypeId
	PULONG TypeFlags
)
{...}

ExtExtension::* ExtProvideValueMethod 


```

## -parameters

### -param Flags: 
### -param ValueName: 
### -param Value: 
### -param TypeModBase: 
### -param TypeId: 
### -param TypeFlags: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also