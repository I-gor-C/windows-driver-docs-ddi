# Declarations in the ksproxy header
This header Ksproxy contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [IKsClockPropertySet::KsGetTime method](nf-ksproxy-iksclockpropertyset-ksgettime.md) | The KsGetTime method retrieves the time of the underlying clock. |
| [IKsDataTypeHandler::KsPrepareIoOperation method](nf-ksproxy-iksdatatypehandler-ksprepareiooperation.md) | The KsPrepareIoOperation method initializes the extended header and prepares the media sample for an I/O operation. |
| [IKsPin::KsQueryInterfaces method](nf-ksproxy-ikspin-ksqueryinterfaces.md) | The KsQueryInterfaces method retrieves interfaces that a pin supports. |
| [IKsPropertySet::QuerySupported method](nf-ksproxy-ikspropertyset-querysupported.md) | The QuerySupported method determines whether a KS object supports a property set and the type of that support. |
| [IKsPin::KsIncrementPendingIoCount method](nf-ksproxy-ikspin-ksincrementpendingiocount.md) | The KsIncrementPendingIoCount method increments the number of input/output (I/O) operations that are in progress on a pin. |
| [IKsClockPropertySet::KsGetCorrelatedPhysicalTime method](nf-ksproxy-iksclockpropertyset-ksgetcorrelatedphysicaltime.md) | The KsGetCorrelatedPhysicalTime method retrieves the physical time and the correlated system time from the underlying clock. |
| [IKsInterfaceHandler::KsProcessMediaSamples method](nf-ksproxy-iksinterfacehandler-ksprocessmediasamples.md) | The KsProcessMediaSamples method processes media samples. |
| [IKsPin::KsPeekAllocator method](nf-ksproxy-ikspin-kspeekallocator.md) | The KsPeekAllocator method returns a pointer to an IMemAllocator interface for a pin's assigned allocator. |
| [DEFINE_GUIDEX function](nf-ksproxy-define-guidex~r13.md) | TBD |
| [IKsClockPropertySet::KsSetCorrelatedPhysicalTime method](nf-ksproxy-iksclockpropertyset-kssetcorrelatedphysicaltime.md) | The KsSetCorrelatedPhysicalTime method sets the physical time with the correlated system time on the underlying clock. |
| [IKsPinFactory::KsPinFactory method](nf-ksproxy-ikspinfactory-kspinfactory.md) | The KsPinFactory method retrieves the identifier of a pin factory. |
| [IKsQualityForwarder::KsFlushClient method](nf-ksproxy-iksqualityforwarder-ksflushclient.md) | The KsFlushClient method flushes information from a pin. |
| [IKsPinPipe::KsGetPipeAllocatorFlag method](nf-ksproxy-ikspinpipe-ksgetpipeallocatorflag.md) | TBD |
| [DEFINE_GUIDEX function](nf-ksproxy-define-guidex~r10.md) | TBD |
| [IKsInterfaceHandler::KsSetPin method](nf-ksproxy-iksinterfacehandler-kssetpin.md) | The KsSetPin method informs the streaming interface handler about the pin with which to communicate when passing data. |
| [DEFINE_GUIDEX function](nf-ksproxy-define-guidex.md) | TBD |
| [IKsDataTypeHandler::KsIsMediaTypeInRanges method](nf-ksproxy-iksdatatypehandler-ksismediatypeinranges.md) | TBD |
| [IKsAllocator::KsSetAllocatorMode method](nf-ksproxy-iksallocator-kssetallocatormode.md) | TBD |
| [DEFINE_GUIDEX function](nf-ksproxy-define-guidex~r4.md) | TBD |
| [IKsAllocatorEx::KsSetProperties method](nf-ksproxy-iksallocatorex-kssetproperties.md) | TBD |
| [KsOpenDefaultDevice function](nf-ksproxy-ksopendefaultdevice.md) | The KsOpenDefaultDevice function opens a handle to the first device that is listed in the specified Plug and Play (PnP) category. |
| [IKsAllocatorEx::KsCreateAllocatorAndGetHandle method](nf-ksproxy-iksallocatorex-kscreateallocatorandgethandle.md) | TBD |
| [IKsPin::KsQueryMediums method](nf-ksproxy-ikspin-ksquerymediums.md) | The KsQueryMediums method retrieves mediums that a pin supports. |
| [IKsPin::KsGetCurrentCommunication method](nf-ksproxy-ikspin-ksgetcurrentcommunication.md) | The KsGetCurrentCommunication method retrieves the current communication direction, interface, and medium of a pin. |
| [IKsPinPipe::KsSetPipe method](nf-ksproxy-ikspinpipe-kssetpipe.md) | TBD |
| [IKsAllocatorEx::KsGetProperties method](nf-ksproxy-iksallocatorex-ksgetproperties.md) | TBD |
| [IKsPinPipe::KsSetPinBusCache method](nf-ksproxy-ikspinpipe-kssetpinbuscache.md) | TBD |
| [IKsPin::KsDecrementPendingIoCount method](nf-ksproxy-ikspin-ksdecrementpendingiocount.md) | The KsDecrementPendingIoCount method decrements the number of input/output (I/O) operations that are in progress on a pin. |
| [DEFINE_GUIDEX function](nf-ksproxy-define-guidex~r3.md) | TBD |
| [IKsPin::KsPropagateAcquire method](nf-ksproxy-ikspin-kspropagateacquire.md) | The KsPropagateAcquire method directs all the pins on the filter to attain the Acquire state. |
| [IKsPinPipe::KsGetConnectedPin method](nf-ksproxy-ikspinpipe-ksgetconnectedpin.md) | TBD |
| [IKsClockPropertySet::KsGetCorrelatedTime method](nf-ksproxy-iksclockpropertyset-ksgetcorrelatedtime.md) | The KsGetCorrelatedTime method retrieves the current time and the correlated system time from the underlying clock. |
| [IKsClockPropertySet::KsSetTime method](nf-ksproxy-iksclockpropertyset-kssettime.md) | The KsSetTime method sets the current time on the underlying clock. |
| [IKsObject::KsGetObjectHandle method](nf-ksproxy-iksobject-ksgetobjecthandle.md) | The KsGetObjectHandle method retrieves a file handle to a KS object. |
| [DEFINE_GUIDEX function](nf-ksproxy-define-guidex~r11.md) | TBD |
| [IKsClockPropertySet::KsSetCorrelatedTime method](nf-ksproxy-iksclockpropertyset-kssetcorrelatedtime.md) | The KsSetCorrelatedTime method sets the current time with the correlated system time on the underlying clock. |
| [IKsControl::KsEvent method](nf-ksproxy-ikscontrol-ksevent.md) | The KsEvent method enables or disables an event, along with any other defined support operations available on an event set. |
| [IKsPinPipe::KsGetPipe method](nf-ksproxy-ikspinpipe-ksgetpipe.md) | TBD |
| [IKsControl::KsProperty method](nf-ksproxy-ikscontrol-ksproperty.md) | The KsProperty method sets a property or retrieves property information, along with any other defined support operations available on a property set. |
| [IKsInterfaceHandler::KsCompleteIo method](nf-ksproxy-iksinterfacehandler-kscompleteio.md) | The KsCompleteIo method cleans up extended headers and releases media samples after input and output (I/O) complete. |
| [IKsClockPropertySet::KsGetState method](nf-ksproxy-iksclockpropertyset-ksgetstate.md) | The KsGetState method retrieves the streaming state of a pin from the underlying clock. |
| [IKsPinPipe::KsGetPinBusCache method](nf-ksproxy-ikspinpipe-ksgetpinbuscache.md) | TBD |
| [IKsPin::KsDeliver method](nf-ksproxy-ikspin-ksdeliver.md) | The KsDeliver method delivers a media sample from an output pin to an input pin, continues an I/O operation by retrieving the next buffer from an allocator, and submits the buffer to the associated device. |
| [DEFINE_GUIDEX function](nf-ksproxy-define-guidex~r7.md) | TBD |
| [IKsAllocator::KsGetAllocatorMode method](nf-ksproxy-iksallocator-ksgetallocatormode.md) | TBD |
| [IKsPinPipe::KsGetFilterName method](nf-ksproxy-ikspinpipe-ksgetfiltername.md) | TBD |
| [IKsPinPipe::KsSetPinFramingCache method](nf-ksproxy-ikspinpipe-kssetpinframingcache.md) | TBD |
| [DEFINE_GUIDEX function](nf-ksproxy-define-guidex~r9.md) | TBD |
| [IKsAllocator::KsGetAllocatorHandle method](nf-ksproxy-iksallocator-ksgetallocatorhandle.md) | TBD |
| [IKsPin::KsMediaSamplesCompleted method](nf-ksproxy-ikspin-ksmediasamplescompleted.md) | The KsMediaSamplesCompleted method informs a pin that a stream segment completed. |
| [IKsPinPipe::KsGetPinFramingCache method](nf-ksproxy-ikspinpipe-ksgetpinframingcache.md) | TBD |
| [IKsPinEx::KsNotifyError method](nf-ksproxy-ikspinex-ksnotifyerror.md) | The KsNotifyError method notifies the filter graph of an error to give the filter graph an opportunity to halt. |
| [DEFINE_GUIDEX function](nf-ksproxy-define-guidex~r5.md) | TBD |
| [IKsPin::KsRenegotiateAllocator method](nf-ksproxy-ikspin-ksrenegotiateallocator.md) | TBD |
| [IKsPin::KsReceiveAllocator method](nf-ksproxy-ikspin-ksreceiveallocator.md) | TBD |
| [IKsControl::KsMethod method](nf-ksproxy-ikscontrol-ksmethod.md) | The KsMethod method sends a method to a KS object, along with any other defined support operations available on a method set. |
| [KsGetMediaType function](nf-ksproxy-ksgetmediatype.md) | The KsGetMediaType function retrieves information about a media type on a pin factory identifier. |
| [DEFINE_GUIDEX function](nf-ksproxy-define-guidex~r1.md) | TBD |
| [IKsPropertySet::Get method](nf-ksproxy-ikspropertyset-get.md) | The Get method retrieves a property identified by a property-set GUID and a property identifier. |
| [KsSynchronousDeviceControl function](nf-ksproxy-kssynchronousdevicecontrol.md) | The KsSynchronousDeviceControl function issues a synchronous device I/O control operation to the KS object that is specified by a file handle. |
| [IKsAggregateControl::KsAddAggregate method](nf-ksproxy-iksaggregatecontrol-ksaddaggregate.md) | The KsAddAggregate method adds a COM server as an aggregate provider to the list of interface providers for the KS object that exposes the IKsAggregateControl interface. |
| [IKsClockPropertySet::KsGetResolution method](nf-ksproxy-iksclockpropertyset-ksgetresolution.md) | The KsGetResolution method retrieves the clock resolution from the underlying clock. |
| [KsGetMediaTypeCount function](nf-ksproxy-ksgetmediatypecount.md) | The KsGetMediaTypeCount function returns the number of available media types on a pin factory identifier. |
| [IKsAllocatorEx::KsSetAllocatorHandle method](nf-ksproxy-iksallocatorex-kssetallocatorhandle.md) | TBD |
| [DEFINE_GUIDEX function](nf-ksproxy-define-guidex~r12.md) | TBD |
| [IKsDataTypeCompletion::KsCompleteMediaType method](nf-ksproxy-iksdatatypecompletion-kscompletemediatype.md) | The KsCompleteMediaType method completes a partially-specified media type that was first presented to the IAMStreamConfig |
| [KsGetMultiplePinFactoryItems function](nf-ksproxy-ksgetmultiplepinfactoryitems.md) | The KsGetMultiplePinFactoryItems function retrieves pin property items in a variable length data buffer. |
| [IKsAggregateControl::KsRemoveAggregate method](nf-ksproxy-iksaggregatecontrol-ksremoveaggregate.md) | The KsRemoveAggregate method removes a previously added COM server aggregate provider from the list of interface providers for the KS object that exposes the IKsAggregateControl interface. |
| [IKsDataTypeHandler::KsSetMediaType method](nf-ksproxy-iksdatatypehandler-kssetmediatype.md) | The KsSetMediaType method sets the media type for a data type handler. |
| [DEFINE_GUIDEX function](nf-ksproxy-define-guidex~r8.md) | TBD |
| [IKsNotifyEvent::KsNotifyEvent method](nf-ksproxy-iksnotifyevent-ksnotifyevent.md) | The KsNotifyEvent method requests that the KS object that owns the given DirectShow event notify the calling application with the given parameters whenever action related to the event occurs. |
| [IKsPin::KsQualityNotify method](nf-ksproxy-ikspin-ksqualitynotify.md) | TBD |
| [IKsPin::KsCreateSinkPinHandle method](nf-ksproxy-ikspin-kscreatesinkpinhandle.md) | The KsCreateSinkPinHandle method creates a pin handle and stores it in the KS pin object. |
| [IKsClockPropertySet::KsGetPhysicalTime method](nf-ksproxy-iksclockpropertyset-ksgetphysicaltime.md) | The KsGetPhysicalTime method retrieves the physical time from the underlying clock. |
| [IKsClockPropertySet::KsSetPhysicalTime method](nf-ksproxy-iksclockpropertyset-kssetphysicaltime.md) | The KsSetPhysicalTime method sets the physical time on the underlying clock. |
| [IKsTopology::CreateNodeInstance method](nf-ksproxy-ikstopology-createnodeinstance.md) | The CreateNodeInstance method requests a KS filter object to open a topology node object. |
| [IKsPinPipe::KsGetPinName method](nf-ksproxy-ikspinpipe-ksgetpinname.md) | TBD |
| [IKsPinPipe::KsSetPipeAllocatorFlag method](nf-ksproxy-ikspinpipe-kssetpipeallocatorflag.md) | TBD |
| [KsResolveRequiredAttributes function](nf-ksproxy-ksresolverequiredattributes.md) | The KsResolveRequiredAttributes function searches the attributes list that is attached to a data range for specified attributes and ensures that all specified attributes were found. |
| [IKsDataTypeHandler::KsQueryExtendedSize method](nf-ksproxy-iksdatatypehandler-ksqueryextendedsize.md) | The KsQueryExtendedSize method retrieves extended header information required for input and output (I/O) operations. |
| [IKsPropertySet::Set method](nf-ksproxy-ikspropertyset-set.md) | The Set method sets a property identified by a property-set GUID and a property identifier. |
| [DEFINE_GUIDEX function](nf-ksproxy-define-guidex~r6.md) | TBD |
| [IKsDataTypeHandler::KsCompleteIoOperation method](nf-ksproxy-iksdatatypehandler-kscompleteiooperation.md) | The KsCompleteIoOperation method cleans up the extended header and completes the input and output (I/O) operation. |
| [IKsAllocator::KsGetAllocatorStatus method](nf-ksproxy-iksallocator-ksgetallocatorstatus.md) | TBD |
| [DEFINE_GUIDEX function](nf-ksproxy-define-guidex~r2.md) | TBD |
Interface

| Title        | Description    |
| ------------- |:-------------:|
| [IKsPinFactory interface](nn-ksproxy-ikspinfactory.md) | TBD |
| [IKsClockPropertySet interface](nn-ksproxy-iksclockpropertyset.md) | TBD |
| [IKsTopology interface](nn-ksproxy-ikstopology.md) | TBD |
| [IKsDataTypeHandler interface](nn-ksproxy-iksdatatypehandler.md) | TBD |
| [IKsControl interface](nn-ksproxy-ikscontrol.md) | The IKsControl interface provides user-mode methods that control a KS filter or KS pin. See the IKsControl AVStream COM interface for information about the user-mode equivalent of this interface. |
| [IKsDataTypeCompletion interface](nn-ksproxy-iksdatatypecompletion.md) | TBD |
| [IKsPinEx interface](nn-ksproxy-ikspinex.md) | TBD |
| [IKsAggregateControl interface](nn-ksproxy-iksaggregatecontrol.md) | TBD |
| [IKsPropertySet interface](nn-ksproxy-ikspropertyset.md) | TBD |
| [IKsQualityForwarder interface](nn-ksproxy-iksqualityforwarder.md) | TBD |
| [IKsPin interface](nn-ksproxy-ikspin~r1.md) | TBD |
| [IKsObject interface](nn-ksproxy-iksobject.md) | TBD |
| [IKsPinPipe interface](nn-ksproxy-ikspinpipe.md) | TBD |
| [IKsAllocator interface](nn-ksproxy-iksallocator~r1.md) | TBD |
| [IKsNotifyEvent interface](nn-ksproxy-iksnotifyevent.md) | TBD |
| [IKsAllocatorEx interface](nn-ksproxy-iksallocatorex~r1.md) | TBD |
| [IKsInterfaceHandler interface](nn-ksproxy-iksinterfacehandler.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [KSALLOCATORMODE enumeration](ne-ksproxy-ksallocatormode.md) | TBD. |
| [FRAMING_PROP enumeration](ne-ksproxy-framing-prop.md) | TBD. |
| [FRAMING_CACHE_OPS enumeration](ne-ksproxy-framing-cache-ops.md) | TBD. |
| [PIPE_ALLOCATOR_PLACE enumeration](ne-ksproxy-pipe-allocator-place.md) | TBD. |
| [KSPEEKOPERATION enumeration](ne-ksproxy-kspeekoperation.md) | TBD. |
| [KSIOOPERATION enumeration](ne-ksproxy-ksiooperation.md) | TBD. |
| [PIPE_STATE enumeration](ne-ksproxy-pipe-state.md) | TBD. |
| [KS_LogicalMemoryType enumeration](ne-ksproxy-ks-logicalmemorytype.md) | TBD. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [IKsAllocatorEx structure](ns-ksproxy-iksallocatorex.md) | TBD |
| [IKsPin structure](ns-ksproxy-ikspin.md) | TBD |
| [KSSTREAM_SEGMENT structure](ns-ksproxy--ksstream-segment.md) | TBD |
| [OPTIMAL_WEIGHT_TOTALS structure](ns-ksproxy-optimal-weight-totals.md) | TBD. |
| [PIPE_TERMINATION structure](ns-ksproxy--pipe-termination.md) | TBD |
| [IKsAllocator structure](ns-ksproxy-iksallocator.md) | TBD |
| [KSSTREAM_SEGMENT structure](ns-ksproxy--ksstream-segment~r1.md) | The KSSTREAM_SEGMENT structure contains information that describes an I/O operation occurring on a stream. |
| [ALLOCATOR_PROPERTIES_EX structure](ns-ksproxy--allocator-properties-ex.md) | TBD |
| [IPin structure](ns-ksproxy-ipin.md) | TBD |
| [PIPE_DIMENSIONS structure](ns-ksproxy--pipe-dimensions.md) | TBD |

This header is used in these topics:

- [stream](..content/_stream)
