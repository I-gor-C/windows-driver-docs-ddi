# Declarations in the ks header
This header Ks contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [DEFINE_KSPROPERTY_ITEM_CLOCK_TIME function](nf-ks-define-ksproperty-item-clock-time.md) | TBD |
| [KsPinGetFirstCloneStreamPointer function](nf-ks-kspingetfirstclonestreampointer.md) | The KsPinGetFirstCloneStreamPointer function returns the first cloned stream pointer on Pin. |
| [KsAddObjectCreateItemToDeviceHeader function](nf-ks-ksaddobjectcreateitemtodeviceheader.md) | The KsAddObjectCreateItemToDeviceHeader function adds the specified create-item to an empty item in the previously allocated create item list for this device header. |
| [DEFINE_KSCREATE_DISPATCH_TABLE function](nf-ks-define-kscreate-dispatch-table.md) | TBD |
| [KsGateRemoveOffInputFromOr function](nf-ks-ksgateremoveoffinputfromor.md) | The KsGateRemoveOffInputFromOr function removes an existing input that is in the OFF state from an OR gate. |
| [DENY_USERMODE_ACCESS function](nf-ks-deny-usermode-access.md) | TBD |
| [KsReleaseDeviceSecurityLock function](nf-ks-ksreleasedevicesecuritylock.md) | The KsReleaseDeviceSecurityLock function releases a previously acquired security lock on the device object header. |
| [DEFINE_KSPIN_INTERFACE_ITEM function](nf-ks-define-kspin-interface-item.md) | TBD |
| [KsDeviceRegisterAggregatedClientUnknown function](nf-ks-ksdeviceregisteraggregatedclientunknown.md) | This inline function is a wrapper for KsRegisterAggregatedClientUnknown. |
| [KsGateCaptureThreshold function](nf-ks-ksgatecapturethreshold.md) | The KsGateCaptureThreshold function is used to capture an ON input of an AND gate specified by Gate. |
| [KsDeviceRegisterAdapterObject function](nf-ks-ksdeviceregisteradapterobject.md) | The KsDeviceRegisterAdapterObject function registers a DMA adapter object with AVStream for performing scatter/gather DMA on the specified device. All drivers compiled for Win64 should use IKsDeviceFunctions |
| [DEFINE_KSMETHOD_ALLOCATORSET function](nf-ks-define-ksmethod-allocatorset.md) | TBD |
| [KsGetNextSibling function](nf-ks-ksgetnextsibling.md) | The KsGetNextSibling function returns the next sibling of a given object. |
| [KsPinAcquireProcessingMutex function](nf-ks-kspinacquireprocessingmutex.md) | The KsPinAcquireProcessingMutex function acquires the processing mutex for the AVStream pin specified by Pin. |
| [DEFINE_KSFILTER_PIN_DESCRIPTORS function](nf-ks-define-ksfilter-pin-descriptors.md) | TBD |
| [KsFilterFactoryGetNextSiblingFilterFactory function](nf-ks-ksfilterfactorygetnextsiblingfilterfactory.md) | The KsFilterFactoryGetNextSiblingFilterFactory function returns the next filter factory belonging to the parent device of FilterFactory. |
| [KsPinGetAndGate function](nf-ks-kspingetandgate.md) | The KsPinGetAndGate function returns the processing control gate for Pin. |
| [KsGateTerminateOr function](nf-ks-ksgateterminateor.md) | The KsGateTerminateOr function deletes an existing OR gate and removes an input from any attached AND gate. |
| [DEFINE_KSMETHOD_SET function](nf-ks-define-ksmethod-set.md) | TBD |
| [KsPinSubmitFrameMdl function](nf-ks-kspinsubmitframemdl.md) | If a pin has been placed into injection mode by a call to KsPinRegisterFrameReturnCallback, the KsPinSubmitFrameMdl function submits a frame directly into the transport circuit. |
| [DEFINE_KSPROPERTY_ITEM_STREAM_PIPE_ID function](nf-ks-define-ksproperty-item-stream-pipe-id.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_PIN_NAME function](nf-ks-define-ksproperty-item-pin-name.md) | TBD |
| [KsStreamPointerCancelTimeout function](nf-ks-ksstreampointercanceltimeout.md) | The KsStreamPointerCancelTimeout function cancels a previously scheduled time-out callback on the specified stream pointer. |
| [KsAddDevice function](nf-ks-ksadddevice.md) | The KsAddDevice function is the default AddDevice handler installed by KsInitializeDriver. |
| [KsAcquireDevice function](nf-ks-ksacquiredevice.md) | The KsAcquireDevice function gains synchronous access for Device by acquiring the device mutex. |
| [KsFreeEventList function](nf-ks-ksfreeeventlist.md) | The KsFreeEventList function handles freeing all events from a specified list, with the assumption that these events are composed of KSEVENT_ENTRY structures. This function can only be called at PASSIVE_LEVEL. |
| [KsFilterGetAndGate function](nf-ks-ksfiltergetandgate.md) | The KsFilterGetAndGate function returns Filter's AND gate. |
| [KsGenerateDataEvent function](nf-ks-ksgeneratedataevent.md) | The KsGenerateDataEvent function generates one of the standard event notifications when given an event entry structure and callback data. |
| [KsGateTurnInputOn function](nf-ks-ksgateturninputon.md) | The KsGateTurnInputOn function turns on an existing input to Gate. |
| [KsPinPropertyHandler function](nf-ks-kspinpropertyhandler.md) | The KsPinPropertyHandler function performs standard handling of the static members of the KSPROPSETID_Pin property set. This handling does not include KSPROPERTY_PIN_CINSTANCES or KSPROPERTY_PIN_DATAINTERSECTION. |
| [KsGateInitialize function](nf-ks-ksgateinitialize.md) | The KsGateInitialize function initializes a gate for use. |
| [KsAllocateDeviceHeader function](nf-ks-ksallocatedeviceheader.md) | The KsAllocateDeviceHeader function allocates and initializes the required device extension header. |
| [KsMergeAutomationTables function](nf-ks-ksmergeautomationtables.md) | The KsMergeAutomationTables function merges two automation tables. |
| [KsSetInformationFile function](nf-ks-kssetinformationfile.md) | The KsSetInformationFile function performs an information set against the specified file object. The function attempts to use FastIoDispatch if possible, or it generates an information set against the device object. |
| [DEFINE_KSPROPERTY_ITEM_MEMORY_TRANSPORT function](nf-ks-define-ksproperty-item-memory-transport.md) | TBD |
| [KsPinGetReferenceClockInterface function](nf-ks-kspingetreferenceclockinterface.md) | The KsPinGetReferenceClockInterface function returns a COM style interface to the reference clock associated with Pin. This interface pointer will be an IKsReferenceClock interface. |
| [DEFINE_KSPROPERTY_ITEM_PIN_PROPOSEDATAFORMAT function](nf-ks-define-ksproperty-item-pin-proposedataformat.md) | TBD |
| [KsAllocateObjectBag function](nf-ks-ksallocateobjectbag.md) | The KsAllocateObjectBag function creates an object bag and associates it with a KSDEVICE. |
| [KsCreateAllocator function](nf-ks-kscreateallocator.md) | The KsCreateAllocator function creates a handle to an allocator for the given sink connection handle. This function does not complete the IRP or set the status in the IRP. |
| [KsStreamPointerClone function](nf-ks-ksstreampointerclone.md) | The KsStreamPointerClone function creates a clone of a given stream pointer. |
| [DEFINE_KSCREATE_ITEM function](nf-ks-define-kscreate-item.md) | TBD |
| [DEFINE_KSEVENT_ITEM function](nf-ks-define-ksevent-item.md) | TBD |
| [KsPinDataIntersectionEx function](nf-ks-kspindataintersectionex.md) | The KsPinDataIntersectionEx function handles the KSPROPERTY_PIN_DATAINTERSECTION through a callback function. |
| [DEFINE_KSPROPERTY_ITEM_CONNECTION_MDLCACHING function](nf-ks-define-ksproperty-item-connection-mdlcaching.md) | TBD |
| [KsStreamIo function](nf-ks-ksstreamio.md) | The KsStreamIo function performs a stream read or write against the specified file object. The function attempts to use FastIoDispatch if possible, or it generates a read or write request against the device object. |
| [KsIncrementCountedWorker function](nf-ks-ksincrementcountedworker.md) | Increments the current worker count, and optionally queues the counted work item with the worker previously created by KsRegisterCountedWorker. |
| [KsProcessPinUpdate function](nf-ks-ksprocesspinupdate.md) | The KsProcessPinUpdate function is called from within a filter-centric filter's AVStrMiniFilterProcess dispatch to update a process pin. |
| [DEFINE_KSPROPERTY_ITEM_CONNECTION_DATAFORMAT function](nf-ks-define-ksproperty-item-connection-dataformat.md) | TBD |
| [KsCreatePin function](nf-ks-kscreatepin~r1.md) | The KsCreatePin function passes a connection request to a device, creating a pin instance. This function can only be called at PASSIVE_LEVEL for kernel-mode clients. |
| [DEFINE_KSCREATE_ITEMNULL function](nf-ks-define-kscreate-itemnull.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_STREAMINTERFACE_HEADERSIZE function](nf-ks-define-ksproperty-item-streaminterface-headersize.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_DURATION function](nf-ks-define-ksproperty-item-mediaseeking-duration.md) | TBD |
| [DEFINE_GUIDNAMED function](nf-ks-define-guidnamed.md) | TBD |
| [KsDeviceGetFirstChildFilterFactory function](nf-ks-ksdevicegetfirstchildfilterfactory.md) | The KsDeviceGetFirstChildFilterFactory function returns the first child filter factory belonging to a given AVStream device. |
| [KsCreatePin function](nf-ks-kscreatepin.md) | The KsCreatePin function passes a connection request to a device, creating a pin instance. This function can only be called at PASSIVE_LEVEL for kernel-mode clients. |
| [DEFINE_KSPROPERTY_ITEM_CLOCK_FUNCTIONTABLE function](nf-ks-define-ksproperty-item-clock-functiontable.md) | TBD |
| [KsPinAttemptProcessing function](nf-ks-kspinattemptprocessing.md) | The KsPinAttemptProcessing function is used to resume processing on a specific pin on a pin-centric filter. It attempts to initiate processing on Pin by sending a processing dispatch call to Pin's processing object. |
| [KsPinGetAvailableByteCount function](nf-ks-kspingetavailablebytecount.md) | The KsPinGetAvailableByteCount routine outputs the number of bytes of input data ahead of the leading edge and the number of bytes of output buffer ahead of the leading edge, both for the queue of a caller-specified pin. |
| [KsValidateConnectRequest function](nf-ks-ksvalidateconnectrequest.md) | The KsValidateConnectRequest function validates a connection request and returns a pointer to the connection structure associated with the request.This function can only be called at PASSIVE_LEVEL. |
| [DEFINE_KSPROPERTY_ITEM_STREAM_QUALITY function](nf-ks-define-ksproperty-item-stream-quality.md) | TBD |
| [SetKsFramingRangeWeighted function](nf-ks-setksframingrangeweighted.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_CLOCK_CORRELATEDTIME function](nf-ks-define-ksproperty-item-clock-correlatedtime.md) | TBD |
| [KsFilterFactoryRegisterAggregatedClientUnknown function](nf-ks-ksfilterfactoryregisteraggregatedclientunknown.md) | This inline function is a wrapper for KsRegisterAggregatedClientUnknown. |
| [KsEnableEvent function](nf-ks-ksenableevent.md) | The KsEnableEvent function enables events requested through IOCTL_KS_ENABLE_EVENT. It responds to all event identifiers defined by the sets. This function can only be called at PASSIVE_LEVEL. |
| [KsAcquireResetValue function](nf-ks-ksacquireresetvalue.md) | The KsAcquireResetValue function retrieves the current reset state from an IOCTL_KS_RESET_STATE IRP. |
| [IKsControl::KsEvent method](nf-ks-ikscontrol-ksevent.md) | The IKsControl |
| [KsGetPinFromFileObject function](nf-ks-ksgetpinfromfileobject.md) | The KsGetPinFromFileObject function returns the AVStream pin object associated with FileObject. |
| [INITIALIZE_SIMPLE_FRAMING_EX function](nf-ks-initialize-simple-framing-ex.md) | TBD |
| [KsPropertyHandler function](nf-ks-kspropertyhandler.md) | Drivers call KsPropertyHandler function for IRP handling. |
| [KsQueryObjectCreateItem function](nf-ks-ksqueryobjectcreateitem.md) | The KsQueryObjectCreateItem function returns the create item assigned to the object when created. |
| [DEFINE_KSPROPERTY_ITEM_PIN_DATAFLOW function](nf-ks-define-ksproperty-item-pin-dataflow.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_STREAMALLOCATOR_STATUS function](nf-ks-define-ksproperty-item-streamallocator-status.md) | TBD |
| [KsPinRegisterPowerCallbacks function](nf-ks-kspinregisterpowercallbacks.md) | The KsPinRegisterPowerCallbacks function registers power management callbacks for Pin. |
| [KsFilterAddTopologyConnections function](nf-ks-ksfilteraddtopologyconnections.md) | The KsFilterAddTopologyConnections function adds new topology connections to a filter. |
| [KsMethodHandlerWithAllocator function](nf-ks-ksmethodhandlerwithallocator.md) | The KsMethodHandlerWithAllocator functions performs the same handling as KsMethodHandler, with the same restrictions, but allows an optional allocator callback to be used to provide a buffer for the parameters. |
| [DEFINE_KSPROPERTY_ITEM_CONNECTION_ALLOCATORFRAMING_EX function](nf-ks-define-ksproperty-item-connection-allocatorframing-ex.md) | TBD |
| [KsGateInitializeAnd function](nf-ks-ksgateinitializeand.md) | The KsGateInitializeAnd function initializes a KSGATE structure as an AND gate and attaches it to the OR gate specified by NextOrGate. |
| [KsFilterAttemptProcessing function](nf-ks-ksfilterattemptprocessing.md) | The KsFilterAttemptProcessing function attempts to initiate processing on Filter. |
| [KsCopyObjectBagItems function](nf-ks-kscopyobjectbagitems.md) | The KsCopyObjectBagItems function copies all items from one object bag into another. |
| [KsFilterGetDevice function](nf-ks-ksfiltergetdevice.md) | The KsFilterGetDevice function returns the AVStream device to which Filter belongs. |
| [KsAddItemToObjectBag function](nf-ks-ksadditemtoobjectbag.md) | The KsAddItemToObjectBag function adds an object or block of memory to the given object bag. |
| [DEFINE_KSPROPERTY_ITEM_CLOCK_PHYSICALTIME function](nf-ks-define-ksproperty-item-clock-physicaltime.md) | TBD |
| [DEFINE_NODE_DESCRIPTOR function](nf-ks-define-node-descriptor.md) | TBD |
| [DEFINE_KSPIN_DESCRIPTOR_TABLE function](nf-ks-define-kspin-descriptor-table.md) | TBD |
| [KsFilterFactorySetDeviceClassesState function](nf-ks-ksfilterfactorysetdeviceclassesstate.md) | The KsFilterFactorySetDeviceClassesState function enables or disables the device classes that have been registered by a given filter factory. |
| [KsSetTargetDeviceObject function](nf-ks-kssettargetdeviceobject.md) | The KsSetTargetDeviceObject function sets the target device object of an object. The function adds the object header to a list of object headers that have target devices. |
| [KsGetDefaultClockTime function](nf-ks-ksgetdefaultclocktime.md) | The KsGetDefaultClockTime function gets the current time of the clock.The function can be called at DISPATCH_LEVEL. |
| [KsAcquireDeviceSecurityLock function](nf-ks-ksacquiredevicesecuritylock.md) | The KsAcquireDeviceSecurityLock function acquires the security lock associated with a device object. |
| [DEFINE_KSPROPERTY_STREAMINTERFACESET function](nf-ks-define-ksproperty-streaminterfaceset.md) | TBD |
| [KsFilterCreateNode function](nf-ks-ksfiltercreatenode.md) | The KsFilterCreateNode function creates a new topology node on the specified filter. |
| [KsPinGetOuterUnknown function](nf-ks-kspingetouterunknown.md) | The KsPinGetOuterUnknown function returns the outer IUnknown of the pin specified by Pin. |
| [KsAllocateDefaultClock function](nf-ks-ksallocatedefaultclock.md) | The KsAllocateDefaultClock function allocates and initializes the default clock structure. |
| [MF_SET_SHARED_MDLHANDLE function](nf-ks-mf-set-shared-mdlhandle.md) | TBD |
| [KsEdit function](nf-ks-ksedit.md) | The _KsEdit function guarantees that a given item is dynamically allocated and associated with an AVStream object through the object bag. |
| [DEFINE_KSPROPERTY_ITEM_STREAMALLOCATOR_FUNCTIONTABLE function](nf-ks-define-ksproperty-item-streamallocator-functiontable.md) | TBD |
| [KsValidateClockCreateRequest function](nf-ks-ksvalidateclockcreaterequest.md) | The KsValidateClockCreateRequest function validates the clock creation request and returns the create structure associated with the request.This can only be called at PASSIVE_LEVEL. |
| [DEFINE_KSPROPERTY_ITEM_STREAM_DEGRADATION function](nf-ks-define-ksproperty-item-stream-degradation.md) | TBD |
| [KsPropertyHandlerWithAllocator function](nf-ks-kspropertyhandlerwithallocator.md) | TBD |
| [KsGenerateEventList function](nf-ks-ksgenerateeventlist.md) | The KsGenerateEventList function enumerates the event list and searches for the specified event to generate. |
| [KsCancelIo function](nf-ks-kscancelio.md) | The KsCancelIo function cancels all IRPs on the specified cancel list. If an IRP on the list does not have a cancel routine, only the cancel bit is set in the IRP. The function can be called at IRQ level DISPATCH_LEVEL or lower. |
| [KsFilterGetFirstChildPin function](nf-ks-ksfiltergetfirstchildpin.md) | The KsFilterGetFirstChildPin function returns the first instantiated pin of type PinID on the filter specified by Filter. |
| [KsStreamPointerGetIrp function](nf-ks-ksstreampointergetirp.md) | The KsStreamPointerGetIrp function returns the IRP associated with the frame that is referenced by the given stream pointer. |
| [KsReferenceBusObject function](nf-ks-ksreferencebusobject.md) | References the bus Physical device object. |
| [KsAllocateExtraData function](nf-ks-ksallocateextradata.md) | The KsAllocateExtraData function is used with streaming IRPs to allocate a buffer to contain additional header data. A pointer to the allocated buffer is returned, and the buffer must eventually be freed by the caller. |
| [KsFilterReleaseControl function](nf-ks-ksfilterreleasecontrol.md) | The KsFilterReleaseControl function releases the control mutex for the AVStream filter specified by Filter. |
| [DEFINE_KSFILTER_DESCRIPTOR_TABLE function](nf-ks-define-ksfilter-descriptor-table.md) | TBD |
| [KsValidateTopologyNodeCreateRequest function](nf-ks-ksvalidatetopologynodecreaterequest.md) | The KsValidateTopologyNodeCreateRequest function validates a topology node creation request and returns the create structure associated with the request. The function can only be called at PASSIVE_LEVEL. |
| [KsFilterGetParentFilterFactory function](nf-ks-ksfiltergetparentfilterfactory.md) | The KsFilterGetParentFilterFactory function returns the parent filter factory of the given filter. |
| [DEFINE_KSPROPERTY_ITEM_STREAM_RATE function](nf-ks-define-ksproperty-item-stream-rate.md) | TBD |
| [KsLoadResource function](nf-ks-ksloadresource.md) | Copies (loads) a resource from the given image. |
| [DEFINE_KSAUTOMATION_TABLE function](nf-ks-define-ksautomation-table.md) | TBD |
| [KsSetDefaultClockState function](nf-ks-kssetdefaultclockstate.md) | The KsSetDefaultClockState function sets the current state of the clock that is used to reflect the current state of the underlying filter pin. |
| [KsDeviceGetOuterUnknown function](nf-ks-ksdevicegetouterunknown.md) | The KsDeviceGetOuterUnknown function returns the outer IUnknown of the AVStream device specified by Device. |
| [KsDereferenceBusObject function](nf-ks-ksdereferencebusobject.md) | Dereferences the bus Physical Device Object. |
| [KsGenerateEvents function](nf-ks-ksgenerateevents.md) | The KsGenerateEvents function generates events of an indicated type that are present in Object's event list. |
| [KsStreamPointerGetMdl function](nf-ks-ksstreampointergetmdl.md) | The KsStreamPointerGetMdl function returns the MDL associated with the frame referenced by StreamPointer. |
| [KsReadFile function](nf-ks-ksreadfile.md) | The KsReadFile function performs a read against the specified file object. |
| [IKsReferenceClock::GetCorrelatedPhysicalTime method](nf-ks-iksreferenceclock-getcorrelatedphysicaltime.md) | The IKsReferenceClock |
| [KsSetDefaultClockTime function](nf-ks-kssetdefaultclocktime.md) | The KsSetDefaultClockTime function sets the current time of the clock. |
| [KsStreamPointerAdvanceOffsetsAndUnlock function](nf-ks-ksstreampointeradvanceoffsetsandunlock.md) | The KsStreamPointerAdvanceOffsetsAndUnlock function advances StreamPointer the specified number of bytes into the stream (adjusting the OffsetIn and OffsetOut fields of StreamPointer as requested) and unlocks it. |
| [KsCreateDefaultSecurity function](nf-ks-kscreatedefaultsecurity.md) | The KsCreateDefaultSecurity function creates a security descriptor with default security, optionally inheriting parameters from a parent security descriptor. |
| [DEFINE_KSPROPERTY_SET_TABLE function](nf-ks-define-ksproperty-set-table.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_PIN_COMMUNICATION function](nf-ks-define-ksproperty-item-pin-communication.md) | TBD |
| [KsPinGetCopyRelationships function](nf-ks-kspingetcopyrelationships.md) | The KsPinGetCopyRelationships function returns copy relationship information for a pin that is contained within a pin-centric filter. |
| [KsAllocateObjectHeader function](nf-ks-ksallocateobjectheader.md) | The KsAllocateObjectHeader function initializes the required file context header. |
| [DEFINE_KSCREATE_ITEMEX function](nf-ks-define-kscreate-itemex.md) | TBD |
| [DEFINE_KSMETHOD_ITEM function](nf-ks-define-ksmethod-item.md) | TBD |
| [SetDefaultKsCompression function](nf-ks-setdefaultkscompression.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_PIN_MEDIUMS function](nf-ks-define-ksproperty-item-pin-mediums.md) | TBD |
| [DEFINE_KSEVENT_SET_TABLE function](nf-ks-define-ksevent-set-table.md) | TBD |
| [KsGetDefaultClockState function](nf-ks-ksgetdefaultclockstate.md) | The KsGetDefaultClockState function gets the current state of the clock.The function can be called at DISPATCH_LEVEL. |
| [DEFINE_KSPROPERTY_ITEM_STREAM_MASTERCLOCK function](nf-ks-define-ksproperty-item-stream-masterclock.md) | TBD |
| [KsPinDataIntersection function](nf-ks-kspindataintersection.md) | The KsPinDataIntersection function handles the KSPROPERTY_PIN_DATAINTERSECTION property through a callback function and performs much of the initial validation of the parameters that are passed. |
| [KsCacheMedium function](nf-ks-kscachemedium.md) | The KsCacheMedium function improves graph building performance of pins that use Mediums to define connectivity. |
| [KsPinAcquireControl function](nf-ks-kspinacquirecontrol.md) | The KsPinAcquireControl function acquires the control mutex for the AVStream pin specified by Pin. |
| [DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_STOPPOSITION function](nf-ks-define-ksproperty-item-mediaseeking-stopposition.md) | TBD |
| [DEFINE_KSPIN_MEDIUM_ITEM function](nf-ks-define-kspin-medium-item.md) | TBD |
| [KsStreamPointerAdvance function](nf-ks-ksstreampointeradvance.md) | The KsStreamPointerAdvance function advances a stream pointer to the next data frame. |
| [KsFilterAcquireControl function](nf-ks-ksfilteracquirecontrol.md) | The KsFilterAcquireControl function acquires the filter control mutex for the AVStream filter specified by Filter. |
| [KsDeviceSetBusData function](nf-ks-ksdevicesetbusdata.md) | The KsDeviceSetBusData function writes data to the bus on which the specified AVStream device resides. |
| [KsDispatchFastIoDeviceControlFailure function](nf-ks-ksdispatchfastiodevicecontrolfailure.md) | The KsDispatchFastIoDeviceControlFailure function is used in a KSDISPATCH_TABLE.FastDeviceIoControl entry that are not handled. The function should always return FALSE. |
| [KsGetObjectTypeFromFileObject function](nf-ks-ksgetobjecttypefromfileobject.md) | The KsGetObjectTypeFromFileObject function returns the AVStream object type that is associated with a given file object. |
| [DEFINE_KSPROPERTY_ITEM_CLOCK_STATE function](nf-ks-define-ksproperty-item-clock-state.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_CONNECTION_ALLOCATORFRAMING function](nf-ks-define-ksproperty-item-connection-allocatorframing.md) | TBD |
| [KSEVENT_SET_IRP_STORAGE function](nf-ks-ksevent-set-irp-storage.md) | TBD |
| [KsPinGetConnectedPinFileObject function](nf-ks-kspingetconnectedpinfileobject.md) | The KsPinGetConnectedPinFileObject function returns the file object for the pin to which Pin is connected. Works only for source pins. |
| [KsGetObjectFromFileObject function](nf-ks-ksgetobjectfromfileobject.md) | The KsGetObjectFromFileObject function returns the AVStream object cast to PVOID from FileObject. |
| [DECLARE_SIMPLE_FRAMING_EX function](nf-ks-declare-simple-framing-ex.md) | TBD |
| [DEFINE_KSEVENT_TABLE function](nf-ks-define-ksevent-table.md) | TBD |
| [KsCreateFilterFactory function](nf-ks-kscreatefilterfactory.md) | The KsCreateFilterFactory function adds a filter factory to a given device. |
| [DEFINE_KSPROPERTY_ITEM_STREAM_RATECAPABILITY function](nf-ks-define-ksproperty-item-stream-ratecapability.md) | TBD |
| [KsGateAddOnInputToOr function](nf-ks-ksgateaddoninputtoor.md) | The KsGateAddOnInputToOr function adds a new input in the ON state to a given OR gate. |
| [DEFINE_KSPROPERTY_ITEM_CLOCK_CORRELATEDPHYSICALTIME function](nf-ks-define-ksproperty-item-clock-correlatedphysicaltime.md) | TBD |
| [KSEVENT_ENTRY_IRP_STORAGE function](nf-ks-ksevent-entry-irp-storage.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_TOPOLOGY_CONNECTIONS function](nf-ks-define-ksproperty-item-topology-connections.md) | TBD |
| [KsReleaseControl function](nf-ks-ksreleasecontrol.md) | The KsReleaseControl function releases the control mutex for Object. |
| [KsDispatchInvalidDeviceRequest function](nf-ks-ksdispatchinvaliddevicerequest.md) | The KsDispatchInvalidDeviceRequest function is used in KSDISPATCH_TABLE entries that are not handled and that need to return STATUS_INVALID_DEVICE_REQUEST. |
| [KsFilterRegisterAggregatedClientUnknown function](nf-ks-ksfilterregisteraggregatedclientunknown.md) | This inline function is a wrapper for KsRegisterAggregatedClientUnknown. |
| [KsGetObjectTypeFromIrp function](nf-ks-ksgetobjecttypefromirp.md) | The KsGetObjectTypeFromIrp function returns the AVStream object type that is associated with a given IRP. |
| [KsStreamPointerUnlock function](nf-ks-ksstreampointerunlock.md) | The KsStreamPointerUnlock function unlocks a stream pointer that has previously been locked by an acquisition function (KsGetXxxEdgeStreamPointer) or by KsStreamPointerLock. |
| [DEFINE_KSPROPERTY_ITEM_PIN_CATEGORY function](nf-ks-define-ksproperty-item-pin-category.md) | TBD |
| [DEFINE_GUIDEX function](nf-ks-define-guidex.md) | TBD |
| [KsInitializeDevice function](nf-ks-ksinitializedevice.md) | The KsInitializeDevice function is called by AVStream to initialize the AVStream device class from within KsCreateDevice. |
| [DEFINE_KSPROPERTY_ITEM_TOPOLOGY_NAME function](nf-ks-define-ksproperty-item-topology-name.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_PIN_CINSTANCES function](nf-ks-define-ksproperty-item-pin-cinstances.md) | TBD |
| [KsStreamPointerLock function](nf-ks-ksstreampointerlock.md) | The KsStreamPointerLock function attempts to lock the specified stream pointer. |
| [KsRecalculateStackDepth function](nf-ks-ksrecalculatestackdepth.md) | TBD |
| [KsDefaultAddEventHandler function](nf-ks-ksdefaultaddeventhandler.md) | The KsDefaultAddEventHandler function is a default routine to handle event 'add' requests. |
| [KsFreeObjectCreateItem function](nf-ks-ksfreeobjectcreateitem.md) | Frees the slot for the specified create item. |
| [DEFINE_KSPROPERTY_ITEM_TOPOLOGY_CATEGORIES function](nf-ks-define-ksproperty-item-topology-categories.md) | TBD |
| [KsInitializeDeviceProfile function](nf-ks-ksinitializedeviceprofile.md) | TBD |
| [KsNullDriverUnload function](nf-ks-ksnulldriverunload.md) | The KsNullDriverUnload function is a default function a driver can use when it has no other tasks to do in its unload function, but must still allow the device to be unloaded by its presence. |
| [KsValidateAllocatorFramingEx function](nf-ks-ksvalidateallocatorframingex.md) | TBD |
| [KsCreateClock2 function](nf-ks-kscreateclock2.md) | Creates a handle to a clock instance. Call this function after the Component Object Model (COM) is initialized. |
| [DEFINE_KSPROPERTY_ITEM_CONNECTION_STATE function](nf-ks-define-ksproperty-item-connection-state.md) | TBD |
| [KsPinSubmitFrame function](nf-ks-kspinsubmitframe.md) | If a pin has been placed into injection mode by a call to KsPinRegisterFrameReturnCallback, the KsPinSubmitFrame function submits a frame directly into the transport circuit. |
| [KsHandleSizedListQuery function](nf-ks-kshandlesizedlistquery.md) | The KsHandleSizedListQuery function, depending on the length of the system buffer, returns either the size of the buffer needed, number of entries in the specified data list, or copies the entries themselves. |
| [KsCreateAllocator function](nf-ks-kscreateallocator~r1.md) | The KsCreateAllocator function creates a handle to an allocator for the given sink connection handle. This function does not complete the IRP or set the status in the IRP. |
| [IKsReferenceClock::GetCorrelatedTime method](nf-ks-iksreferenceclock-getcorrelatedtime.md) | The IKsReferenceClock |
| [MAKEINTRESOURCE function](nf-ks-makeintresource.md) | TBD |
| [IKsControl::KsProperty method](nf-ks-ikscontrol-ksproperty.md) | The IKsControl |
| [DEFINE_KSFILTER_CATEGORIES function](nf-ks-define-ksfilter-categories.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_PIN_GLOBALCINSTANCES function](nf-ks-define-ksproperty-item-pin-globalcinstances.md) | TBD |
| [KsGateAddOnInputToAnd function](nf-ks-ksgateaddoninputtoand.md) | The KsGateAddOnInputToAnd function adds a new input in the ON state to a given AND gate. |
| [KsGetDeviceForDeviceObject function](nf-ks-ksgetdevicefordeviceobject.md) | The KsGetDeviceForDeviceObject function returns the AVStream device structure for a given functional device object. |
| [KsGateTurnInputOff function](nf-ks-ksgateturninputoff.md) | The KsGateTurnInputOff function turns off an existing input to Gate. |
| [KsFilterAcquireProcessingMutex function](nf-ks-ksfilteracquireprocessingmutex.md) | The KsFilterAcquireProcessingMutex function acquires the processing mutex for a specified AVStream filter. |
| [DEFINE_KSMETHOD_TABLE function](nf-ks-define-ksmethod-table.md) | TBD |
| [KsFilterFactoryGetSymbolicLink function](nf-ks-ksfilterfactorygetsymboliclink.md) | The KsFilterFactoryGetSymbolicLink function returns the symbolic link associated with a given filter factory. |
| [DEFINE_KSPROPERTY_ITEM_STREAM_TIMEFORMAT function](nf-ks-define-ksproperty-item-stream-timeformat.md) | TBD |
| [SIZEOF_ARRAY function](nf-ks-sizeof-array.md) | TBD |
| [KsForwardIrp function](nf-ks-ksforwardirp.md) | The KsForwardIrp function forwards an IRP to the specified driver after initializing the next stack location and setting the file object. |
| [KsQueueWorkItem function](nf-ks-ksqueueworkitem.md) | The KsQueueWorkItem function queues the specified work item with a worker previous created by the KsRegisterWorker function. |
| [DEFINE_KSPROPERTY_ITEM_PIN_DATAINTERSECTION function](nf-ks-define-ksproperty-item-pin-dataintersection.md) | TBD |
| [KsDispatchIrp function](nf-ks-ksdispatchirp.md) | KsDispatchIrp calls a dispatch routine corresponding to the function code of the specified IRP. KsDispatchIrp then returns the status code from this call. |
| [DEFINE_KSMETHOD_ITEM_STREAMIO_READ function](nf-ks-define-ksmethod-item-streamio-read.md) | TBD |
| [IKsReferenceClock::GetPhysicalTime method](nf-ks-iksreferenceclock-getphysicaltime.md) | The IKsReferenceClock |
| [DEFINE_KSFILTER_DESCRIPTOR function](nf-ks-define-ksfilter-descriptor.md) | TBD |
| [DEFINE_KSAUTOMATION_METHODS function](nf-ks-define-ksautomation-methods.md) | TBD |
| [KsCreateTopologyNode function](nf-ks-kscreatetopologynode.md) | The KsCreateTopologyNode function creates a handle to a topology node instance. The function can only be called at PASSIVE_LEVEL. |
| [KSPROPERTY_SET_IRP_STORAGE function](nf-ks-ksproperty-set-irp-storage.md) | TBD |
| [KsDeviceGetBusData function](nf-ks-ksdevicegetbusdata.md) | The KsDeviceGetBusData function reads data from the bus where the given AVStream device resides. |
| [KsFilterAddEvent function](nf-ks-ksfilteraddevent.md) | The KsFilterAddEvent function adds an event to Filter's event list. |
| [KsGateRemoveOffInputFromAnd function](nf-ks-ksgateremoveoffinputfromand.md) | The KsGateRemoveOffInputFromAnd function removes an existing input that is in the OFF state from an AND gate. |
| [KsGateGetStateUnsafe function](nf-ks-ksgategetstateunsafe.md) | The KsGateGetStateUnsafe function returns the state of the given gate (open or closed) in an unsafe manner, that is without regard to synchronization. |
| [KsCreateDefaultClock function](nf-ks-kscreatedefaultclock.md) | Given an IRP_MJ_CREATE request, the KsCreateDefaultClock function creates a default clock that uses the system clock as a time base and associates the IoGetCurrentIrpStackLocation(Irp)-&gt;FileObject with the clock using an internal dispatch table (KSDISPATCH_TABLE). Does not complete the IRP or set the status in the IRP.The KsCreateDefaultClock function can only be called at PASSIVE_LEVEL. |
| [DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_CAPABILITIES function](nf-ks-define-ksproperty-item-mediaseeking-capabilities.md) | TBD |
| [KsMoveIrpsOnCancelableQueue function](nf-ks-ksmoveirpsoncancelablequeue.md) | The KsMoveIrpsOnCancelableQueue function moves the specified IRPs from the SourceList parameter to the DestinationList parameter depending on the value returned from the minidriver-defined KStrIrpListCallback function. |
| [KSMETHOD_SET_IRP_STORAGE function](nf-ks-ksmethod-set-irp-storage.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_CONNECTION_PRIORITY function](nf-ks-define-ksproperty-item-connection-priority.md) | TBD |
| [KsGetFilterFromFileObject function](nf-ks-ksgetfilterfromfileobject.md) | The KsGetFilterFromFileObject function returns the AVStream filter object associated with FileObject. |
| [KsPinRegisterFrameReturnCallback function](nf-ks-kspinregisterframereturncallback.md) | The KsPinRegisterFrameReturnCallback function registers a frame return callback with AVStream for a given pin. |
| [KsGateTerminateAnd function](nf-ks-ksgateterminateand.md) | The KsGateTerminateAnd function deletes an existing AND gate and removes an input from any attached OR gate. |
| [DEFINE_KSPROPERTY_ITEM_PIN_INTERFACES function](nf-ks-define-ksproperty-item-pin-interfaces.md) | TBD |
| [DEFINE_KSPROPERTY_SET function](nf-ks-define-ksproperty-set.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_CONNECTION_PROPOSEDATAFORMAT function](nf-ks-define-ksproperty-item-connection-proposedataformat.md) | TBD |
| [KsDefaultDeviceIoCompletion function](nf-ks-ksdefaultdeviceiocompletion.md) | The KsDefaultDeviceIoCompletion function is used to return a default response and to complete any device I/O control. |
| [KsReleaseDevice function](nf-ks-ksreleasedevice.md) | The KsReleaseDevice function releases the device mutex and exits the critical region. |
| [DEFINE_GUIDSTRUCT function](nf-ks-define-guidstruct.md) | TBD |
| [SetDontCareKsFramingRange function](nf-ks-setdontcareksframingrange.md) | TBD |
| [KsQueryObjectAccessMask function](nf-ks-ksqueryobjectaccessmask.md) | The KsQueryObjectAccessMask function returns the access originally granted to the first client that created a handle on the associated object. Access cannot be changed by duplicating handles. |
| [KsGetParent function](nf-ks-ksgetparent.md) | The KsGetParent function acquires the parent of the given object. |
| [KsFilterFactoryAddCreateItem function](nf-ks-ksfilterfactoryaddcreateitem.md) | The KsFilterFactoryAddCreateItem function adds a new create item for the specified filter factory. |
| [KsStreamPointerGetNextClone function](nf-ks-ksstreampointergetnextclone.md) | The KsStreamPointerGetNextClone function returns the clone stream pointer that was cloned immediately after the specified clone. |
| [KsFastMethodHandler function](nf-ks-ksfastmethodhandler.md) | The KsFastMethodHandler function handles fast methods requested through IOCTL_KS_METHOD. It responds to all method identifiers defined by the sets that are also contained in the fast I/O list. This function can only be called at PASSIVE_LEVEL. |
| [KsFreeObjectBag function](nf-ks-ksfreeobjectbag.md) | The KsFreeObjectBag function empties and frees an object bag. |
| [IKsReferenceClock::GetState method](nf-ks-iksreferenceclock-getstate.md) | The IKsReferenceClock |
| [KsCreateDevice function](nf-ks-kscreatedevice.md) | The KsCreateDevice function creates an AVStream device. |
| [DEFINE_KSMETHOD_ITEM_STREAMIO_WRITE function](nf-ks-define-ksmethod-item-streamio-write.md) | TBD |
| [KsUnserializeObjectPropertiesFromRegistry function](nf-ks-ksunserializeobjectpropertiesfromregistry.md) | The KsUnserializeObjectPropertiesFromRegistry function, when given a destination object and a registry path, enumerates the named values and applies them as serialized data to the specified property sets listed in the serialized data. |
| [KsAllocateObjectCreateItem function](nf-ks-ksallocateobjectcreateitem.md) | The KsAllocateObjectCreateItem function allocates a slot for the specified create item, optionally allocating space for and copying the create item data as well. |
| [DEFINE_KSPROPERTY_ITEM_PIN_DATARANGES function](nf-ks-define-ksproperty-item-pin-dataranges.md) | TBD |
| [KsFastPropertyHandler function](nf-ks-ksfastpropertyhandler.md) | The KsFastPropertyHandler function handles fast property requests through IOCTL_KS_PROPERTY. It responds to all property identifiers defined by the sets that are also contained in the fast I/O list. This function can only be called at PASSIVE_LEVEL. |
| [IKsDeviceFunctions::RegisterAdapterObjectEx method](nf-ks-iksdevicefunctions-registeradapterobjectex.md) | The IKsDeviceFunctions |
| [KsPinGetConnectedPinInterface function](nf-ks-kspingetconnectedpininterface.md) | The KsPinGetConnectedPinInterface function queries the pin to which Pin is connected for a COM style interface. |
| [KsEditSized function](nf-ks-kseditsized.md) | TBD |
| [DEFINE_KSPIN_DESCRIPTOR_ITEM function](nf-ks-define-kspin-descriptor-item.md) | TBD |
| [KsDispatchSetSecurity function](nf-ks-ksdispatchsetsecurity.md) | The KsDispatchSetSecurity function is used in the KSDISPATCH_TABLE.SetSecurity entry to handle setting the current security descriptor. |
| [KsAddEvent function](nf-ks-ksaddevent.md) | The KsAddEvent function adds an event to Object's event list. |
| [KsMapModuleName function](nf-ks-ksmapmodulename.md) | The KsMapModuleName function returns the image name and resource identifier that corresponds to the PhysicalDeviceObject and ModuleName parameters. |
| [KsFreeObjectCreateItemsByContext function](nf-ks-ksfreeobjectcreateitemsbycontext.md) | Frees all create items with a specific context. |
| [DEFINE_KSPROPERTY_ITEM_PIN_NECESSARYINSTANCES function](nf-ks-define-ksproperty-item-pin-necessaryinstances.md) | TBD |
| [KsFilterCreatePinFactory function](nf-ks-ksfiltercreatepinfactory.md) | The KsFilterCreatePinFactory function creates a new pin factory on the specified filter. |
| [KsGenerateThermalEvent function](nf-ks-ksgeneratethermalevent.md) | This function is used by clients (miniport drivers) that do not want to subscribe to the thermal manager, but want to do their own thermal management. |
| [DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_PREROLL function](nf-ks-define-ksproperty-item-mediaseeking-preroll.md) | TBD |
| [KsCompletePendingRequest function](nf-ks-kscompletependingrequest.md) | The KsCompletePendingRequest function is used to complete an I/O request in response to which an AVStream dispatch function previously returned STATUS_PENDING. |
| [KsSynchronousIoControlDevice function](nf-ks-kssynchronousiocontroldevice.md) | The KsSynchronousIoControlDevice function performs a synchronous device I/O control on the target device object. It waits in a nonalertable state until the I/O completes. This function can only be called at PASSIVE_LEVEL. |
| [KsDeviceRegisterThermalDispatch function](nf-ks-ksdeviceregisterthermaldispatch.md) | This function is used by the Avstream miniport driver to register callbacks for thermal notifications with the KS port driver. |
| [KsFilterFactoryUpdateCacheData function](nf-ks-ksfilterfactoryupdatecachedata.md) | The KsFilterFactoryUpdateCacheData function updates the FilterData registry key and the Medium cache (a set of registry keys) for a given filter factory. |
| [KsPinHandshake function](nf-ks-kspinhandshake.md) | The KsPinHandshake function attempts a protocol handshake with a connected pin. |
| [DEFINE_KSPROPERTY_ITEM_STREAM_FRAMETIME function](nf-ks-define-ksproperty-item-stream-frametime.md) | TBD |
| [KsGetOuterUnknown function](nf-ks-ksgetouterunknown.md) | The KsGetOuterUnknown function returns the outer IUnknown of a given AVStream object. |
| [KsTopologyPropertyHandler function](nf-ks-kstopologypropertyhandler.md) | The KsTopologyPropertyHandler function performs standard handling of the static members of the KSPROPSETID_Topology Property Set. The function uses the KSTOPOLOGY structure, which describes the set of information that is returned by this property set. |
| [KsGateAddOffInputToAnd function](nf-ks-ksgateaddoffinputtoand.md) | The KsGateAddOffInputToAnd function adds a new input in the OFF state to a given AND gate. |
| [DEFINE_KSPROPERTY_ITEM function](nf-ks-define-ksproperty-item.md) | TBD |
| [KsCreateAllocator2 function](nf-ks-kscreateallocator2.md) | Creates a handle to an allocator for the given sink connection handle. This function does not complete the IRP or set the status in the IRP. |
| [KsAllocateDefaultClockEx function](nf-ks-ksallocatedefaultclockex.md) | The KsAllocateDefaultClockEx function allocates and initializes the default clock structure. |
| [KsPinGetNextSiblingPin function](nf-ks-kspingetnextsiblingpin.md) | The KsPinGetNextSiblingPin function returns the next instantiated pin of the same type and on the same filter as Pin. |
| [KSEVENT_ITEM_IRP_STORAGE function](nf-ks-ksevent-item-irp-storage.md) | TBD |
| [KsInitializeDriver function](nf-ks-ksinitializedriver.md) | The KsInitializeDriver function initializes the driver object of an AVStream minidriver. |
| [KsSetTargetState function](nf-ks-kssettargetstate.md) | Sets the enabled state of a target device associated with the specified object header. |
| [DEFINE_KSAUTOMATION_PROPERTIES function](nf-ks-define-ksautomation-properties.md) | TBD |
| [KsPinGetTrailingEdgeStreamPointer function](nf-ks-kspingettrailingedgestreampointer.md) | The KsPinGetTrailingEdgeStreamPointer function acquires the trailing edge stream pointer for the queue associated with the specified pin. |
| [KsAcquireCachedMdl function](nf-ks-ksacquirecachedmdl.md) | This function is used to acquire the MDL cached by the KS port driver. The function is used by a kernel mode driver to acquire the MDL for a pipeline-supplied sample generated by an Avstream driver. |
| [KsWriteFile function](nf-ks-kswritefile.md) | The KsWriteFile function performs a write against the specified file object. |
| [KSCONVERT_PERFORMANCE_TIME function](nf-ks-ksconvert-performance-time.md) | TBD |
| [KsUnregisterWorker function](nf-ks-ksunregisterworker.md) | The KsUnregisterWorker function allows clients to unregister a worker. |
| [KsPinAddEvent function](nf-ks-kspinaddevent.md) | The KsPinAddEvent function adds a specified event to Pin's event list. |
| [KsCreateDefaultAllocator function](nf-ks-kscreatedefaultallocator.md) | Given a validated IRP_MJ_CREATE request, the KsCreateDefaultAllocator function creates a default allocator that uses the specified memory pool and associates the IoGetCurrentIrpStackLocation(Irp)-&gt;FileObject with the allocator using an internal dispatch table (KSDISPATCH_TABLE). |
| [KSPROPERTY_ATTRIBUTES_IRP_STORAGE function](nf-ks-ksproperty-attributes-irp-storage.md) | TBD |
| [DEFINE_KSPIN_INTERFACE_TABLE function](nf-ks-define-kspin-interface-table.md) | TBD |
| [KsFilterGenerateEvents function](nf-ks-ksfiltergenerateevents.md) | The KsFilterGenerateEvents function generates events of an indicated type that are present in Filter's event list. |
| [DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_POSITION function](nf-ks-define-ksproperty-item-mediaseeking-position.md) | TBD |
| [KsCreatePin2 function](nf-ks-kscreatepin2.md) | Passes a connection request to a device, creating a pin instance. |
| [DEFINE_KSPROPERTY_ITEM_PIN_CONSTRAINEDDATARANGES function](nf-ks-define-ksproperty-item-pin-constraineddataranges.md) | TBD |
| [DEFINE_KSDISPATCH_TABLE function](nf-ks-define-ksdispatch-table.md) | TBD |
| [KsFreeObjectHeader function](nf-ks-ksfreeobjectheader.md) | The KsFreeObjectHeader function cleans up and frees a previously allocated object header. |
| [DEFINE_KSPROPERTY_CLOCKSET function](nf-ks-define-ksproperty-clockset.md) | TBD |
| [KsStreamPointerSetStatusCode function](nf-ks-ksstreampointersetstatuscode.md) | The KsStreamPointerSetStatusCode function allows specification of a successful or unsuccessful error code with which to complete the given IRP. |
| [KsForwardAndCatchIrp function](nf-ks-ksforwardandcatchirp.md) | The KsForwardAndCatchIrp function forwards an IRP to the specified driver after initializing the next stack location, and regains control of the IRP on completion from that driver. |
| [KsQueryDevicePnpObject function](nf-ks-ksquerydevicepnpobject.md) | The KsQueryDevicePnpObject function returns the PnP device object that can be stored in the device header. This is the next device object on the PnP stack and is the device object that PnP requests are forwarded to if KsDefaultDispatchPnp is used. |
| [KsCreateTopologyNode2 function](nf-ks-kscreatetopologynode2.md) | Creates a handle to a topology node instance. |
| [DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_FORMATS function](nf-ks-define-ksproperty-item-mediaseeking-formats.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_PIN_CTYPES function](nf-ks-define-ksproperty-item-pin-ctypes.md) | TBD |
| [KsRegisterFilterWithNoKSPins function](nf-ks-ksregisterfilterwithnokspins.md) | The KsRegisterFilterWithNoKSPins function registers with DirectShow filters that have no kernel streaming pins and, therefore, do not stream in kernel mode. |
| [KsDispatchSpecificMethod function](nf-ks-ksdispatchspecificmethod.md) | The KsDispatchSpecificMethod function dispatches a method to a specific handler. The function assumes that the caller has previously dispatched the IRP to a handler through the KsMethodHandler function. The function can only be called at PASSIVE_LEVEL. |
| [KsRegisterWorker function](nf-ks-ksregisterworker.md) | The KsRegisterWorker function handles clients registering for use of a thread. |
| [DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_POSITIONS function](nf-ks-define-ksproperty-item-mediaseeking-positions.md) | TBD |
| [KsReleaseIrpOnCancelableQueue function](nf-ks-ksreleaseirponcancelablequeue.md) | The KsReleaseIrpOnCancelableQueue function releases an acquired IRP that is already on a queue that can be canceled. |
| [KsGetNodeIdFromIrp function](nf-ks-ksgetnodeidfromirp.md) | The KsGetNodeIdFromIrp function returns the node ID of the node to which Irp was submitted. |
| [KsStreamPointerScheduleTimeout function](nf-ks-ksstreampointerscheduletimeout.md) | The KsStreamPointerScheduleTimeout function registers a timeout callback with AVStream for the given stream pointer. |
| [DEFINE_KSPROPERTY_TABLE function](nf-ks-define-ksproperty-table.md) | TBD |
| [DEFINE_KSAUTOMATION_EVENTS function](nf-ks-define-ksautomation-events.md) | TBD |
| [KsSetPowerDispatch function](nf-ks-kssetpowerdispatch.md) | Sets the power dispatch function to be called when the driver object receives an IRP_MJ_POWER IRP. |
| [DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_CONVERTTIMEFORMAT function](nf-ks-define-ksproperty-item-mediaseeking-converttimeformat.md) | TBD |
| [KSMETHOD_ITEM_IRP_STORAGE function](nf-ks-ksmethod-item-irp-storage.md) | TBD |
| [KsRemoveItemFromObjectBag function](nf-ks-ksremoveitemfromobjectbag.md) | The KsRemoveItemFromObjectBag function removes an item from an object bag. |
| [DEFINE_KSPROPERTY_PINSETCONSTRAINED function](nf-ks-define-ksproperty-pinsetconstrained.md) | TBD |
| [KsRegisterCountedWorker function](nf-ks-ksregistercountedworker.md) | Handles clients registering for use of a thread. |
| [DEFINE_KSPIN_DESCRIPTOR_ITEMEX function](nf-ks-define-kspin-descriptor-itemex.md) | TBD |
| [KsAcquireControl function](nf-ks-ksacquirecontrol.md) | The KsAcquireControl function acquires the filter control mutex for Object. |
| [KsGetDevice function](nf-ks-ksgetdevice.md) | The KsGetDevice function returns the AVStream device structure to which Object belongs. |
| [KsFilterGetNextSiblingFilter function](nf-ks-ksfiltergetnextsiblingfilter.md) | The KsFilterGetNextSiblingFilter function returns the next instantiated filter belonging to the parent filter factory of Filter. |
| [KsPinReleaseProcessingMutex function](nf-ks-kspinreleaseprocessingmutex.md) | The KsPinReleaseProcessingMutex function releases the processing mutex for the AVStream pin specified by Pin. |
| [DEFINE_KSPROPERTY_ITEM_STREAM_PRESENTATIONEXTENT function](nf-ks-define-ksproperty-item-stream-presentationextent.md) | TBD |
| [DEFINE_KSFASTPROPERTY_ITEM function](nf-ks-define-ksfastproperty-item.md) | TBD |
| [KsPinGetLeadingEdgeStreamPointer function](nf-ks-kspingetleadingedgestreampointer.md) | The KsPinGetLeadingEdgeStreamPointer function acquires the leading edge stream pointer for the queue associated with the given pin. |
| [_KsEdit function](nf-ks--ksedit.md) | The _KsEdit function guarantees that a given item is dynamically allocated and associated with an AVStream object through the object bag. |
| [DEFINE_KSPROPERTY_ALLOCATORSET function](nf-ks-define-ksproperty-allocatorset.md) | TBD |
| [KsPinReleaseControl function](nf-ks-kspinreleasecontrol.md) | The KsPinReleaseControl function releases the control mutex for the AVStream pin specified by Pin. |
| [KsPinGetParentFilter function](nf-ks-kspingetparentfilter.md) | The KsPinGetParentFilter function returns the parent filter of Pin. |
| [KsGateRemoveOnInputFromOr function](nf-ks-ksgateremoveoninputfromor.md) | The KsGateRemoveOnInputFromOr function removes an existing input that is in the ON state from an OR gate. |
| [DEFINE_KSPROPERTY_ITEM_QUALITY_REPORT function](nf-ks-define-ksproperty-item-quality-report.md) | TBD |
| [KsGateInitializeOr function](nf-ks-ksgateinitializeor.md) | The KsGateInitializeOr function initializes a KSGATE structure as an OR gate and attaches it to the AND gate specified by NextAndGate. |
| [KsFilterFactoryGetDevice function](nf-ks-ksfilterfactorygetdevice.md) | The KsFilterFactoryGetDevice function returns the AVStream device to which FilterFactory belongs. |
| [KsDispatchQuerySecurity function](nf-ks-ksdispatchquerysecurity.md) | The KsDispatchQuerySecurity function is used in the KSDISPATCH_TABLE.QuerySecurity entry to handle querying about the current security descriptor. |
| [DEFINE_KSPROPERTY_PINSET function](nf-ks-define-ksproperty-pinset.md) | TBD |
| [DEFINE_KSFASTMETHOD_ITEM function](nf-ks-define-ksfastmethod-item.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_QUALITY_ERROR function](nf-ks-define-ksproperty-item-quality-error.md) | TBD |
| [KsCreateClock function](nf-ks-kscreateclock.md) | The KsCreateClock function creates a handle to a clock instance. |
| [KsFilterRegisterPowerCallbacks function](nf-ks-ksfilterregisterpowercallbacks.md) | The KsFilterRegisterPowerCallbacks function registers power management callbacks for Filter. |
| [KsPublishDeviceProfile function](nf-ks-kspublishdeviceprofile.md) | TBD |
| [KsDecrementCountedWorker function](nf-ks-ksdecrementcountedworker.md) | Decrements the current worker count of a worker previous created by KsRegisterCountedWorker. This should be called after each task within a worker has been completed. |
| [DEFINE_KSPROPERTY_ITEM_CONNECTION_ACQUIREORDERING function](nf-ks-define-ksproperty-item-connection-acquireordering.md) | TBD |
| [DEFINE_KSPROPERTY_TOPOLOGYSET function](nf-ks-define-ksproperty-topologyset.md) | TBD |
| [KsFreeDefaultClock function](nf-ks-ksfreedefaultclock.md) | The KsFreeDefaultClock function frees a default clock structure previously allocated with KsAllocateDefaultClock, taking into account any currently running timer DPCs. |
| [KsGetImageNameAndResourceId function](nf-ks-ksgetimagenameandresourceid.md) | The KsGetImageNameAndResourceId function returns the image name and resource identifier that corresponds to the RegKey handle. |
| [KsStreamPointerDelete function](nf-ks-ksstreampointerdelete.md) | The KsStreamPointerDelete function deletes a clone stream pointer, releasing a reference on the frame to which this stream pointer referred. |
| [KsDeleteFilterFactory function](nf-ks-ksdeletefilterfactory.md) | KsDeleteFilterFactory deletes a given filter factory. |
| [KsPinAttachOrGate function](nf-ks-kspinattachorgate.md) | The KsPinAttachOrGate function connects Pin as an input to a previously initialized OR gate, and connects OrGate as an input to the relevant filter's AND gate. |
| [KsFilterFactoryGetParentDevice function](nf-ks-ksfilterfactorygetparentdevice.md) | The KsFilterFactoryGetParentDevice function returns the parent device of the given filter factory. |
| [DEFINE_KSEVENT_SET function](nf-ks-define-ksevent-set.md) | TBD |
| [KSPROPERTY_ITEM_IRP_STORAGE function](nf-ks-ksproperty-item-irp-storage.md) | TBD |
| [KsFilterFactoryGetOuterUnknown function](nf-ks-ksfilterfactorygetouterunknown.md) | The KsFilterFactoryGetOuterUnknown function returns the outer IUnknown of the specified filter factory. |
| [DEFINE_KSPROPERTY_ITEM_GENERAL_COMPONENTID function](nf-ks-define-ksproperty-item-general-componentid.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_STREAM_ALLOCATOR function](nf-ks-define-ksproperty-item-stream-allocator.md) | TBD |
| [KsSetDevicePnpAndBaseObject function](nf-ks-kssetdevicepnpandbaseobject.md) | The KsSetDevicePnpAndBaseObject function sets the PnP device object in the device header, which is the next device object on the PnP stack and is the device object that PnP requests are forwarded to if KsDefaultDispatchPnp is used. |
| [KsPersistDeviceProfile function](nf-ks-kspersistdeviceprofile.md) | TBD |
| [KsEnableEventWithAllocator function](nf-ks-ksenableeventwithallocator.md) | The KsEnableEventWithAllocator function enables events requested through IOCTL_KS_ENABLE_EVENT but also allows an optional allocator callback to be used to provide a buffer for the parameters. |
| [KsFreeDeviceHeader function](nf-ks-ksfreedeviceheader.md) | The KsFreeDeviceHeader function cleans up and frees a previously allocated device header. |
| [KsDispatchFastReadFailure function](nf-ks-ksdispatchfastreadfailure.md) | The KsDispatchFastReadFailure function is used in a KSDISPATCH_TABLE.FastRead entry when fast I/O read is not handled. The function should always return FALSE. |
| [KsPinGenerateEvents function](nf-ks-kspingenerateevents.md) | The KsPinGenerateEvents function generates events of an indicated type that are present in Pin's event list. |
| [KsQueryInformationFile function](nf-ks-ksqueryinformationfile.md) | The KsQueryInformationFile function performs an information query against the specified file object. The function attempts to use FastIoDispatch if possible, or it generates an information request against the device object. |
| [DEFINE_KSMETHOD_ITEM_STREAMALLOCATOR_FREE function](nf-ks-define-ksmethod-item-streamallocator-free.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_CLOCK_RESOLUTION function](nf-ks-define-ksproperty-item-clock-resolution.md) | TBD |
| [KsDispatchSpecificProperty function](nf-ks-ksdispatchspecificproperty.md) | The KsDispatchSpecificProperty function dispatches the property to a specific handler. |
| [KsGenerateEvent function](nf-ks-ksgenerateevent.md) | The KsGenerateEvent function generates a standard event notification given an event entry structure. |
| [DEFINE_KSFILTER_NODE_DESCRIPTORS function](nf-ks-define-ksfilter-node-descriptors.md) | TBD |
| [KsTerminateDevice function](nf-ks-ksterminatedevice.md) | The KsTerminateDevice function removes an AVStream device. |
| [KsValidateAllocatorCreateRequest function](nf-ks-ksvalidateallocatorcreaterequest.md) | The KsValidateAllocatorCreateRequest function validates an IRP_MJ_CREATE request as an allocator request and returns the create structure associated with the request on success. |
| [KsDiscard function](nf-ks-ksdiscard.md) | The KsDiscard macro removes a given item from an object bag. |
| [KsRemoveSpecificIrpFromCancelableQueue function](nf-ks-ksremovespecificirpfromcancelablequeue.md) | The KsRemoveSpecificIrpFromCancelableQueue function removes the specified IRP from the specified queue. This is performed on an IRP that was previously acquired using KsRemoveIrpFromCancelableQueue, but that was not actually removed from the queue. |
| [DEFINE_KSPROPERTY_ITEM_PIN_PHYSICALCONNECTION function](nf-ks-define-ksproperty-item-pin-physicalconnection.md) | TBD |
| [KsRemoveIrpFromCancelableQueue function](nf-ks-ksremoveirpfromcancelablequeue.md) | The KsRemoveIrpFromCancelableQueue function pops the next noncanceled IRP from the specified queue that can be canceled and removes its cancel status. |
| [DEFINE_KSFILTER_CONNECTIONS function](nf-ks-define-ksfilter-connections.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_TOPOLOGY_NODES function](nf-ks-define-ksproperty-item-topology-nodes.md) | TBD |
| [KsFilterFactoryGetFirstChildFilter function](nf-ks-ksfilterfactorygetfirstchildfilter.md) | The KsFilterFactoryGetFirstChildFilter function returns the first instantiated filter created by FilterFactory. |
| [KsStreamPointerAdvanceOffsets function](nf-ks-ksstreampointeradvanceoffsets.md) | The KsStreamPointerAdvanceOffsets function advances the offsets of StreamPointer. |
| [KsPinSetPinClockTime function](nf-ks-kspinsetpinclocktime.md) | The KsPinSetPinClockTime function sets the current time on the clock exposed by Pin. |
| [KSCREATE_ITEM_IRP_STORAGE function](nf-ks-kscreate-item-irp-storage.md) | TBD |
| [KsGetFilterFromIrp function](nf-ks-ksgetfilterfromirp.md) | The KsGetFilterFromIrp function returns the AVStream filter object associated with a given IRP. |
| [IKsControl::KsMethod method](nf-ks-ikscontrol-ksmethod.md) | The IKsControl |
| [KsPinRegisterIrpCompletionCallback function](nf-ks-kspinregisterirpcompletioncallback.md) | The KsPinRegisterIrpCompletionCallback function registers a minidriver-defined callback routine for a specified pin. |
| [STATICGUIDOF function](nf-ks-staticguidof.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_TIMEFORMAT function](nf-ks-define-ksproperty-item-mediaseeking-timeformat.md) | TBD |
| [KsPinGetConnectedFilterInterface function](nf-ks-kspingetconnectedfilterinterface.md) | The KsPinGetConnectedFilterInterface function queries the filter to which Pin is connected in order to obtain a pointer to a COM interface. |
| [DEFINE_KSFILTER_CATEGORY function](nf-ks-define-ksfilter-category.md) | TBD |
| [KsPinGetConnectedPinDeviceObject function](nf-ks-kspingetconnectedpindeviceobject.md) | The KsPinGetConnectedPinDeviceObject function returns the device object at the top of the device stack corresponding to the sink pin attached to the source pin Pin. |
| [DEFINE_KSPROPERTY_ITEM_CONNECTION_STARTAT function](nf-ks-define-ksproperty-item-connection-startat.md) | TBD |
| [DEFINE_KSPROPERTY_ITEM_STREAM_PRESENTATIONTIME function](nf-ks-define-ksproperty-item-stream-presentationtime.md) | TBD |
| [KsCreateDefaultAllocatorEx function](nf-ks-kscreatedefaultallocatorex.md) | Creates a default allocator that uses the specified memory pool and associates the IoGetCurrentIrpStackLocation(pIrp)-&gt;FileObject with this allocator using an internal dispatch table (KSDISPATCH_TABLE). |
| [KSMETHOD_TYPE_IRP_STORAGE function](nf-ks-ksmethod-type-irp-storage.md) | TBD |
| [KsCreateClock function](nf-ks-kscreateclock~r1.md) | The KsCreateClock function creates a handle to a clock instance. |
| [DEFINE_KSPIN_MEDIUM_TABLE function](nf-ks-define-kspin-medium-table.md) | TBD |
| [KsAddObjectCreateItemToObjectHeader function](nf-ks-ksaddobjectcreateitemtoobjectheader.md) | The KsAddObjectCreateItemToObjectHeader function adds the specified create-item to an empty item in the previously allocated create item list for this object header. |
| [DEFINE_KSPROPERTY_ITEM_MEDIASEEKING_AVAILABLE function](nf-ks-define-ksproperty-item-mediaseeking-available.md) | TBD |
| [IKsReferenceClock::GetTime method](nf-ks-iksreferenceclock-gettime.md) | The IKsReferenceClock |
| [KsGateRemoveOnInputFromAnd function](nf-ks-ksgateremoveoninputfromand.md) | The KsGateRemoveOnInputFromAnd function removes an existing input that is in the ON state from an AND gate. |
| [KsMethodHandler function](nf-ks-ksmethodhandler.md) | The KsMethodHandler function handles methods requested through IOCTL_KS_METHOD. It works with all method identifiers defined by the sets. The function can only be called at PASSIVE_LEVEL. |
| [KsSetMajorFunctionHandler function](nf-ks-kssetmajorfunctionhandler.md) | The KsSetMajorFunctionHandler function sets the handler for a specified major function to use the internal dispatching. |
| [KsReleaseCachedMdl function](nf-ks-ksreleasecachedmdl.md) | The KsReleaseCachedMdl function is used to release the MDL acquired by the KsAcquireCachedMdl call. |
| [KsPinRegisterHandshakeCallback function](nf-ks-kspinregisterhandshakecallback.md) | The KsPinRegisterHandshakeCallback function registers a minidriver-provided callback routine for a given pin. |
| [KsFilterGetOuterUnknown function](nf-ks-ksfiltergetouterunknown.md) | The KsFilterGetOuterUnknown function returns the outer IUnknown interface of the filter specified by Filter. |
| [KsCreateTopologyNode function](nf-ks-kscreatetopologynode~r1.md) | The KsCreateTopologyNode function creates a handle to a topology node instance. The function can only be called at PASSIVE_LEVEL. |
| [KsPinRegisterAggregatedClientUnknown function](nf-ks-kspinregisteraggregatedclientunknown.md) | This inline function is a wrapper for KsRegisterAggregatedClientUnknown. |
| [SetKsFramingRange function](nf-ks-setksframingrange.md) | TBD |
| [DEFINE_KSMETHOD_SET_TABLE function](nf-ks-define-ksmethod-set-table.md) | TBD |
| [KsGetPinFromIrp function](nf-ks-ksgetpinfromirp.md) | The KsGetPinFromIrp function returns the AVStream pin object associated with the given IRP. |
| [KsAddIrpToCancelableQueue function](nf-ks-ksaddirptocancelablequeue.md) | The KsAddIrpToCancelableQueue function adds an IRP to a queue of cancelable IRPs, thus allowing the IRP to be canceled. If the IRP had been previously set to a canceled state, the KsAddIrpToCancelableQueue function completes the canceling of that IRP. |
| [KsGateAddOffInputToOr function](nf-ks-ksgateaddoffinputtoor.md) | The KsGateAddOffInputToOr function adds a new input in the OFF state to a given OR gate. |
| [DEFINE_KSMETHOD_ITEM_STREAMALLOCATOR_ALLOC function](nf-ks-define-ksmethod-item-streamallocator-alloc.md) | TBD |
| [KsDiscardEvent function](nf-ks-ksdiscardevent.md) | The KsDiscardEvent function discards the memory used by an event entry after the objects have been dereferenced. |
| [KsFilterGetChildPinCount function](nf-ks-ksfiltergetchildpincount.md) | The KsFilterGetChildPinCountfunctionreturns the number of pins of a given type that are currently instantiated on a given filter. |
| [KsGetFirstChild function](nf-ks-ksgetfirstchild.md) | The KsGetFirstChild function returns the first AVStream child object of Object. |
| [IKsReferenceClock::GetResolution method](nf-ks-iksreferenceclock-getresolution.md) | The IKsReferenceClock |
| [KsPinAttachAndGate function](nf-ks-kspinattachandgate.md) | The KsPinAttachAndGate function connects Pin as an input to a previously initialized AND gate, and connects AndGate as an input to the relevant filter's AND gate. |
| [KsDisableEvent function](nf-ks-ksdisableevent.md) | The KsDisableEvent function disables events requested through IOCTL_KS_DISABLE_EVENT. |
| [KsProbeStreamIrp function](nf-ks-ksprobestreamirp.md) | The KsProbeStreamIrp function makes the specified modifications to the input and output buffers of the given IRP based on the flags passed, and it then validates the stream header. |
| [KsFilterReleaseProcessingMutex function](nf-ks-ksfilterreleaseprocessingmutex.md) | The KsFilterReleaseProcessingMutex function releases the processing mutex for the AVStream filter specified by Filter. |
| [KsRegisterAggregatedClientUnknown function](nf-ks-ksregisteraggregatedclientunknown.md) | In a manner very similar to COM, the KsRegisterAggregatedClientUnknown function aggregates two objects |
| [KSQUEUE_SPINLOCK_IRP_STORAGE function](nf-ks-ksqueue-spinlock-irp-storage.md) | TBD |
| [KsPinGetDevice function](nf-ks-kspingetdevice.md) | The KsPinGetDevice function returns the AVStream device to which Pin belongs. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [KSPROPERTY_PIN enumeration](ne-ks-ksproperty-pin.md) | TBD. |
| [KSLIST_ENTRY_LOCATION enumeration](ne-ks-kslist-entry-location.md) | TBD. |
| [KSPROPERTY_QUALITY enumeration](ne-ks-ksproperty-quality.md) | TBD. |
| [KSPROPERTY_GENERAL enumeration](ne-ks-ksproperty-general.md) | TBD. |
| [KSSTACK_USE enumeration](ne-ks-ksstack-use.md) | TBD. |
| [PKSPIN_DATAFLOW enumeration](ne-ks-pkspin-dataflow.md) | An instance of the KSPIN_DATAFLOW enumeration is returned by KSPROPERTY_PIN_DATAFLOW. |
| [KSEVENT_DEVICE enumeration](ne-ks-ksevent-device.md) | Specifies event notifications that the driver generates to indicate that a device has been lost or preempted. |
| [KSDEGRADE_STANDARD enumeration](ne-ks-ksdegrade-standard.md) | The KSDEGRADE_STANDARD enumeration lists different types of degradation. |
| [KSEVENT_PINCAPS_CHANGENOTIFICATIONS enumeration](ne-ks-ksevent-pincaps-changenotifications.md) | TBD. |
| [VARENUM enumeration](ne-ks-varenum.md) | TBD. |
| [KSPROPERTY_STREAMALLOCATOR enumeration](ne-ks-ksproperty-streamallocator.md) | TBD. |
| [KSMETHOD_STREAMALLOCATOR enumeration](ne-ks-ksmethod-streamallocator.md) | TBD. |
| [KSEVENT_VOLUMELIMIT enumeration](ne-ks-ksevent-volumelimit.md) | TBD. |
| [KSEVENT_STREAMALLOCATOR enumeration](ne-ks-ksevent-streamallocator.md) | TBD. |
| [KSDEVICE_THERMAL_STATE enumeration](ne-ks-ksdevice-thermal-state.md) | A KS-defined enumeration for thermal state changes. |
| [KSPIN_MDL_CACHING_EVENT enumeration](ne-ks-kspin-mdl-caching-event.md) | This enumeration is used internally by the operating system. |
| [KSRESET enumeration](ne-ks-ksreset.md) | TBD. |
| [KSPROPERTY_STREAM enumeration](ne-ks-ksproperty-stream.md) | TBD. |
| [KSIRP_REMOVAL_OPERATION enumeration](ne-ks-ksirp-removal-operation.md) | TBD. |
| [KSINTERFACE_STANDARD enumeration](ne-ks-ksinterface-standard.md) | TBD. |
| [KSMETHOD_STREAMIO enumeration](ne-ks-ksmethod-streamio.md) | TBD. |
| [KSOBJECTTYPE enumeration](ne-ks-ksobjecttype.md) | The KSOBJECTTYPE enumeration lists different types of kernel streaming objects. |
| [KSSTREAM_POINTER_STATE enumeration](ne-ks-ksstream-pointer-state.md) | TBD. |
| [KSEVENTS_LOCKTYPE enumeration](ne-ks-ksevents-locktype.md) | The KSEVENTS_LOCKTYPE enumeration identifies the type of exclusion lock. The types are used with EventFlags in several event-set helper functions. |
| [KSEVENT_CLOCK_POSITION enumeration](ne-ks-ksevent-clock-position.md) | TBD. |
| [PKSSTATE enumeration](ne-ks-pksstate.md) | The KSSTATE enumeration lists possible states of a kernel streaming object. |
| [unnamed_enum_0cc4_74 enumeration](ne-ks---unnamed-enum-0cc4-74.md) | TBD |
| [PKSPIN_COMMUNICATION enumeration](ne-ks-pkspin-communication.md) | TBD. |
| [KSEVENT_CONNECTION enumeration](ne-ks-ksevent-connection.md) | TBD. |
| [KS_SEEKING_CAPABILITIES enumeration](ne-ks-ks-seeking-capabilities.md) | TBD. |
| [KSPROPERTY_CLOCK enumeration](ne-ks-ksproperty-clock.md) | TBD. |
| [KSPPROPERTY_ALLOCATOR_MDLCACHING enumeration](ne-ks-kspproperty-allocator-mdlcaching.md) | This enumeration is used internally by the operating system. |
| [KSPROPERTY_STREAMINTERFACE enumeration](ne-ks-ksproperty-streaminterface.md) | TBD. |
| [KSPROPERTY_GM enumeration](ne-ks-ksproperty-gm.md) | TBD. |
| [KSINTERFACE_FILEIO enumeration](ne-ks-ksinterface-fileio.md) | TBD. |
| [KSPROPERTY_TOPOLOGY enumeration](ne-ks-ksproperty-topology.md) | TBD. |
| [KSCOMPLETION_INVOCATION enumeration](ne-ks-kscompletion-invocation.md) | TBD. |
| [KSTARGET_STATE enumeration](ne-ks-kstarget-state.md) | TBD. |
| [KS_SEEKING_FLAGS enumeration](ne-ks-ks-seeking-flags.md) | The KS_SEEKING_FLAGS enumeration lists positioning options that can be used in conjunction with the KSPROPERTY_POSITIONS structure. |
| [KSPROPERTY_MEDIASEEKING enumeration](ne-ks-ksproperty-mediaseeking.md) | TBD. |
| [KSPROPERTY_CONNECTION enumeration](ne-ks-ksproperty-connection.md) | TBD. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFNKSCANCELTIMER callback function](nc-ks-pfnkscanceltimer.md) | TBD |
| [PFNKSDEVICETHERMALACTIVECOOLING callback function](nc-ks-pfnksdevicethermalactivecooling.md) | TBD |
| [PFNKSFASTHANDLER callback function](nc-ks-pfnksfasthandler.md) | TBD |
| [PFNKSPINVOID callback function](nc-ks-pfnkspinvoid.md) | TBD |
| [PFNKSSTREAMPOINTER callback function](nc-ks-pfnksstreampointer.md) | TBD |
| [PFNKSDEVICETHERMALPASSIVECOOLING callback function](nc-ks-pfnksdevicethermalpassivecooling.md) | TBD |
| [PFNKSDEVICEIRPVOID callback function](nc-ks-pfnksdeviceirpvoid.md) | TBD |
| [PFNKSPINFRAMERETURN callback function](nc-ks-pfnkspinframereturn.md) | TBD |
| [PFNKSHANDLER callback function](nc-ks-pfnkshandler.md) | TBD |
| [PFNKSPINCORRELATEDTIME callback function](nc-ks-pfnkspincorrelatedtime.md) | TBD |
| [PFNKSITEMFREECALLBACK callback function](nc-ks-pfnksitemfreecallback.md) | TBD |
| [PFNKSINTERSECTHANDLER callback function](nc-ks-pfnksintersecthandler.md) | TBD |
| [PFNKSPIN callback function](nc-ks-pfnkspin.md) | TBD |
| [PFNKSCONTEXT_DISPATCH callback function](nc-ks-pfnkscontext-dispatch.md) | TBD |
| [PFNKSFILTERFACTORYVOID callback function](nc-ks-pfnksfilterfactoryvoid.md) | TBD |
| [PFNKSPININITIALIZEALLOCATOR callback function](nc-ks-pfnkspininitializeallocator.md) | TBD |
| [PFNKSDEVICEQUERYPOWER callback function](nc-ks-pfnksdevicequerypower.md) | TBD |
| [PFNKSFILTERIRP callback function](nc-ks-pfnksfilterirp.md) | TBD |
| [PFNKSDEFAULTFREE callback function](nc-ks-pfnksdefaultfree.md) | TBD |
| [PFNKSPINSETDEVICESTATE callback function](nc-ks-pfnkspinsetdevicestate.md) | TBD |
| [PFNQUERYREFERENCESTRING callback function](nc-ks-pfnqueryreferencestring.md) | TBD |
| [PFNKSADDEVENT callback function](nc-ks-pfnksaddevent.md) | TBD |
| [PFNKSPINHANDSHAKE callback function](nc-ks-pfnkspinhandshake.md) | TBD |
| [PFNKSDEVICEIRP callback function](nc-ks-pfnksdeviceirp.md) | TBD |
| [PFNKSFILTERPROCESS callback function](nc-ks-pfnksfilterprocess.md) | TBD |
| [PFNQUERYMEDIUMSLIST callback function](nc-ks-pfnquerymediumslist.md) | TBD |
| [PFNKSPINSETDATAFORMAT callback function](nc-ks-pfnkspinsetdataformat.md) | TBD |
| [PFNKSDEVICEQUERYCAPABILITIES callback function](nc-ks-pfnksdevicequerycapabilities.md) | TBD |
| [PFNKSFILTERPOWER callback function](nc-ks-pfnksfilterpower.md) | TBD |
| [PFNALLOCATOR_FREEFRAME callback function](nc-ks-pfnallocator-freeframe.md) | TBD |
| [PFNKSGRAPHMANAGER_NOTIFY callback function](nc-ks-pfnksgraphmanager-notify.md) | TBD |
| [PFNKSSETTIMER callback function](nc-ks-pfnkssettimer.md) | TBD |
| [PFNKSINTERSECTHANDLEREX callback function](nc-ks-pfnksintersecthandlerex.md) | TBD |
| [PFNKSPINSETTIMER callback function](nc-ks-pfnkspinsettimer.md) | TBD |
| [PFNKSDEVICESETPOWER callback function](nc-ks-pfnksdevicesetpower.md) | TBD |
| [PFNKSDEVICE callback function](nc-ks-pfnksdevice.md) | TBD |
| [PFNKSFREE callback function](nc-ks-pfnksfree.md) | TBD |
| [PFNKSIRPLISTCALLBACK callback function](nc-ks-pfnksirplistcallback.md) | TBD |
| [PFNKSDEFAULTALLOCATE callback function](nc-ks-pfnksdefaultallocate.md) | TBD |
| [PFNKSPINIRP callback function](nc-ks-pfnkspinirp.md) | TBD |
| [PFNKSREMOVEEVENT callback function](nc-ks-pfnksremoveevent.md) | TBD |
| [PFNALLOCATOR_ALLOCATEFRAME callback function](nc-ks-pfnallocator-allocateframe.md) | TBD |
| [PFNKSINITIALIZEALLOCATOR callback function](nc-ks-pfnksinitializeallocator.md) | TBD |
| [PFNKSFILTERFACTORYPOWER callback function](nc-ks-pfnksfilterfactorypower.md) | TBD |
| [PFNKSPINIRPCOMPLETION callback function](nc-ks-pfnkspinirpcompletion.md) | TBD |
| [PFNKSCLOCK_CORRELATEDTIME callback function](nc-ks-pfnksclock-correlatedtime.md) | TBD |
| [PFNKSGENERATEEVENTCALLBACK callback function](nc-ks-pfnksgenerateeventcallback.md) | TBD |
| [PFNKSCLOCK_GETTIME callback function](nc-ks-pfnksclock-gettime.md) | TBD |
| [PFNREFERENCEDEVICEOBJECT callback function](nc-ks-pfnreferencedeviceobject.md) | TBD |
| [PFNKSFILTERVOID callback function](nc-ks-pfnksfiltervoid.md) | TBD |
| [PFNDEREFERENCEDEVICEOBJECT callback function](nc-ks-pfndereferencedeviceobject.md) | TBD |
| [PFNKSALLOCATOR callback function](nc-ks-pfnksallocator.md) | TBD |
| [PFNKSDEVICECREATE callback function](nc-ks-pfnksdevicecreate.md) | TBD |
| [PFNKSPINCANCELTIMER callback function](nc-ks-pfnkspincanceltimer.md) | TBD |
| [PFNKSDEVICEPNPSTART callback function](nc-ks-pfnksdevicepnpstart.md) | TBD |
| [PFNKSCANCELPINNEDMDL callback function](nc-ks-pfnkscancelpinnedmdl.md) | TBD |
| [PFNKSPINPOWER callback function](nc-ks-pfnkspinpower.md) | TBD |
| [PFNKSDELETEALLOCATOR callback function](nc-ks-pfnksdeleteallocator.md) | TBD |
| [PFNKSCORRELATEDTIME callback function](nc-ks-pfnkscorrelatedtime.md) | TBD |
| [PFNKSPINRESOLUTION callback function](nc-ks-pfnkspinresolution.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [KSGRAPHMANAGER_FUNCTIONTABLE structure](ns-ks-ksgraphmanager-functiontable.md) | TBD. |
| [PKSPROPERTY_ITEM structure](ns-ks-pksproperty-item.md) | Drivers use the KSPROPERTY_ITEM structure to describe how they support a property in a property set. |
| [PKS_FRAMING_RANGE_WEIGHTED structure](ns-ks-pks-framing-range-weighted.md) | Drivers can use the KS_FRAMING_RANGE_WEIGHTED structure to specify a range of weighted frame sizes. |
| [PKSPROPERTY_MEDIAAVAILABLE structure](ns-ks-pksproperty-mediaavailable.md) | The KSPROPERTY_MEDIAAVAILABLE structure specifies the media time span (the time span that a client can seek within) that is currently available on a filter. |
| [KSRELATIVEEVENT structure](ns-ks-ksrelativeevent.md) | TBD |
| [PKSOBJECT_CREATE structure](ns-ks-pksobject-create.md) | The KSOBJECT_CREATE structure contains an array of create handlers for base object classes supported by this device object. |
| [KSAUTOMATION_TABLE_ structure](ns-ks-ksautomation-table-~r1.md) | TBD |
| [KSDEVICE_DISPATCH structure](ns-ks--ksdevice-dispatch.md) | TBD |
| [KSGATE structure](ns-ks--ksgate~r1.md) | TBD |
| [PKSPIN_PHYSICALCONNECTION structure](ns-ks-pkspin-physicalconnection.md) | A structure of type KSPIN_PHYSICALCONNECTION is returned in response to a KSPROPERTY_PIN_PHYSICALCONNECTION request. |
| [PKS_FRAMING_ITEM structure](ns-ks-pks-framing-item.md) | The KS_FRAMING_ITEM structure is used to declare allocator requirements on a kernel-mode pin. |
| [PKSPROPERTY_POSITIONS structure](ns-ks-pksproperty-positions.md) | The KSPROPERTY_POSITIONS structure specifies the current position and stop position, relative to the total duration of the stream. |
| [KSSTREAM_POINTER structure](ns-ks--ksstream-pointer~r1.md) | TBD |
| [KSFILTER structure](ns-ks--ksfilter.md) | TBD |
| [KSNODE_DESCRIPTOR structure](ns-ks--ksnode-descriptor~r1.md) | TBD |
| [PKSDPC_ITEM structure](ns-ks-pksdpc-item.md) | The KSDPC_ITEM structure is used to store information related to any internal DPCs that might be used to generate event notification from a raised IRQL. |
| [PKSIDENTIFIER structure](ns-ks-pksidentifier.md) | The KSIDENTIFIER structure specifies a GUID that uniquely identifies a related set of GUIDs, and an index value to refer to a specific member within that set. |
| [PKSQUERYBUFFER structure](ns-ks-pksquerybuffer.md) | The KSQUERYBUFFER structure is used when querying for outstanding buffers available on an event with KSEVENT_TYPE_QUERYBUFFER. |
| [PKSP_PIN structure](ns-ks-pksp-pin.md) | Kernel streaming clients use the KSP_PIN structure to specify the property and pin type within a KSPROPSETID_Pin property request. |
| [PKSTOPOLOGY_CONNECTION structure](ns-ks-pkstopology-connection.md) | The KSTOPOLOGY_CONNECTION structure describes a single data-path connection inside a kernel streaming filter. |
| [KSPROCESSPIN_INDEXENTRY structure](ns-ks--ksprocesspin-indexentry~r1.md) | TBD |
| [KSDEVICE_PROFILE_INFO structure](ns-ks--ksdevice-profile-info.md) | TBD |
| [PKSPROPERTY_SERIAL structure](ns-ks-pksproperty-serial.md) | The KSPROPERTY_SERIAL structure is a header that is included for each property that follows a KSPROPERTY_SERIALHDR structure. |
| [KSSTREAM_POINTER_OFFSET structure](ns-ks--ksstream-pointer-offset.md) | TBD |
| [PKSMETHOD_SET structure](ns-ks-pksmethod-set.md) | The KSMETHOD_SET structure describes the methods that comprise a kernel streaming method set. |
| [KSPROCESSPIN_INDEXENTRY structure](ns-ks--ksprocesspin-indexentry.md) | TBD |
| [KSSTREAM_POINTER structure](ns-ks--ksstream-pointer.md) | TBD |
| [PKSNODE_CREATE structure](ns-ks-pksnode-create.md) | The KSNODE_CREATE structure describes the set of information used to create the node handle. |
| [PKSPIN_MDL_CACHING_NOTIFICATION32 structure](ns-ks-pkspin-mdl-caching-notification32.md) | This structure is used internally by the operating system. |
| [KSDEVICE_DESCRIPTOR structure](ns-ks--ksdevice-descriptor.md) | TBD |
| [PKSHANDSHAKE structure](ns-ks-pkshandshake.md) | The KSHANDSHAKE structure is used to pass information back and forth while pins are handshaking in an attempt to negotiate a private interface. |
| [PKSSTREAMALLOCATOR_STATUS_EX structure](ns-ks-pksstreamallocator-status-ex.md) | Client use KSSTREAMALLOCATOR_STATUS_EX to query the status for allocators supporting the extended allocator framing. |
| [PKSFASTPROPERTY_ITEM structure](ns-ks-pksfastproperty-item.md) | The KSFASTPROPERTY_ITEM structure is used with items for fast I/O dispatching. |
| [IKsControl structure](ns-ks-ikscontrol.md) | TBD |
| [IKsFastClock structure](ns-ks-iksfastclock.md) | TBD |
| [PKSPROPERTY_VALUES structure](ns-ks-pksproperty-values.md) | The KSPROPERTY_VALUES structure describes the type and acceptable default values of a property. |
| [KSFILTER_DESCRIPTOR structure](ns-ks--ksfilter-descriptor.md) | TBD |
| [KSPIN_DISPATCH structure](ns-ks--kspin-dispatch.md) | TBD |
| [PKSPROPERTY_BOUNDS_LONGLONG structure](ns-ks-pksproperty-bounds-longlong.md) | The KSPROPERTY_BOUNDS_LONGLONG structure defines the bounds for a 64-bit property. |
| [KSDEVICE_DISPATCH structure](ns-ks--ksdevice-dispatch~r1.md) | TBD |
| [PKSPROPERTY_STEPPING_LONGLONG structure](ns-ks-pksproperty-stepping-longlong.md) | The KSPROPERTY_STEPPING_LONGLONG structure defines the valid range of values for a 64-bit property. |
| [KSFILTER_DISPATCH structure](ns-ks--ksfilter-dispatch~r1.md) | TBD |
| [KSFILTER_DESCRIPTOR structure](ns-ks--ksfilter-descriptor~r1.md) | TBD |
| [PKSPIN_MDL_CACHING_NOTIFICATION structure](ns-ks-pkspin-mdl-caching-notification.md) | This structure is used internally by the operating system. |
| [PKSCLOCK_CREATE structure](ns-ks-pksclock-create.md) | The KSCLOCK_CREATE structure is used in clock create parameters for the KsCreateClock function. |
| [PKSE_NODE structure](ns-ks-pkse-node.md) | The KSE_NODE structure specifies an event request on a specific node. |
| [PKSINTERVAL structure](ns-ks-pksinterval.md) | The KSINTERVAL structure specifies a base time and time interval for recurring events. |
| [PKS_COMPRESSION structure](ns-ks-pks-compression.md) | The KS_COMPRESSION structure defines the compression of frames on an output pin. |
| [PKSPROPERTY_SET structure](ns-ks-pksproperty-set.md) | A kernel streaming driver or pin may use the KSPROPERTY_SET structure to describe how it supports a property set. |
| [MF_MDL_SHARED_PAYLOAD_KEY structure](ns-ks--mf-mdl-shared-payload-key.md) | This union is used internally by the operating system. |
| [KSFILTERFACTORY structure](ns-ks--ksfilterfactory.md) | TBD |
| [PKSPIN_CONNECT structure](ns-ks-pkspin-connect.md) | Clients use the KSPIN_CONNECT structure to describe the connection they request from a driver in a KsCreatePin call. |
| [KSDEVICE structure](ns-ks--ksdevice.md) | TBD |
| [PKSPIN_DESCRIPTOR structure](ns-ks-pkspin-descriptor.md) | The KSPIN_DESCRIPTOR structure describes the basic KSPROPSETID_Pin properties of a pin type. |
| [PKSPROPERTY_MEMBERSLIST structure](ns-ks-pksproperty-memberslist.md) | The KSPROPERTY_MEMBERSLIST structure contains a list of legal values or ranges for a property. |
| [KSPROCESSPIN structure](ns-ks--ksprocesspin~r1.md) | TBD |
| [PKSRESOLUTION structure](ns-ks-pksresolution.md) | The KSRESOLUTION structure specifies granularity and error of a kernel streaming clock. |
| [PKSALLOCATOR_FRAMING_EX structure](ns-ks-pksallocator-framing-ex.md) | The KSALLOCATOR_FRAMING_EX structure is the AVStream replacement for KSALLOCATOR_FRAMING. KSALLOCATOR_FRAMING_EX defines allocator requirements on a pin in a kernel level filter. |
| [PKSQUALITY structure](ns-ks-pksquality.md) | The KSQUALITY structure is used to report QM problems in both kernel and user mode to their respective quality managers. |
| [PKSE_PIN structure](ns-ks-pkse-pin.md) | TBD. |
| [PKSPROPERTY_BOUNDS_LONG structure](ns-ks-pksproperty-bounds-long.md) | The KSPROPERTY_BOUNDS_LONG structure defines the bounds for a 32-bit property. |
| [PKSEVENT_ITEM structure](ns-ks-pksevent-item.md) | The KSEVENT_ITEM structure describe a minidriver's support for a specific event within an event set. |
| [PKSPROPERTY_MEMBERSHEADER structure](ns-ks-pksproperty-membersheader.md) | A driver provides a structure of type KSPROPERTY_MEMBERSHEADER to describe the size and type of each element in an array containing property values or ranges. |
| [KSAUTOMATION_TABLE_ structure](ns-ks-ksautomation-table-.md) | TBD |
| [PKSDISPATCH_TABLE structure](ns-ks-pksdispatch-table.md) | The KSDISPATCH_TABLE structure contains pointers to minidriver implemented IRP dispatch routines. |
| [PKSM_NODE structure](ns-ks-pksm-node.md) | Just as KSP_NODE is used for properties on a node, the KSM_NODE structure is used for methods on a node. |
| [KSPIN_DESCRIPTOR_EX structure](ns-ks--kspin-descriptor-ex.md) | TBD |
| [PKSCOMPONENTID structure](ns-ks-pkscomponentid.md) | The KSCOMPONENTID structure contains unique identifiers that describe an individual kernel streaming object. |
| [KSFILTER_DISPATCH structure](ns-ks--ksfilter-dispatch.md) | TBD |
| [KSMAPPING structure](ns-ks--ksmapping~r1.md) | TBD |
| [PKSP_NODE structure](ns-ks-pksp-node.md) | Kernel streaming clients use the KSP_NODE structure to specify the property and node type within a KSPROPERTY_TOPOLOGY_NAME property request. |
| [PKSBUFFER_ITEM structure](ns-ks-pksbuffer-item.md) | The KSBUFFER_ITEM structure is used to store a list of data buffers copied from the event source, which can be retrieved by the event sink through KSEVENT_TYPE_QUERYBUFFER. |
| [IKsDeviceFunctions structure](ns-ks-iksdevicefunctions.md) | TBD |
| [KSPROCESSPIN structure](ns-ks--ksprocesspin.md) | TBD |
| [PBUS_INTERFACE_REFERENCE structure](ns-ks-pbus-interface-reference.md) | A software device enumerator exports this interface to allow drivers to reference count physical device objects (PDOs) such that the device remains active while in use and is unloaded when not in use. |
| [PKSCLOCK_FUNCTIONTABLE structure](ns-ks-pksclock-functiontable.md) | The KSCLOCK_FUNCTIONTABLE structure describes a function table for the master clock. |
| [PKSFASTMETHOD_ITEM structure](ns-ks-pksfastmethod-item.md) | Drivers provide a structure of type KSFASTMETHOD_ITEM to support fast I/O dispatching. |
| [PKSDATARANGE structure](ns-ks-pksdatarange.md) | The KSDATARANGE structure is a variable-length structure that describes a range of data formats. |
| [KSPIN structure](ns-ks--kspin.md) | TBD |
| [KSNODE_DESCRIPTOR structure](ns-ks--ksnode-descriptor.md) | TBD |
| [KSPIN_DESCRIPTOR_EX structure](ns-ks--kspin-descriptor-ex~r1.md) | TBD |
| [PKSPROPERTY_DESCRIPTION structure](ns-ks-pksproperty-description.md) | The KSPROPERTY_DESCRIPTION structure specifies the size and type of values contained in a specific property. |
| [KSPROPERTY_GRAPHMANAGER_INTERFACE structure](ns-ks--ksproperty-graphmanager-interface.md) | TBD. |
| [PKSALLOCATOR_FRAMING structure](ns-ks-pksallocator-framing.md) | The KSALLOCATOR_FRAMING structure is used to query framing requirements and submit allocator creation requests. |
| [PKSDATARANGE structure](ns-ks-pksdatarange~r1.md) | The KSDATARANGE structure is a variable-length structure that describes a range of data formats. |
| [PKSPROPERTY_SERIALHDR structure](ns-ks-pksproperty-serialhdr.md) | The format of the serialization buffer is a KSPROPERTY_SERIALHDR structure, followed by serialized properties. |
| [PKSRATE structure](ns-ks-pksrate.md) | The query is passed a KSRATE structure appended to the property containing the rate request (known as a KSRATE_CAPABILITY structure), and is returned a KSRATE structure filled in with the capability given the rate request. |
| [KSDEVICE structure](ns-ks--ksdevice~r1.md) | TBD |
| [PKSRATE_CAPABILITY structure](ns-ks-pksrate-capability.md) | The client uses the KSRATE_CAPABILITY structure in a KSPROPERTY_STREAM_RATECAPABILITY property request. |
| [KSCLOCK_DISPATCH structure](ns-ks--ksclock-dispatch.md) | TBD |
| [KSEVENT_ENTRY structure](ns-ks--ksevent-entry~r1.md) | TBD |
| [PKSEVENT_TIME_INTERVAL structure](ns-ks-pksevent-time-interval.md) | The KSEVENT_TIME_INTERVAL structure is used in various events within the KSEVENTSETID_Clock event set. |
| [PKSPRIORITY structure](ns-ks-pkspriority.md) | The KSPRIORITY structure is used to specify priority and is used with the KSPROPERTY_CONNECTION_PRIORITY property. |
| [PKSSTREAM_UVC_METADATA structure](ns-ks-pksstream-uvc-metadata.md) | The KSSTREAM_UVC_METADATA structure contains start and end of frame timestamp information. |
| [KSFILTERFACTORY structure](ns-ks--ksfilterfactory~r1.md) | TBD |
| [PKSSTREAMALLOCATOR_FUNCTIONTABLE structure](ns-ks-pksstreamallocator-functiontable.md) | Clients can request the function table of a given allocator by sending a KSSTREAMALLOCATOR_FUNCTIONTABLE structure in a KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE property request. |
| [PKSEVENT_SET structure](ns-ks-pksevent-set.md) | The KSEVENT_SET structure describes the events that comprise a kernel streaming event set. |
| [PKSPROPERTY_STEPPING_LONG structure](ns-ks-pksproperty-stepping-long.md) | The KSPROPERTY_STEPPING_LONG structure defines the valid range of values for a 32-bit property. |
| [PKSSTREAM_METADATA_INFO structure](ns-ks-pksstream-metadata-info.md) | This structure contains the metadata information that is passed down to the driver. |
| [KSPIN structure](ns-ks--kspin~r1.md) | TBD |
| [PKSSTREAM_UVC_METADATATYPE_TIMESTAMP structure](ns-ks-pksstream-uvc-metadatatype-timestamp.md) | The KSSTREAM_UVC_METADATATYPE_TIMESTAMP structure contains USB video class (UVC) clock and timestamp information. |
| [PKSEVENTDATA structure](ns-ks-pkseventdata.md) | Kernel streaming clients send the KSEVENTDATA structure to the class driver to specify a notification method. |
| [PKSMULTIPLE_ITEM structure](ns-ks-pksmultiple-item.md) | The KSMULTIPLE_ITEM structure is a generic header for property data that can contain multiple entries. |
| [KSALLOCATOR_DISPATCH structure](ns-ks--ksallocator-dispatch.md) | TBD |
| [KSDEVICE_THERMAL_DISPATCH structure](ns-ks--ksdevice-thermal-dispatch.md) | The KSDEVICE_THERMAL_DISPATCH structure is used by the miniport driver in the API call to register thermal notification callbacks. This structure contains the callback function pointers for active and passive cooling interfaces. |
| [KSALLOCATOR_DISPATCH structure](ns-ks--ksallocator-dispatch~r1.md) | TBD |
| [PKSCORRELATED_TIME structure](ns-ks-pkscorrelated-time.md) | The KSCORRELATED_TIME structure contains a clock time as well as the corresponding number of clock ticks since system boot. |
| [PKSSTREAMALLOCATOR_STATUS structure](ns-ks-pksstreamallocator-status.md) | The KSSTREAMALLOCATOR_STATUS structure describes framing requirements and current number of allocated frames for a specific allocator. |
| [KSGATE structure](ns-ks--ksgate.md) | TBD |
| [PKSATTRIBUTE_LIST structure](ns-ks-pksattribute-list.md) | The KSATTRIBUTE_LIST structure contains an attribute defined in a KSATTRIBUTE structure. |
| [PKSATTRIBUTE structure](ns-ks-pksattribute.md) | The KSATTRIBUTE structure defines an additional attribute of a data format or data range that is not covered by the KSDATAFORMAT and KSDATARANGE structures or the extended information based on the format and range specifiers. |
| [PKSFRAMETIME structure](ns-ks-pksframetime.md) | The KSFRAMETIME structure is supported by rendering pins, and is used to return the duration of the next &#0034;frame&#0034; of data, and flags associated with that frame. |
| [PKSOBJECT_CREATE_ITEM structure](ns-ks-pksobject-create-item.md) | The KSOBJECT_CREATE_ITEM structure is used to look up the string passed to a create request. |
| [KSPIN_DISPATCH structure](ns-ks--kspin-dispatch~r1.md) | TBD |
| [KSSTREAM_POINTER_OFFSET structure](ns-ks--ksstream-pointer-offset~r1.md) | TBD |
| [PKSTOPOLOGY structure](ns-ks-pkstopology.md) | The KSTOPOLOGY structure describes the topology of pins and nodes. |
| [PKS_FRAMING_RANGE structure](ns-ks-pks-framing-range.md) | The KS_FRAMING_RANGE structure specifies a range for frame sizes for a given framing item. |
| [KSFILTER structure](ns-ks--ksfilter~r1.md) | TBD |
| [PKSSTREAM_HEADER structure](ns-ks-pksstream-header.md) | The KSSTREAM_HEADER structure is a variable-length structure that describes a packet of data to be read from or written to a streaming driver pin. |
| [PKSP_TIMEFORMAT structure](ns-ks-pksp-timeformat.md) | The KSP_TIMEFORMAT structure corresponds to KSPROPERTY_MEDIASEEKING_CONVERTTIMEFORMAT. |
| [PKSERROR structure](ns-ks-pkserror.md) | The KSERROR structure is used to report streaming errors in both kernel and user mode to their respective quality managers. |
| [PKSTIME structure](ns-ks-pkstime.md) | The KSTIME structure specifies a time stamp that can be used to indicate stream position. |
| [PKSEVENT_TIME_MARK structure](ns-ks-pksevent-time-mark.md) | The KSEVENT_TIME_MARK structure is used in various events within the KSEVENTSETID_Clock event set. |
| [PBUS_INTERFACE_MEDIUMS structure](ns-ks-pbus-interface-mediums.md) | TBD. |
| [KSDEVICE_DESCRIPTOR structure](ns-ks--ksdevice-descriptor~r1.md) | TBD |
| [KSMAPPING structure](ns-ks--ksmapping.md) | TBD |
| [PKSPIN_CINSTANCES structure](ns-ks-pkspin-cinstances.md) | TBD. |
| [PKSMETHOD_ITEM structure](ns-ks-pksmethod-item.md) | The KSMETHOD_ITEM structure describes a single method within a method set. |
| [PKSQUALITY_MANAGER structure](ns-ks-pksquality-manager.md) | The KSQUALITY_MANAGER structure is used with the KSPROPERTY_STREAM_QUALITY property and contains the handle of the quality manager sink and a context to pass in the quality complaints. |
| [KSCLOCK_DISPATCH structure](ns-ks--ksclock-dispatch~r1.md) | TBD |
| [KSEVENT_ENTRY structure](ns-ks--ksevent-entry.md) | TBD |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_KS_HANDSHAKE IOCTL](ni-ks-ioctl-ks-handshake.md) | TBD |
| [IOCTL_KS_PROPERTY IOCTL](ni-ks-ioctl-ks-property.md) | TBD |
| [IOCTL_KS_RESET_STATE IOCTL](ni-ks-ioctl-ks-reset-state.md) | TBD |
| [IOCTL_KS_ENABLE_EVENT IOCTL](ni-ks-ioctl-ks-enable-event.md) | TBD |
| [IOCTL_KS_METHOD IOCTL](ni-ks-ioctl-ks-method.md) | TBD |
| [IOCTL_KS_DISABLE_EVENT IOCTL](ni-ks-ioctl-ks-disable-event.md) | TBD |
| [IOCTL_KS_READ_STREAM IOCTL](ni-ks-ioctl-ks-read-stream.md) | TBD |
| [IOCTL_KS_WRITE_STREAM IOCTL](ni-ks-ioctl-ks-write-stream.md) | TBD |
Interface

| Title        | Description    |
| ------------- |:-------------:|
| [IKsDeviceFunctions interface](nn-ks-iksdevicefunctions~r1.md) | TBD |
| [IKsReferenceClock interface](nn-ks-iksreferenceclock.md) | TBD |
| [IKsControl interface](nn-ks-ikscontrol~r1.md) | The IKsControl interface is a COM-style interface implemented on AVStream filters and pins. |

This header is used in these topics:

- [stream](..content/_stream)
