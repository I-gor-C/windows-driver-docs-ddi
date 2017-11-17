---
UID: NC.icm.PCMSCALLBACKA
title: PCMSCALLBACKA
author: windows-driver-content
description: 
ms.assetid: ced34a82-8d3a-4cc4-b3a3-47f813263ffd
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: icm.h
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

# PCMSCALLBACKA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCMSCALLBACKA Pcmscallbacka; 

// Definition

BOOL Pcmscallbacka 
(
	_tagCOLORMATCHSETUPA *
	 LPARAM
)
{...}

PCMSCALLBACKA 


```

## -parameters

### -param *: 
### -param LPARAM: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also