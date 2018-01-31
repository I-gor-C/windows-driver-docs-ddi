---
UID : NS:ksmedia.tagTRANSPORTVIDEOPARMS
title : tagTRANSPORTVIDEOPARMS
author : windows-driver-content
description : The TRANSPORTVIDEOPARMS structure is defined but not presently used. It may be used in the future.
old-location : stream\transportvideoparms.htm
old-project : stream
ms.assetid : 14bc6133-78f1-4f25-8638-9348245180fa
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : stream.transportvideoparms, PTRANSPORTVIDEOPARMS, TRANSPORTVIDEOPARMS, ksmedia/TRANSPORTVIDEOPARMS, TRANSPORTVIDEOPARMS structure [Streaming Media Devices], *PTRANSPORTVIDEOPARMS, PTRANSPORTVIDEOPARMS structure pointer [Streaming Media Devices], vidcapstruct_6438f7be-abd8-4d45-969d-6f80e7833216.xml, tagTRANSPORTVIDEOPARMS, ksmedia/PTRANSPORTVIDEOPARMS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ksmedia.h
req.include-header : Ksmedia.h
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
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : TRANSPORTVIDEOPARMS, *PTRANSPORTVIDEOPARMS
---

# tagTRANSPORTVIDEOPARMS structure
The TRANSPORTVIDEOPARMS structure is defined but not presently used. It may be used in the future.

## Syntax
````
typedef struct tagTRANSPORTVIDEOPARMS {
  LONG OutputMode;
  LONG Input;
} TRANSPORTVIDEOPARMS, *PTRANSPORTVIDEOPARMS;
````

## Members


`Input`

Specifies the video input to use. For example, specify zero to use the first (zeroth) video input.

`OutputMode`

Specifies the video output mode. For example ED_PLAYBACK.

## Remarks
Any ED_Xxx tokens are defined in <i>xprtdefs.h</i> in the Microsoft DirectX SDK.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ksmedia.h (include Ksmedia.h) |