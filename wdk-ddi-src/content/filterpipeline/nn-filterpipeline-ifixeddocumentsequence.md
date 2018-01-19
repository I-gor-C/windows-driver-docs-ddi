---
UID : NN:filterpipeline.IFixedDocumentSequence
title : IFixedDocumentSequence
author : windows-driver-content
description : The IFixedDocumentSequence interface represents the fixed document sequence for an XPS document.
old-location : print\ifixeddocumentsequence.htm
old-project : print
ms.assetid : 8919e2d1-0c39-46b6-b06e-83fe61f67751
ms.author : windowsdriverdev
ms.date : 1/8/2018
ms.keywords : IXpsPartIterator, IXpsPartIterator::Reset, Reset
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : filterpipeline.h
req.include-header : Filterpipeline.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IFixedDocumentSequence
req.alt-loc : filterpipeline.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : EXpsFontRestriction
---

# IFixedDocumentSequence interface

The <b>IFixedDocumentSequence</b> interface represents the fixed document sequence for an XPS document.

## Methods

<p>The <b>IFixedDocumentSequence</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [filterpipeline.IFixedDocumentSequence.GetPrintTicket](nf-filterpipeline-ifixeddocumentsequence-getprintticket.md) | The GetPrintTicket method gets the print ticket object for the fixed document sequence. |
| [filterpipeline.IFixedDocumentSequence.GetUri](nf-filterpipeline-ifixeddocumentsequence-geturi.md) | The GetUri method gets the URI of the fixed document sequence. |
| [filterpipeline.IFixedDocumentSequence.SetPrintTicket](nf-filterpipeline-ifixeddocumentsequence-setprintticket.md) | The SetPrintTicket method inserts a print ticket into the fixed document sequence. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | filterpipeline.h (include Filterpipeline.h) |
| **DLL** |  |