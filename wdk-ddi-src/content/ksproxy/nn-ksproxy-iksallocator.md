---
UID : NN:ksproxy.IKsAllocator
title : IKsAllocator
author : windows-driver-content
description : TheIKsAllocator interface provides methods that control and query an allocator. IKsAllocator is for proxy use and not recommended for application use.
old-location : stream\iksallocator.htm
old-project : stream
ms.assetid : 0d6db041-e5ea-4394-9d88-b4b5b377fe1d
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
req.alt-api : IKsAllocator
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

# IKsAllocator interface

The<b>IKsAllocator</b> interface provides methods that control and query an allocator.  <b>IKsAllocator</b>  is for proxy use and not recommended for application use.

## Methods

<p>The <b>IKsAllocator</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [ksproxy.IKsAllocator.KsGetAllocatorHandle](nf-ksproxy-iksallocator-ksgetallocatorhandle.md) | Retrieves a file handle to an allocator. |
| [ksproxy.IKsAllocator.KsGetAllocatorMode](nf-ksproxy-iksallocator-ksgetallocatormode.md) | Returns the mode in which an allocator allocates memory. |
| [ksproxy.IKsAllocator.KsGetAllocatorStatus](nf-ksproxy-iksallocator-ksgetallocatorstatus.md) | Retrieves the status of an allocator. |
| [ksproxy.IKsAllocator.KsSetAllocatorMode](nf-ksproxy-iksallocator-kssetallocatormode.md) | Sets the mode in which an allocator allocates memory. |

## Remarks

The IID for this interface is IID_IKsAllocator.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | ksproxy.h (include Ksproxy.h) |
| **DLL** |  |