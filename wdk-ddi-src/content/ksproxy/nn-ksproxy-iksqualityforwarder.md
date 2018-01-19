---
UID : NN:ksproxy.IKsQualityForwarder
title : IKsQualityForwarder
author : windows-driver-content
description : The IKsQualityForwarder interface inherits the method of the IKsObject interface and extends IKsObject to provide a method that flushes information from a pin.
old-location : stream\iksqualityforwarder.htm
old-project : stream
ms.assetid : 1f0ebadc-4a6c-4d57-ba96-936ce138142b
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KsSynchronousDeviceControl
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
req.alt-api : IKsQualityForwarder
req.alt-loc : ksproxy.h
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
req.typenames : PIPE_STATE
---

# IKsQualityForwarder interface

The <b>IKsQualityForwarder</b> interface inherits the method of the <a href="..\ksproxy\nn-ksproxy-iksobject.md">IKsObject</a> interface and extends <b>IKsObject</b> to provide a method that flushes information from a pin.

## Methods

<p>The <b>IKsQualityForwarder</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [ksproxy.IKsQualityForwarder.KsFlushClient](nf-ksproxy-iksqualityforwarder-ksflushclient.md) | The KsFlushClient method flushes information from a pin. |

## Remarks

The IID for this interface is IID_IKsQualityForwarder.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | ksproxy.h |
| **DLL** |  |