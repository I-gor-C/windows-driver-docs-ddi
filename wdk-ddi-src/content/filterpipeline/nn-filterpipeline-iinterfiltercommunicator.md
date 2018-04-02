---
UID: NN:filterpipeline.IInterFilterCommunicator
title: IInterFilterCommunicator
author: windows-driver-content
description: The IInterFilterCommunicator interface is implemented in an object that resides in the PrintFilterPipelineSvc service and is made available to filters through methods in the IPrintPipelineFilter interface.
old-location: print\iinterfiltercommunicator.htm
old-project: print
ms.assetid: 777da1db-5522-48fc-bf35-8e6bf9203d6a
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IInterFilterCommunicator, IInterFilterCommunicator interface [Print Devices], IInterFilterCommunicator interface [Print Devices], described, filterpipeline/IInterFilterCommunicator, filterpipeline_80929d81-f333-4d23-9e46-72682784f0a2.xml, print.iinterfiltercommunicator
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
req.lib: 
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
-	IInterFilterCommunicator
product: Windows
targetos: Windows
req.typenames: EXpsFontRestriction
---

# IInterFilterCommunicator interface

The <b>IInterFilterCommunicator</b> interface is implemented in an object that resides in the PrintFilterPipelineSvc service and is made available to filters through methods in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554286">IPrintPipelineFilter</a> interface.<b>IInterFilterCommunicator</b> inherits from the <b>IUnknown</b> interface.

## Methods

<p>The <b>IInterFilterCommunicator</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IInterFilterCommunicator::RequestReader](nf-filterpipeline-iinterfiltercommunicator-requestreader.md) | The RequestReader method retrieves the reader interface for an IInterFilterCommunicator object. |
| [IInterFilterCommunicator::RequestWriter](nf-filterpipeline-iinterfiltercommunicator-requestwriter.md) | The RequestWriter method retrieves the writer interface for an IInterFilterCommunicator object. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | filterpipeline.h (include Filterpipeline.h) |