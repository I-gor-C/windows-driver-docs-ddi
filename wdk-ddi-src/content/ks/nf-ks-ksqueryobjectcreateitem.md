---
UID : NF:ks.KsQueryObjectCreateItem
title : KsQueryObjectCreateItem function
author : windows-driver-content
description : The KsQueryObjectCreateItem function returns the create item assigned to the object when created.
old-location : stream\ksqueryobjectcreateitem.htm
old-project : stream
ms.assetid : dd6d436c-6166-4baf-b180-67f7aa7238e3
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KsQueryObjectCreateItem
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ks.h
req.include-header : Ks.h
req.target-type : Universal
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : KsQueryObjectCreateItem
req.alt-loc : Ks.lib,Ks.dll
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Ks.lib
req.dll : 
req.irql : 
req.typenames : 
---


# KsQueryObjectCreateItem function
The <b>KsQueryObjectCreateItem</b> function returns the create item assigned to the object when created.

## Syntax

````
PKSOBJECT_CREATE_ITEM KsQueryObjectCreateItem(
  _In_ KSOBJECT_HEADER Header
);
````

## Parameters

`Header`

Indicates the header previously allocated.


## Return Value

The <b>KsQueryObjectCreateItem</b> function returns a pointer to a create item.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ks.h (include Ks.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |