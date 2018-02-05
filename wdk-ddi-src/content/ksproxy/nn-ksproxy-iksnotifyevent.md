---
UID : NN:ksproxy.IKsNotifyEvent
title : IKsNotifyEvent
author : windows-driver-content
description : The IKsNotifyEvent interface provides a method to cause the KS object that owns a DirectShow event to issue the event with the given parameters.
old-location : stream\iksnotifyevent.htm
old-project : stream
ms.assetid : 1de4db64-be4c-4a9b-b1ab-29f703e17959
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : stream.iksnotifyevent, IKsNotifyEvent interface [Streaming Media Devices], IKsNotifyEvent interface [Streaming Media Devices], described, IKsNotifyEvent, ksproxy/IKsNotifyEvent, ksproxy_1ef13fd1-5ccb-410c-8b0e-4942d9ba790e.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : ksproxy.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Ksproxy.lib
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : PIPE_STATE
---

# IKsNotifyEvent interface

<b>DirectX 9.0 and later versions only.</b>

The <b>IKsNotifyEvent</b> interface provides a method to cause the KS object that owns a DirectShow event to issue the event with the given parameters.

The IID for this interface is IID_IKsNotifyEvent

## Methods

<p>The <b>IKsNotifyEvent</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [ksproxy.IKsNotifyEvent.KsNotifyEvent](nf-ksproxy-iksnotifyevent-ksnotifyevent.md) | The KsNotifyEvent method requests that the KS object that owns the given DirectShow event notify the calling application with the given parameters whenever action related to the event occurs. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | ksproxy.h |