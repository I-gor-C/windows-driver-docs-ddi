---
UID : NN:ksproxy.IKsTopology
title : IKsTopology
author : windows-driver-content
description : The IKsTopology interface provides a method that opens topology node objects contained within a filter.
old-location : stream\ikstopology.htm
old-project : stream
ms.assetid : 418a415c-b4db-41a1-825e-66704c45e134
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
req.alt-api : IKsTopology
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

# IKsTopology interface

The <b>IKsTopology</b> interface provides a method that opens topology node objects contained within a filter.

## Methods

<p>The <b>IKsTopology</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [ksproxy.IKsTopology.CreateNodeInstance](nf-ksproxy-ikstopology-createnodeinstance.md) | The CreateNodeInstance method requests a KS filter object to open a topology node object. |

## Remarks

The IID for this interface is IID_IKsTopology.

The <b>IKsTopology</b> interface is supported by filters. </p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | ksproxy.h |
| **DLL** |  |