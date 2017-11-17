---
UID: NC.icm.PCMSCALLBACKW
title: PCMSCALLBACKW
author: windows-driver-content
description: 
ms.assetid: af5cc3fb-278d-4274-8474-1f7eee20d639
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

# PCMSCALLBACKW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCMSCALLBACKW Pcmscallbackw; 

// Definition

BOOL Pcmscallbackw 
(
	_tagCOLORMATCHSETUPW *
	 LPARAM
)
{...}

PCMSCALLBACKW 


```

## -parameters

### -param *: 
### -param LPARAM: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also