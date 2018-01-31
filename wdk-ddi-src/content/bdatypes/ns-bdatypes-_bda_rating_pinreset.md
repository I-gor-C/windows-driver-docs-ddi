---
UID : NS:bdatypes._BDA_RATING_PINRESET
title : "_BDA_RATING_PINRESET"
author : windows-driver-content
description : "."
old-location : stream\bda_rating_pinreset.htm
old-project : stream
ms.assetid : 237463EC-3C57-4DCA-9757-870B5F55C584
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : "_BDA_RATING_PINRESET, PBDA_RATING_PINRESET structure pointer [Streaming Media Devices], *PBDA_RATING_PINRESET, BDA_RATING_PINRESET structure [Streaming Media Devices], PBDA_RATING_PINRESET, stream.bda_rating_pinreset, bdatypes/PBDA_RATING_PINRESET, bdatypes/BDA_RATING_PINRESET, BDA_RATING_PINRESET"
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : bdatypes.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PBDA_RATING_PINRESET, BDA_RATING_PINRESET"
---

# _BDA_RATING_PINRESET structure


## Syntax
````
typedef struct _BDA_RATING_PINRESET {
  BYTE bPinLength;
  BYTE argbNewPin[MIN_DIMENSION];
} BDA_RATING_PINRESET, *PBDA_RATING_PINRESET;
````

## Members


`argbNewPin`

Specifies null-terminated UTF8. Use an empty string if the pin is disabled.

`bPinLength`

Specifies the buffer size including a null termination.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | bdatypes.h |