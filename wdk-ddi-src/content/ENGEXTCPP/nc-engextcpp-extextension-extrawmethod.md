---
UID: NC.engextcpp.ExtExtension.ExtRawMethod
title: ExtExtension::* ExtRawMethod
author: windows-driver-content
description: 
ms.assetid: a21f9cde-037a-4c41-897d-39f256966646
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

# ExtExtension::* ExtRawMethod callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

ExtExtension::* ExtRawMethod Extextension::* Extrawmethod; 

// Definition

HRESULT Extextension::* Extrawmethod 
(
	PVOID Context
)
{...}

ExtExtension::* ExtRawMethod 


```

## -parameters

### -param Context: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also