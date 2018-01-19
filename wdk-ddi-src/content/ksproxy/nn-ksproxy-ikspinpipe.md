---
UID : NN:ksproxy.IKsPinPipe
title : IKsPinPipe
author : windows-driver-content
description : The IKsPinPipe interface is for proxy use and not recommended for application use. IKsPinPipe provides methods that control a pin pipe.
old-location : stream\ikspinpipe.htm
old-project : stream
ms.assetid : bb9ebe0b-4a6e-41ff-a460-6c0b3a749d8d
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : KsSynchronousDeviceControl
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : interface
req.header : ksproxy.h
req.include-header : Ksproxy.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : IKsPinPipe
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

# IKsPinPipe interface

The <b>IKsPinPipe</b> interface is for proxy use and not recommended for application use. <b>IKsPinPipe</b> provides methods that control a pin pipe. 

The IID for this interface is IID_IKsPinPipe.

## Methods

<p>The <b>IKsPinPipe</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [ksproxy.IKsPinPipe.KsGetConnectedPin](nf-ksproxy-ikspinpipe-ksgetconnectedpin.md) | Not recommended for application use. |
| [ksproxy.IKsPinPipe.KsGetFilterName](nf-ksproxy-ikspinpipe-ksgetfiltername.md) | Returns the name of a filter. |
| [ksproxy.IKsPinPipe.KsGetPinBusCache](nf-ksproxy-ikspinpipe-ksgetpinbuscache.md) | Not recommended for application use. |
| [ksproxy.IKsPinPipe.KsGetPinFramingCache](nf-ksproxy-ikspinpipe-ksgetpinframingcache.md) | Not recommended for application use. |
| [ksproxy.IKsPinPipe.KsGetPinName](nf-ksproxy-ikspinpipe-ksgetpinname.md) | Returns the name of a pin. |
| [ksproxy.IKsPinPipe.KsGetPipe](nf-ksproxy-ikspinpipe-ksgetpipe.md) | Not recommended for application use. |
| [ksproxy.IKsPinPipe.KsGetPipeAllocatorFlag](nf-ksproxy-ikspinpipe-ksgetpipeallocatorflag.md) | Not recommended for application use. |
| [ksproxy.IKsPinPipe.KsSetPinBusCache](nf-ksproxy-ikspinpipe-kssetpinbuscache.md) | Not recommended for application use. |
| [ksproxy.IKsPinPipe.KsSetPinFramingCache](nf-ksproxy-ikspinpipe-kssetpinframingcache.md) | Not recommended for application use. |
| [ksproxy.IKsPinPipe.KsSetPipe](nf-ksproxy-ikspinpipe-kssetpipe.md) | Not recommended for application use. |
| [ksproxy.IKsPinPipe.KsSetPipeAllocatorFlag](nf-ksproxy-ikspinpipe-kssetpipeallocatorflag.md) | Not recommended for application use. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | ksproxy.h (include Ksproxy.h) |
| **DLL** |  |