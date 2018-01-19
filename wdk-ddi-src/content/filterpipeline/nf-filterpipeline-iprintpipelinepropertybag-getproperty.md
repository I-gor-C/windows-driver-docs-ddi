---
UID : NF:filterpipeline.IPrintPipelinePropertyBag.GetProperty
title : IPrintPipelinePropertyBag::GetProperty method
author : windows-driver-content
description : The GetProperty method gets a property from a property bag.
old-location : print\iprintpipelinepropertybag_getproperty.htm
old-project : print
ms.assetid : 10a5ada8-98ab-4e1c-a4b5-2f6d60674952
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : IPrintPipelinePropertyBag, IPrintPipelinePropertyBag::GetProperty, GetProperty
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
req.alt-api : IPrintPipelinePropertyBag.GetProperty
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


# GetProperty method
The <code>GetProperty</code> method gets a property from a property bag.

## Syntax

````
HRESULT GetProperty(
  [in]  const wchar_t *pszName,
  [out]       VARIANT *pVar
);
````

## Parameters

`pszName`

The name of the property that you want to get from the property bag.

`pVar`

The <b>VARIANT</b> value to get from the property bag.


## Return Value

<code>GetProperty</code> returns an <b>HRESULT</b> value.


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