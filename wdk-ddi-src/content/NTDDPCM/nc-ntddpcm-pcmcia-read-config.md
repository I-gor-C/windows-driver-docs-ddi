---
UID: NC.ntddpcm.PCMCIA_READ_CONFIG
title: PCMCIA_READ_CONFIG
author: windows-driver-content
description: 
ms.assetid: 94f4e73d-d59a-4d84-a420-fb289ca1d06a
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddpcm.h
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

# PCMCIA_READ_CONFIG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCMCIA_READ_CONFIG PcmciaReadConfig; 

// Definition

ULONG PcmciaReadConfig 
(
	PVOID Context
	ULONG WhichSpace
	PUCHAR Buffer
	ULONG Offset
	ULONG Length
)
{...}

PCMCIA_READ_CONFIG PPCMCIA_READ_CONFIG


```

## -parameters

### -param Context: 
### -param WhichSpace: 
### -param Buffer: 
### -param Offset: 
### -param Length: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also