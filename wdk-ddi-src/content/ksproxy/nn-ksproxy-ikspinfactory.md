---
UID: NN:ksproxy.IKsPinFactory
title: IKsPinFactory
author: windows-driver-content
description: The IKsPinFactory interface provides a method that retrieves the identifier of a pin factory.
old-location: stream\ikspinfactory.htm
old-project: stream
ms.assetid: b86f4048-c175-4062-969c-c9c443d6d394
ms.author: windowsdriverdev
ms.date: 2/20/2018
ms.keywords: stream.ikspinfactory, IKsPinFactory interface [Streaming Media Devices], IKsPinFactory interface [Streaming Media Devices], described, IKsPinFactory, ksproxy/IKsPinFactory, ksproxy_df24cea8-a5d7-474c-bd70-53068078e6c6.xml
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	COM
apilocation:
-	Ksproxy.lib
-	Ksproxy.dll
apiname:
-	IKsPinFactory
product: Windows
targetos: Windows
req.typenames: PIPE_STATE
---

# IKsPinFactory interface

The <b>IKsPinFactory</b> interface provides a method that retrieves the identifier of a pin factory.

## Methods

<p>The <b>IKsPinFactory</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [ksproxy.IKsPinFactory.KsPinFactory](nf-ksproxy-ikspinfactory-kspinfactory.md) | The KsPinFactory method retrieves the identifier of a pin factory. |

## Remarks

The IID for this interface is IID_IKsPinFactory.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | ksproxy.h |