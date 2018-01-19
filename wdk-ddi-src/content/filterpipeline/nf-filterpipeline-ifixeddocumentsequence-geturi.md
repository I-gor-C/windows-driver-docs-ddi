---
UID : NF:filterpipeline.IFixedDocumentSequence.GetUri
title : IFixedDocumentSequence::GetUri method
author : windows-driver-content
description : The GetUri method gets the URI of the fixed document sequence.
old-location : print\ifixeddocumentsequence_geturi.htm
old-project : print
ms.assetid : 45017249-2ea5-43f6-9712-787f52cb6e4b
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : IFixedDocumentSequence, IFixedDocumentSequence::GetUri, GetUri
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
req.alt-api : IFixedDocumentSequence.GetUri
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


# GetUri method
The <b>GetUri</b> method gets the URI of the fixed document sequence.

## Syntax

````
HRESULT GetUri(
  [out] BSTR *uri
);
````

## Parameters

`uri`

The URI of the fixed document sequence.


## Return Value

<b>GetUri</b> returns an <b>HRESULT</b> value.


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