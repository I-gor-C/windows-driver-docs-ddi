---
UID: NN:ksproxy.IKsAllocatorEx
title: IKsAllocatorEx
author: windows-driver-content
description: The IKsAllocatorEx interface is for proxy use and not recommended for application use. IKsAllocatorEx inherits all the methods of the IKsAllocator interface and extends IKsAllocator to provide methods that further control and query an allocator.
old-location: stream\iksallocatorex.htm
old-project: stream
ms.assetid: 42abaf2b-8ee9-450e-aef3-fa29d1b558e5
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IKsAllocatorEx, IKsAllocatorEx interface [Streaming Media Devices], IKsAllocatorEx interface [Streaming Media Devices], described, ksproxy/IKsAllocatorEx, ksproxy_58c9c83a-1a11-4e08-bf7f-e0694bf2eda5.xml, stream.iksallocatorex
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: ksproxy.h
req.include-header: Ksproxy.h
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
-	IKsAllocatorEx
product:
- Windows
targetos: Windows
req.typenames: PIPE_STATE
---

# IKsAllocatorEx interface

The <b>IKsAllocatorEx</b> interface is for proxy use and not recommended for application use. <b>IKsAllocatorEx</b> inherits all the methods of the <b>IKsAllocator</b> interface and extends <b>IKsAllocator</b> to provide methods that further control and query an allocator. 

The IID for this interface is IID_IKsAllocatorEx.

## Methods

<p>The <b>IKsAllocatorEx</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IKsAllocatorEx::KsGetProperties](nf-ksproxy-iksallocatorex-ksgetproperties.md) | Returns the properties for an allocator. |
| [IKsAllocatorEx::KsSetAllocatorHandle](nf-ksproxy-iksallocatorex-kssetallocatorhandle.md) | Sets the handle for an allocator. |
| [IKsAllocatorEx::KsSetProperties](nf-ksproxy-iksallocatorex-kssetproperties.md) | Sets the properties for an allocator. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | ksproxy.h (include Ksproxy.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff559719">IKsAllocator</a>