---
UID: NC.engextcpp.ExtExtension.ExtKnownStructMethod
title: ExtExtension::* ExtKnownStructMethod
author: windows-driver-content
description: 
ms.assetid: 7e43a175-8a29-41f7-bef5-c7c202a36e3c
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

# ExtExtension::* ExtKnownStructMethod callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

ExtExtension::* ExtKnownStructMethod Extextension::* Extknownstructmethod; 

// Definition

void Extextension::* Extknownstructmethod 
(
	PCSTR TypeName
	ULONG Flags
	ULONG64 Offset
)
{...}

ExtExtension::* ExtKnownStructMethod 


```

## -parameters

### -param TypeName: 
### -param Flags: 
### -param Offset: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also