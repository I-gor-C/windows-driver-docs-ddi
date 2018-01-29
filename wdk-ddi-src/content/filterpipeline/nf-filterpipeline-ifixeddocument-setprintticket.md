---
UID : NF:filterpipeline.IFixedDocument.SetPrintTicket
title : IFixedDocument::SetPrintTicket method
author : windows-driver-content
description : The SetPrintTicket method inserts a print ticket into the fixed document.
old-location : print\ifixeddocument_setprintticket.htm
old-project : print
ms.assetid : 701c53d5-bb1e-4003-9505-19b9c46689c6
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : SetPrintTicket method [Print Devices], IFixedDocument interface, IFixedDocument, filterpipeline_96d89fc9-899f-4ede-8da5-898471f6b769.xml, SetPrintTicket method [Print Devices], SetPrintTicket, filterpipeline/IFixedDocument::SetPrintTicket, IFixedDocument::SetPrintTicket, IFixedDocument interface [Print Devices], SetPrintTicket method, print.ifixeddocument_setprintticket
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


# SetPrintTicket method
The <b>SetPrintTicket</b> method inserts a print ticket into the fixed document.

## Syntax

````
HRESULT SetPrintTicket(
  [in] IPartPrintTicket *pPrintTicket
);
````

## Parameters

`pPrintTicket`

A pointer to the print ticket to be inserted.


## Return Value

<b>SetPrintTicket</b> returns an <b>HRESULT</b> value.


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