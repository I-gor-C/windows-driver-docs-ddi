---
UID : NC:ks.PFNKSFASTHANDLER
title : PFNKSFASTHANDLER
author : windows-driver-content
description : KStrFastHandler is a driver-supplied routine that handles a property or method request without the creation of an IRP.
old-location : stream\kstrfasthandler.htm
old-project : stream
ms.assetid : 9a72cdb5-2b57-4331-9836-82653732decf
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : stream.kstrfasthandler, KStrFastHandler routine [Streaming Media Devices], KStrFastHandler, PFNKSFASTHANDLER, PFNKSFASTHANDLER, ks/KStrFastHandler, ksfunc_e78a76eb-b3e6-4864-bae2-49536d3a9d52.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : ks.h
req.include-header : Ks.h
req.target-type : Desktop
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
req.typenames : KEYWORDSELECTOR
---


# PFNKSFASTHANDLER callback function
<i>KStrFastHandler</i> is a driver-supplied routine that handles a property or method request without the creation of an IRP.

## Syntax

```
PFNKSFASTHANDLER Pfnksfasthandler;

BOOLEAN Pfnksfasthandler(
  PFILE_OBJECT FileObject,
  PKSIDENTIFIER Request,
  ULONG RequestLength,
  PVOID Data,
  ULONG DataLength,
  PIO_STATUS_BLOCK IoStatus
)
{...}
```

## Parameters

`FileObject`

Specifies the file object on which the request was made.

`Request`

Specifies the original property parameter. This will always be on FILE_LONG_ALIGNMENT, but cannot be on FILE_QUAD_ALIGNMENT.

`RequestLength`

Specifies the length indicated by the caller of the property parameter.

`Data`

Specifies the original unaligned data parameter.

`DataLength`

Specifies the length indicated by the caller of the data parameter.

`IoStatus`

Specifies an aligned structure that is used to return error status and information. This information is then copied to the original I/O status structure on completion.


## Return Value

<i>KStrFastHandler</i> returns <b>TRUE</b> if the call was handled. If the call was not handled, it returns <b>FALSE</b> and an IRP is generated to handle the request.

## Remarks

The minidriver provides an entry point for this routine in <a href="..\ks\ns-ks-ksfastproperty_item.md">KSFASTPROPERTY_ITEM</a> or <a href="..\ks\ns-ks-ksfastmethod_item.md">KSFASTMETHOD_ITEM</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |