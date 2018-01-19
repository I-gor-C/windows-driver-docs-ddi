---
UID : NN:ksproxy.IKsPinFactory
title : IKsPinFactory
author : windows-driver-content
description : The IKsPinFactory interface provides a method that retrieves the identifier of a pin factory.
old-location : stream\ikspinfactory.htm
old-project : stream
ms.assetid : b86f4048-c175-4062-969c-c9c443d6d394
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
req.alt-api : IKsPinFactory
req.alt-loc : Ksproxy.lib,Ksproxy.dll
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

# IKsPinFactory interface

The <b>IKsPinFactory</b> interface provides a method that retrieves the identifier of a pin factory.

## Methods

<p>The <b>IKsPinFactory</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [ksproxy.IKsPinFactory.KsPinFactory](nf-ksproxy-ikspinfactory-kspinfactory.md) | The KsPinFactory method retrieves the identifier of a pin factory. |

## Remarks

The IID for this interface is IID_IKsPinFactory.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | ksproxy.h |
| **DLL** |  |