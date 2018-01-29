---
UID : NS:ksmedia.KSCAMERA_PERFRAMESETTING_CAP_HEADER
title : KSCAMERA_PERFRAMESETTING_CAP_HEADER
author : windows-driver-content
description : This structure contains the header information for the per frame settings capabilities.
old-location : stream\kscamera_perframesetting_cap_header.htm
old-project : stream
ms.assetid : 7478E83E-0657-4547-993A-84AECBB2562D
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KSCAMERA_PERFRAMESETTING_CAP_HEADER structure [Streaming Media Devices], ksmedia/KSCAMERA_PERFRAMESETTING_CAP_HEADER, stream.kscamera_perframesetting_cap_header, KSCAMERA_PERFRAMESETTING_CAP_HEADER, PKSCAMERA_PERFRAMESETTING_CAP_HEADER structure pointer [Streaming Media Devices], PKSCAMERA_PERFRAMESETTING_CAP_HEADER, ksmedia/PKSCAMERA_PERFRAMESETTING_CAP_HEADER, *PKSCAMERA_PERFRAMESETTING_CAP_HEADER
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ksmedia.h
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
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PKSCAMERA_PERFRAMESETTING_CAP_HEADER, KSCAMERA_PERFRAMESETTING_CAP_HEADER"
---

# KSCAMERA_PERFRAMESETTING_CAP_HEADER structure
This structure contains the header information for the per frame settings capabilities.

## Syntax
````
typedef struct {
  ULONG     Size;
  ULONG     ItemCount;
  ULONGLONG Flags;
} KSCAMERA_PERFRAMESETTING_CAP_HEADER, *PKSCAMERA_PERFRAMESETTING_CAP_HEADER;
````

## Members


`Flags`

Not used.

`ItemCount`

The number of capability items.

`Size`

The size of the entire capability payload, including this header, all the item headers, and the item payloads that follow.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ksmedia.h |