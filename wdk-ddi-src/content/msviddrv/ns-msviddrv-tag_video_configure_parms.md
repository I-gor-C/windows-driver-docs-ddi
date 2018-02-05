---
UID : NS:msviddrv.tag_video_configure_parms
title : tag_video_configure_parms
author : windows-driver-content
description : "."
old-location : stream\videoconfigparms.htm
old-project : stream
ms.assetid : 58FE3B56-AFC6-46DE-BBE1-CCFA8FF1390A
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : stream.videoconfigparms, VIDEOCONFIGPARMS structure [Streaming Media Devices], LPVIDEOCONFIGPARMS, tag_video_configure_parms, *LPVIDEOCONFIGPARMS, msviddrv/LPVIDEOCONFIGPARMS, LPVIDEOCONFIGPARMS structure pointer [Streaming Media Devices], msviddrv/VIDEOCONFIGPARMS, VIDEOCONFIGPARMS
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : msviddrv.h
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
req.irql : "<= APC_LEVEL"
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*LPVIDEOCONFIGPARMS, VIDEOCONFIGPARMS"
---

# tag_video_configure_parms structure


## Syntax
````
typedef struct tag_video_configure_parms {
  LPDWORD lpdwReturn;
  LPVOID  lpData1;
  DWORD   dwSize1;
  LPVOID  lpData2;
  DWORD   dwSize2;
} VIDEOCONFIGPARMS, *LPVIDEOCONFIGPARMS;
````

## Members


`dwSize1`

Specifies the size of data buffer 1.

`dwSize2`

Specifies the size of data buffer 2.

`lpData1`

Specifies a pointer to data 1.

`lpData2`

Specifies a pointer to data 2.

`lpdwReturn`

Specifies the return parameter from the configure MSG.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | msviddrv.h |