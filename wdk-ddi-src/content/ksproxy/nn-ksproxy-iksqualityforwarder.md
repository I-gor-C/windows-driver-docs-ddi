---
UID: NN:ksproxy.IKsQualityForwarder
title: IKsQualityForwarder
author: windows-driver-content
description: The IKsQualityForwarder interface inherits the method of the IKsObject interface and extends IKsObject to provide a method that flushes information from a pin.
old-location: stream\iksqualityforwarder.htm
old-project: stream
ms.assetid: 1f0ebadc-4a6c-4d57-ba96-936ce138142b
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IKsQualityForwarder, IKsQualityForwarder interface [Streaming Media Devices], IKsQualityForwarder interface [Streaming Media Devices], described, ksproxy/IKsQualityForwarder, ksproxy_ed147fca-8a84-407c-861a-f33625d90bc7.xml, stream.iksqualityforwarder
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
-	IKsQualityForwarder
product:
- Windows
targetos: Windows
req.typenames: PIPE_STATE
---

# IKsQualityForwarder interface

The <b>IKsQualityForwarder</b> interface inherits the method of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559883">IKsObject</a> interface and extends <b>IKsObject</b> to provide a method that flushes information from a pin.

## Methods

<p>The <b>IKsQualityForwarder</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IKsQualityForwarder::KsFlushClient](nf-ksproxy-iksqualityforwarder-ksflushclient.md) | The KsFlushClient method flushes information from a pin. |

## Remarks
The IID for this interface is IID_IKsQualityForwarder.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | ksproxy.h |