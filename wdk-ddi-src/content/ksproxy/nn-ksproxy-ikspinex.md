---
UID: NN:ksproxy.IKsPinEx
title: IKsPinEx
author: windows-driver-content
description: The IKsPinEx interface inherits all the methods of the IKsPin interface and extends IKsPin to provide a method that notifies the filter graph of an error to give the filter graph an opportunity to halt.
old-location: stream\ikspinex.htm
old-project: stream
ms.assetid: 9e6fd96d-c78e-44f3-ae4c-3688da48a494
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IKsPinEx, IKsPinEx interface [Streaming Media Devices], IKsPinEx interface [Streaming Media Devices], described, ksproxy/IKsPinEx, ksproxy_3c92d570-f22f-4165-bafd-9a22f5516137.xml, stream.ikspinex
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
-	Ksproxy.lib
-	Ksproxy.dll
api_name:
-	IKsPinEx
product: Windows
targetos: Windows
req.typenames: PIPE_STATE
---

# IKsPinEx interface

The <b>IKsPinEx</b> interface inherits all the methods of the <b>IKsPin</b> interface and extends <b>IKsPin</b> to provide a method that notifies the filter graph of an error to give the filter graph an opportunity to halt.

The IID for this interface is IID_IKsPinEx.

## Methods

<p>The <b>IKsPinEx</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IKsPinEx::KsNotifyError](nf-ksproxy-ikspinex-ksnotifyerror.md) | The KsNotifyError method notifies the filter graph of an error to give the filter graph an opportunity to halt. |

## Remarks
An interface handler (<a href="..\ksproxy\nn-ksproxy-iksinterfacehandler.md">IKsInterfaceHandler</a>) uses many of the <b>IKsPinEx</b> methods to route media samples of a particular media type.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | ksproxy.h |

## See Also

<a href="..\ksproxy\nn-ksproxy-iksinterfacehandler.md">IKsInterfaceHandler</a>



<a href="..\ksproxy\nn-ksproxy-ikspin.md">IKsPin</a>