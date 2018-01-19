---
UID : NF:filterpipeline.IPrintClassObjectFactory.GetPrintClassObject
title : IPrintClassObjectFactory::GetPrintClassObject method
author : windows-driver-content
description : The GetPrintClassObject method creates a print filter-related object for a specified printer by using the IID of the interface object to create.
old-location : print\iprintclassobjectfactory_getprintclassobject.htm
old-project : print
ms.assetid : 96ba0c27-d512-4bca-9053-a753434e461d
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : IPrintClassObjectFactory, IPrintClassObjectFactory::GetPrintClassObject, GetPrintClassObject
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
req.alt-api : IPrintClassObjectFactory.GetPrintClassObject
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


# GetPrintClassObject method
The <b>GetPrintClassObject</b> method creates a print filter-related object for a specified printer by using the IID of the interface object to create.

## Syntax

````
HRESULT GetPrintClassObject(
  [in]  const wchar_t *pszPrinterName,
  [in]        REFIID  riid,
  [out]       void    **ppNewObject
);
````

## Parameters

`pszPrinterName`

The printer name.

`riid`

The IID of the interface to create. Filters should use IID_IPrintAsyncNotify to create notification channels.

`ppNewObject`

The new object that this method creates.


## Return Value

<b>GetPrintClassObject</b> returns an <b>HRESULT</b> value.


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