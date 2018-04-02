---
UID: NN:ksproxy.IKsDataTypeCompletion
title: IKsDataTypeCompletion
author: windows-driver-content
description: The IKsDataTypeCompletion interface provides a method to complete partially specified media types that are passed to the IAMStreamConfig::SetFormat method.
old-location: stream\iksdatatypecompletion.htm
old-project: stream
ms.assetid: 52976c7d-522e-4ff6-96a2-8ed98abe1739
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IKsDataTypeCompletion, IKsDataTypeCompletion interface [Streaming Media Devices], IKsDataTypeCompletion interface [Streaming Media Devices], described, ksproxy/IKsDataTypeCompletion, ksproxy_0ae81dab-7e72-45e0-9577-069d41973670.xml, stream.iksdatatypecompletion
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: ksproxy.h
req.include-header: 
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
req.lib: Ksproxy.lib
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	ksproxy.h
api_name:
-	IKsDataTypeCompletion
product: Windows
targetos: Windows
req.typenames: PIPE_STATE
---

# IKsDataTypeCompletion interface

The <b>IKsDataTypeCompletion</b> interface provides a method to complete partially specified media types that are passed to the <b>IAMStreamConfig::SetFormat</b> method. 

The IID for this interface is IID_IKsDataTypeCompletion.

## Methods

<p>The <b>IKsDataTypeCompletion</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IKsDataTypeCompletion::KsCompleteMediaType](nf-ksproxy-iksdatatypecompletion-kscompletemediatype.md) | The KsCompleteMediaType method completes a partially-specified media type that was first presented to the IAMStreamConfig::SetFormat method. |

## Remarks
In order to keep the proxy data type neutral, optional data type handlers can be loaded to massage the data stream as it passes to or from kernel-mode filters. You should implement a data type handler as a COM server that, at least, supports the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559807">IKsDataTypeHandler</a> interface. The <b>IKsDataTypeCompletion</b> interface is optional for data type handlers. A data type handler only supports <b>IKsDataTypeCompletion</b> if the media format has a partially specified form.

A data type handler is typically loaded during the pin connection process, and unloaded when the connection is broken. However, a data type handler is sometimes loaded briefly for other purposes. For instance, if an application uses DirectShow's <b>IAMStreamConfig::SetFormat</b> method, the application possibly uses a data type handler to complete a partial media type parameter returned from <b>IAMStreamConfig::SetFormat</b>. For more information about <b>IAMStreamConfig::SetFormat</b>, see the Microsoft Windows SDK documentation.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | ksproxy.h |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff559807">IKsDataTypeHandler</a>