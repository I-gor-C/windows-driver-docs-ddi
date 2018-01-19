---
UID : NN:ksproxy.IKsAllocatorEx
title : IKsAllocatorEx
author : windows-driver-content
description : The IKsAllocatorEx interface is for proxy use and not recommended for application use. IKsAllocatorEx inherits all the methods of the IKsAllocator interface and extends IKsAllocator to provide methods that further control and query an allocator.
old-location : stream\iksallocatorex.htm
old-project : stream
ms.assetid : 42abaf2b-8ee9-450e-aef3-fa29d1b558e5
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
req.alt-api : IKsAllocatorEx
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

# IKsAllocatorEx interface

The <b>IKsAllocatorEx</b> interface is for proxy use and not recommended for application use. <b>IKsAllocatorEx</b> inherits all the methods of the <b>IKsAllocator</b> interface and extends <b>IKsAllocator</b> to provide methods that further control and query an allocator. 

The IID for this interface is IID_IKsAllocatorEx.

## Methods

<p>The <b>IKsAllocatorEx</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [ksproxy.IKsAllocatorEx.KsGetProperties](nf-ksproxy-iksallocatorex-ksgetproperties.md) | Returns the properties for an allocator. |
| [ksproxy.IKsAllocatorEx.KsSetAllocatorHandle](nf-ksproxy-iksallocatorex-kssetallocatorhandle.md) | Sets the handle for an allocator. |
| [ksproxy.IKsAllocatorEx.KsSetProperties](nf-ksproxy-iksallocatorex-kssetproperties.md) | Sets the properties for an allocator. |

## Remarks



## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | ksproxy.h (include Ksproxy.h) |
| **DLL** |  |

    ## See Also

        <dl>
<dt>
<a href="..\ksproxy\nn-ksproxy-iksallocator.md">IKsAllocator</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsAllocatorEx interface%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>