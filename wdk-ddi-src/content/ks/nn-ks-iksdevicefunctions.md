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
ms.keywords : stream.iksdevicefunctions, IKsDeviceFunctions interface [Streaming Media Devices], IKsDeviceFunctions interface [Streaming Media Devices], described, IKsDeviceFunctions, ks/IKsDeviceFunctions, avintfc_68e124c6-7a91-4c68-8327-e2c83b982699.xml
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
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