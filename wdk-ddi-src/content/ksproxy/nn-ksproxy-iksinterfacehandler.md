---
UID: NN:ksproxy.IKsInterfaceHandler
title: IKsInterfaceHandler
author: windows-driver-content
description: The IKsInterfaceHandler interface provides methods that marshal samples into the kernel based on the KSPIN_INTERFACE structure specified for the established connection. The IID for this interface is IID_IKsInterfaceHandler.
old-location: stream\iksinterfacehandler.htm
old-project: stream
ms.assetid: b9f72e79-930c-456e-8001-5df808604caa
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IKsInterfaceHandler, IKsInterfaceHandler interface [Streaming Media Devices], IKsInterfaceHandler interface [Streaming Media Devices], described, ksproxy/IKsInterfaceHandler, ksproxy_9d597bae-a5d7-4575-a4ac-983b827b0ae4.xml, stream.iksinterfacehandler
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: ksproxy.h
req.include-header: 
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
-	IKsInterfaceHandler
product: Windows
targetos: Windows
req.typenames: PIPE_STATE
---

# IKsInterfaceHandler interface

The <b>IKsInterfaceHandler</b> interface provides methods that marshal samples into the kernel based on the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563537">KSPIN_INTERFACE</a> structure specified for the established connection. The IID for this interface is IID_IKsInterfaceHandler.

## Methods

<p>The <b>IKsInterfaceHandler</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IKsInterfaceHandler::KsCompleteIo](nf-ksproxy-iksinterfacehandler-kscompleteio.md) | The KsCompleteIo method cleans up extended headers and releases media samples after input and output (I/O) complete. |
| [IKsInterfaceHandler::KsProcessMediaSamples](nf-ksproxy-iksinterfacehandler-ksprocessmediasamples.md) | The KsProcessMediaSamples method processes media samples. |
| [IKsInterfaceHandler::KsSetPin](nf-ksproxy-iksinterfacehandler-kssetpin.md) | The KsSetPin method informs the streaming interface handler about the pin with which to communicate when passing data. |

## Remarks
In order to keep the proxy neutral with regard to the interface used to stream data, interface handlers are loaded to translate DirectShow media samples to and from a kernel-level driver. An interface handler implements the methods of the <b>IKsInterfaceHandler</b> interface to perform preprocessing and postprocessing on all media samples and to signal the completion of input and output (I/O).

Each interface handler can marshal media samples using its own method. The standard interface handler that KS proxy implements uses IOCTL_KS_WRITE_STREAM for the receive operation and IOCTL_KS_READ_STREAM for the send operation, but a custom interface handler can use some other method.

When a pin is connected, the proxy uses the GUID in the <b>Set</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563537">KSPIN_INTERFACE</a> structure to determine what interface handler to load. The interface handler is registered as a COM server under that GUID class. The interface handler must handle all variations of the interface within the interface set. Bridge pins are not expected to stream data, and interface handlers are not loaded for them.

On an interface handler create request through <b>CoCreateInstance</b>, the server is always presented an outer <b>IUnknown</b> with which to create the COM object. This <b>IUnknown</b> is an interface on the pin object that is loading this interface handler. The <b>IUnknown</b> interface pointer can be used to query information or interfaces, such as the <b>IKsControl</b> interface, from the pin, although the kernel-mode pin may not have been created at the time the interface handler is loaded. No reference should be left on the outer object through acquiring any interfaces, as it will result in a circular reference count. Using the interfaces without a reference count is acceptable, because the outer object owns the handler and, by definition, is destroyed when the outer object's reference count reaches zero.

For more information about <b>CoCreateInstance</b>, see the Microsoft Windows SDK documentation.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | ksproxy.h |

## See Also

<a href="..\ks\nn-ks-ikscontrol.md">IKsControl</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff563537">KSPIN_INTERFACE</a>



 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsInterfaceHandler interface%20 RELEASE:%20(2/23/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>