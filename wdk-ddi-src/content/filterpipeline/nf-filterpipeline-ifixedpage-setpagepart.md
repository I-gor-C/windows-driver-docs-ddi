---
UID : NF:filterpipeline.IFixedPage.SetPagePart
title : IFixedPage::SetPagePart method
author : windows-driver-content
description : The SetPagePart method associates a new part with the page.
old-location : print\ifixedpage_setpagepart.htm
old-project : print
ms.assetid : 12970111-3d25-4004-9c6d-8582ef7afef3
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : filterpipeline/IFixedPage::SetPagePart, print.ifixedpage_setpagepart, filterpipeline_03059a3d-9aac-4ff2-8506-7754327942f6.xml, IFixedPage, IFixedPage::SetPagePart, SetPagePart method [Print Devices], IFixedPage interface, IFixedPage interface [Print Devices], SetPagePart method, SetPagePart method [Print Devices], SetPagePart
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


# SetPagePart method
The <b>SetPagePart</b> method associates a new part with the page.

## Syntax

````
HRESULT SetPagePart(
  [in] IUnknown *pUnk
);
````

## Parameters

`pUnk`

A pointer to the new part.


## Return Value

<b>SetPagePart</b> returns an <b>HRESULT</b> value.


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