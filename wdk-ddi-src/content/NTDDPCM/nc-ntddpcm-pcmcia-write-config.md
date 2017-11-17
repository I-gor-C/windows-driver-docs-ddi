---
UID: NC.ntddpcm.PCMCIA_WRITE_CONFIG
title: PCMCIA_WRITE_CONFIG
author: windows-driver-content
description: 
ms.assetid: 3119dad0-88c2-4a53-b232-c8a971cc9cdf
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

# PCMCIA_WRITE_CONFIG callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCMCIA_WRITE_CONFIG PcmciaWriteConfig; 

// Definition

ULONG PcmciaWriteConfig 
(
	PVOID Context
	ULONG WhichSpace
	PUCHAR Buffer
	ULONG Offset
	ULONG Length
)
{...}

PCMCIA_WRITE_CONFIG PPCMCIA_WRITE_CONFIG


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