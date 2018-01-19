---
UID : NN:filterpipeline.IXpsDocumentConsumer
title : IXpsDocumentConsumer
author : windows-driver-content
description : A filter uses the IXpsDocumentConsumer interface when it generates XPS content for the pipeline to consume.
old-location : print\ixpsdocumentconsumer.htm
old-project : print
ms.assetid : 98e603e6-2786-4bc8-ad8a-0e91b0d444d8
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
req.alt-api : IXpsDocumentConsumer
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

# IXpsDocumentConsumer interface

A filter uses the <code>IXpsDocumentConsumer</code> interface when it generates XPS content for the pipeline to consume.

## Methods

<p>The <b>IXpsDocumentConsumer</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [filterpipeline.IXpsDocumentConsumer.CloseSender](nf-filterpipeline-ixpsdocumentconsumer-closesender.md) | The CloseSender method tells the Pipeline Manager that the filter is done sending XPS parts. |
| [filterpipeline.IXpsDocumentConsumer.GetNewEmptyPart](nf-filterpipeline-ixpsdocumentconsumer-getnewemptypart.md) | The GetNewEmptyPart method creates a new XPS part. |
| [filterpipeline.IXpsDocumentConsumer.SendFixedDocument](nf-filterpipeline-ixpsdocumentconsumer-sendfixeddocument.md) | The SendFixedDocument method sends a fixed document object to the pipeline. |
| [filterpipeline.IXpsDocumentConsumer.SendFixedDocumentSequence](nf-filterpipeline-ixpsdocumentconsumer-sendfixeddocumentsequence.md) | The SendFixedDocumentSequence method sends a fixed document sequence to the pipeline. |
| [filterpipeline.IXpsDocumentConsumer.SendFixedPage](nf-filterpipeline-ixpsdocumentconsumer-sendfixedpage.md) | The SendFixedPage method sends a fixed page of an XPS document to the pipeline. |
| [filterpipeline.IXpsDocumentConsumer.SendXpsDocument](nf-filterpipeline-ixpsdocumentconsumer-sendxpsdocument.md) | The SendXpsDocument method sends an XPS document to the pipeline. |
| [filterpipeline.IXpsDocumentConsumer.SendXpsUnknown](nf-filterpipeline-ixpsdocumentconsumer-sendxpsunknown.md) | The SendXpsUnknown method sends an XPS document part that cannot be identified to the filter pipeline. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | filterpipeline.h (include Filterpipeline.h) |
| **DLL** |  |