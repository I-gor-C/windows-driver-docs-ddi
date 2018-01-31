---
UID : NF:filterpipeline.IFixedDocumentSequence.SetPrintTicket
title : IFixedDocumentSequence::SetPrintTicket method
author : windows-driver-content
description : The SetPrintTicket method inserts a print ticket into the fixed document sequence.
old-location : print\ifixeddocumentsequence_setprintticket.htm
old-project : print
ms.assetid : 636db99c-9195-4476-b1a6-a8067f27c6bd
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : print.ifixeddocumentsequence_setprintticket, SetPrintTicket method [Print Devices], IFixedDocumentSequence, filterpipeline_01f88943-7bfe-4819-b553-a6c563ac5f49.xml, IFixedDocumentSequence::SetPrintTicket, IFixedDocumentSequence interface [Print Devices], SetPrintTicket method, SetPrintTicket, SetPrintTicket method [Print Devices], IFixedDocumentSequence interface, filterpipeline/IFixedDocumentSequence::SetPrintTicket
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
The <b>SetPrintTicket</b> method inserts a print ticket into the fixed document sequence.

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