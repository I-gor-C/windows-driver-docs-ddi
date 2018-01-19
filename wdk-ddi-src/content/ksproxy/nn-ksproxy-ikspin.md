---
UID : NN:ksproxy.IKsPin
title : IKsPin
author : windows-driver-content
description : The IKsPin interface provides methods that control and retrieve information about a pin.
old-location : stream\ikspin.htm
old-project : stream
ms.assetid : 4717300c-bc98-4e1f-83c3-cbd368b45140
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
req.alt-api : IKsPin,IKsPin.KsReceiveAllocator,IKsPin.KsRenegotiateAllocator,IKsPin.KsQualityNotify
req.alt-loc : ksproxy.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Ksproxy.h
req.dll : 
req.irql : 
req.typenames : PIPE_STATE
---

# IKsPin interface

The <b>IKsPin</b> interface provides methods that control and retrieve information about a pin.

The IID for this interface is IID_IKsPin.

## Methods

<p>The <b>IKsPin</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [ksproxy.IKsPin.KsCreateSinkPinHandle](nf-ksproxy-ikspin-kscreatesinkpinhandle.md) | The KsCreateSinkPinHandle method creates a pin handle and stores it in the KS pin object. |
| [ksproxy.IKsPin.KsDecrementPendingIoCount](nf-ksproxy-ikspin-ksdecrementpendingiocount.md) | The KsDecrementPendingIoCount method decrements the number of input/output (I/O) operations that are in progress on a pin. |
| [ksproxy.IKsPin.KsDeliver](nf-ksproxy-ikspin-ksdeliver.md) | The KsDeliver method delivers a media sample from an output pin to an input pin, continues an I/O operation by retrieving the next buffer from an allocator, and submits the buffer to the associated device. |
| [ksproxy.IKsPin.KsGetCurrentCommunication](nf-ksproxy-ikspin-ksgetcurrentcommunication.md) | The KsGetCurrentCommunication method retrieves the current communication direction, interface, and medium of a pin. |
| [ksproxy.IKsPin.KsIncrementPendingIoCount](nf-ksproxy-ikspin-ksincrementpendingiocount.md) | The KsIncrementPendingIoCount method increments the number of input/output (I/O) operations that are in progress on a pin. |
| [ksproxy.IKsPin.KsMediaSamplesCompleted](nf-ksproxy-ikspin-ksmediasamplescompleted.md) | The KsMediaSamplesCompleted method informs a pin that a stream segment completed. |
| [ksproxy.IKsPin.KsPeekAllocator](nf-ksproxy-ikspin-kspeekallocator.md) | The KsPeekAllocator method returns a pointer to an IMemAllocator interface for a pin's assigned allocator. |
| [ksproxy.IKsPin.KsPropagateAcquire](nf-ksproxy-ikspin-kspropagateacquire.md) | The KsPropagateAcquire method directs all the pins on the filter to attain the Acquire state. |
| [ksproxy.IKsPin.KsQueryInterfaces](nf-ksproxy-ikspin-ksqueryinterfaces.md) | The KsQueryInterfaces method retrieves interfaces that a pin supports. |
| [ksproxy.IKsPin.KsQueryMediums](nf-ksproxy-ikspin-ksquerymediums.md) | The KsQueryMediums method retrieves mediums that a pin supports. |

## Remarks

An interface handler (<a href="..\ksproxy\nn-ksproxy-iksinterfacehandler.md">IKsInterfaceHandler</a>) uses many of the <b>IKsPin</b> methods to route media samples of a particular media type.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum UMDF version** |  |
| **Header** | ksproxy.h |
| **DLL** |  |

    ## See Also

        <dl>
<dt>
<a href="..\ksproxy\nn-ksproxy-iksinterfacehandler.md">IKsInterfaceHandler</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsPin interface%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>