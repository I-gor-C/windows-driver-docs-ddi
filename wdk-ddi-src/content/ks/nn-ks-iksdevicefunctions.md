---
UID : NN:ks.IKsDeviceFunctions
title : IKsDeviceFunctions
author : windows-driver-content
description : The IKsDeviceFunctions interface is a COM-style interface implemented on AVStream devices. This interface is available in Windows Server 2003 SP1 and later versions of Windows.
old-location : stream\iksdevicefunctions.htm
old-project : stream
ms.assetid : d29e7b39-5fcf-4543-9363-6f8ac6a9c7dc
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : _KsEdit
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : ks.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IKsDeviceFunctions
req.alt-loc : ks.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : 
---

# IKsDeviceFunctions interface

The IKsDeviceFunctions interface is a COM-style interface implemented on AVStream devices. This interface is available in Windows Server 2003 SP1 and later versions of Windows.

## Methods

<p>The <b>IKsDeviceFunctions</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [ks.IKsDeviceFunctions.RegisterAdapterObjectEx](nf-ks-iksdevicefunctions-registeradapterobjectex.md) | The IKsDeviceFunctions::RegisterAdapterObjectEx method registers a DMA adapter object with AVStream. All drivers compiled for Win64 platforms should use this method instead of KsDeviceRegisterAdapterObject. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | ks.h |
| **DLL** |  |