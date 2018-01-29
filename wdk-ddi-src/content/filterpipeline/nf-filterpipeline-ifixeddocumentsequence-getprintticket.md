---
UID : NF:filterpipeline.IFixedDocumentSequence.GetPrintTicket
title : IFixedDocumentSequence::GetPrintTicket method
author : windows-driver-content
description : The GetPrintTicket method gets the print ticket object for the fixed document sequence.
old-location : print\ifixeddocumentsequence_getprintticket.htm
old-project : print
ms.assetid : dba0ac90-a895-4daf-ba7c-b7a8a32fed19
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : GetPrintTicket, GetPrintTicket method [Print Devices], GetPrintTicket method [Print Devices], IFixedDocumentSequence interface, IFixedDocumentSequence interface [Print Devices], GetPrintTicket method, IFixedDocumentSequence, print.ifixeddocumentsequence_getprintticket, IFixedDocumentSequence::GetPrintTicket, filterpipeline_f94c6c29-91ba-4820-ad22-12cc9604993c.xml, filterpipeline/IFixedDocumentSequence::GetPrintTicket
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


# GetPrintTicket method
The <b>GetPrintTicket</b> method gets the print ticket object for the fixed document sequence.

## Syntax

````
HRESULT GetPrintTicket(
  [out] IPartPrintTicket **ppPrintTicket
);
````

## Parameters

`ppPrintTicket`

The print ticket object for the sequence.


## Return Value

<b>GetPrintTicket</b> returns an <b>HRESULT</b> value. If a print ticket is not in the fixed document sequence, <b>GetPrintTicket</b> might return E_ELEMENT_NOT_FOUND.


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