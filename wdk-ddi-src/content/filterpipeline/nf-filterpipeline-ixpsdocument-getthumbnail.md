---
UID : NF:filterpipeline.IXpsDocument.GetThumbnail
title : IXpsDocument::GetThumbnail method
author : windows-driver-content
description : The GetThumbnail method gets the document thumbnail object.
old-location : print\ixpsdocument_getthumbnail.htm
old-project : print
ms.assetid : 74466609-4408-4065-a607-cd338902335d
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : IXpsDocument, IXpsDocument::GetThumbnail, GetThumbnail
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
req.alt-api : IXpsDocument.GetThumbnail
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


# GetThumbnail method
The <code>GetThumbnail</code> method gets the document thumbnail object.

## Syntax

````
HRESULT GetThumbnail(
  [out] IPartThumbnail **ppThumbnail
);
````

## Parameters

`ppThumbnail`

The thumbnail object in the document.


## Return Value

<code>GetThumbnail</code> returns an <b>HRESULT</b> value. This method might return E_ELEMENT_NOT_FOUND if a thumbnail cannot be found.


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