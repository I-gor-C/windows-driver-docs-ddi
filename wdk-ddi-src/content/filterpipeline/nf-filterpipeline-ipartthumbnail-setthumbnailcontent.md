---
UID : NF:filterpipeline.IPartThumbnail.SetThumbnailContent
title : IPartThumbnail::SetThumbnailContent method
author : windows-driver-content
description : The SetThumbnailContent method sets the thumbnail content for the part.
old-location : print\ipartthumbnail_setthumbnailcontent.htm
old-project : print
ms.assetid : 7392aa0b-479a-473f-b8b5-34e14494e050
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : IPartThumbnail, IPartThumbnail::SetThumbnailContent, SetThumbnailContent
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : method
req.header : filterpipeline.h
req.include-header : 
req.target-type : Desktop
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IPartThumbnail.SetThumbnailContent
req.alt-loc : filterpipeline.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : Filterpipeline.idl
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : EXpsFontRestriction
---


# SetThumbnailContent method
The <b>SetThumbnailContent</b> method sets the thumbnail content for the part.

## Syntax

````
HRESULT SetThumbnailContent(
  [in] const wchar_t *contentType
);
````

## Parameters

`pContentType`




## Return Value

<b>SetThumbnailContent</b> returns an <b>HRESULT</b> value.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | filterpipeline.h |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |