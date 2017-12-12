---
UID: NA:
---

# Ksproxy.h header

## -description

This header is used by Streaming media devices. For more information, see
- [Streaming media devices](../_stream/index.md)

Ksproxy.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [KsGetMediaType function](nf-ksproxy-ksgetmediatype.md) | The KsGetMediaType function retrieves information about a media type on a pin factory identifier. |
| [KsGetMediaTypeCount function](nf-ksproxy-ksgetmediatypecount.md) | The KsGetMediaTypeCount function returns the number of available media types on a pin factory identifier. |
| [KsGetMultiplePinFactoryItems function](nf-ksproxy-ksgetmultiplepinfactoryitems.md) | The KsGetMultiplePinFactoryItems function retrieves pin property items in a variable length data buffer. |
| [KsOpenDefaultDevice function](nf-ksproxy-ksopendefaultdevice.md) | The KsOpenDefaultDevice function opens a handle to the first device that is listed in the specified Plug and Play (PnP) category. |
| [KsResolveRequiredAttributes function](nf-ksproxy-ksresolverequiredattributes.md) | The KsResolveRequiredAttributes function searches the attributes list that is attached to a data range for specified attributes and ensures that all specified attributes were found. |
| [KsSynchronousDeviceControl function](nf-ksproxy-kssynchronousdevicecontrol.md) | The KsSynchronousDeviceControl function issues a synchronous device I/O control operation to the KS object that is specified by a file handle. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [OPTIMAL_WEIGHT_TOTALS structure](ns-ksproxy-optimal_weight_totals.md) | . |
| [_KSSTREAM_SEGMENT structure](ns-ksproxy-_ksstream_segment.md) | The KSSTREAM_SEGMENT structure contains information that describes an I/O operation occurring on a stream. |
| [_KSSTREAM_SEGMENT structure](ns-ksproxy-_ksstream_segment~r1.md) | The KSSTREAM_SEGMENT structure contains information that describes an I/O operation occurring on a stream. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [FRAMING_CACHE_OPS enumeration](ne-ksproxy-framing_cache_ops.md) | . |
| [FRAMING_PROP enumeration](ne-ksproxy-framing_prop.md) | . |
| [KSALLOCATORMODE enumeration](ne-ksproxy-ksallocatormode.md) | . |
| [KSIOOPERATION enumeration](ne-ksproxy-ksiooperation.md) | . |
| [KSPEEKOPERATION enumeration](ne-ksproxy-kspeekoperation.md) | . |
| [KS_LogicalMemoryType enumeration](ne-ksproxy-ks_logicalmemorytype.md) | . |
| [PIPE_ALLOCATOR_PLACE enumeration](ne-ksproxy-pipe_allocator_place.md) | . |
| [PIPE_STATE enumeration](ne-ksproxy-pipe_state.md) | . |

## Interfaces

| Title   | Description   |
| ---- |:---- |
| [IKsAggregateControl interface](nn-ksproxy-iksaggregatecontrol.md) | The IKsAggregateControl interface provides methods that add and remove COM servers as aggregate providers on KS objects that support the interface. |
| [IKsClockPropertySet interface](nn-ksproxy-iksclockpropertyset.md) | The IKsClockPropertySet interface provides methods that let the proxy accurately reflect time. |
| [IKsControl interface](nn-ksproxy-ikscontrol.md) | The IKsControl interface provides user-mode methods that control a KS filter or KS pin. See the IKsControl AVStream COM interface for information about the user-mode equivalent of this interface. |
| [IKsDataTypeCompletion interface](nn-ksproxy-iksdatatypecompletion.md) | The IKsDataTypeCompletion interface provides a method to complete partially specified media types that are passed to the IAMStreamConfig |
| [IKsDataTypeHandler interface](nn-ksproxy-iksdatatypehandler.md) | The IKsDataTypeHandler interface provides methods that perform optional preprocessing and postprocessing of media samples. |
| [IKsInterfaceHandler interface](nn-ksproxy-iksinterfacehandler.md) | The IKsInterfaceHandler interface provides methods that marshal samples into the kernel based on the KSPIN_INTERFACE structure specified for the established connection. The IID for this interface is IID_IKsInterfaceHandler. |
| [IKsNotifyEvent interface](nn-ksproxy-iksnotifyevent.md) | The IKsNotifyEvent interface provides a method to cause the KS object that owns a DirectShow event to issue the event with the given parameters. |
| [IKsObject interface](nn-ksproxy-iksobject.md) | The IKsObject interface provides a method to retrieve the file handle of a KS object. |
| [IKsPin interface](nn-ksproxy-ikspin~r1.md) | The IKsPin interface provides methods that control and retrieve information about a pin. |
| [IKsPinEx interface](nn-ksproxy-ikspinex.md) | The IKsPinEx interface inherits all the methods of the IKsPin interface and extends IKsPin to provide a method that notifies the filter graph of an error to give the filter graph an opportunity to halt. |
| [IKsPinFactory interface](nn-ksproxy-ikspinfactory.md) | The IKsPinFactory interface provides a method that retrieves the identifier of a pin factory. |
| [IKsQualityForwarder interface](nn-ksproxy-iksqualityforwarder.md) | The IKsQualityForwarder interface inherits the method of the IKsObject interface and extends IKsObject to provide a method that flushes information from a pin. |
| [IKsTopology interface](nn-ksproxy-ikstopology.md) | The IKsTopology interface provides a method that opens topology node objects contained within a filter. |
