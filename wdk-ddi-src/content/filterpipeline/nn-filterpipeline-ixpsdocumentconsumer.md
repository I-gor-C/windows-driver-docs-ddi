---
UID: NN:filterpipeline.IXpsDocumentConsumer
title: IXpsDocumentConsumer
author: windows-driver-content
description: A filter uses the IXpsDocumentConsumer interface when it generates XPS content for the pipeline to consume.
old-location: print\ixpsdocumentconsumer.htm
old-project: print
ms.assetid: 98e603e6-2786-4bc8-ad8a-0e91b0d444d8
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IXpsDocumentConsumer, IXpsDocumentConsumer interface [Print Devices], IXpsDocumentConsumer interface [Print Devices], described, filterpipeline/IXpsDocumentConsumer, filterpipeline_230eb0f6-427a-4986-b8ad-bc1d41853d67.xml, print.ixpsdocumentconsumer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: filterpipeline.h
req.include-header: Filterpipeline.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: filterpipeline.h
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	filterpipeline.h
api_name:
-	IXpsDocumentConsumer
product: Windows
targetos: Windows
req.typenames: EXpsFontRestriction
---

# IXpsDocumentConsumer interface

A filter uses the <code>IXpsDocumentConsumer</code> interface when it generates XPS content for the pipeline to consume. 
<div class="alert"><b>Note</b>    The XPS print filter pipeline does not preserve digital signatures or story fragments. You may be able to work around this by using stream filters.</div><div> </div>

## Methods

<p>The <b>IXpsDocumentConsumer</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IXpsDocumentConsumer::CloseSender](nf-filterpipeline-ixpsdocumentconsumer-closesender.md) | The CloseSender method tells the Pipeline Manager that the filter is done sending XPS parts. |
| [IXpsDocumentConsumer::GetNewEmptyPart](nf-filterpipeline-ixpsdocumentconsumer-getnewemptypart.md) | The GetNewEmptyPart method creates a new XPS part. |
| [IXpsDocumentConsumer::SendFixedDocument](nf-filterpipeline-ixpsdocumentconsumer-sendfixeddocument.md) | The SendFixedDocument method sends a fixed document object to the pipeline. |
| [IXpsDocumentConsumer::SendFixedDocumentSequence](nf-filterpipeline-ixpsdocumentconsumer-sendfixeddocumentsequence.md) | The SendFixedDocumentSequence method sends a fixed document sequence to the pipeline. |
| [IXpsDocumentConsumer::SendFixedPage](nf-filterpipeline-ixpsdocumentconsumer-sendfixedpage.md) | The SendFixedPage method sends a fixed page of an XPS document to the pipeline. |
| [IXpsDocumentConsumer::SendXpsDocument](nf-filterpipeline-ixpsdocumentconsumer-sendxpsdocument.md) | The SendXpsDocument method sends an XPS document to the pipeline. |
| [IXpsDocumentConsumer::SendXpsUnknown](nf-filterpipeline-ixpsdocumentconsumer-sendxpsunknown.md) | The SendXpsUnknown method sends an XPS document part that cannot be identified to the filter pipeline. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | filterpipeline.h (include Filterpipeline.h) |