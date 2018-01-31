---
UID : NF:filterpipeline.IPartFont.SetFontContent
title : IPartFont::SetFontContent method
author : windows-driver-content
description : The SetFontContent method sets the content of the font.
old-location : print\ipartfont_setfontcontent.htm
old-project : print
ms.assetid : bd77d32f-97fd-4f80-945d-9fff7553fcc5
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : SetFontContent, filterpipeline/IPartFont::SetFontContent, filterpipeline_1639cc2b-b1b6-4fa3-997b-3c98e32d2783.xml, IPartFont::SetFontContent, SetFontContent method [Print Devices], IPartFont interface, IPartFont interface [Print Devices], SetFontContent method, IPartFont, print.ipartfont_setfontcontent, SetFontContent method [Print Devices]
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
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : Filterpipeline.idl
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


# SetFontContent method
The <b>SetFontContent</b> method sets the content of the font.

## Syntax

````
HRESULT SetFontContent(
  [in] const wchar_t *contentType
);
````

## Parameters

`pContentType`




## Return Value

<b>SetFontContent</b> returns an <b>HRESULT</b> value.


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