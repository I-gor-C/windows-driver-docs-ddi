---
UID : NF:filterpipeline.IPrintPipelinePropertyBag.DeleteProperty
title : IPrintPipelinePropertyBag::DeleteProperty method
author : windows-driver-content
description : The DeleteProperty method deletes a property from a property bag.
old-location : print\iprintpipelinepropertybag_deleteproperty.htm
old-project : print
ms.assetid : f3de5514-9a7f-4e27-9be0-4aec4b84a5a7
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : IPrintPipelinePropertyBag, IPrintPipelinePropertyBag::DeleteProperty, DeleteProperty
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
req.alt-api : IPrintPipelinePropertyBag.DeleteProperty
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


# DeleteProperty method
The <code>DeleteProperty</code> method deletes a property from a property bag.

## Syntax

````
BOOL DeleteProperty(
  [in] const wchar_t *pszName
);
````

## Parameters

`pszName`

The name of the property to delete from the property bag.


## Return Value

<code>DeleteProperty</code> returns "true" if the property was deleted from the property bag.


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