---
UID : NN:filterpipeline.IPartBase
title : IPartBase
author : windows-driver-content
description : The IPartBase interface is a common base for document part interfaces.
old-location : print\ipartbase.htm
old-project : print
ms.assetid : 7523990f-04de-4182-99d9-fba100bebb84
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : print.ipartbase, IPartBase interface [Print Devices], IPartBase interface [Print Devices], described, IPartBase, filterpipeline/IPartBase, filterpipeline_aaad898e-c110-439c-9983-fedbab82c06d.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : filterpipeline.h
req.include-header : Filterpipeline.h
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
req.lib : filterpipeline.h
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : EXpsFontRestriction
---

# IPartBase interface

The <b>IPartBase </b>interface is a common base for document part interfaces.

## Methods

<p>The <b>IPartBase</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [filterpipeline.IPartBase.GetPartCompression](nf-filterpipeline-ipartbase-getpartcompression.md) | The GetPartCompression method gets the compression of the part. |
| [filterpipeline.IPartBase.GetStream](nf-filterpipeline-ipartbase-getstream.md) | The GetStream method gets the stream object that contains the part data. Each part has part-specific data that is associated with it (for example, a font, image, and page markup). |
| [filterpipeline.IPartBase.GetUri](nf-filterpipeline-ipartbase-geturi.md) | The GetUri method gets the URI of the part. |
| [filterpipeline.IPartBase.SetPartCompression](nf-filterpipeline-ipartbase-setpartcompression.md) | The SetPartCompression method sets the compression of the part. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | filterpipeline.h (include Filterpipeline.h) |
| **DLL** |  |