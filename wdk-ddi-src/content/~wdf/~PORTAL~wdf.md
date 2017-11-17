# Declarations in the wdf technology
This technology  contains these programming interfaces:

Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_RETRIEVE_CHILD_FLAGS enumeration](..\wdfchildlist\ne-wdfchildlist--wdf-retrieve-child-flags.md) | The WDF_RETRIEVE_CHILD_FLAGS enumeration defines flags that a driver can set before calling WdfChildListBeginIteration. |
| [WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS enumeration](..\wdfchildlist\ne-wdfchildlist--wdf-child-list-retrieve-device-status.md) | The WDF_CHILD_LIST_RETRIEVE_DEVICE_STATUS enumeration defines device status values that the framework stores in a driver's WDF_CHILD_RETRIEVE_INFO structure. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_COPY callback](..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-address-description-copy.md) | A driver's EvtChildListAddressDescriptionCopy event callback function copies a child address description from one specified location to another. |
| [EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_CLEANUP callback](..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-address-description-cleanup.md) | A driver's EvtChildListAddressDescriptionCleanup event callback function frees any memory allocations for an address description that the driver's EvtChildListAddressDescriptionDuplicate callback function allocated. |
| [EVT_WDF_CHILD_LIST_DEVICE_REENUMERATED callback](..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-device-reenumerated.md) | A driver's EvtChildListDeviceReenumerated event callback function enables the driver to approve or cancel a reenumeration of a specified device. |
| [EVT_WDF_CHILD_LIST_ADDRESS_DESCRIPTION_DUPLICATE callback](..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-address-description-duplicate.md) | A driver's EvtChildListAddressDescriptionDuplicate event callback function duplicates a child address description. |
| [EVT_WDF_CHILD_LIST_SCAN_FOR_CHILDREN callback](..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-scan-for-children.md) | A driver's EvtChildListScanForChildren event callback function must report all of the child devices that are present. |
| [EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_CLEANUP callback](..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-identification-description-cleanup.md) | A driver's EvtChildListIdentificationDescriptionCleanup event callback function frees any memory allocations for an identification description that the driver's EvtChildListIdentificationDescriptionDuplicate callback function allocated. |
| [EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_COPY callback](..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-identification-description-copy.md) | A driver's EvtChildListIdentificationDescriptionCopy event callback function copies a child identification description from one specified location to another. |
| [EVT_WDF_CHILD_LIST_CREATE_DEVICE callback](..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-create-device.md) | A bus driver'sEvtChildListCreateDevice event callback function creates a framework device object for a new device that has been dynamically enumerated. |
| [EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_COMPARE callback](..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-identification-description-compare.md) | A driver's EvtChildListIdentificationDescriptionCompare event callback function compares one child identification description with another. |
| [EVT_WDF_CHILD_LIST_IDENTIFICATION_DESCRIPTION_DUPLICATE callback](..\wdfchildlist\nc-wdfchildlist-evt-wdf-child-list-identification-description-duplicate.md) | A driver's EvtChildListIdentificationDescriptionDuplicate event callback function duplicates a child identification description. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_CHILD_LIST_CONFIG structure](..\wdfchildlist\ns-wdfchildlist--wdf-child-list-config.md) | The WDF_CHILD_LIST_CONFIG structure contains configuration information for a list of child devices. |
| [WDF_CHILD_LIST_ITERATOR structure](..\wdfchildlist\ns-wdfchildlist--wdf-child-list-iterator.md) | The WDF_CHILD_LIST_ITERATOR structure identifies the type of child devices that the framework will retrieve when a driver calls WdfChildListRetrieveNextDevice. |
| [WDF_CHILD_RETRIEVE_INFO structure](..\wdfchildlist\ns-wdfchildlist--wdf-child-retrieve-info.md) | The WDF_CHILD_RETRIEVE_INFO structure contains information about a child device that is obtained by calling WdfChildListRetrieveNextDevice or WdfChildListRetrievePdo. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfChildListUpdateAllChildDescriptionsAsPresent function](..\wdfchildlist\nf-wdfchildlist-wdfchildlistupdateallchilddescriptionsaspresent.md) | The WdfChildListUpdateAllChildDescriptionsAsPresent method informs the framework that all of the child devices in a specified child list are plugged in and available. |
| [WDF_CHILD_LIST_CONFIG_INIT function](..\wdfchildlist\nf-wdfchildlist-wdf-child-list-config-init.md) | The WDF_CHILD_LIST_CONFIG_INIT function initializes a WDF_CHILD_LIST_CONFIG structure. |
| [WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT function](..\wdfchildlist\nf-wdfchildlist-wdf-child-identification-description-header-init.md) | The WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER_INIT function initializes a WDF_CHILD_IDENTIFICATION_DESCRIPTION_HEADER structure. |
| [WDF_CHILD_LIST_ITERATOR_INIT function](..\wdfchildlist\nf-wdfchildlist-wdf-child-list-iterator-init.md) | The WDF_CHILD_LIST_ITERATOR_INIT function initializes a WDF_CHILD_LIST_ITERATOR structure. |
| [WdfChildListBeginIteration function](..\wdfchildlist\nf-wdfchildlist-wdfchildlistbeginiteration.md) | The WdfChildListBeginIteration method prepares the framework for retrieving items from a specified child list. |
| [WdfChildListGetDevice function](..\wdfchildlist\nf-wdfchildlist-wdfchildlistgetdevice.md) | The WdfChildListGetDevice method returns a handle to the framework device object that represents the parent device of a specified child list. |
| [WdfChildListCreate function](..\wdfchildlist\nf-wdfchildlist-wdfchildlistcreate.md) | The WdfChildListCreate method creates a child list for a specified parent device. |
| [WdfChildListRetrievePdo function](..\wdfchildlist\nf-wdfchildlist-wdfchildlistretrievepdo.md) | The WdfChildListRetrievePdo method returns a handle to the framework device object that is associated with a specified child description in a child list. |
| [WdfChildListUpdateChildDescriptionAsMissing function](..\wdfchildlist\nf-wdfchildlist-wdfchildlistupdatechilddescriptionasmissing.md) | The WdfChildListUpdateChildDescriptionAsMissing method informs the framework that a specified child device is currently unplugged or otherwise unavailable. |
| [WdfChildListEndScan function](..\wdfchildlist\nf-wdfchildlist-wdfchildlistendscan.md) | The WdfChildListEndScan method processes modifications to a specified child list. |
| [WdfChildListEndIteration function](..\wdfchildlist\nf-wdfchildlist-wdfchildlistenditeration.md) | The WdfChildListEndIteration method processes modifications to a specified child list. |
| [WdfChildListRequestChildEject function](..\wdfchildlist\nf-wdfchildlist-wdfchildlistrequestchildeject.md) | The WdfChildListRequestChildEject method informs the framework that a specified device is about to be ejected from its docking station. |
| [WdfChildListAddOrUpdateChildDescriptionAsPresent function](..\wdfchildlist\nf-wdfchildlist-wdfchildlistaddorupdatechilddescriptionaspresent.md) | The WdfChildListAddOrUpdateChildDescriptionAsPresent method adds a new child description to a list of children or updates an existing child description. |
| [WDF_CHILD_RETRIEVE_INFO_INIT function](..\wdfchildlist\nf-wdfchildlist-wdf-child-retrieve-info-init.md) | The WDF_CHILD_RETRIEVE_INFO_INIT function initializes a WDF_CHILD_RETRIEVE_INFO structure. |
| [WdfChildListRetrieveNextDevice function](..\wdfchildlist\nf-wdfchildlist-wdfchildlistretrievenextdevice.md) | The WdfChildListRetrieveNextDevice method traverses a specified child list and retrieves the next child device that matches specified criteria. |
| [WDF_CHILD_ADDRESS_DESCRIPTION_HEADER_INIT function](..\wdfchildlist\nf-wdfchildlist-wdf-child-address-description-header-init.md) | The WDF_CHILD_ADDRESS_DESCRIPTION_HEADER_INIT function initializes a WDF_CHILD_ADDRESS_DESCRIPTION_HEADER structure. |
| [WdfChildListRetrieveAddressDescription function](..\wdfchildlist\nf-wdfchildlist-wdfchildlistretrieveaddressdescription.md) | The WdfChildListRetrieveAddressDescription method locates a child device that has a specified identification description and retrieves the device's address description. |
| [WdfChildListBeginScan function](..\wdfchildlist\nf-wdfchildlist-wdfchildlistbeginscan.md) | The WdfChildListBeginScan method prepares a specified list of child devices so the driver can update the information in the list. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfCollectionGetCount function](..\wdfcollection\nf-wdfcollection-wdfcollectiongetcount.md) | The WdfCollectionGetCount method returns the number of objects that are currently in an object collection. |
| [WdfCollectionRemoveItem function](..\wdfcollection\nf-wdfcollection-wdfcollectionremoveitem.md) | The WdfCollectionRemoveItem method removes a specified object from an object collection, based on a specified index value. |
| [WdfCollectionRemove function](..\wdfcollection\nf-wdfcollection-wdfcollectionremove.md) | The WdfCollectionRemove method removes an object from a specified object collection. |
| [WdfCollectionGetItem function](..\wdfcollection\nf-wdfcollection-wdfcollectiongetitem.md) | The WdfCollectionGetItem method returns a handle to the object that is contained in a specified object collection and associated with a specified index value. |
| [WdfCollectionGetLastItem function](..\wdfcollection\nf-wdfcollection-wdfcollectiongetlastitem.md) | The WdfCollectionGetLastItem method returns a handle to the last object that is in an object collection. |
| [WdfCollectionCreate function](..\wdfcollection\nf-wdfcollection-wdfcollectioncreate.md) | The WdfCollectionCreate method creates a framework collection object. |
| [WdfCollectionGetFirstItem function](..\wdfcollection\nf-wdfcollection-wdfcollectiongetfirstitem.md) | The WdfCollectionGetFirstItem method returns a handle to the first object that is in an object collection. |
| [WdfCollectionAdd function](..\wdfcollection\nf-wdfcollection-wdfcollectionadd.md) | The WdfCollectionAdd method adds a specified framework object to an object collection. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_COMMON_BUFFER_CONFIG structure](..\wdfcommonbuffer\ns-wdfcommonbuffer--wdf-common-buffer-config.md) | The WDF_COMMON_BUFFER_CONFIG structure contains configuration information for a common buffer. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfCommonBufferGetAlignedVirtualAddress function](..\wdfcommonbuffer\nf-wdfcommonbuffer-wdfcommonbuffergetalignedvirtualaddress.md) | The WdfCommonBufferGetAlignedVirtualAddress method returns the virtual address that is associated with a specified common buffer. |
| [WdfCommonBufferCreate function](..\wdfcommonbuffer\nf-wdfcommonbuffer-wdfcommonbuffercreate.md) | The WdfCommonBufferCreate method creates a memory buffer that both the driver and a direct memory access (DMA) device can access simultaneously. |
| [WdfCommonBufferCreateWithConfig function](..\wdfcommonbuffer\nf-wdfcommonbuffer-wdfcommonbuffercreatewithconfig.md) | The WdfCommonBufferCreateWithConfig method creates a memory buffer that both the driver and a direct memory access (DMA) device can access simultaneously, and the method also specifies buffer configuration information. |
| [WdfCommonBufferGetLength function](..\wdfcommonbuffer\nf-wdfcommonbuffer-wdfcommonbuffergetlength.md) | The WdfCommonBufferGetLength method returns the length of a specified common buffer. |
| [WDF_COMMON_BUFFER_CONFIG_INIT function](..\wdfcommonbuffer\nf-wdfcommonbuffer-wdf-common-buffer-config-init.md) | The WDF_COMMON_BUFFER_CONFIG_INIT function initializes a WDF_COMMON_BUFFER_CONFIG structure. |
| [WdfCommonBufferGetAlignedLogicalAddress function](..\wdfcommonbuffer\nf-wdfcommonbuffer-wdfcommonbuffergetalignedlogicaladdress.md) | The WdfCommonBufferGetAlignedLogicalAddress method returns the logical address that is associated with a specified common buffer. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_COMPANION_EVENT_CALLBACKS_INIT function](..\wdfcompanion\nf-wdfcompanion-wdf-companion-event-callbacks-init.md) | For internal use only. |
| [WdfDeviceInitSetCompanionEventCallbacks function](..\wdfcompanion\nf-wdfcompanion-wdfdeviceinitsetcompanioneventcallbacks.md) | For internal use only. |
| [WdfCompanionWdmGetSecureDeviceHandle function](..\wdfcompanion\nf-wdfcompanion-wdfcompanionwdmgetsecuredevicehandle.md) | For internal use only. |
| [WDF_TASK_QUEUE_CONFIG_INIT function](..\wdfcompanion\nf-wdfcompanion-wdf-task-queue-config-init.md) | For internal use only. |
| [WdfCompanionCreateTaskQueue function](..\wdfcompanion\nf-wdfcompanion-wdfcompanioncreatetaskqueue.md) | For internal use only. |
| [WdfCompanionCreate function](..\wdfcompanion\nf-wdfcompanion-wdfcompanioncreate.md) | For internal use only. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_TASK_QUEUE_CONFIG structure](..\wdfcompanion\ns-wdfcompanion--wdf-task-queue-config.md) | For internal use only. |
| [WDF_COMPANION_EVENT_CALLBACKS structure](..\wdfcompanion\ns-wdfcompanion--wdf-companion-event-callbacks.md) | For internal use only. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_WDF_TASK_QUEUE_TASK_EXECUTE_SYNC callback](..\wdfcompanion\nc-wdfcompanion-evt-wdf-task-queue-task-execute-sync.md) | For internal use only. |
| [EVT_WDF_COMPANION_POST_D0_EXIT callback](..\wdfcompanion\nc-wdfcompanion-evt-wdf-companion-post-d0-exit.md) | For internal use only. |
| [EVT_WDF_COMPANION_PRE_PREPARE_HARDWARE callback](..\wdfcompanion\nc-wdfcompanion-evt-wdf-companion-pre-prepare-hardware.md) | For internal use only. |
| [EVT_WDF_COMPANION_PRE_D0_ENTRY callback](..\wdfcompanion\nc-wdfcompanion-evt-wdf-companion-pre-d0-entry.md) | For internal use only. |
| [EVT_WDF_COMPANION_POST_RELEASE_HARDWARE callback](..\wdfcompanion\nc-wdfcompanion-evt-wdf-companion-post-release-hardware.md) | For internal use only. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_TASK_QUEUE_DISPATCH_TYPE enumeration](..\wdfcompanion\ne-wdfcompanion--wdf-task-queue-dispatch-type.md) | For internal use only. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_TASK_SEND_OPTIONS structure](..\wdfcompaniontarget\ns-wdfcompaniontarget--wdf-task-send-options.md) | For internal use only. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfCompanionTargetSendTaskSynchronously function](..\wdfcompaniontarget\nf-wdfcompaniontarget-wdfcompaniontargetsendtasksynchronously.md) | For internal use only. |
| [WDF_TASK_SEND_OPTIONS_INIT function](..\wdfcompaniontarget\nf-wdfcompaniontarget-wdf-task-send-options-init.md) | For internal use only. |
| [WdfCompanionTargetWdmGetCompanionProcess function](..\wdfcompaniontarget\nf-wdfcompaniontarget-wdfcompaniontargetwdmgetcompanionprocess.md) | For internal use only. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_TASK_SEND_OPTIONS_FLAGS enumeration](..\wdfcompaniontarget\ne-wdfcompaniontarget--wdf-task-send-options-flags.md) | For internal use only. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfControlFinishInitializing function](..\wdfcontrol\nf-wdfcontrol-wdfcontrolfinishinitializing.md) | The WdfControlFinishInitializing method informs the framework that a driver has finished initializing a specified control device object. |
| [WdfControlDeviceInitSetShutdownNotification function](..\wdfcontrol\nf-wdfcontrol-wdfcontroldeviceinitsetshutdownnotification.md) | The WdfControlDeviceInitSetShutdownNotification method sets shutdown notification information for a control device object. |
| [WdfControlDeviceInitAllocate function](..\wdfcontrol\nf-wdfcontrol-wdfcontroldeviceinitallocate.md) | The WdfControlDeviceInitAllocate method allocates a WDFDEVICE_INIT structure that a driver uses when creating a new control device object. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_DEVICE_SHUTDOWN_FLAGS enumeration](..\wdfcontrol\ne-wdfcontrol--wdf-device-shutdown-flags.md) | The WDF_DEVICE_SHUTDOWN_FLAGS enumeration defines flags that identify types of shutdown notifications that a driver can receive. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_REL_TIMEOUT_IN_US function](..\wdfcore\nf-wdfcore-wdf-rel-timeout-in-us.md) | The WDF_REL_TIMEOUT_IN_US function converts a specified number of microseconds to a relative time value. |
| [WDF_ABS_TIMEOUT_IN_MS function](..\wdfcore\nf-wdfcore-wdf-abs-timeout-in-ms.md) | The WDF_ABS_TIMEOUT_IN_MS function converts a specified number of milliseconds to an absolute time value. |
| [WDF_REL_TIMEOUT_IN_MS function](..\wdfcore\nf-wdfcore-wdf-rel-timeout-in-ms.md) | The WDF_REL_TIMEOUT_IN_MS function converts a specified number of milliseconds to a relative time value. |
| [WDF_ABS_TIMEOUT_IN_US function](..\wdfcore\nf-wdfcore-wdf-abs-timeout-in-us.md) | The WDF_ABS_TIMEOUT_IN_US function converts a specified number of microseconds to an absolute time value. |
| [WDF_ABS_TIMEOUT_IN_SEC function](..\wdfcore\nf-wdfcore-wdf-abs-timeout-in-sec.md) | The WDF_ABS_TIMEOUT_IN_SEC function converts a specified number of seconds to an absolute time value. |
| [WDF_REL_TIMEOUT_IN_SEC function](..\wdfcore\nf-wdfcore-wdf-rel-timeout-in-sec.md) | The WDF_REL_TIMEOUT_IN_SEC function converts a specified number of seconds to a relative time value. |
| [WDF_ALIGN_SIZE_DOWN function](..\wdfcore\nf-wdfcore-wdf-align-size-down.md) | The WDF_ALIGN_SIZE_DOWN function returns the next-lower buffer size that is aligned to a specified alignment offset. |
| [WDF_ALIGN_SIZE_UP function](..\wdfcore\nf-wdfcore-wdf-align-size-up.md) | The WDF_ALIGN_SIZE_UP function returns the next-higher buffer size that is aligned to a specified alignment offset. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfDeviceInitSetDeviceType function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetdevicetype.md) | The WdfDeviceInitSetDeviceType method sets the device type for a specified device. |
| [WdfDeviceSetFailed function](..\wdfdevice\nf-wdfdevice-wdfdevicesetfailed.md) | The WdfDeviceSetFailed method informs the framework that the driver encountered a hardware or software error that is associated with a specified device. |
| [WdfDeviceIndicateWakeStatus function](..\wdfdevice\nf-wdfdevice-wdfdeviceindicatewakestatus.md) | The WdfDeviceIndicateWakeStatus method informs the framework that the calling bus driver has stopped waiting for a specified device to trigger a wake signal on the bus. |
| [WdfDeviceSetPnpCapabilities function](..\wdfdevice\nf-wdfdevice-wdfdevicesetpnpcapabilities.md) | The WdfDeviceSetPnpCapabilities method reports a device's Plug and Play capabilities. |
| [WdfDeviceGetDevicePowerPolicyState function](..\wdfdevice\nf-wdfdevice-wdfdevicegetdevicepowerpolicystate.md) | The WdfDeviceGetDevicePowerPolicyState method returns the current state of the framework's power policy state machine, for a specified device. |
| [WdfDevStateNormalize function](..\wdfdevice\nf-wdfdevice-wdfdevstatenormalize.md) | The WdfDevStateNormalize method removes extra bits from a specified framework state machine value so that the driver can use the value as an index into an array of machine states. |
| [WDF_DEVICE_STATE_INIT function](..\wdfdevice\nf-wdfdevice-wdf-device-state-init.md) | The WDF_DEVICE_STATE_INIT function initializes a driver's WDF_DEVICE_STATE structure. |
| [WdfWdmDeviceGetWdfDeviceHandle function](..\wdfdevice\nf-wdfdevice-wdfwdmdevicegetwdfdevicehandle.md) | The WdfWdmDeviceGetWdfDeviceHandle method returns a handle to the framework device object that is associated with a specified WDM device object. |
| [WdfDeviceGetFileObject function](..\wdfdevice\nf-wdfdevice-wdfdevicegetfileobject.md) | The WdfDeviceGetFileObject method returns a handle to the framework file object that is associated with a specified WDM file object. |
| [WDF_DEVICE_INTERFACE_PROPERTY_DATA_INIT function](..\wdfdevice\nf-wdfdevice-wdf-device-interface-property-data-init.md) | The WDF_DEVICE_INTERFACE_PROPERTY_DATA_INIT function initializes a driver's WDF_DEVICE_INTERFACE_PROPERTY_DATA structure. |
| [WdfDeviceWdmGetAttachedDevice function](..\wdfdevice\nf-wdfdevice-wdfdevicewdmgetattacheddevice.md) | The WdfDeviceWdmGetAttachedDevice method returns the next-lower WDM device object in the device stack. |
| [WdfDeviceCreateDeviceInterface function](..\wdfdevice\nf-wdfdevice-wdfdevicecreatedeviceinterface.md) | The WdfDeviceCreateDeviceInterface method creates a device interface for a specified device. |
| [WdfDeviceInitRegisterPowerStateChangeCallback function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitregisterpowerstatechangecallback.md) | The WdfDeviceInitRegisterPowerStateChangeCallback method registers a driver-supplied event callback function that the framework calls when a device's power state machine changes state. |
| [WdfDeviceInitSetPowerPolicyOwnership function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetpowerpolicyownership.md) | The WdfDeviceInitSetPowerPolicyOwnership method establishes whether the calling driver is, or is not, the power policy owner for a specified device. |
| [WdfDeviceResumeIdle function](..\wdfdevice\nf-wdfdevice-wdfdeviceresumeidle.md) | The WdfDeviceResumeIdle method informs the framework that the specified device is not in use and can be placed in a device low-power state if it remains idle. |
| [WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS_INIT function](..\wdfdevice\nf-wdfdevice-wdf-device-power-policy-wake-settings-init.md) | The WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS_INIT function initializes a driver's WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS structure. |
| [WdfDeviceInitSetIoTypeEx function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetiotypeex.md) | The WdfDeviceInitSetIoTypeEx method sets the method or preference for how a driver will access the data buffers that are included in read and write requests, as well as device I/O control requests, for a specified device. |
| [WdfDeviceInitSetPowerPolicyEventCallbacks function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetpowerpolicyeventcallbacks.md) | The WdfDeviceInitSetPowerPolicyEventCallbacks method registers a driver's power policy event callback functions. |
| [WdfDeviceInitSetPowerPageable function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetpowerpageable.md) | The WdfDeviceInitSetPowerPageable method informs the power manager that the driver must be able to access pageable data while the system is transitioning between a sleeping state and the working (S0) state. |
| [WdfDeviceGetDevicePnpState function](..\wdfdevice\nf-wdfdevice-wdfdevicegetdevicepnpstate.md) | The WdfDeviceGetDevicePnpState method returns the current state of the framework's Plug and Play state machine for a specified device. |
| [WdfDeviceSetDeviceState function](..\wdfdevice\nf-wdfdevice-wdfdevicesetdevicestate.md) | The WdfDeviceSetDeviceState method sets the device state for a specified device. |
| [WdfDeviceAddDependentUsageDeviceObject function](..\wdfdevice\nf-wdfdevice-wdfdeviceadddependentusagedeviceobject.md) | The WdfDeviceAddDependentUsageDeviceObject method indicates that a specified device depends on another device when the specified device is used to store special files. |
| [WdfDeviceGetDeviceState function](..\wdfdevice\nf-wdfdevice-wdfdevicegetdevicestate.md) | The WdfDeviceGetDeviceState method retrieves the device state for a specified device. |
| [WdfDeviceGetDevicePowerState function](..\wdfdevice\nf-wdfdevice-wdfdevicegetdevicepowerstate.md) | The WdfDeviceGetDevicePowerState method returns the current state of the framework's power state machine, for a specified device. |
| [WDF_DEVICE_POWER_CAPABILITIES_INIT function](..\wdfdevice\nf-wdfdevice-wdf-device-power-capabilities-init.md) | The WDF_DEVICE_POWER_CAPABILITIES_INIT function initializes a WDF_DEVICE_POWER_CAPABILITIES structure. |
| [WdfDeviceInitAssignWdmIrpPreprocessCallback function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitassignwdmirppreprocesscallback.md) | The WdfDeviceInitAssignWdmIrpPreprocessCallback method registers a callback function to handle an IRP major function code and, optionally, one or more minor function codes that are associated with the major function code. |
| [WdfDeviceInitAssignName function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitassignname.md) | The WdfDeviceInitAssignName method assigns a device name to a device's device object. |
| [WdfDeviceQueryInterfaceProperty function](..\wdfdevice\nf-wdfdevice-wdfdevicequeryinterfaceproperty.md) | The WdfDeviceQueryInterfaceProperty method retrieves a specified device interface property. |
| [WdfDevStateIsNP function](..\wdfdevice\nf-wdfdevice-wdfdevstateisnp.md) | The WdfDevStateIsNP method returns a Boolean value that indicates whether a specified power state or power policy state is a nonpageable state. |
| [WdfDeviceEnqueueRequest function](..\wdfdevice\nf-wdfdevice-wdfdeviceenqueuerequest.md) | The WdfDeviceEnqueueRequest method delivers a specified I/O request to the framework, so that the framework can subsequently add the request to one of the I/O queues that the driver has created for the specified device. |
| [WdfDeviceRetrieveCompanionTarget function](..\wdfdevice\nf-wdfdevice-wdfdeviceretrievecompaniontarget.md) | For internal use only. |
| [WdfDeviceInitFree function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitfree.md) | The WdfDeviceInitFree method deallocates a WDFDEVICE_INIT structure. |
| [WdfDeviceOpenRegistryKey function](..\wdfdevice\nf-wdfdevice-wdfdeviceopenregistrykey.md) | The WdfDeviceOpenRegistryKey method opens a device's hardware key or a driver's software key in the registry and creates a framework registry-key object that represents the registry key. |
| [WDF_POWER_POLICY_EVENT_CALLBACKS_INIT function](..\wdfdevice\nf-wdfdevice-wdf-power-policy-event-callbacks-init.md) | The WDF_POWER_POLICY_EVENT_CALLBACKS_INIT function initializes a driver's WDF_POWER_POLICY_EVENT_CALLBACKS structure. |
| [WdfDeviceSetDeviceInterfaceState function](..\wdfdevice\nf-wdfdevice-wdfdevicesetdeviceinterfacestate.md) | The WdfDeviceSetDeviceInterfaceState method enables or disables a device interface for a specified device. |
| [WdfDeviceCreate function](..\wdfdevice\nf-wdfdevice-wdfdevicecreate.md) | The WdfDeviceCreate method creates a framework device object. |
| [WdfDeviceWdmDispatchPreprocessedIrp function](..\wdfdevice\nf-wdfdevice-wdfdevicewdmdispatchpreprocessedirp.md) | The WdfDeviceWdmDispatchPreprocessedIrp method returns a preprocessed IRP to the framework. |
| [WdfDeviceSetStaticStopRemove function](..\wdfdevice\nf-wdfdevice-wdfdevicesetstaticstopremove.md) | The WdfDeviceSetStaticStopRemove method informs the framework whether a device can be stopped and removed. |
| [WDF_DEVICE_PNP_CAPABILITIES_INIT function](..\wdfdevice\nf-wdfdevice-wdf-device-pnp-capabilities-init.md) | The WDF_DEVICE_PNP_CAPABILITIES_INIT function initializes a WDF_DEVICE_PNP_CAPABILITIES structure. |
| [WdfDeviceWriteToHardware function](..\wdfdevice\nf-wdfdevice-wdfdevicewritetohardware.md) | The WdfDeviceWriteToHardware method is used internally by the framework. Do not use. |
| [WdfDeviceGetAlignmentRequirement function](..\wdfdevice\nf-wdfdevice-wdfdevicegetalignmentrequirement.md) | The WdfDeviceGetAlignmentRequirement method retrieves a device's address alignment requirement for memory transfer operations. |
| [WdfDeviceInitSetExclusive function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetexclusive.md) | The WdfDeviceInitSetExclusive method indicates whether a specified device is an exclusive device. |
| [WdfDeviceGetIoTarget function](..\wdfdevice\nf-wdfdevice-wdfdevicegetiotarget.md) | The WdfDeviceGetIoTarget method returns a handle to a function or filter driver's local I/O target, for a specified device. |
| [WdfDeviceInitSetIoInCallerContextCallback function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetioincallercontextcallback.md) | The WdfDeviceInitSetIoInCallerContextCallback method registers a driver's EvtIoInCallerContext event callback function. |
| [WdfDeviceGetSystemPowerAction function](..\wdfdevice\nf-wdfdevice-wdfdevicegetsystempoweraction.md) | The WdfDeviceGetSystemPowerAction method returns the system power action, if any, that is currently occurring for the computer. |
| [WdfDeviceRemoveRemovalRelationsPhysicalDevice function](..\wdfdevice\nf-wdfdevice-wdfdeviceremoveremovalrelationsphysicaldevice.md) | The WdfDeviceRemoveRemovalRelationsPhysicalDevice method removes a specified device from the list of devices that must be removed when another specified device is removed. |
| [WdfDeviceQueryPropertyEx function](..\wdfdevice\nf-wdfdevice-wdfdevicequerypropertyex.md) | The WdfDeviceQueryPropertyEx method retrieves a specified device property. |
| [WdfDeviceGetCharacteristics function](..\wdfdevice\nf-wdfdevice-wdfdevicegetcharacteristics.md) | The WdfDeviceGetCharacteristics method returns device characteristics for a specified device. |
| [WdfDeviceInitSetRequestAttributes function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetrequestattributes.md) | The WdfDeviceInitSetRequestAttributes method sets object attributes that will be used for all of the framework request objects that the framework delivers to the driver from the device's I/O queues. |
| [WDF_FILEOBJECT_CONFIG_INIT function](..\wdfdevice\nf-wdfdevice-wdf-fileobject-config-init.md) | The WDF_FILEOBJECT_CONFIG_INIT function initializes a driver's WDF_FILEOBJECT_CONFIG structure. |
| [WDF_POWER_FRAMEWORK_SETTINGS_INIT function](..\wdfdevice\nf-wdfdevice-wdf-power-framework-settings-init.md) | The WDF_POWER_FRAMEWORK_SETTINGS_INIT function initializes a WDF_POWER_FRAMEWORK_SETTINGS structure. |
| [WdfDeviceGetDefaultQueue function](..\wdfdevice\nf-wdfdevice-wdfdevicegetdefaultqueue.md) | The WdfDeviceGetDefaultQueue method returns a handle to a device's default I/O queue. |
| [WdfDeviceInitSetIoType function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetiotype.md) | The WdfDeviceInitSetIoType method sets the method or preference for how a driver will access the data buffers that are included in read and write requests for a specified device. |
| [WdfDeviceRetrieveDeviceInterfaceString function](..\wdfdevice\nf-wdfdevice-wdfdeviceretrievedeviceinterfacestring.md) | The WdfDeviceRetrieveDeviceInterfaceString method retrieves the symbolic link name that the operating system assigned to a device interface that the driver registered for a specified device. |
| [WdfDeviceInitSetReleaseHardwareOrderOnFailure function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetreleasehardwareorderonfailure.md) | The WdfDeviceInitSetReleaseHardwareOrderOnFailure method specifies whether the framework calls the driver's EvtDeviceReleaseHardware callback function immediately after device failure, or waits until all child devices have been removed. |
| [WdfDeviceInitSetFileObjectConfig function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetfileobjectconfig.md) | The WdfDeviceInitSetFileObjectConfig method registers event callback functions and sets configuration information for the driver's framework file objects. |
| [WdfDeviceAllocAndQueryProperty function](..\wdfdevice\nf-wdfdevice-wdfdeviceallocandqueryproperty.md) | The WdfDeviceAllocAndQueryProperty method allocates a buffer and retrieves a specified device property. |
| [WdfDeviceAssignProperty function](..\wdfdevice\nf-wdfdevice-wdfdeviceassignproperty.md) | The WdfDeviceAssignProperty method modifies the current setting of a device property. |
| [WdfDeviceClearRemovalRelationsDevices function](..\wdfdevice\nf-wdfdevice-wdfdeviceclearremovalrelationsdevices.md) | The WdfDeviceClearRemovalRelationsDevices method removes all devices from the list of devices that must be removed when a specified device is removed. |
| [WdfDeviceOpenDevicemapKey function](..\wdfdevice\nf-wdfdevice-wdfdeviceopendevicemapkey.md) | The WdfDeviceOpenDevicemapKey method opens the DEVICEMAP key and creates a framework registry-key object that represents the registry key. |
| [WdfDeviceInitSetCharacteristics function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetcharacteristics.md) | The WdfDeviceInitSetCharacteristics method sets device characteristics for a specified device. |
| [WDF_REMOVE_LOCK_OPTIONS_INIT function](..\wdfdevice\nf-wdfdevice-wdf-remove-lock-options-init.md) | The WDF_REMOVE_LOCK_OPTIONS_INIT function initializes a WDF_REMOVE_LOCK_OPTIONS structure. |
| [WdfDeviceQueryProperty function](..\wdfdevice\nf-wdfdevice-wdfdevicequeryproperty.md) | The WdfDeviceQueryProperty method retrieves a specified device property. |
| [WdfDevicePostEvent function](..\wdfdevice\nf-wdfdevice-wdfdevicepostevent.md) | The WdfDevicePostEvent method asynchronously notifies applications that are waiting for the specified event from a driver. |
| [WdfDeviceAllocAndQueryPropertyEx function](..\wdfdevice\nf-wdfdevice-wdfdeviceallocandquerypropertyex.md) | The WdfDeviceAllocAndQueryPropertyEx method allocates a buffer and retrieves a specified device property. |
| [WDF_PNPPOWER_EVENT_CALLBACKS_INIT function](..\wdfdevice\nf-wdfdevice-wdf-pnppower-event-callbacks-init.md) | The WDF_PNPPOWER_EVENT_CALLBACKS_INIT function initializes a driver's WDF_PNPPOWER_EVENT_CALLBACKS structure. |
| [WdfDeviceAssignInterfaceProperty function](..\wdfdevice\nf-wdfdevice-wdfdeviceassigninterfaceproperty.md) | The WdfDeviceAssignInterfaceProperty method modifies the current value of a device interface property. |
| [WdfDeviceAllocAndQueryInterfaceProperty function](..\wdfdevice\nf-wdfdevice-wdfdeviceallocandqueryinterfaceproperty.md) | The WdfDeviceAllocAndQueryInterfaceProperty method allocates a buffer and retrieves a specified device interface property. |
| [WdfDeviceStopIdle function](..\wdfdevice\nf-wdfdevice-wdfdevicestopidle.md) | The WdfDeviceStopIdle method informs the framework that the specified device must be placed in its working (D0) power state. |
| [WdfDeviceConfigureRequestDispatching function](..\wdfdevice\nf-wdfdevice-wdfdeviceconfigurerequestdispatching.md) | The WdfDeviceConfigureRequestDispatching method causes the framework to queue a specified type of I/O requests to a specified I/O queue. |
| [WdfDeviceWdmGetDeviceObject function](..\wdfdevice\nf-wdfdevice-wdfdevicewdmgetdeviceobject.md) | The WdfDeviceWdmGetDeviceObject method returns the Windows Driver Model (WDM) device object that is associated with a specified framework device object. |
| [WdfDeviceWdmDispatchIrpToIoQueue function](..\wdfdevice\nf-wdfdevice-wdfdevicewdmdispatchirptoioqueue.md) | The WdfDeviceWdmDispatchIrpToIoQueue method forwards the IRP to a specified I/O queue. |
| [WdfDeviceSetBusInformationForChildren function](..\wdfdevice\nf-wdfdevice-wdfdevicesetbusinformationforchildren.md) | The WdfDeviceSetBusInformationForChildren method sets information about a bus that a bus driver supports. This information is available to the bus's child devices. |
| [WdfDeviceWdmAssignPowerFrameworkSettings function](..\wdfdevice\nf-wdfdevice-wdfdevicewdmassignpowerframeworksettings.md) | The WdfDeviceWdmAssignPowerFrameworkSettings method registers power management framework (PoFx) settings for single-component devices. |
| [WdfDeviceInitSetRemoveLockOptions function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetremovelockoptions.md) | The WdfDeviceInitSetRemoveLockOptions method causes the framework to acquire a remove lock before delivering an IRP of any type to the driver. |
| [WdfDeviceAssignSxWakeSettings function](..\wdfdevice\nf-wdfdevice-wdfdeviceassignsxwakesettings.md) | The WdfDeviceAssignSxWakeSettings method provides driver-supplied information about a device's ability to trigger a wake signal while both the device and the system are in a low-power state. |
| [WdfDeviceRemoveDependentUsageDeviceObject function](..\wdfdevice\nf-wdfdevice-wdfdeviceremovedependentusagedeviceobject.md) | The WdfDeviceRemoveDependentUsageDeviceObject method indicates that a specified device no longer depends on another device when the specified device is used to store special files. |
| [WdfDeviceInitSetPowerNotPageable function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetpowernotpageable.md) | The WdfDeviceInitSetPowerNotPageable method informs the power manager that the driver will not access pageable data while the system is transitioning between a sleeping state and the working (S0) state. |
| [WdfDeviceInitAssignSDDLString function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitassignsddlstring.md) | The WdfDeviceInitAssignSDDLString method assigns a security setting for a device. |
| [WdfDeviceInitSetDeviceClass function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetdeviceclass.md) | The WdfDeviceInitSetDeviceClass method specifies a GUID that identifies the device's device setup class. |
| [WdfDeviceSetSpecialFileSupport function](..\wdfdevice\nf-wdfdevice-wdfdevicesetspecialfilesupport.md) | The WdfDeviceSetSpecialFileSupport method enables or disables a function driver's support for special files, for the specified device. |
| [WdfDeviceMapIoSpace function](..\wdfdevice\nf-wdfdevice-wdfdevicemapiospace.md) | The WdfDeviceMapIoSpace function maps the given physical address range to system address space and returns a pseudo base address. |
| [WdfDeviceInitRegisterPowerPolicyStateChangeCallback function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitregisterpowerpolicystatechangecallback.md) | The WdfDeviceInitRegisterPowerPolicyStateChangeCallback method registers a driver-supplied event callback function that the framework calls when a device's power policy state machine changes state. |
| [WdfDeviceSetCharacteristics function](..\wdfdevice\nf-wdfdevice-wdfdevicesetcharacteristics.md) | The WdfDeviceSetCharacteristics method sets device characteristics for a specified device. |
| [WdfDeviceInitSetPnpPowerEventCallbacks function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetpnppowereventcallbacks.md) | The WdfDeviceInitSetPnpPowerEventCallbacks method registers a driver's Plug and Play and power management event callback functions. |
| [WdfDeviceAddRemovalRelationsPhysicalDevice function](..\wdfdevice\nf-wdfdevice-wdfdeviceaddremovalrelationsphysicaldevice.md) | The WdfDeviceAddRemovalRelationsPhysicalDevice method indicates that a specified device must be removed when another specified device is removed. |
| [WdfDeviceSetAlignmentRequirement function](..\wdfdevice\nf-wdfdevice-wdfdevicesetalignmentrequirement.md) | The WdfDeviceSetAlignmentRequirement method registers the driver's preferred address alignment for the data buffers that the device uses during memory transfer operations. |
| [WdfDeviceReadFromHardware function](..\wdfdevice\nf-wdfdevice-wdfdevicereadfromhardware.md) | The WdfDeviceReadFromHardware method is used internally by the framework. Do not use. |
| [WdfDeviceSetPowerCapabilities function](..\wdfdevice\nf-wdfdevice-wdfdevicesetpowercapabilities.md) | The WdfDeviceSetPowerCapabilities method reports a device's power capabilities. |
| [WdfDeviceInitRegisterPnpStateChangeCallback function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitregisterpnpstatechangecallback.md) | The WdfDeviceInitRegisterPnpStateChangeCallback method registers a driver-supplied event callback function that the framework calls when a device's Plug and Play state machine changes state. |
| [WdfDeviceAssignMofResourceName function](..\wdfdevice\nf-wdfdevice-wdfdeviceassignmofresourcename.md) | The WdfDeviceAssignMofResourceName method registers a MOF resource name for a specified device. |
| [WdfDeviceAssignS0IdleSettings function](..\wdfdevice\nf-wdfdevice-wdfdeviceassigns0idlesettings.md) | The WdfDeviceAssignS0IdleSettings method provides driver-supplied information that the framework uses when a device is idle and the system is in its working (S0) state. |
| [WdfDeviceGetDeviceStackIoType function](..\wdfdevice\nf-wdfdevice-wdfdevicegetdevicestackiotype.md) | The WdfDeviceGetDeviceStackIoType method retrieves the buffer access methods that the framework is using for a device. |
| [WdfDeviceWdmGetPhysicalDevice function](..\wdfdevice\nf-wdfdevice-wdfdevicewdmgetphysicaldevice.md) | The WdfDeviceWdmGetPhysicalDevice method retrieves the physical device's WDM PDO from the device stack. |
| [WdfDeviceWdmDispatchIrp function](..\wdfdevice\nf-wdfdevice-wdfdevicewdmdispatchirp.md) | The WdfDeviceWdmDispatchIrp method returns a dispatched IRP to the framework from EvtDeviceWdmIrpDispatch. |
| [WdfDeviceRetrieveDeviceName function](..\wdfdevice\nf-wdfdevice-wdfdeviceretrievedevicename.md) | The WdfDeviceRetrieveDeviceName method returns the device name for a specified device. |
| [WdfDeviceGetDriver function](..\wdfdevice\nf-wdfdevice-wdfdevicegetdriver.md) | The WdfDeviceGetDriver method returns a handle to the framework driver object that is associated with a specified framework device object. |
| [WdfDeviceConfigureWdmIrpDispatchCallback function](..\wdfdevice\nf-wdfdevice-wdfdeviceconfigurewdmirpdispatchcallback.md) | The WdfDeviceConfigureWdmIrpDispatchCallback method registers a driver's EvtDeviceWdmIrpDispatch callback function. |
| [WdfDeviceGetHardwareRegisterMappedAddress function](..\wdfdevice\nf-wdfdevice-wdfdevicegethardwareregistermappedaddress.md) | A driver calls WdfDeviceGetHardwareRegisterMappedAddress to get the user-mode mapped address of the memory resource it mapped previously using WdfDeviceMapIoSpace. |
| [WdfDeviceCreateSymbolicLink function](..\wdfdevice\nf-wdfdevice-wdfdevicecreatesymboliclink.md) | The WdfDeviceCreateSymbolicLink method creates a symbolic link to a specified device. |
| [WdfDeviceInitSetPowerInrush function](..\wdfdevice\nf-wdfdevice-wdfdeviceinitsetpowerinrush.md) | The WdfDeviceInitSetPowerInrush method informs the power manager that the specified device requires an inrush of current when it starts. |
| [WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT function](..\wdfdevice\nf-wdfdevice-wdf-device-power-policy-idle-settings-init.md) | The WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT function initializes a driver's WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS structure. |
| [WdfDeviceUnmapIoSpace function](..\wdfdevice\nf-wdfdevice-wdfdeviceunmapiospace.md) | The WdfDeviceUnmapIoSpace function unmaps a specified range of physical addresses previously mapped by the WdfDeviceMapIoSpace function. |
| [WDF_IO_TYPE_CONFIG_INIT function](..\wdfdevice\nf-wdfdevice-wdf-io-type-config-init.md) | The WDF_IO_TYPE_CONFIG_INIT function initializes a driver's WDF_IO_TYPE_CONFIG structure. |
| [WDF_DEVICE_PROPERTY_DATA_INIT function](..\wdfdevice\nf-wdfdevice-wdf-device-property-data-init.md) | The WDF_DEVICE_PROPERTY_DATA_INIT function initializes a driver's WDF_DEVICE_PROPERTY_DATA structure. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_WDF_DEVICE_USAGE_NOTIFICATION callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-usage-notification.md) | A driver's EvtDeviceUsageNotification event callback function informs the driver when a device is being used for special files. |
| [EVT_WDF_DEVICE_SELF_MANAGED_IO_FLUSH callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-self-managed-io-flush.md) | A driver's EvtDeviceSelfManagedIoFlush event callback function handles flush activity for the device's self-managed I/O operations. |
| [EVT_WDF_FILE_CLOSE callback](..\wdfdevice\nc-wdfdevice-evt-wdf-file-close.md) | A driver's EvtFileClose callback function handles operations that must be performed when all of an application's accesses to a device have been closed. |
| [EVT_WDFDEVICE_WDM_PRE_PO_FX_UNREGISTER_DEVICE callback](..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-pre-po-fx-unregister-device.md) | The EvtDeviceWdmPrePoFxUnregisterDevice callback function performs device-specific operations before the framework deletes a specified registration with the power framework. |
| [EVT_WDF_DEVICE_POWER_POLICY_STATE_CHANGE_NOTIFICATION callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-power-policy-state-change-notification.md) | A driver's EvtDevicePowerPolicyStateChange event callback function informs the driver that a device's power policy state machine is moving from one state to another. |
| [EVT_WDF_DEVICE_POWER_STATE_CHANGE_NOTIFICATION callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-power-state-change-notification.md) | A driver's EvtDevicePowerStateChange event callback function informs the driver that a device's power state machine is moving from one state to another. |
| [EVT_WDF_DEVICE_WAKE_FROM_SX_TRIGGERED callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-wake-from-sx-triggered.md) | A driver's EvtDeviceWakeFromSxTriggered event callback function informs the driver that its device, which had previously entered a low-power device state because system power was reduced, might have triggered a wake signal. |
| [EVT_WDF_DEVICE_PREPARE_HARDWARE callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-prepare-hardware.md) | A driver's EvtDevicePrepareHardware event callback function performs any operations that are needed to make a device accessible to the driver. |
| [EVT_WDFDEVICE_WDM_IRP_PREPROCESS callback](..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-preprocess.md) | A driver's EvtDeviceWdmIrpPreprocess event callback function receives an IRP before the framework processes the IRP. |
| [EVT_WDF_DEVICE_D0_ENTRY_POST_INTERRUPTS_ENABLED callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-entry-post-interrupts-enabled.md) | A driver's EvtDeviceD0EntryPostInterruptsEnabled event callback function performs device-specific operations that are required after the driver has enabled the device's hardware interrupts. |
| [EVT_WDF_DEVICE_SELF_MANAGED_IO_RESTART callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-self-managed-io-restart.md) | A driver's EvtDeviceSelfManagedIoRestart event callback function restarts a device's self-managed I/O operations. |
| [EVT_WDF_DEVICE_SELF_MANAGED_IO_INIT callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-self-managed-io-init.md) | A driver's EvtDeviceSelfManagedIoInit event callback function initializes and starts the device's self-managed I/O operations. |
| [EVT_WDF_DEVICE_ARM_WAKE_FROM_SX_WITH_REASON callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-arm-wake-from-sx-with-reason.md) | A driver's EvtDeviceArmWakeFromSxWithReason event callback function arms (that is, enables) a device so that it can trigger a wake signal while in a low-power device state. |
| [EVT_WDF_DEVICE_ARM_WAKE_FROM_S0 callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-arm-wake-from-s0.md) | A driver's EvtDeviceArmWakeFromS0 event callback function arms (that is, enables) a device so that it can trigger a wake signal while in a low-power device state, if the system remains in the system working state (S0). |
| [EVT_WDF_DEVICE_QUERY_REMOVE callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-query-remove.md) | A driver's EvtDeviceQueryRemove event callback function determines whether a specified device can be stopped and removed. |
| [EVT_WDF_DEVICE_SELF_MANAGED_IO_SUSPEND callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-self-managed-io-suspend.md) | A driver's EvtDeviceSelfManagedIoSuspend event callback function suspends a device's self-managed I/O operations. |
| [EVT_WDF_DEVICE_WAKE_FROM_S0_TRIGGERED callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-wake-from-s0-triggered.md) | A driver's EvtDeviceWakeFromS0Triggered event callback function informs the driver that its device, which had previously entered a low-power device state while the system power state remained at S0, might have triggered a wake signal. |
| [EVT_WDFDEVICE_WDM_POST_PO_FX_REGISTER_DEVICE callback](..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-post-po-fx-register-device.md) | The EvtDeviceWdmPostPoFxRegisterDevice callback function performs device-specific operations after the framework has registered with the power framework. |
| [EVT_WDF_IO_IN_CALLER_CONTEXT callback](..\wdfdevice\nc-wdfdevice-evt-wdf-io-in-caller-context.md) | A driver's EvtIoInCallerContext event callback function preprocesses an I/O request before the framework places it into an I/O queue. |
| [EVT_WDF_DEVICE_D0_EXIT callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-exit.md) | A driver's EvtDeviceD0Exit event callback function performs operations that are needed when the driver's device leaves the D0 power state. |
| [EVT_WDF_DEVICE_DISARM_WAKE_FROM_SX callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-disarm-wake-from-sx.md) | A driver's EvtDeviceDisarmWakeFromSx event callback function disarms (that is, disables) a device's ability to trigger a wake signal while the device and system are in low-power states. |
| [EVT_WDF_DEVICE_RELATIONS_QUERY callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-relations-query.md) | A driver's EvtDeviceRelationsQuery event callback reports changes in the relationships among devices that are supported by the driver. |
| [EVT_WDF_DEVICE_SURPRISE_REMOVAL callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-surprise-removal.md) | A driver's EvtDeviceSurpriseRemoval event callback function performs any operations that are needed after a device has been unexpectedly removed from the system or after a driver reports that the device has failed. |
| [EVT_WDF_FILE_CLEANUP callback](..\wdfdevice\nc-wdfdevice-evt-wdf-file-cleanup.md) | A driver's EvtFileCleanup callback function handles operations that must be performed when an application is closing all accesses to a device. |
| [EVT_WDF_DEVICE_SELF_MANAGED_IO_CLEANUP callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-self-managed-io-cleanup.md) | A driver's EvtDeviceSelfManagedIoCleanup event callback function handles deallocation activity for the device's self-managed I/O operations, after a device has been removed. |
| [EVT_WDF_DEVICE_D0_EXIT_PRE_INTERRUPTS_DISABLED callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-exit-pre-interrupts-disabled.md) | A driver's EvtDeviceD0ExitPreInterruptsDisabled event callback function performs device-specific operations that are required before the driver disables the device's hardware interrupts. |
| [EVT_WDFDEVICE_WDM_IRP_DISPATCH callback](..\wdfdevice\nc-wdfdevice-evt-wdfdevice-wdm-irp-dispatch.md) | A driver's EvtDeviceWdmIrpDispatch event callback function receives an IRP before the framework processes the IRP. |
| [EVT_WDF_DEVICE_ARM_WAKE_FROM_SX callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-arm-wake-from-sx.md) | A driver's EvtDeviceArmWakeFromSx event callback function arms (that is, enables) a device so that it can trigger a wake signal while in a low-power device state. |
| [EVT_WDF_DEVICE_USAGE_NOTIFICATION_EX callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-usage-notification-ex.md) | A driver's EvtDeviceUsageNotificationEx event callback function determines whether a device can support a special file type. |
| [EVT_WDF_DEVICE_DISARM_WAKE_FROM_S0 callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-disarm-wake-from-s0.md) | A driver's EvtDeviceDisarmWakeFromS0 event callback function disarms (that is, disables) a device's ability to trigger a wake signal while in a low-power device state, if the system remains in the system working state (S0). |
| [EVT_WDF_DEVICE_PNP_STATE_CHANGE_NOTIFICATION callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-pnp-state-change-notification.md) | A driver's EvtDevicePnpStateChange event callback function informs the driver that a device's Plug and Play (PnP) state machine is moving from one state to another. |
| [EVT_WDF_DEVICE_RELEASE_HARDWARE callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-release-hardware.md) | A driver's EvtDeviceReleaseHardware event callback function performs operations that are needed when a device is no longer accessible. |
| [EVT_WDF_DEVICE_FILE_CREATE callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-file-create.md) | A driver's EvtDeviceFileCreate callback function handles operations that must be performed when an application requests access to a device. |
| [EVT_WDF_DEVICE_D0_ENTRY callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-d0-entry.md) | A driver's EvtDeviceD0Entry event callback function performs operations that are needed when the driver's device enters the D0 power state. |
| [EVT_WDF_DEVICE_QUERY_STOP callback](..\wdfdevice\nc-wdfdevice-evt-wdf-device-query-stop.md) | A driver's EvtDeviceQueryStop event callback function determines whether a specified device can be stopped so that the PnP manager can redistribute system hardware resources. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_POWER_POLICY_IDLE_TIMEOUT_CONSTANTS enumeration](..\wdfdevice\ne-wdfdevice--wdf-power-policy-idle-timeout-constants.md) | The WDF_POWER_POLICY_IDLE_TIMEOUT_CONSTANTS enumeration is reserved for internal use. |
| [WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE enumeration](..\wdfdevice\ne-wdfdevice--wdf-power-policy-idle-timeout-type.md) | The WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE enumeration identifies how the idle timeout for a device is determined. |
| [WDF_DEVICE_PNP_STATE enumeration](..\wdfdevice\ne-wdfdevice--wdf-device-pnp-state.md) | The WDF_DEVICE_PNP_STATE enumeration identifies all of the states that the framework's Plug and Play state machine can enter. |
| [WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE enumeration](..\wdfdevice\ne-wdfdevice--wdf-release-hardware-order-on-failure.md) | The WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE enumeration specifies when the framework calls a driver's EvtDeviceReleaseHardware callback function. |
| [WDF_DEVICE_HWACCESS_TARGET_TYPE enumeration](..\wdfdevice\ne-wdfdevice--wdf-device-hwaccess-target-type.md) | The WDF_DEVICE_HWACCESS_TARGET_TYPE enumeration is used internally by the framework. Do not use. |
| [WDF_DEVICE_POWER_POLICY_STATE enumeration](..\wdfdevice\ne-wdfdevice--wdf-device-power-policy-state.md) | The WDF_DEVICE_POWER_POLICY_STATE enumeration identifies all of the states that the framework's power policy state machine can enter. |
| [WDF_SPECIAL_FILE_TYPE enumeration](..\wdfdevice\ne-wdfdevice--wdf-special-file-type.md) | The WDF_SPECIAL_FILE_TYPE enumeration identifies special file types that a device can support. |
| [WDF_DEVICE_POWER_STATE enumeration](..\wdfdevice\ne-wdfdevice--wdf-device-power-state.md) | The WDF_DEVICE_POWER_STATE enumeration identifies all of the states that the framework's power state machine can enter. |
| [WDF_EVENT_TYPE enumeration](..\wdfdevice\ne-wdfdevice--wdf-event-type.md) | The WDF_EVENT_TYPE enumeration specifies. |
| [WDF_POWER_POLICY_SX_WAKE_USER_CONTROL enumeration](..\wdfdevice\ne-wdfdevice--wdf-power-policy-sx-wake-user-control.md) | The WDF_POWER_POLICY_SX_WAKE_USER_CONTROL enumeration identifies whether a user can control a device's ability to wake the system from a low system power state. |
| [WDF_REMOVE_LOCK_OPTIONS_FLAGS enumeration](..\wdfdevice\ne-wdfdevice--wdf-remove-lock-options-flags.md) | The WDF_REMOVE_LOCK_OPTIONS_FLAGS enumeration type defines flags that are used in a driver's WDF_REMOVE_LOCK_OPTIONS structure. |
| [WDF_DEVICE_IO_TYPE enumeration](..\wdfdevice\ne-wdfdevice--wdf-device-io-type.md) | The WDF_DEVICE_IO_TYPE enumeration is used to specify a method for accessing data buffers. |
| [WDF_POWER_POLICY_S0_IDLE_CAPABILITIES enumeration](..\wdfdevice\ne-wdfdevice--wdf-power-policy-s0-idle-capabilities.md) | The WDF_POWER_POLICY_S0_IDLE_CAPABILITIES enumeration identifies the capabilities that a device can support when it enters a low-power state while it is idling. |
| [WDF_DEVICE_HWACCESS_TARGET_SIZE enumeration](..\wdfdevice\ne-wdfdevice--wdf-device-hwaccess-target-size.md) | The WDF_DEVICE_HWACCESS_TARGET_SIZE enumeration is used internally by the framework. Do not use. |
| [WDF_FILEOBJECT_CLASS enumeration](..\wdfdevice\ne-wdfdevice--wdf-fileobject-class.md) | The WDF_FILEOBJECT_CLASS enumeration defines values that identify whether a driver requires a framework file object to represent a file that an application or another driver is attempting to create or open. |
| [WDF_DISPATCH_IRP_TO_IO_QUEUE_FLAGS enumeration](..\wdfdevice\ne-wdfdevice--wdf-dispatch-irp-to-io-queue-flags.md) | The WDF_DISPATCH_IRP_TO_IO_QUEUE_FLAGS enumeration type defines flags that the driver can specify when it calls WdfDeviceWdmDispatchIrpToIoQueue. |
| [WDF_DEVICE_FAILED_ACTION enumeration](..\wdfdevice\ne-wdfdevice--wdf-device-failed-action.md) | The WDF_DEVICE_FAILED_ACTION enumeration identifies the action that the framework will take when a driver reports an unrecoverable software or hardware failure. |
| [WDF_STATE_NOTIFICATION_TYPE enumeration](..\wdfdevice\ne-wdfdevice--wdf-state-notification-type.md) | The WDF_STATE_NOTIFICATION_TYPE enumeration identifies the type of Plug and Play, power, or power policy notification that a framework-based driver will receive. |
| [WDF_POWER_POLICY_S0_IDLE_USER_CONTROL enumeration](..\wdfdevice\ne-wdfdevice--wdf-power-policy-s0-idle-user-control.md) | The WDF_POWER_POLICY_S0_IDLE_USER_CONTROL enumeration identifies whether a user can control a device's behavior when the device is idle and the system is in its working (S0) state. |
| [WDF_POWER_DEVICE_STATE enumeration](..\wdfdevice\ne-wdfdevice--wdf-power-device-state.md) | The WDF_POWER_DEVICE_STATE enumeration identifies the device power states that a device might support. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA structure](..\wdfdevice\ns-wdfdevice--wdf-device-power-policy-notification-data.md) | The WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA structure describes a state change within a device's power policy state machine. |
| [WDF_DEVICE_PNP_NOTIFICATION_DATA structure](..\wdfdevice\ns-wdfdevice--wdf-device-pnp-notification-data.md) | The WDF_DEVICE_PNP_NOTIFICATION_DATA structure describes a state change within a device's Plug and Play state machine. |
| [WDF_DEVICE_STATE structure](..\wdfdevice\ns-wdfdevice--wdf-device-state.md) | The WDF_DEVICE_STATE structure specifies a device's Plug and Play state. |
| [WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS structure](..\wdfdevice\ns-wdfdevice--wdf-device-power-policy-idle-settings.md) | The WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS structure contains driver-supplied information that the framework uses when a device is idle and the system is in the system working state (S0). |
| [WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS structure](..\wdfdevice\ns-wdfdevice--wdf-device-power-policy-wake-settings.md) | The WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS structure contains driver-supplied information about a device's ability to wake itself and the system, when both are in a low-power state. |
| [WDF_IO_TYPE_CONFIG structure](..\wdfdevice\ns-wdfdevice--wdf-io-type-config.md) | The WDF_IO_TYPE_CONFIG structure specifies the driver's preferred buffer access method for read and write requests, and for device I/O control requests. |
| [WDF_DEVICE_POWER_NOTIFICATION_DATA structure](..\wdfdevice\ns-wdfdevice--wdf-device-power-notification-data.md) | The WDF_DEVICE_POWER_NOTIFICATION_DATA structure describes a state change within a device's power state machine. |
| [WDF_DEVICE_INTERFACE_PROPERTY_DATA structure](..\wdfdevice\ns-wdfdevice--wdf-device-interface-property-data.md) | The WDF_DEVICE_INTERFACE_PROPERTY_DATA structure describes a device interface property. |
| [WDF_DEVICE_POWER_CAPABILITIES structure](..\wdfdevice\ns-wdfdevice--wdf-device-power-capabilities.md) | The WDF_DEVICE_POWER_CAPABILITIES structure describes a device's power capabilities. |
| [WDF_DEVICE_PROPERTY_DATA structure](..\wdfdevice\ns-wdfdevice--wdf-device-property-data.md) | The WDF_DEVICE_PROPERTY_DATA structure describes a device property. |
| [WDF_PNPPOWER_EVENT_CALLBACKS structure](..\wdfdevice\ns-wdfdevice--wdf-pnppower-event-callbacks.md) | The WDF_PNPPOWER_EVENT_CALLBACKS structure contains pointers to a driver's Plug and Play and power event callback functions. |
| [WDF_POWER_POLICY_EVENT_CALLBACKS structure](..\wdfdevice\ns-wdfdevice--wdf-power-policy-event-callbacks.md) | The WDF_POWER_POLICY_EVENT_CALLBACKS structure contains pointers to a driver's power policy event callback functions. |
| [WDF_REMOVE_LOCK_OPTIONS structure](..\wdfdevice\ns-wdfdevice--wdf-remove-lock-options.md) | The WDF_REMOVE_LOCK_OPTIONS structure specifies options for acquiring a remove lock before delivering an IRP to the driver. |
| [WDF_POWER_FRAMEWORK_SETTINGS structure](..\wdfdevice\ns-wdfdevice--wdf-power-framework-settings.md) | The WDF_POWER_FRAMEWORK_SETTINGS structure describes power management framework (PoFx) settings for single-component devices. |
| [WDF_FILEOBJECT_CONFIG structure](..\wdfdevice\ns-wdfdevice--wdf-fileobject-config.md) | The WDF_FILEOBJECT_CONFIG structure contains configuration information of a driver's framework file objects. |
| [WDF_DEVICE_PNP_CAPABILITIES structure](..\wdfdevice\ns-wdfdevice--wdf-device-pnp-capabilities.md) | The WDF_DEVICE_PNP_CAPABILITIES structure describes a device's Plug and Play capabilities. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_DMA_ENABLER_CONFIG_FLAGS enumeration](..\wdfdmaenabler\ne-wdfdmaenabler--wdf-dma-enabler-config-flags.md) | The WDF_DMA_ENABLER_CONFIG_FLAGS enumeration type defines flags that are used in a driver's WDF_DMA_ENABLER_CONFIG structure. |
| [WDF_DMA_PROFILE enumeration](..\wdfdmaenabler\ne-wdfdmaenabler--wdf-dma-profile.md) | The WDF_DMA_PROFILE enumeration identifies the types of bus-master or system-mode DMA operations that devices can support. |
| [WDF_DMA_DIRECTION enumeration](..\wdfdmaenabler\ne-wdfdmaenabler--wdf-dma-direction.md) | The WDF_DMA_DIRECTION enumeration defines the direction of a DMA transfer. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfDmaEnablerGetMaximumScatterGatherElements function](..\wdfdmaenabler\nf-wdfdmaenabler-wdfdmaenablergetmaximumscattergatherelements.md) | The WdfDmaEnablerGetMaximumScatterGatherElements method returns the maximum number of scatter/gather elements that the device and driver support, for a specified DMA enabler object. |
| [WdfDmaEnablerWdmGetDmaAdapter function](..\wdfdmaenabler\nf-wdfdmaenabler-wdfdmaenablerwdmgetdmaadapter.md) | The WdfDmaEnablerWdmGetDmaAdapter method returns a pointer to a WDM DMA_ADAPTER structure that is associated with a DMA enabler object. |
| [WDF_DMA_ENABLER_CONFIG_INIT function](..\wdfdmaenabler\nf-wdfdmaenabler-wdf-dma-enabler-config-init.md) | The WDF_DMA_ENABLER_CONFIG_INIT function initializes a driver's WDF_DMA_ENABLER_CONFIG structure. |
| [WdfDmaEnablerSetMaximumScatterGatherElements function](..\wdfdmaenabler\nf-wdfdmaenabler-wdfdmaenablersetmaximumscattergatherelements.md) | The WdfDmaEnablerSetMaximumScatterGatherElements method sets the maximum number of scatter/gather elements that a device supports, for a specified DMA enabler object. |
| [WDF_DMA_SYSTEM_PROFILE_CONFIG_INIT function](..\wdfdmaenabler\nf-wdfdmaenabler-wdf-dma-system-profile-config-init.md) | The WDF_DMA_SYSTEM_PROFILE_CONFIG_INIT function initializes a driver's WDF_DMA_SYSTEM_PROFILE_CONFIG structure. |
| [WdfDmaEnablerConfigureSystemProfile function](..\wdfdmaenabler\nf-wdfdmaenabler-wdfdmaenablerconfiguresystemprofile.md) | The WdfDmaEnablerConfigureSystemProfile method configures the hardware-specific settings for a system-mode DMA enabler and completes the resource initialization. |
| [WdfDmaEnablerGetFragmentLength function](..\wdfdmaenabler\nf-wdfdmaenabler-wdfdmaenablergetfragmentlength.md) | The WdfDmaEnablerGetFragmentLength method returns the maximum transfer length that the operating system supports for a single DMA transfer. |
| [WdfDmaEnablerCreate function](..\wdfdmaenabler\nf-wdfdmaenabler-wdfdmaenablercreate.md) | The WdfDmaEnablerCreate method creates a DMA enabler object. |
| [WdfDmaEnablerGetMaximumLength function](..\wdfdmaenabler\nf-wdfdmaenabler-wdfdmaenablergetmaximumlength.md) | The WdfDmaEnablerGetMaximumLength method returns the maximum transfer length, for a single DMA transfer, that a device supports. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_WDF_DMA_ENABLER_DISABLE callback](..\wdfdmaenabler\nc-wdfdmaenabler-evt-wdf-dma-enabler-disable.md) | A driver's EvtDmaEnablerDisable event callback function disables a device's DMA capability before the device leaves its working (D0) state. |
| [EVT_WDF_DMA_ENABLER_FILL callback](..\wdfdmaenabler\nc-wdfdmaenabler-evt-wdf-dma-enabler-fill.md) | A driver's EvtDmaEnablerFill event callback function allocates a device's DMA buffers. |
| [EVT_WDF_DMA_ENABLER_SELFMANAGED_IO_START callback](..\wdfdmaenabler\nc-wdfdmaenabler-evt-wdf-dma-enabler-selfmanaged-io-start.md) | A driver's EvtDmaEnablerSelfManagedIoStart event callback function starts a DMA device's self-managed I/O operations. |
| [EVT_WDF_DMA_ENABLER_FLUSH callback](..\wdfdmaenabler\nc-wdfdmaenabler-evt-wdf-dma-enabler-flush.md) | A driver's EvtDmaEnablerFlush event callback function deallocates a device's DMA buffers. |
| [EVT_WDF_DMA_ENABLER_ENABLE callback](..\wdfdmaenabler\nc-wdfdmaenabler-evt-wdf-dma-enabler-enable.md) | A driver's EvtDmaEnablerEnable event callback function enables a device's DMA capability after the device enters its working (D0) state. |
| [EVT_WDF_DMA_ENABLER_SELFMANAGED_IO_STOP callback](..\wdfdmaenabler\nc-wdfdmaenabler-evt-wdf-dma-enabler-selfmanaged-io-stop.md) | A driver's EvtDmaEnablerSelfManagedIoStop event callback function stops a DMA device's self-managed I/O operations. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_DMA_SYSTEM_PROFILE_CONFIG structure](..\wdfdmaenabler\ns-wdfdmaenabler--wdf-dma-system-profile-config.md) | The WDF_DMA_SYSTEM_PROFILE_CONFIG structure describes the hardware-specific settings related to a system-mode DMA enabler. |
| [WDF_DMA_ENABLER_CONFIG structure](..\wdfdmaenabler\ns-wdfdmaenabler--wdf-dma-enabler-config.md) | The WDF_DMA_ENABLER_CONFIG structure supplies characteristics for a DMA enabler object. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfDmaTransactionSetChannelConfigurationCallback function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionsetchannelconfigurationcallback.md) | The WdfDmaTransactionSetChannelConfigurationCallback method registers a channel configuration event callback function for a system-mode DMA transaction. |
| [WdfDmaTransactionInitializeUsingOffset function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactioninitializeusingoffset.md) | The WdfDmaTransactionInitializeUsingOffset method initializes a specified DMA transaction by using a byte offset into an MDL chain. |
| [WdfDmaTransactionExecute function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionexecute.md) | The WdfDmaTransactionExecute method begins the execution of a specified DMA transaction. |
| [WdfDmaTransactionGetRequest function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactiongetrequest.md) | The WdfDmaTransactionGetRequest method retrieves a handle to the framework request object that is associated with a specified DMA transaction. |
| [WdfDmaTransactionSetSingleTransferRequirement function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionsetsingletransferrequirement.md) | The WdfDmaTransactionSetSingleTransferRequirement method specifies that a DMA transaction must complete in a single transfer. |
| [WdfDmaTransactionSetTransferCompleteCallback function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionsettransfercompletecallback.md) | The WdfDmaTransactionSetTransferCompleteCallback method registers a transfer completion event callback function for a system-mode DMA transaction. |
| [WdfDmaTransactionInitialize function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactioninitialize.md) | The WdfDmaTransactionInitialize method initializes a specified DMA transaction. |
| [WdfDmaTransactionGetCurrentDmaTransferLength function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactiongetcurrentdmatransferlength.md) | The WdfDmaTransactionGetCurrentDmaTransferLength method returns the size of the current DMA transfer. |
| [WdfDmaTransactionDmaCompletedFinal function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactiondmacompletedfinal.md) | The WdfDmaTransactionDmaCompletedFinal method notifies the framework that a device's DMA transfer operation has completed with an underrun condition and supplies the length of the completed transfer. |
| [WdfDmaTransactionInitializeUsingRequest function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactioninitializeusingrequest.md) | The WdfDmaTransactionInitializeUsingRequest method initializes a specified DMA transaction by using the parameters of a specified I/O request. |
| [WdfDmaTransactionFreeResources function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionfreeresources.md) | The WdfDmaTransactionFreeResources method releases DMA resources that the driver previously allocated by calling WdfDmaTransactionAllocateResources. |
| [WdfDmaTransactionRelease function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionrelease.md) | The WdfDmaTransactionRelease method terminates a specified DMA transaction without deleting the associated DMA transaction object. |
| [WdfDmaTransactionStopSystemTransfer function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionstopsystemtransfer.md) | The WdfDmaTransactionStopSystemTransfer method attempts to stop a system-mode DMA transfer after the framework has called EvtProgramDma. |
| [WdfDmaTransactionWdmGetTransferContext function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionwdmgettransfercontext.md) | The WdfDmaTransactionWdmGetTransferContext method retrieves the WDM transfer context that is associated with a DMA transaction. |
| [WdfDmaTransactionGetTransferInfo function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactiongettransferinfo.md) | The WdfDmaTransactionGetTransferInfo method returns the number of map registers and scatter/gather list entries required for an initialized DMA transaction. |
| [WdfDmaTransactionDmaCompleted function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactiondmacompleted.md) | The WdfDmaTransactionDmaCompleted method notifies the framework that a device's DMA transfer operation is completed. |
| [WdfDmaTransactionAllocateResources function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionallocateresources.md) | The WdfDmaTransactionAllocateResources method reserves a single-packet or system-mode DMA enabler for exclusive (and repeated) use with the specified transaction object. |
| [WdfDmaTransactionCancel function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactioncancel.md) | The WdfDmaTransactionCancel method attempts to cancel a DMA transaction that is waiting for the allocation of map registers. |
| [WdfDmaTransactionSetDeviceAddressOffset function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionsetdeviceaddressoffset.md) | The WdfDmaTransactionSetDeviceAddressOffset method specifies the offset of the register that the system DMA controller will access when performing the DMA operation. |
| [WdfDmaTransactionSetImmediateExecution function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionsetimmediateexecution.md) | The WdfDmaTransactionSetImmediateExecution method marks the specified DMA transaction so that calls to WdfDmaTransactionExecute and WdfDmaTransactionAllocateResources initiate the transaction immediately or fail. |
| [WdfDmaTransactionSetMaximumLength function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactionsetmaximumlength.md) | The WdfDmaTransactionSetMaximumLength method sets the maximum length for the DMA transfers that are associated with a specified DMA transaction. |
| [WdfDmaTransactionGetBytesTransferred function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactiongetbytestransferred.md) | The WdfDmaTransactionGetBytesTransferred method returns the total number of bytes that have been transferred for a specified DMA transaction. |
| [WdfDmaTransactionGetDevice function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactiongetdevice.md) | The WdfDmaTransactionGetDevice method returns a handle to the framework device object that is associated with a specified DMA transaction. |
| [WdfDmaTransactionCreate function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactioncreate.md) | The WdfDmaTransactionCreate method creates a DMA transaction. |
| [WdfDmaTransactionDmaCompletedWithLength function](..\wdfdmatransaction\nf-wdfdmatransaction-wdfdmatransactiondmacompletedwithlength.md) | The WdfDmaTransactionDmaCompletedWithLength method notifies the framework that a device's DMA transfer operation is complete and supplies the length of the completed transfer. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_WDF_DMA_TRANSACTION_CONFIGURE_DMA_CHANNEL callback](..\wdfdmatransaction\nc-wdfdmatransaction-evt-wdf-dma-transaction-configure-dma-channel.md) | A driver's EvtDmaTransactionConfigureDmaChannel event callback function configures the DMA adapter for a system-mode DMA enabler. |
| [EVT_WDF_DMA_TRANSACTION_DMA_TRANSFER_COMPLETE callback](..\wdfdmatransaction\nc-wdfdmatransaction-evt-wdf-dma-transaction-dma-transfer-complete.md) | A driver's EvtDmaTransactionDmaTransferComplete event callback function is called when the system-mode controller has completed the current DMA transfer. |
| [EVT_WDF_RESERVE_DMA callback](..\wdfdmatransaction\nc-wdfdmatransaction-evt-wdf-reserve-dma.md) | The EvtReserveDma event callback function is called when the framework has reserved resources to execute and release a transaction. Reserved resources include map registers and the WDM DMA adapter's lock. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_DPC_CONFIG_INIT function](..\wdfdpc\nf-wdfdpc-wdf-dpc-config-init.md) | The WDF_DPC_CONFIG_INIT function initializes a driver's WDF_DPC_CONFIG structure. |
| [WdfDpcEnqueue function](..\wdfdpc\nf-wdfdpc-wdfdpcenqueue.md) | The WdfDpcEnqueue method schedules the execution of a DPC object's EvtDpcFunc callback function. |
| [WdfDpcGetParentObject function](..\wdfdpc\nf-wdfdpc-wdfdpcgetparentobject.md) | The WdfDpcGetParentObject method returns the parent object of a specified DPC object. |
| [WdfDpcCancel function](..\wdfdpc\nf-wdfdpc-wdfdpccancel.md) | The WdfDpcCancel method attempts to cancel the execution of a DPC object's scheduled EvtDpcFunc callback function. |
| [WdfDpcWdmGetDpc function](..\wdfdpc\nf-wdfdpc-wdfdpcwdmgetdpc.md) | The WdfDpcWdmGetDpc method returns a pointer to the KDPC structure that is associated with a specified framework DPC object. |
| [WdfDpcCreate function](..\wdfdpc\nf-wdfdpc-wdfdpccreate.md) | The WdfDpcCreate method creates a framework DPC object and registers an EvtDpcFunc callback function. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_DPC_CONFIG structure](..\wdfdpc\ns-wdfdpc--wdf-dpc-config.md) | The WDF_DPC_CONFIG structure contains configuration information for a DPC object. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfGetDriver function](..\wdfdriver\nf-wdfdriver-wdfgetdriver.md) | The WdfGetDriver method returns a handle to the framework driver object that represents the calling driver. |
| [WdfDriverGetRegistryPath function](..\wdfdriver\nf-wdfdriver-wdfdrivergetregistrypath.md) | The WdfDriverGetRegistryPath method retrieves the path to the driver's registry key in the registry's Services tree. |
| [WdfDriverIsVersionAvailable function](..\wdfdriver\nf-wdfdriver-wdfdriverisversionavailable.md) | The WdfDriverIsVersionAvailable method returns a Boolean value that indicates whether the driver is running with a specified version of the Kernel-Mode Driver Framework library. |
| [WDF_DRIVER_CONFIG_INIT function](..\wdfdriver\nf-wdfdriver-wdf-driver-config-init.md) | The WDF_DRIVER_CONFIG_INIT function initializes a driver's WDF_DRIVER_CONFIG structure. |
| [WdfDriverRetrieveVersionString function](..\wdfdriver\nf-wdfdriver-wdfdriverretrieveversionstring.md) | The WdfDriverRetrieveVersionString method retrieves a Unicode string that identifies the version of the Kernel-Mode Driver Framework that the driver is running with. |
| [WdfDriverOpenParametersRegistryKey function](..\wdfdriver\nf-wdfdriver-wdfdriveropenparametersregistrykey.md) | The WdfDriverOpenParametersRegistryKey method opens the driver's Parameters registry key and retrieves a handle to a framework registry-key object that represents the key. |
| [WDF_DRIVER_VERSION_AVAILABLE_PARAMS_INIT function](..\wdfdriver\nf-wdfdriver-wdf-driver-version-available-params-init.md) | The WDF_DRIVER_VERSION_AVAILABLE_PARAMS_INIT function initializes a WDF_DRIVER_VERSION_AVAILABLE_PARAMS structure. |
| [WdfWdmDriverGetWdfDriverHandle function](..\wdfdriver\nf-wdfdriver-wdfwdmdrivergetwdfdriverhandle.md) | The WdfWdmDriverGetWdfDriverHandle method returns a handle to the framework driver object that is associated with a specified Windows Driver Model (WDM) driver object. |
| [WdfDriverRegisterTraceInfo function](..\wdfdriver\nf-wdfdriver-wdfdriverregistertraceinfo.md) | The WdfDriverRegisterTraceInfo method is reserved for internal use only. |
| [WdfDriverWdmGetDriverObject function](..\wdfdriver\nf-wdfdriver-wdfdriverwdmgetdriverobject.md) | The WdfDriverWdmGetDriverObject method retrieves a pointer to the Windows Driver Model (WDM) driver object that is associated with a specified framework driver object. |
| [WdfDriverCreate function](..\wdfdriver\nf-wdfdriver-wdfdrivercreate.md) | The WdfDriverCreate method creates a framework driver object for the calling driver. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_DRIVER_VERSION_AVAILABLE_PARAMS structure](..\wdfdriver\ns-wdfdriver--wdf-driver-version-available-params.md) | The WDF_DRIVER_VERSION_AVAILABLE_PARAMS structure specifies major and minor version numbers for the Kernel-Mode Driver Framework's library. |
| [WDF_DRIVER_CONFIG structure](..\wdfdriver\ns-wdfdriver--wdf-driver-config.md) | The WDF_DRIVER_CONFIG structure is an input parameter to WdfDriverCreate. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_DRIVER_INIT_FLAGS enumeration](..\wdfdriver\ne-wdfdriver--wdf-driver-init-flags.md) | The WDF_DRIVER_INIT_FLAGS enumeration specifies driver initialization flags. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_WDF_DRIVER_UNLOAD callback](..\wdfdriver\nc-wdfdriver-evt-wdf-driver-unload.md) | A driver's EvtDriverUnload event callback function performs operations that must take place before the driver is unloaded. |
| [EVT_WDF_DRIVER_DEVICE_ADD callback](..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md) | A driver's EvtDriverDeviceAdd event callback function performs device initialization operations when the Plug and Play (PnP) manager reports the existence of a device. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfFdoInitSetFilter function](..\wdffdo\nf-wdffdo-wdffdoinitsetfilter.md) | The WdfFdoInitSetFilter method identifies the calling driver as an upper-level or lower-level filter driver, for a specified device. |
| [WdfFdoAddStaticChild function](..\wdffdo\nf-wdffdo-wdffdoaddstaticchild.md) | The WdfFdoAddStaticChild method adds a specified device to a function driver's list of child devices that have been identified by static enumeration. |
| [WdfFdoUnlockStaticChildListFromIteration function](..\wdffdo\nf-wdffdo-wdffdounlockstaticchildlistfromiteration.md) | The WdfFdoUnlockStaticChildListFromIteration method unlocks the list of child devices for a specified device and processes any changes to the list that the driver made while the list was locked. |
| [WDF_FDO_EVENT_CALLBACKS_INIT function](..\wdffdo\nf-wdffdo-wdf-fdo-event-callbacks-init.md) | The WDF_FDO_EVENT_CALLBACKS_INIT function initializes a WDF_FDO_EVENT_CALLBACKS structure. |
| [WdfFdoInitSetDefaultChildListConfig function](..\wdffdo\nf-wdffdo-wdffdoinitsetdefaultchildlistconfig.md) | The WdfFdoInitSetDefaultChildListConfig method configures a bus driver's default child list. |
| [WdfFdoRetrieveNextStaticChild function](..\wdffdo\nf-wdffdo-wdffdoretrievenextstaticchild.md) | The WdfFdoRetrieveNextStaticChild method retrieves a handle to the next framework device object in a list of child devices. |
| [WdfFdoInitQueryProperty function](..\wdffdo\nf-wdffdo-wdffdoinitqueryproperty.md) | The WdfFdoInitQueryProperty method retrieves a specified device property. |
| [WdfFdoGetDefaultChildList function](..\wdffdo\nf-wdffdo-wdffdogetdefaultchildlist.md) | The WdfFdoGetDefaultChildList method returns a handle to a specified device's default child list. |
| [WdfFdoInitSetEventCallbacks function](..\wdffdo\nf-wdffdo-wdffdoinitseteventcallbacks.md) | The WdfFdoInitSetEventCallbacks method registers a framework-based function driver's event callback functions, for a specified device. |
| [WdfFdoInitOpenRegistryKey function](..\wdffdo\nf-wdffdo-wdffdoinitopenregistrykey.md) | The WdfFdoInitOpenRegistryKey method opens a device's hardware key or a driver's software key in the registry and creates a framework registry-key object that represents the registry key. |
| [WdfFdoInitWdmGetPhysicalDevice function](..\wdffdo\nf-wdffdo-wdffdoinitwdmgetphysicaldevice.md) | The WdfFdoInitWdmGetPhysicalDevice method retrieves a device's WDM physical device object (PDO). |
| [WdfFdoQueryForInterface function](..\wdffdo\nf-wdffdo-wdffdoqueryforinterface.md) | The WdfFdoQueryForInterface method obtains access to another driver's GUID-identified interface. |
| [WdfFdoInitAllocAndQueryProperty function](..\wdffdo\nf-wdffdo-wdffdoinitallocandqueryproperty.md) | The WdfFdoInitAllocAndQueryProperty method allocates a buffer and retrieves a specified device property. |
| [WdfFdoInitQueryPropertyEx function](..\wdffdo\nf-wdffdo-wdffdoinitquerypropertyex.md) | The WdfFdoInitQueryPropertyEx method retrieves a specified device property. |
| [WdfFdoInitAllocAndQueryPropertyEx function](..\wdffdo\nf-wdffdo-wdffdoinitallocandquerypropertyex.md) | The WdfFdoInitAllocAndQueryPropertyEx method allocates a buffer and retrieves a specified device property. |
| [WdfFdoLockStaticChildListForIteration function](..\wdffdo\nf-wdffdo-wdffdolockstaticchildlistforiteration.md) | The WdfFdoLockStaticChildListForIteration method prepares the framework for retrieving items from the static child list that belongs to a specified parent device. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_WDF_DEVICE_REMOVE_ADDED_RESOURCES callback](..\wdffdo\nc-wdffdo-evt-wdf-device-remove-added-resources.md) | A driver's EvtDeviceRemoveAddedResources event callback function removes hardware resources that the driver's EvtDeviceFilterAddResourceRequirements callback function added. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_FDO_EVENT_CALLBACKS structure](..\wdffdo\ns-wdffdo--wdf-fdo-event-callbacks.md) | The WDF_FDO_EVENT_CALLBACKS structure contains pointers to a function driver's PnP event callback functions. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfFileObjectWdmGetFileObject function](..\wdffileobject\nf-wdffileobject-wdffileobjectwdmgetfileobject.md) | The WdfFileObjectWdmGetFileObject method returns the Windows Driver Model (WDM) file object that is associated with a specified framework file object. |
| [WdfFileObjectGetRelatedFileObject function](..\wdffileobject\nf-wdffileobject-wdffileobjectgetrelatedfileobject.md) | The WdfFileObjectGetRelatedFileObject method retrieves the related file object to a framework file object. |
| [WdfFileObjectGetFileName function](..\wdffileobject\nf-wdffileobject-wdffileobjectgetfilename.md) | The WdfFileObjectGetFileName method returns the file name that a specified framework file object contains. |
| [WdfFileObjectGetInitiatorProcessId function](..\wdffileobject\nf-wdffileobject-wdffileobjectgetinitiatorprocessid.md) | The WdfFileObjectGetInitiatorProcessId function retrieves the initiator process ID that is associated with a specified framework file object. |
| [WdfFileObjectGetFlags function](..\wdffileobject\nf-wdffileobject-wdffileobjectgetflags.md) | The WdfFileObjectGetFlags method returns the flags that a specified framework file object contains. |
| [WdfFileObjectGetDevice function](..\wdffileobject\nf-wdffileobject-wdffileobjectgetdevice.md) | The WdfFileObjectGetDevice method returns the framework device object that is associated with a specified framework file object. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_FILE_INFORMATION_CLASS enumeration](..\wdffileobject\ne-wdffileobject--wdf-file-information-class.md) | The WDF_FILE_INFORMATION_CLASS enumeration identifies the types of file information that a driver can obtain or set. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_READ_REGISTER_BUFFER_ULONG64 function](..\wdfhwaccess\nf-wdfhwaccess-wdf-read-register-buffer-ulong64.md) | The WDF_READ_REGISTER_BUFFER_ULONG64 function reads a number of ULONG64 values from the specified register address into a buffer. |
| [WDF_READ_REGISTER_USHORT function](..\wdfhwaccess\nf-wdfhwaccess-wdf-read-register-ushort.md) | The WDF_READ_REGISTER_USHORT function reads a USHORT value from the specified register address. |
| [WDF_READ_PORT_ULONG function](..\wdfhwaccess\nf-wdfhwaccess-wdf-read-port-ulong.md) | The WDF_READ_PORT_ULONG function reads a ULONG value from the specified port address. |
| [WDF_READ_REGISTER_BUFFER_USHORT function](..\wdfhwaccess\nf-wdfhwaccess-wdf-read-register-buffer-ushort.md) | The WDF_READ_REGISTER_BUFFER_USHORT function reads a number of USHORT values from the specified register address into a buffer. |
| [WDF_WRITE_REGISTER_BUFFER_ULONG64 function](..\wdfhwaccess\nf-wdfhwaccess-wdf-write-register-buffer-ulong64.md) | The WDF_WRITE_REGISTER_BUFFER_ULONG64 function writes a number of ULONG64 values from a buffer to the specified register. |
| [WDF_READ_REGISTER_UCHAR function](..\wdfhwaccess\nf-wdfhwaccess-wdf-read-register-uchar.md) | The WDF_READ_REGISTER_UCHAR function reads a byte from the specified register address. |
| [WDF_WRITE_REGISTER_ULONG64 function](..\wdfhwaccess\nf-wdfhwaccess-wdf-write-register-ulong64.md) | The WDF_WRITE_REGISTER_ULONG64 function writes a ULONG64 value to the specified address. |
| [WDF_WRITE_REGISTER_UCHAR function](..\wdfhwaccess\nf-wdfhwaccess-wdf-write-register-uchar.md) | The WDF_WRITE_REGISTER_UCHAR routine writes a byte to the specified address. |
| [WDF_WRITE_PORT_ULONG function](..\wdfhwaccess\nf-wdfhwaccess-wdf-write-port-ulong.md) | The WDF_WRITE_PORT_ULONG function writes a ULONG value to the specified port address. |
| [WDF_READ_PORT_BUFFER_UCHAR function](..\wdfhwaccess\nf-wdfhwaccess-wdf-read-port-buffer-uchar.md) | The WDF_READ_PORT_BUFFER_UCHAR function reads a number of bytes from the specified port address into a buffer. |
| [WDF_READ_PORT_UCHAR function](..\wdfhwaccess\nf-wdfhwaccess-wdf-read-port-uchar.md) | The WDF_READ_PORT_UCHAR function reads a byte from the specified port address. |
| [WDF_READ_REGISTER_BUFFER_UCHAR function](..\wdfhwaccess\nf-wdfhwaccess-wdf-read-register-buffer-uchar.md) | The WDF_READ_REGISTER_BUFFER_UCHAR function reads a number of bytes from the specified register address into a buffer. |
| [WDF_WRITE_REGISTER_BUFFER_UCHAR function](..\wdfhwaccess\nf-wdfhwaccess-wdf-write-register-buffer-uchar.md) | The WDF_WRITE_REGISTER_BUFFER_UCHAR function writes a number of bytes from a buffer to the specified register. |
| [WDF_WRITE_PORT_BUFFER_ULONG function](..\wdfhwaccess\nf-wdfhwaccess-wdf-write-port-buffer-ulong.md) | The WDF_WRITE_PORT_BUFFER_ULONG function writes a number of ULONG values from a buffer to the specified port address. |
| [WDF_READ_REGISTER_ULONG function](..\wdfhwaccess\nf-wdfhwaccess-wdf-read-register-ulong.md) | The WDF_READ_REGISTER_ULONG function reads a ULONG value from the specified register address. |
| [WDF_READ_PORT_USHORT function](..\wdfhwaccess\nf-wdfhwaccess-wdf-read-port-ushort.md) | The WDF_READ_PORT_USHORT function reads a USHORT value from the specified port address. |
| [WDF_WRITE_PORT_USHORT function](..\wdfhwaccess\nf-wdfhwaccess-wdf-write-port-ushort.md) | The WDF_WRITE_PORT_USHORT function writes a USHORT value to the specified port address. |
| [WDF_READ_REGISTER_BUFFER_ULONG function](..\wdfhwaccess\nf-wdfhwaccess-wdf-read-register-buffer-ulong.md) | The WDF_READ_REGISTER_BUFFER_ULONG function reads a number of ULONG values from the specified register address into a buffer. |
| [WDF_WRITE_PORT_BUFFER_UCHAR function](..\wdfhwaccess\nf-wdfhwaccess-wdf-write-port-buffer-uchar.md) | The WDF_WRITE_PORT_BUFFER_UCHAR function writes a number of bytes from a buffer to the specified port. |
| [WDF_WRITE_REGISTER_BUFFER_USHORT function](..\wdfhwaccess\nf-wdfhwaccess-wdf-write-register-buffer-ushort.md) | The WDF_WRITE_REGISTER_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified register. |
| [WDF_READ_PORT_BUFFER_ULONG function](..\wdfhwaccess\nf-wdfhwaccess-wdf-read-port-buffer-ulong.md) | The WDF_READ_PORT_BUFFER_ULONG function reads a number of ULONG values from the specified port address into a buffer. |
| [WDF_WRITE_REGISTER_ULONG function](..\wdfhwaccess\nf-wdfhwaccess-wdf-write-register-ulong.md) | The WDF_WRITE_REGISTER_ULONG routine writes a ULONG value to the specified address. |
| [WDF_WRITE_PORT_BUFFER_USHORT function](..\wdfhwaccess\nf-wdfhwaccess-wdf-write-port-buffer-ushort.md) | The WDF_WRITE_PORT_BUFFER_USHORT function writes a number of USHORT values from a buffer to the specified port address. |
| [WDF_READ_REGISTER_ULONG64 function](..\wdfhwaccess\nf-wdfhwaccess-wdf-read-register-ulong64.md) | The WDF_READ_REGISTER_ULONG64 function reads a ULONG64 value from the specified register address. |
| [WDF_READ_PORT_BUFFER_USHORT function](..\wdfhwaccess\nf-wdfhwaccess-wdf-read-port-buffer-ushort.md) | The WDF_READ_PORT_BUFFER_USHORT function reads a number of USHORT values from the specified port address into a buffer. |
| [WDF_WRITE_PORT_UCHAR function](..\wdfhwaccess\nf-wdfhwaccess-wdf-write-port-uchar.md) | The WDF_WRITE_PORT_UCHAR function writes a byte to the specified port address. |
| [WDF_WRITE_REGISTER_BUFFER_ULONG function](..\wdfhwaccess\nf-wdfhwaccess-wdf-write-register-buffer-ulong.md) | The WDF_WRITE_REGISTER_BUFFER_ULONG function writes a number of ULONG values from a buffer to the specified register. |
| [WDF_WRITE_REGISTER_USHORT function](..\wdfhwaccess\nf-wdfhwaccess-wdf-write-register-ushort.md) | The WDF_WRITE_REGISTER_USHORT routine writes a USHORT value to the specified address. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfPostDeviceInstall function](..\wdfinstaller\nf-wdfinstaller-wdfpostdeviceinstall.md) | The co-installer's WdfPostDeviceInstall function performs any operations that the co-installer might require after a non-Plug and Play (PnP) driver's installer has created the driver's kernel-mode service. |
| [WdfPreDeviceInstall function](..\wdfinstaller\nf-wdfinstaller-wdfpredeviceinstall.md) | The co-installer's WdfPreDeviceInstall function performs any operations that the co-installer might require before a non-Plug and Play (PnP) driver's installer creates the driver's kernel-mode service. |
| [WdfPreDeviceRemove function](..\wdfinstaller\nf-wdfinstaller-wdfpredeviceremove.md) | The co-installer's WdfPreDeviceRemove function performs any operations that the co-installer might require before a non-Plug and Play (PnP) driver's installer deletes the driver's kernel-mode service. |
| [WdfPostDeviceRemove function](..\wdfinstaller\nf-wdfinstaller-wdfpostdeviceremove.md) | The co-installer's WdfPostDeviceRemove function performs any operations that the co-installer might require after a non-Plug and Play (PnP) driver's installer has deleted the driver's kernel-mode service. |
| [WDF_COINSTALLER_INSTALL_OPTIONS_INIT function](..\wdfinstaller\nf-wdfinstaller-wdf-coinstaller-install-options-init.md) | The WDF_COINSTALLER_INSTALL_OPTIONS_INIT function initializes a WDF_COINSTALLER_INSTALL_OPTIONS structure. |
| [WdfPreDeviceInstallEx function](..\wdfinstaller\nf-wdfinstaller-wdfpredeviceinstallex.md) | The co-installer's WdfPreDeviceInstallEx function performs any operations that the co-installer might require before a non-Plug and Play (PnP) driver's installer creates the driver's kernel-mode service. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_COINSTALLER_INSTALL_OPTIONS structure](..\wdfinstaller\ns-wdfinstaller--wdf-coinstaller-install-options.md) | The WDF_COINSTALLER_INSTALL_OPTIONS structure contains installation options that a framework-based driver's installer can specify to the framework's co-installer. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_WDF_INTERRUPT_DPC callback](..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-dpc.md) | A driver's EvtInterruptDpc event callback function processes interrupt information that the driver's EvtInterruptIsr callback function has stored. |
| [EVT_WDF_INTERRUPT_SYNCHRONIZE callback](..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-synchronize.md) | A driver's EvtInterruptSynchronize event callback function performs operations that must be synchronized with an EvtInterruptIsr callback function. |
| [EVT_WDF_INTERRUPT_ISR callback](..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-isr.md) | A driver's EvtInterruptIsr event callback function services a hardware interrupt. |
| [EVT_WDF_INTERRUPT_ENABLE callback](..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-enable.md) | A driver's EvtInterruptEnable event callback function enables a specified hardware interrupt. |
| [EVT_WDF_INTERRUPT_WORKITEM callback](..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-workitem.md) | A driver's EvtInterruptWorkItem event callback function processes interrupt information that the driver's EvtInterruptIsr callback function has stored. |
| [EVT_WDF_INTERRUPT_DISABLE callback](..\wdfinterrupt\nc-wdfinterrupt-evt-wdf-interrupt-disable.md) | A driver's EvtInterruptDisable event callback function disables a specified hardware interrupt. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfInterruptSetExtendedPolicy function](..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptsetextendedpolicy.md) | The WdfInterruptSetExtendedPolicy method specifies the interrupt priority, processor affinity, affinity policy, and processor group for a specified interrupt. |
| [WDF_INTERRUPT_CONFIG_INIT function](..\wdfinterrupt\nf-wdfinterrupt-wdf-interrupt-config-init.md) | The WDF_INTERRUPT_CONFIG_INIT function initializes a WDF_INTERRUPT_CONFIG structure. |
| [WdfInterruptWdmGetInterrupt function](..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptwdmgetinterrupt.md) | The WdfInterruptWdmGetInterrupt method returns a pointer to the WDM interrupt object that is associated with a specified framework interrupt object. |
| [WdfInterruptReportActive function](..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptreportactive.md) | The WdfInterruptReportActive informs the system that the interrupt is active and the driver is ready to process interrupt requests on the associated lines. |
| [WdfInterruptQueueDpcForIsr function](..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptqueuedpcforisr.md) | The WdfInterruptQueueDpcForIsr method queues a framework interrupt object's EvtInterruptDpc callback function for execution. |
| [WdfInterruptTryToAcquireLock function](..\wdfinterrupt\nf-wdfinterrupt-wdfinterrupttrytoacquirelock.md) | The WdfInterruptTryToAcquireLock method attempts to acquire an interrupt object's passive lock. |
| [WdfInterruptQueueWorkItemForIsr function](..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptqueueworkitemforisr.md) | The WdfInterruptQueueWorkItemForIsr method queues a framework interrupt object's EvtInterruptWorkItem callback function for execution. |
| [WdfInterruptDisable function](..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptdisable.md) | The WdfInterruptDisable method disables a specified device interrupt by calling the driver's EvtInterruptDisable callback function. |
| [WdfInterruptEnable function](..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptenable.md) | The WdfInterruptEnable method enables a specified device interrupt by calling the driver's EvtInterruptEnable callback function. |
| [WdfInterruptGetInfo function](..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptgetinfo.md) | The WdfInterruptGetInfo method retrieves information about a specified interrupt. |
| [WDF_INTERRUPT_EXTENDED_POLICY_INIT function](..\wdfinterrupt\nf-wdfinterrupt-wdf-interrupt-extended-policy-init.md) | The WDF_INTERRUPT_EXTENDED_POLICY_INIT function initializes a WDF_INTERRUPT_EXTENDED_POLICY structure. |
| [WdfInterruptReportInactive function](..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptreportinactive.md) | The WdfInterruptReportInactive method informs the system that the interrupt is no longer active and the driver is not expecting interrupt requests on the associated lines. |
| [WdfInterruptCreate function](..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptcreate.md) | The WdfInterruptCreate method creates a framework interrupt object. |
| [WdfInterruptSynchronize function](..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptsynchronize.md) | The WdfInterruptSynchronize method executes a specified callback function at the device's DIRQL while holding an interrupt object's spin lock. |
| [WDF_INTERRUPT_INFO_INIT function](..\wdfinterrupt\nf-wdfinterrupt-wdf-interrupt-info-init.md) | The WDF_INTERRUPT_INFO_INIT function initializes a WDF_INTERRUPT_INFO structure. |
| [WdfInterruptSetPolicy function](..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptsetpolicy.md) | The WdfInterruptSetPolicy method specifies the interrupt priority, processor affinity, and affinity policy for a specified interrupt. |
| [WdfInterruptGetDevice function](..\wdfinterrupt\nf-wdfinterrupt-wdfinterruptgetdevice.md) | The WdfInterruptGetDevice method returns a handle to the framework device object that is associated with a specified framework interrupt object. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_INTERRUPT_INFO structure](..\wdfinterrupt\ns-wdfinterrupt--wdf-interrupt-info.md) | The WDF_INTERRUPT_INFO structure contains information about a device's interrupt resource. |
| [WDF_INTERRUPT_EXTENDED_POLICY structure](..\wdfinterrupt\ns-wdfinterrupt--wdf-interrupt-extended-policy.md) | The WDF_INTERRUPT_EXTENDED_POLICY structure contains information about an interrupt's policy, priority, affinity, and group. |
| [WDF_INTERRUPT_CONFIG structure](..\wdfinterrupt\ns-wdfinterrupt--wdf-interrupt-config.md) | The WDF_INTERRUPT_CONFIG structure contains configuration information for a device interrupt. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_INTERRUPT_PRIORITY enumeration](..\wdfinterrupt\ne-wdfinterrupt--wdf-interrupt-priority.md) | The WDF_INTERRUPT_PRIORITY enumeration type identifies relative priorities for device interrupts. |
| [WDF_INTERRUPT_POLICY enumeration](..\wdfinterrupt\ne-wdfinterrupt--wdf-interrupt-policy.md) | The WDF_INTERRUPT_POLICY enumeration type identifies the affinity policies that the PnP manager can use when it assigns a device's interrupts to the processors of a multiprocessor system. |
| [WDF_INTERRUPT_POLARITY enumeration](..\wdfinterrupt\ne-wdfinterrupt--wdf-interrupt-polarity.md) | The WDF_INTERRUPT_POLARITY enumeration type is used to specify an interrupt signal's polarity. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfIoQueueStopSynchronously function](..\wdfio\nf-wdfio-wdfioqueuestopsynchronously.md) | The WdfIoQueueStopSynchronously method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests. The method returns after all delivered requests have been canceled or completed. |
| [WDF_IO_QUEUE_DRAINED function](..\wdfio\nf-wdfio-wdf-io-queue-drained.md) | The WDF_IO_QUEUE_DRAINED function returns TRUE if the I/O queue's state indicates that the queue is drained. |
| [WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY_DEFAULT_INIT function](..\wdfio\nf-wdfio-wdf-io-queue-forward-progress-policy-default-init.md) | The WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY_DEFAULT_INIT function initializes a driver's WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY structure. |
| [WDF_IO_QUEUE_READY function](..\wdfio\nf-wdfio-wdf-io-queue-ready.md) | The WDF_IO_QUEUE_READY function returns TRUE if an I/O queue's state indicates that the queue is drained. |
| [WdfIoQueueRetrieveNextRequest function](..\wdfio\nf-wdfio-wdfioqueueretrievenextrequest.md) | The WdfIoQueueRetrieveNextRequest method retrieves the next available I/O request from a specified I/O queue. |
| [WDF_IO_QUEUE_PURGED function](..\wdfio\nf-wdfio-wdf-io-queue-purged.md) | The WDF_IO_QUEUE_PURGED function returns TRUE if an I/O queue's state indicates that the queue is drained. |
| [WdfIoQueueAssignForwardProgressPolicy function](..\wdfio\nf-wdfio-wdfioqueueassignforwardprogresspolicy.md) | The WdfIoQueueAssignForwardProgressPolicy method enables the framework's ability to guarantee forward progress for a specified I/O queue. |
| [WdfIoQueueStopAndPurgeSynchronously function](..\wdfio\nf-wdfio-wdfioqueuestopandpurgesynchronously.md) | The WdfIoQueueStopAndPurgeSynchronously method prevents an I/O queue from delivering new I/O requests and causes the framework to cancel existing unprocessed requests and driver-owned cancellable requests, but the queue receives and stores new requests. |
| [WdfIoQueueFindRequest function](..\wdfio\nf-wdfio-wdfioqueuefindrequest.md) | The WdfIoQueueFindRequest method locates the next request in an I/O queue, or the next request that matches specified criteria, but does not grant ownership of the request to the driver. |
| [WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY_PAGINGIO_INIT function](..\wdfio\nf-wdfio-wdf-io-queue-forward-progress-policy-pagingio-init.md) | The WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY_PAGINGIO_INIT function initializes a driver's WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY structure. |
| [WdfIoQueueDrain function](..\wdfio\nf-wdfio-wdfioqueuedrain.md) | The WdfIoQueueDrain method causes the framework to stop queuing I/O requests to an I/O queue, while allowing already-queued requests to be delivered and processed. |
| [WdfIoQueueGetDevice function](..\wdfio\nf-wdfio-wdfioqueuegetdevice.md) | The WdfIoQueueGetDevice method returns a handle to the framework device object that a specified I/O queue belongs to. |
| [WDF_IO_QUEUE_CONFIG_INIT_DEFAULT_QUEUE function](..\wdfio\nf-wdfio-wdf-io-queue-config-init-default-queue.md) | The WDF_IO_QUEUE_CONFIG_INIT_DEFAULT_QUEUE function initializes a driver's WDF_IO_QUEUE_CONFIG structure. |
| [WDF_IO_QUEUE_CONFIG_INIT function](..\wdfio\nf-wdfio-wdf-io-queue-config-init.md) | The WDF_IO_QUEUE_CONFIG_INIT function initializes a driver's WDF_IO_QUEUE_CONFIG structure. |
| [WdfIoQueueRetrieveRequestByFileObject function](..\wdfio\nf-wdfio-wdfioqueueretrieverequestbyfileobject.md) | The WdfIoQueueRetrieveRequestByFileObject method retrieves the next available I/O request, from a specified I/O queue, that is associated with a specified file object. |
| [WDF_IO_QUEUE_IDLE function](..\wdfio\nf-wdfio-wdf-io-queue-idle.md) | The WDF_IO_QUEUE_IDLE function returns TRUE if an I/O queue's state indicates that the queue is drained. |
| [WdfIoQueueGetState function](..\wdfio\nf-wdfio-wdfioqueuegetstate.md) | The WdfIoQueueGetState method returns the status of a specified I/O queue. |
| [WdfIoQueuePurgeSynchronously function](..\wdfio\nf-wdfio-wdfioqueuepurgesynchronously.md) | The WdfIoQueuePurgeSynchronously method causes the framework to stop queuing I/O requests to an I/O queue and to cancel unprocessed requests and driver-owned cancellable requests. |
| [WdfIoQueuePurge function](..\wdfio\nf-wdfio-wdfioqueuepurge.md) | The WdfIoQueuePurge method causes the framework to stop queuing I/O requests to an I/O queue and to cancel unprocessed requests. |
| [WdfIoQueueCreate function](..\wdfio\nf-wdfio-wdfioqueuecreate.md) | The WdfIoQueueCreate method creates and configures an I/O queue for a specified device. |
| [WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY_EXAMINE_INIT function](..\wdfio\nf-wdfio-wdf-io-queue-forward-progress-policy-examine-init.md) | The WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY_EXAMINE_INIT function initializes a driver's WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY structure. |
| [WdfIoQueueStart function](..\wdfio\nf-wdfio-wdfioqueuestart.md) | The WdfIoQueueStart method enables an I/O queue to start receiving and delivering new I/O requests. |
| [WdfIoQueueReadyNotify function](..\wdfio\nf-wdfio-wdfioqueuereadynotify.md) | The WdfIoQueueReadyNotify method registers (or deregisters) an event callback function that the framework calls each time a specified I/O queue that was previously empty receives one or more I/O requests. |
| [WDF_IO_QUEUE_STOPPED function](..\wdfio\nf-wdfio-wdf-io-queue-stopped.md) | The WDF_IO_QUEUE_STOPPED function returns TRUE if an I/O queue's state indicates that the queue is stopped. |
| [WdfIoQueueStopAndPurge function](..\wdfio\nf-wdfio-wdfioqueuestopandpurge.md) | The WdfIoQueueStopAndPurge method prevents an I/O queue from delivering new requests and cancels existing unprocessed requests and driver-owned cancellable requests, but the queue receives and stores new requests. |
| [WdfIoQueueStop function](..\wdfio\nf-wdfio-wdfioqueuestop.md) | The WdfIoQueueStop method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests. |
| [WdfIoQueueDrainSynchronously function](..\wdfio\nf-wdfio-wdfioqueuedrainsynchronously.md) | The WdfIoQueueDrainSynchronously method causes the framework to stop queuing I/O requests to an I/O queue, while allowing already-queued requests to be delivered and processed. The method returns after all requests are completed or canceled. |
| [WdfIoQueueRetrieveFoundRequest function](..\wdfio\nf-wdfio-wdfioqueueretrievefoundrequest.md) | The WdfIoQueueRetrieveFoundRequest method delivers a specified request to the driver, so that the driver can process the request. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_WDF_IO_QUEUE_IO_CANCELED_ON_QUEUE callback](..\wdfio\nc-wdfio-evt-wdf-io-queue-io-canceled-on-queue.md) | A driver's EvtIoCanceledOnQueue event callback function informs the driver that it must complete an I/O request that the framework has removed from an I/O queue. |
| [EVT_WDF_IO_QUEUE_IO_WRITE callback](..\wdfio\nc-wdfio-evt-wdf-io-queue-io-write.md) | A driver's EvtIoWrite event callback function processes a specified write request. |
| [EVT_WDF_IO_QUEUE_IO_DEVICE_CONTROL callback](..\wdfio\nc-wdfio-evt-wdf-io-queue-io-device-control.md) | A driver's EvtIoDeviceControl event callback function processes a specified device I/O control request. |
| [EVT_WDF_IO_QUEUE_IO_RESUME callback](..\wdfio\nc-wdfio-evt-wdf-io-queue-io-resume.md) | A driver's EvtIoResume event callback function resumes processing a specified I/O request after the underlying device returns to its working (D0) power state. |
| [EVT_WDF_IO_ALLOCATE_REQUEST_RESOURCES callback](..\wdfio\nc-wdfio-evt-wdf-io-allocate-request-resources.md) | A driver's EvtIoAllocateRequestResources callback function allocates request-specific resources that the driver requires to process the specified request. |
| [EVT_WDF_IO_QUEUE_IO_DEFAULT callback](..\wdfio\nc-wdfio-evt-wdf-io-queue-io-default.md) | A driver's EvtIoDefault event callback function processes a specified I/O request. |
| [EVT_WDF_IO_QUEUE_IO_INTERNAL_DEVICE_CONTROL callback](..\wdfio\nc-wdfio-evt-wdf-io-queue-io-internal-device-control.md) | A driver's EvtIoInternalDeviceControl event callback function processes an I/O request that contains an internal device I/O control code (IOCTL). |
| [EVT_WDF_IO_QUEUE_IO_STOP callback](..\wdfio\nc-wdfio-evt-wdf-io-queue-io-stop.md) | A driver's EvtIoStop event callback function completes, requeues, or suspends processing of a specified request because the request's I/O queue is being stopped. |
| [EVT_WDF_IO_QUEUE_STATE callback](..\wdfio\nc-wdfio-evt-wdf-io-queue-state.md) | A driver's EvtIoQueueState event callback function delivers queue state information to the driver. |
| [EVT_WDF_IO_WDM_IRP_FOR_FORWARD_PROGRESS callback](..\wdfio\nc-wdfio-evt-wdf-io-wdm-irp-for-forward-progress.md) | A driver's EvtIoWdmIrpForForwardProgress callback function examines an I/O request packet (IRP) and determines whether to use a reserved request object to process the I/O request or to fail the I/O request. |
| [EVT_WDF_IO_ALLOCATE_RESOURCES_FOR_RESERVED_REQUEST callback](..\wdfio\nc-wdfio-evt-wdf-io-allocate-resources-for-reserved-request.md) | A driver's EvtIoAllocateResourcesForReservedRequest callback function allocates request-specific resources that the driver can use to process an I/O request in the future. |
| [EVT_WDF_IO_QUEUE_IO_READ callback](..\wdfio\nc-wdfio-evt-wdf-io-queue-io-read.md) | A driver's EvtIoRead event callback function processes a specified read request. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_IO_FORWARD_PROGRESS_ACTION enumeration](..\wdfio\ne-wdfio--wdf-io-forward-progress-action.md) | The WDF_IO_FORWARD_PROGRESS_ACTION enumeration identifies actions that the framework can take for an I/O request packet (IRP) that your driver examines during a low-memory situation. |
| [WDF_IO_QUEUE_DISPATCH_TYPE enumeration](..\wdfio\ne-wdfio--wdf-io-queue-dispatch-type.md) | The WDF_IO_QUEUE_DISPATCH_TYPE enumeration type identifies the request dispatching methods that can be associated with a framework queue object. |
| [WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY enumeration](..\wdfio\ne-wdfio--wdf-io-forward-progress-reserved-policy.md) | The WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY enumeration identifies actions that the framework can take when it receives an I/O request for your driver, if a low-memory situation exists. |
| [WDF_IO_QUEUE_STATE enumeration](..\wdfio\ne-wdfio--wdf-io-queue-state.md) | The WDF_IO_QUEUE_STATE enumeration type identifies the status of a framework queue object. The enumerators are used as bit masks. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_IO_QUEUE_CONFIG structure](..\wdfio\ns-wdfio--wdf-io-queue-config.md) | The WDF_IO_QUEUE_CONFIG structure contains configuration information for a framework queue object. |
| [WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY structure](..\wdfio\ns-wdfio--wdf-io-queue-forward-progress-policy.md) | The WDF_IO_QUEUE_FORWARD_PROGRESS_POLICY structure contains driver-supplied information that the framework uses to enable guaranteed forward progress for an I/O queue. |
| [WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY_SETTINGS structure](..\wdfio\ns-wdfio--wdf-io-forward-progress-reserved-policy-settings.md) | The WDF_IO_FORWARD_PROGRESS_RESERVED_POLICY_SETTINGS structure contains information about specific actions that the framework can take when it receives an I/O request for your driver, if a low-memory situation exists. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_WDF_IO_TARGET_QUERY_REMOVE callback](..\wdfiotarget\nc-wdfiotarget-evt-wdf-io-target-query-remove.md) | A driver's EvtIoTargetQueryRemove event callback function indicates whether the framework can safely remove a specified remote I/O target's device. |
| [EVT_WDF_IO_TARGET_REMOVE_CANCELED callback](..\wdfiotarget\nc-wdfiotarget-evt-wdf-io-target-remove-canceled.md) | A driver's EvtIoTargetRemoveCanceled event callback function performs operations when the removal of a specified remote I/O target is canceled. |
| [EVT_WDF_IO_TARGET_REMOVE_COMPLETE callback](..\wdfiotarget\nc-wdfiotarget-evt-wdf-io-target-remove-complete.md) | A driver's EvtIoTargetRemoveComplete event callback function performs operations when the removal of a specified remote I/O target is complete. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_IO_TARGET_OPEN_TYPE enumeration](..\wdfiotarget\ne-wdfiotarget--wdf-io-target-open-type.md) | The WDF_IO_TARGET_OPEN_TYPE enumeration specifies how a driver identifies a remote I/O target when the driver calls WdfIoTargetOpen. |
| [WDF_IO_TARGET_SENT_IO_ACTION enumeration](..\wdfiotarget\ne-wdfiotarget--wdf-io-target-sent-io-action.md) | The WDF_IO_TARGET_SENT_IO_ACTION enumeration identifies the actions that the framework can take when a driver calls WdfIoTargetStop to stop an I/O target. |
| [WDF_IO_TARGET_STATE enumeration](..\wdfiotarget\ne-wdfiotarget--wdf-io-target-state.md) | The WDF_IO_TARGET_STATE enumeration specifies the states that an I/O target can be in. |
| [WDF_IO_TARGET_PURGE_IO_ACTION enumeration](..\wdfiotarget\ne-wdfiotarget--wdf-io-target-purge-io-action.md) | The WDF_IO_TARGET_PURGE_IO_ACTION enumeration identifies the actions that the framework can take when a driver calls WdfIoTargetPurge to purge an I/O target. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfIoTargetGetState function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetgetstate.md) | The WdfIoTargetGetState method returns state information for a local or remote I/O target. |
| [WdfIoTargetOpen function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetopen.md) | The WdfIoTargetOpen method opens a remote I/O target so the driver can send I/O requests to it. |
| [WdfIoTargetWdmGetTargetFileHandle function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetwdmgettargetfilehandle.md) | The WdfIoTargetWdmGetTargetFileHandle method returns a handle to the file that is associated with a specified remote I/O target. |
| [WdfIoTargetGetDevice function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetgetdevice.md) | The WdfIoTargetGetDevice method returns a handle to the framework device object that is the parent of the specified local or remote I/O target. |
| [WdfIoTargetFormatRequestForIoctl function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetformatrequestforioctl.md) | The WdfIoTargetFormatRequestForIoctl method builds a device control request for an I/O target but does not send the request. |
| [WDF_IO_TARGET_OPEN_PARAMS_INIT_EXISTING_DEVICE function](..\wdfiotarget\nf-wdfiotarget-wdf-io-target-open-params-init-existing-device.md) | The WDF_IO_TARGET_OPEN_PARAMS_INIT_EXISTING_DEVICE function initializes a driver's WDF_IO_TARGET_OPEN_PARAMS structure so that the driver can open a remote I/O target by specifying a Windows Driver Model (WDM) device object. |
| [WDF_IO_TARGET_OPEN_PARAMS_INIT_CREATE_BY_NAME function](..\wdfiotarget\nf-wdfiotarget-wdf-io-target-open-params-init-create-by-name.md) | The WDF_IO_TARGET_OPEN_PARAMS_INIT_CREATE_BY_NAME function initializes a driver's WDF_IO_TARGET_OPEN_PARAMS structure so the driver can open an I/O target by specifying the name of the device, file, or device interface. |
| [WdfIoTargetWdmGetTargetPhysicalDevice function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetwdmgettargetphysicaldevice.md) | The WdfIoTargetWdmGetTargetPhysicalDevice method returns a pointer to the Windows Driver Model (WDM) physical device object (PDO) that represents a remote I/O target's device. |
| [WdfIoTargetFormatRequestForInternalIoctlOthers function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetformatrequestforinternalioctlothers.md) | The WdfIoTargetFormatRequestForInternalIoctlOthers method builds a non-standard internal device control request for an I/O target but does not send the request. |
| [WdfIoTargetCreate function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetcreate.md) | The WdfIoTargetCreate method creates a remote I/O target for a specified device. |
| [WdfIoTargetSendInternalIoctlSynchronously function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetsendinternalioctlsynchronously.md) | The WdfIoTargetSendInternalIoctlSynchronously method builds an internal device control request and sends it synchronously to an I/O target. |
| [WdfIoTargetWdmGetTargetFileObject function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetwdmgettargetfileobject.md) | The WdfIoTargetWdmGetTargetFileObject method returns a pointer to the Windows Driver Model (WDM) file object that is associated with a specified remote I/O target. |
| [WdfIoTargetStop function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetstop.md) | The WdfIoTargetStop method stops sending queued requests to a local or remote I/O target. |
| [WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_NAME function](..\wdfiotarget\nf-wdfiotarget-wdf-io-target-open-params-init-open-by-name.md) | The WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_NAME function initializes a driver's WDF_IO_TARGET_OPEN_PARAMS structure so the driver can open an I/O target by specifying the name of the device, file, or device interface. |
| [WdfIoTargetSendReadSynchronously function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetsendreadsynchronously.md) | The WdfIoTargetSendReadSynchronously method builds a read request and sends it synchronously to an I/O target. |
| [WdfIoTargetCloseForQueryRemove function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetcloseforqueryremove.md) | The WdfIoTargetCloseForQueryRemove method temporarily closes a specified remote I/O target because the target device might soon be removed. |
| [WdfIoTargetQueryTargetProperty function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetquerytargetproperty.md) | The WdfIoTargetQueryTargetProperty method retrieves a specified device property for a specified I/O target. |
| [WdfIoTargetQueryForInterface function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetqueryforinterface.md) | The WdfIoTargetQueryForInterface method obtains access to the GUID-identified, driver-defined interface of a remote I/O target. |
| [WdfIoTargetFormatRequestForWrite function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetformatrequestforwrite.md) | The WdfIoTargetFormatRequestForWrite method builds a write request for an I/O target but does not send the request. |
| [WdfIoTargetSendIoctlSynchronously function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetsendioctlsynchronously.md) | The WdfIoTargetSendIoctlSynchronously method builds a device control request and sends it synchronously to an I/O target. |
| [WdfIoTargetFormatRequestForRead function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetformatrequestforread.md) | The WdfIoTargetFormatRequestForRead method builds a read request for an I/O target but does not send the request. |
| [WdfIoTargetClose function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetclose.md) | The WdfIoTargetClose method closes a specified remote I/O target. |
| [WdfIoTargetWdmGetTargetDeviceObject function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetwdmgettargetdeviceobject.md) | The WdfIoTargetWdmGetTargetDeviceObject method returns a pointer to the Windows Driver Model (WDM) device object that is associated with a specified local or remote I/O target. |
| [WdfIoTargetFormatRequestForInternalIoctl function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetformatrequestforinternalioctl.md) | The WdfIoTargetFormatRequestForInternalIoctl method builds an internal device control request for an I/O target but does not send the request. |
| [WdfIoTargetAllocAndQueryTargetProperty function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetallocandquerytargetproperty.md) | The WdfIoTargetAllocAndQueryTargetProperty method allocates a buffer and retrieves a specified device property for a specified I/O target. |
| [WdfIoTargetPurge function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetpurge.md) | The WdfIoTargetPurge method cancels all I/O requests queued to a local, remote, or specialized I/O target and prevents any new I/O requests from being queued. |
| [WdfIoTargetSendInternalIoctlOthersSynchronously function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetsendinternalioctlotherssynchronously.md) | The WdfIoTargetSendInternalIoctlOthersSynchronously method builds a non-standard internal device control request and sends it synchronously to an I/O target. |
| [WDF_IO_TARGET_OPEN_PARAMS_INIT_REOPEN function](..\wdfiotarget\nf-wdfiotarget-wdf-io-target-open-params-init-reopen.md) | The WDF_IO_TARGET_OPEN_PARAMS_INIT_REOPEN function initializes a driver's WDF_IO_TARGET_OPEN_PARAMS structure so the driver can reopen a remote I/O target. |
| [WdfIoTargetStart function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetstart.md) | The WdfIoTargetStart method starts sending queued requests to a local or remote I/O target. |
| [WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_FILE function](..\wdfiotarget\nf-wdfiotarget-wdf-io-target-open-params-init-open-by-file.md) | The WDF_IO_TARGET_OPEN_PARAMS_INIT_OPEN_BY_FILE function initializes a driver's WDF_IO_TARGET_OPEN_PARAMS structure so the driver can open an I/O target by specifying a filename. |
| [WdfIoTargetSendWriteSynchronously function](..\wdfiotarget\nf-wdfiotarget-wdfiotargetsendwritesynchronously.md) | The WdfIoTargetSendWriteSynchronously method builds a write request and sends it synchronously to an I/O target. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_IO_TARGET_OPEN_PARAMS structure](..\wdfiotarget\ns-wdfiotarget--wdf-io-target-open-params.md) | The WDF_IO_TARGET_OPEN_PARAMS structure contains parameters that the WdfIoTargetOpen method uses. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfMemoryGetBuffer function](..\wdfmemory\nf-wdfmemory-wdfmemorygetbuffer.md) | The WdfMemoryGetBuffer method returns a pointer to the buffer that is associated with a specified memory object. |
| [WdfLookasideListCreate function](..\wdfmemory\nf-wdfmemory-wdflookasidelistcreate.md) | The WdfLookasideListCreate method creates a lookaside-list object, from which the driver can obtain memory objects. |
| [WDF_MEMORY_DESCRIPTOR_INIT_HANDLE function](..\wdfmemory\nf-wdfmemory-wdf-memory-descriptor-init-handle.md) | The WDF_MEMORY_DESCRIPTOR_INIT_HANDLE function initializes a WDF_MEMORY_DESCRIPTOR structure so that it describes a specified framework memory object. |
| [WdfMemoryAssignBuffer function](..\wdfmemory\nf-wdfmemory-wdfmemoryassignbuffer.md) | The WdfMemoryAssignBuffer method assigns a specified buffer to a memory object that a driver created by calling WdfMemoryCreatePreallocated. |
| [WDF_MEMORY_DESCRIPTOR_INIT_BUFFER function](..\wdfmemory\nf-wdfmemory-wdf-memory-descriptor-init-buffer.md) | The WDF_MEMORY_DESCRIPTOR_INIT_BUFFER function initializes a WDF_MEMORY_DESCRIPTOR structure so that it describes a specified buffer. |
| [WDF_MEMORY_DESCRIPTOR_INIT_MDL function](..\wdfmemory\nf-wdfmemory-wdf-memory-descriptor-init-mdl.md) | The WDF_MEMORY_DESCRIPTOR_INIT_MDL function initializes a WDF_MEMORY_DESCRIPTOR structure so that it describes a specified memory descriptor list (MDL). |
| [WdfMemoryCopyFromBuffer function](..\wdfmemory\nf-wdfmemory-wdfmemorycopyfrombuffer.md) | The WdfMemoryCopyFromBuffer method copies the contents of a specified source buffer into a specified memory object's buffer. |
| [WdfMemoryCreateFromLookaside function](..\wdfmemory\nf-wdfmemory-wdfmemorycreatefromlookaside.md) | The WdfMemoryCreateFromLookaside method creates a framework memory object and obtains a memory buffer from a specified lookaside list. |
| [WdfMemoryCopyToBuffer function](..\wdfmemory\nf-wdfmemory-wdfmemorycopytobuffer.md) | The WdfMemoryCopyToBuffer method copies the contents of a specified memory object's buffer into a specified destination buffer. |
| [WdfMemoryCreate function](..\wdfmemory\nf-wdfmemory-wdfmemorycreate.md) | The WdfMemoryCreate method creates a framework memory object and allocates a memory buffer of a specified size. |
| [WdfMemoryCreatePreallocated function](..\wdfmemory\nf-wdfmemory-wdfmemorycreatepreallocated.md) | The WdfMemoryCreatePreallocated method creates a framework memory object for a driver-supplied memory buffer. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_MEMORY_DESCRIPTOR structure](..\wdfmemory\ns-wdfmemory--wdf-memory-descriptor.md) | The WDF_MEMORY_DESCRIPTOR structure describes a memory buffer. |
| [WDFMEMORY_OFFSET structure](..\wdfmemory\ns-wdfmemory--wdfmemory-offset.md) | The WDFMEMORY_OFFSET structure identifies a subsection of a memory object's buffer. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_MEMORY_DESCRIPTOR_TYPE enumeration](..\wdfmemory\ne-wdfmemory--wdf-memory-descriptor-type.md) | The WDF_MEMORY_DESCRIPTOR_TYPE enumeration identifies the types of memory descriptions that a WDF_MEMORY_DESCRIPTOR structure can specify. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfDeviceMiniportCreate function](..\wdfminiport\nf-wdfminiport-wdfdeviceminiportcreate.md) | The WdfDeviceMiniportCreate method creates a framework device object that a miniport driver can use. |
| [WdfDriverMiniportUnload function](..\wdfminiport\nf-wdfminiport-wdfdriverminiportunload.md) | The WdfDriverMiniportUnload method deletes a specified miniport driver's framework driver object. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfObjectAllocateContext function](..\wdfobject\nf-wdfobject-wdfobjectallocatecontext.md) | The WdfObjectAllocateContext method allocates context space for a specified framework object. |
| [WDF_OBJECT_ATTRIBUTES_INIT function](..\wdfobject\nf-wdfobject-wdf-object-attributes-init.md) | The WDF_OBJECT_ATTRIBUTES_INIT function initializes a driver's WDF_OBJECT_ATTRIBUTES structure. |
| [WdfObjectContextGetObject function](..\wdfobject\nf-wdfobject-wdfobjectcontextgetobject.md) | The WdfObjectContextGetObject method returns a handle to the framework object that a specified context space belongs to. |
| [WdfObjectGetTypedContextWorker function](..\wdfobject\nf-wdfobject-wdfobjectgettypedcontextworker.md) | The WdfObjectGetTypedContextWorker method is reserved for internal use only. Use the WdfObjectGetTypedContext macro instead. |
| [WdfObjectReferenceActual function](..\wdfobject\nf-wdfobject-wdfobjectreferenceactual.md) | The WdfObjectReferenceActual method increments the reference count for a specified framework object and assigns a tag value, line number, and file name to the reference. |
| [WdfObjectCreate function](..\wdfobject\nf-wdfobject-wdfobjectcreate.md) | The WdfObjectCreate method creates a general framework object. |
| [WdfObjectDereferenceActual function](..\wdfobject\nf-wdfobject-wdfobjectdereferenceactual.md) | The WdfObjectDereferenceActual method decrements the reference count for a specified framework object and assigns a tag value, line number, and file name to the reference. |
| [WdfObjectDelete function](..\wdfobject\nf-wdfobject-wdfobjectdelete.md) | The WdfObjectDelete method deletes a framework object and its child objects. |
| [WdfObjectQuery function](..\wdfobject\nf-wdfobject-wdfobjectquery.md) | The WdfObjectQuery method is not implemented. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_WDF_OBJECT_CONTEXT_CLEANUP callback](..\wdfobject\nc-wdfobject-evt-wdf-object-context-cleanup.md) | A driver's EvtCleanupCallback event callback function removes the driver's references on an object so that the object can be deleted. |
| [EVT_WDF_OBJECT_CONTEXT_DESTROY callback](..\wdfobject\nc-wdfobject-evt-wdf-object-context-destroy.md) | A driver's EvtDestroyCallback event callback function performs operations that are associated with the deletion of a framework object. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_SYNCHRONIZATION_SCOPE enumeration](..\wdfobject\ne-wdfobject--wdf-synchronization-scope.md) | The WDF_SYNCHRONIZATION_SCOPE enumeration type specifies how the framework will synchronize execution of an object's event callback functions. |
| [WDF_EXECUTION_LEVEL enumeration](..\wdfobject\ne-wdfobject--wdf-execution-level.md) | The WDF_EXECUTION_LEVEL enumeration type specifies the maximum IRQL at which the framework will call the event callback functions that a driver has supplied for a framework object. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_OBJECT_CONTEXT_TYPE_INFO structure](..\wdfobject\ns-wdfobject--wdf-object-context-type-info~r1.md) | The WDF_OBJECT_CONTEXT_TYPE_INFO structure describes a framework object's driver-defined context memory. |
| [WDF_OBJECT_ATTRIBUTES structure](..\wdfobject\ns-wdfobject--wdf-object-attributes.md) | The WDF_OBJECT_ATTRIBUTES structure describes attributes that can be associated with any framework object. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_PDO_EVENT_CALLBACKS structure](..\wdfpdo\ns-wdfpdo--wdf-pdo-event-callbacks.md) | The WDF_PDO_EVENT_CALLBACKS structure is the dispatch table for a bus driver's event callback functions. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_WDF_DEVICE_DISABLE_WAKE_AT_BUS callback](..\wdfpdo\nc-wdfpdo-evt-wdf-device-disable-wake-at-bus.md) | A bus driver's EvtDeviceDisableWakeAtBus event callback function performs bus-level operations that disable the ability of one of the bus's devices to trigger a wake-up signal on the bus. |
| [EVT_WDF_DEVICE_SET_LOCK callback](..\wdfpdo\nc-wdfpdo-evt-wdf-device-set-lock.md) | A driver's EvtDeviceSetLock event callback function locks the specified device so that it cannot be ejected, or unlocks the device so that it can be ejected. |
| [EVT_WDF_DEVICE_RESOURCE_REQUIREMENTS_QUERY callback](..\wdfpdo\nc-wdfpdo-evt-wdf-device-resource-requirements-query.md) | A bus driver's EvtDeviceResourceRequirementsQuery event callback function creates a resource requirements list that represents the device's required hardware resources. |
| [EVT_WDF_DEVICE_EJECT callback](..\wdfpdo\nc-wdfpdo-evt-wdf-device-eject.md) | A driver's EvtDeviceEject event callback function handles operations that are necessary to eject a device from its docking station. |
| [EVT_WDF_DEVICE_ENABLE_WAKE_AT_BUS callback](..\wdfpdo\nc-wdfpdo-evt-wdf-device-enable-wake-at-bus.md) | A bus driver's EvtDeviceEnableWakeAtBus event callback function performs bus-level operations that enable one of the bus's devices to trigger a wake-up signal on the bus. |
| [EVT_WDF_DEVICE_REPORTED_MISSING callback](..\wdfpdo\nc-wdfpdo-evt-wdf-device-reported-missing.md) | A bus driver's EvtDeviceReportedMissing event callback function informs the driver that the framework has reported the physical device object (PDO) missing to the Plug and Play manager. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfPdoRetrieveAddressDescription function](..\wdfpdo\nf-wdfpdo-wdfpdoretrieveaddressdescription.md) | The WdfPdoRetrieveAddressDescription method retrieves the address description that is associated with a specified framework device object. |
| [WdfPdoInitAssignContainerID function](..\wdfpdo\nf-wdfpdo-wdfpdoinitassigncontainerid.md) | The WdfPdoInitAssignContainerID method updates the container ID for a child device. |
| [WdfPdoInitAddHardwareID function](..\wdfpdo\nf-wdfpdo-wdfpdoinitaddhardwareid.md) | The WdfPdoInitAddHardwareID method adds a hardware ID to the list of hardware IDs for a child device. |
| [WdfPdoInitAllocate function](..\wdfpdo\nf-wdfpdo-wdfpdoinitallocate.md) | The WdfPdoInitAllocate method allocates a WDFDEVICE_INIT structure for a framework-based bus driver, which the bus driver uses when reporting a new device. |
| [WdfPdoAddEjectionRelationsPhysicalDevice function](..\wdfpdo\nf-wdfpdo-wdfpdoaddejectionrelationsphysicaldevice.md) | The WdfPdoAddEjectionRelationsPhysicalDevice method indicates that a specified device is ejected when another specified device is ejected. |
| [WdfPdoInitSetDefaultLocale function](..\wdfpdo\nf-wdfpdo-wdfpdoinitsetdefaultlocale.md) | The WdfPdoInitSetDefaultLocale method sets a device's default locale. |
| [WdfPdoInitAssignInstanceID function](..\wdfpdo\nf-wdfpdo-wdfpdoinitassigninstanceid.md) | The WdfPdoInitAssignInstanceID method updates the instance ID for a child device. |
| [WdfPdoInitAddDeviceText function](..\wdfpdo\nf-wdfpdo-wdfpdoinitadddevicetext.md) | The WdfPdoInitAddDeviceText method adds a device description and device location to a device, for a specified locale. |
| [WdfPdoUpdateAddressDescription function](..\wdfpdo\nf-wdfpdo-wdfpdoupdateaddressdescription.md) | The WdfPdoUpdateAddressDescription method updates the address description that is associated with a specified framework device object. |
| [WdfPdoInitAssignDeviceID function](..\wdfpdo\nf-wdfpdo-wdfpdoinitassigndeviceid.md) | The WdfPdoInitAssignDeviceID method updates the device ID for a child device. |
| [WdfPdoInitAddCompatibleID function](..\wdfpdo\nf-wdfpdo-wdfpdoinitaddcompatibleid.md) | The WdfPdoInitAddCompatibleID method adds a compatible ID to the list of compatible IDs for a child device. |
| [WdfPdoInitAllowForwardingRequestToParent function](..\wdfpdo\nf-wdfpdo-wdfpdoinitallowforwardingrequesttoparent.md) | The WdfPdoInitAllowForwardingRequestToParent method enables a driver's ability to call WdfRequestForwardToParentDeviceIoQueue. |
| [WdfPdoRemoveEjectionRelationsPhysicalDevice function](..\wdfpdo\nf-wdfpdo-wdfpdoremoveejectionrelationsphysicaldevice.md) | The WdfPdoRemoveEjectionRelationsPhysicalDevice method removes a specified device from the list of devices that must be ejected when another specified device is ejected. |
| [WdfPdoClearEjectionRelationsDevices function](..\wdfpdo\nf-wdfpdo-wdfpdoclearejectionrelationsdevices.md) | The WdfPdoClearEjectionRelationsDevices method removes all devices from the list of devices that must be ejected when a specified device is ejected. |
| [WdfPdoInitSetEventCallbacks function](..\wdfpdo\nf-wdfpdo-wdfpdoinitseteventcallbacks.md) | The WdfPdoInitSetEventCallbacks method registers a bus driver's event callback functions. |
| [WdfPdoInitAssignRawDevice function](..\wdfpdo\nf-wdfpdo-wdfpdoinitassignrawdevice.md) | The WdfPdoInitAssignRawDevice method indicates that the calling driver can support a specified device in raw mode. |
| [WdfPdoRequestEject function](..\wdfpdo\nf-wdfpdo-wdfpdorequesteject.md) | The WdfPdoRequestEject method informs the framework that a specified device is about to be ejected from its docking station. |
| [WdfPdoGetParent function](..\wdfpdo\nf-wdfpdo-wdfpdogetparent.md) | The WdfPdoGetParent method returns a handle to the framework device object that represents the parent device of a specified device. |
| [WdfPdoMarkMissing function](..\wdfpdo\nf-wdfpdo-wdfpdomarkmissing.md) | The WdfPdoMarkMissing method informs the framework that a device is no longer accessible. |
| [WDF_PDO_EVENT_CALLBACKS_INIT function](..\wdfpdo\nf-wdfpdo-wdf-pdo-event-callbacks-init.md) | The WDF_PDO_EVENT_CALLBACKS_INIT function initializes a WDF_PDO_EVENT_CALLBACKS structure. |
| [WdfPdoRetrieveIdentificationDescription function](..\wdfpdo\nf-wdfpdo-wdfpdoretrieveidentificationdescription.md) | The WdfPdoRetrieveIdentificationDescription method retrieves the identification description that is associated with a specified framework device object. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfDeviceInterfaceReferenceNoOp function](..\wdfqueryinterface\nf-wdfqueryinterface-wdfdeviceinterfacereferencenoop.md) | The WdfDeviceInterfaceReferenceNoOp method can be used for driver-defined interfaces that do not require reference counts. |
| [WDF_QUERY_INTERFACE_CONFIG_INIT function](..\wdfqueryinterface\nf-wdfqueryinterface-wdf-query-interface-config-init.md) | The WDF_QUERY_INTERFACE_CONFIG_INIT function initializes a driver's WDF_QUERY_INTERFACE_CONFIG structure. |
| [WdfDeviceInterfaceDereferenceNoOp function](..\wdfqueryinterface\nf-wdfqueryinterface-wdfdeviceinterfacedereferencenoop.md) | The WdfDeviceInterfaceDereferenceNoOp method can be used for driver-defined interfaces that do not require reference counts. |
| [WdfDeviceAddQueryInterface function](..\wdfqueryinterface\nf-wdfqueryinterface-wdfdeviceaddqueryinterface.md) | The WdfDeviceAddQueryInterface method creates a driver-defined interface that other drivers can query and use. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_QUERY_INTERFACE_CONFIG structure](..\wdfqueryinterface\ns-wdfqueryinterface--wdf-query-interface-config.md) | The WDF_QUERY_INTERFACE_CONFIG structure describes a driver-defined interface. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfRegistryAssignMultiString function](..\wdfregistry\nf-wdfregistry-wdfregistryassignmultistring.md) | The WdfRegistryAssignMultiString method assigns a set of strings to a specified value name in the registry. The strings are contained in a specified collection of framework string objects. |
| [WdfRegistryClose function](..\wdfregistry\nf-wdfregistry-wdfregistryclose.md) | The WdfRegistryClose method closes the registry key that is associated with a specified framework registry-key object and then deletes the registry-key object. |
| [WdfRegistryRemoveValue function](..\wdfregistry\nf-wdfregistry-wdfregistryremovevalue.md) | The WdfRegistryRemoveValue method removes a specified value and its data from a specified registry key. |
| [WdfRegistryAssignULong function](..\wdfregistry\nf-wdfregistry-wdfregistryassignulong.md) | The WdfRegistryAssignULong method assigns a specified unsigned long word value to a specified value name in the registry. |
| [WdfRegistryAssignValue function](..\wdfregistry\nf-wdfregistry-wdfregistryassignvalue.md) | The WdfRegistryAssignValue method assigns specified data to a specified value name in the registry. |
| [WdfRegistryCreateKey function](..\wdfregistry\nf-wdfregistry-wdfregistrycreatekey.md) | The WdfRegistryCreateKey method creates and opens a specified registry key, or just opens the key if it already exists, and creates a framework registry-key object that represents the registry key. |
| [WdfRegistryQueryULong function](..\wdfregistry\nf-wdfregistry-wdfregistryqueryulong.md) | The WdfRegistryQueryULong method retrieves the unsigned long word (REG_DWORD) data that is currently assigned to a specified registry value and copies the data to a specified location. |
| [WdfRegistryQueryMemory function](..\wdfregistry\nf-wdfregistry-wdfregistryquerymemory.md) | The WdfRegistryQueryMemory method retrieves the data that is currently assigned to a specified registry value, stores the data in a framework-allocated buffer, and creates a framework memory object to represent the buffer. |
| [WdfRegistryQueryString function](..\wdfregistry\nf-wdfregistry-wdfregistryquerystring.md) | The WdfRegistryQueryString method retrieves the string data that is currently assigned to a specified registry string value and assigns the string to a specified framework string object. |
| [WdfRegistryAssignUnicodeString function](..\wdfregistry\nf-wdfregistry-wdfregistryassignunicodestring.md) | The WdfRegistryAssignUnicodeString method assigns a specified Unicode string to a specified value name in the registry. |
| [WdfRegistryRemoveKey function](..\wdfregistry\nf-wdfregistry-wdfregistryremovekey.md) | The WdfRegistryRemoveKey method removes the registry key that is associated with a specified framework registry-key object and then deletes the registry-key object. |
| [WdfRegistryQueryMultiString function](..\wdfregistry\nf-wdfregistry-wdfregistryquerymultistring.md) | The WdfRegistryQueryMultiString method retrieves the strings that are currently assigned to a specified multi-string registry value, creates a framework string object for each string, and adds each string object to a specified object collection. |
| [WdfRegistryQueryValue function](..\wdfregistry\nf-wdfregistry-wdfregistryqueryvalue.md) | The WdfRegistryQueryValue method retrieves the data that is currently assigned to a specified registry value. |
| [WdfRegistryWdmGetHandle function](..\wdfregistry\nf-wdfregistry-wdfregistrywdmgethandle.md) | The WdfRegistryWdmGetHandle method returns a Windows Driver Model (WDM) handle to the registry key that a specified framework registry-key object represents. |
| [WdfRegistryQueryUnicodeString function](..\wdfregistry\nf-wdfregistry-wdfregistryqueryunicodestring.md) | The WdfRegistryQueryUnicodeString method retrieves the string data that is currently assigned to a specified registry string value and copies the string to a specified UNICODE_STRING structure. |
| [WdfRegistryOpenKey function](..\wdfregistry\nf-wdfregistry-wdfregistryopenkey.md) | The WdfRegistryOpenKey method opens a specified registry key and creates a framework registry-key object that represents the registry key. |
| [WdfRegistryAssignMemory function](..\wdfregistry\nf-wdfregistry-wdfregistryassignmemory.md) | The WdfRegistryAssignMemory method assigns data that is contained in a specified memory buffer to a specified value name in the registry. |
| [WdfRegistryAssignString function](..\wdfregistry\nf-wdfregistry-wdfregistryassignstring.md) | The WdfRegistryAssignString method assigns a string to a specified value name in the registry. The string is contained in a specified framework string object. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_REQUEST_FORWARD_OPTIONS structure](..\wdfrequest\ns-wdfrequest--wdf-request-forward-options.md) | The WDF_REQUEST_FORWARD_OPTIONS structure contains options for requeuing an I/O request from a child device's I/O queue to the parent device's I/O queue. |
| [WDF_REQUEST_COMPLETION_PARAMS structure](..\wdfrequest\ns-wdfrequest--wdf-request-completion-params.md) | The WDF_REQUEST_COMPLETION_PARAMS structure contains parameters that are associated with the completion of an I/O request. |
| [WDF_REQUEST_PARAMETERS structure](..\wdfrequest\ns-wdfrequest--wdf-request-parameters.md) | The WDF_REQUEST_PARAMETERS structure receives parameters that are associated with an I/O request. |
| [WDF_REQUEST_REUSE_PARAMS structure](..\wdfrequest\ns-wdfrequest--wdf-request-reuse-params.md) | The WDF_REQUEST_REUSE_PARAMS structure specifies information that is associated with a reused I/O request. |
| [WDF_REQUEST_SEND_OPTIONS structure](..\wdfrequest\ns-wdfrequest--wdf-request-send-options.md) | The WDF_REQUEST_SEND_OPTIONS structure specifies options that are associated with sending an I/O request to an I/O target. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfRequestCreateFromIrp function](..\wdfrequest\nf-wdfrequest-wdfrequestcreatefromirp.md) | The WdfRequestCreateFromIrp method creates a framework request object from a specified WDM IRP. |
| [WdfRequestSetUserModeDriverInitiatedIo function](..\wdfrequest\nf-wdfrequest-wdfrequestsetusermodedriverinitiatedio.md) | The WdfRequestSetUserModeDriverInitiatedIo method indicates to kernel-mode drivers that sit below the UMDF driver in the same device stack that a particular request should be treated as though it came from a UMDF driver. |
| [WDF_REQUEST_FORWARD_OPTIONS_INIT function](..\wdfrequest\nf-wdfrequest-wdf-request-forward-options-init.md) | The WDF_REQUEST_FORWARD_OPTIONS_INIT function initializes a WDF_REQUEST_FORWARD_OPTIONS structure. |
| [WdfRequestRetrieveUnsafeUserInputBuffer function](..\wdfrequest\nf-wdfrequest-wdfrequestretrieveunsafeuserinputbuffer.md) | The WdfRequestRetrieveUnsafeUserInputBuffer method retrieves an I/O request's input buffer, if the request's technique for accessing data buffers is neither buffered nor direct I/O. |
| [WdfRequestMarkCancelableEx function](..\wdfrequest\nf-wdfrequest-wdfrequestmarkcancelableex.md) | The WdfRequestMarkCancelableEx method enables cancellation of a specified I/O request. |
| [WdfRequestWdmGetIrp function](..\wdfrequest\nf-wdfrequest-wdfrequestwdmgetirp.md) | The WdfRequestWdmGetIrp method returns the WDM IRP structure that is associated with a specified framework request object. |
| [WDF_REQUEST_PARAMETERS_INIT function](..\wdfrequest\nf-wdfrequest-wdf-request-parameters-init.md) | The WDF_REQUEST_PARAMETERS_INIT function initializes a WDF_REQUEST_PARAMETERS structure. |
| [WDF_REQUEST_SEND_OPTIONS_INIT function](..\wdfrequest\nf-wdfrequest-wdf-request-send-options-init.md) | The WDF_REQUEST_SEND_OPTIONS_INIT function initializes a driver's WDF_REQUEST_SEND_OPTIONS structure. |
| [WdfRequestProbeAndLockUserBufferForRead function](..\wdfrequest\nf-wdfrequest-wdfrequestprobeandlockuserbufferforread.md) | The WdfRequestProbeAndLockUserBufferForRead method verifies that an I/O request's user-mode buffer is readable, and then it locks the buffer's physical memory pages so drivers in the driver stack can read the buffer. |
| [WdfRequestGetRequestorMode function](..\wdfrequest\nf-wdfrequest-wdfrequestgetrequestormode.md) | The WdfRequestGetRequestorMode method returns the processor access mode of the originator of a specified I/O request. |
| [WDF_REQUEST_COMPLETION_PARAMS_INIT function](..\wdfrequest\nf-wdfrequest-wdf-request-completion-params-init.md) | The WDF_REQUEST_COMPLETION_PARAMS_INIT function initializes a WDF_REQUEST_COMPLETION_PARAMS structure. |
| [WdfRequestIsFrom32BitProcess function](..\wdfrequest\nf-wdfrequest-wdfrequestisfrom32bitprocess.md) | The WdfRequestIsFrom32BitProcess method checks whether the originator of a specified I/O request is a 32-bit user-mode application. |
| [WdfRequestGetRequestorProcessId function](..\wdfrequest\nf-wdfrequest-wdfrequestgetrequestorprocessid.md) | The WdfRequestGetRequestorProcessId method retrieves the identifier of the process that sent an I/O request. |
| [WdfRequestGetInformation function](..\wdfrequest\nf-wdfrequest-wdfrequestgetinformation.md) | The WdfRequestGetInformation method returns completion status information for a specified I/O request. |
| [WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT function](..\wdfrequest\nf-wdfrequest-wdf-request-send-options-set-timeout.md) | The WDF_REQUEST_SEND_OPTIONS_SET_TIMEOUT function sets a time-out value in a driver's WDF_REQUEST_SEND_OPTIONS structure. |
| [WdfRequestProbeAndLockUserBufferForWrite function](..\wdfrequest\nf-wdfrequest-wdfrequestprobeandlockuserbufferforwrite.md) | The WdfRequestProbeAndLockUserBufferForWrite method verifies that an I/O request's user-mode buffer is writeable, and then it locks the buffer's physical memory pages so drivers in the driver stack can write into the buffer. |
| [WdfRequestCompleteWithInformation function](..\wdfrequest\nf-wdfrequest-wdfrequestcompletewithinformation.md) | The WdfRequestCompleteWithInformation method stores completion information and then completes a specified I/O request with a supplied completion status. |
| [WdfRequestSetCompletionRoutine function](..\wdfrequest\nf-wdfrequest-wdfrequestsetcompletionroutine.md) | The WdfRequestSetCompletionRoutine method registers or deregisters a completion routine for the specified framework request object. |
| [WdfRequestRetrieveOutputWdmMdl function](..\wdfrequest\nf-wdfrequest-wdfrequestretrieveoutputwdmmdl.md) | The WdfRequestRetrieveOutputWdmMdl method retrieves a memory descriptor list (MDL) that represents an I/O request's output buffer. |
| [WdfRequestReuse function](..\wdfrequest\nf-wdfrequest-wdfrequestreuse.md) | The WdfRequestReuse method reinitializes a framework request object so that it can be reused. |
| [WdfRequestRetrieveInputWdmMdl function](..\wdfrequest\nf-wdfrequest-wdfrequestretrieveinputwdmmdl.md) | The WdfRequestRetrieveInputWdmMdl method retrieves a memory descriptor list (MDL) that represents an I/O request's input buffer. |
| [WDF_REQUEST_REUSE_PARAMS_INIT function](..\wdfrequest\nf-wdfrequest-wdf-request-reuse-params-init.md) | The WDF_REQUEST_REUSE_PARAMS_INIT function initializes a driver's WDF_REQUEST_REUSE_PARAMS structure. |
| [WdfRequestGetParameters function](..\wdfrequest\nf-wdfrequest-wdfrequestgetparameters.md) | The WdfRequestGetParameters method retrieves the parameters that are associated with a specified framework request object. |
| [WdfRequestIsFromUserModeDriver function](..\wdfrequest\nf-wdfrequest-wdfrequestisfromusermodedriver.md) | The WdfRequestIsFromUserModeDriver method indicates whether an I/O request came from a user-mode driver or an application. |
| [WdfRequestGetStatus function](..\wdfrequest\nf-wdfrequest-wdfrequestgetstatus.md) | The WdfRequestGetStatus method returns the status of an I/O request. |
| [WDF_REQUEST_REUSE_PARAMS_SET_NEW_IRP function](..\wdfrequest\nf-wdfrequest-wdf-request-reuse-params-set-new-irp.md) | The WDF_REQUEST_REUSE_PARAMS_SET_NEW_IRP function sets a new IRP in a driver's WDF_REQUEST_REUSE_PARAMS structure. |
| [WdfRequestSetActivityId function](..\wdfrequest\nf-wdfrequest-wdfrequestsetactivityid.md) | The WdfRequestSetActivityId method associates an activity identifier with an I/O request. |
| [WdfRequestRetrieveInputBuffer function](..\wdfrequest\nf-wdfrequest-wdfrequestretrieveinputbuffer.md) | The WdfRequestRetrieveInputBuffer method retrieves an I/O request's input buffer. |
| [WdfRequestGetFileObject function](..\wdfrequest\nf-wdfrequest-wdfrequestgetfileobject.md) | The WdfRequestGetFileObject method retrieves the framework file object that is associated with a specified I/O request. |
| [WdfRequestForwardToParentDeviceIoQueue function](..\wdfrequest\nf-wdfrequest-wdfrequestforwardtoparentdeviceioqueue.md) | The WdfRequestForwardToParentDeviceIoQueue method requeues an I/O request from a child device's I/O queue to a specified I/O queue of the child's parent device. |
| [WdfRequestForwardToIoQueue function](..\wdfrequest\nf-wdfrequest-wdfrequestforwardtoioqueue.md) | The WdfRequestForwardToIoQueue method requeues an I/O request to one of the calling driver's I/O queues. |
| [WdfRequestRetrieveUnsafeUserOutputBuffer function](..\wdfrequest\nf-wdfrequest-wdfrequestretrieveunsafeuseroutputbuffer.md) | The WdfRequestRetrieveUnsafeUserOutputBuffer method retrieves an I/O request's output buffer, if the request's technique for accessing data buffers is neither buffered nor direct I/O. |
| [WdfRequestFormatRequestUsingCurrentType function](..\wdfrequest\nf-wdfrequest-wdfrequestformatrequestusingcurrenttype.md) | The WdfRequestFormatRequestUsingCurrentType method formats a specified I/O request so that the driver can forward it, unmodified, to the driver's local I/O target. |
| [WdfRequestImpersonate function](..\wdfrequest\nf-wdfrequest-wdfrequestimpersonate.md) | The WdfRequestImpersonate method registers a driver-supplied event callback function that the framework should call for impersonation. |
| [WdfRequestRetrieveInputMemory function](..\wdfrequest\nf-wdfrequest-wdfrequestretrieveinputmemory.md) | The WdfRequestRetrieveInputMemory method retrieves a handle to a framework memory object that represents an I/O request's input buffer. |
| [WdfRequestAllocateTimer function](..\wdfrequest\nf-wdfrequest-wdfrequestallocatetimer.md) | The WdfRequestAllocateTimer method allocates a timer for a specified I/O request. |
| [WdfRequestCreate function](..\wdfrequest\nf-wdfrequest-wdfrequestcreate.md) | The WdfRequestCreate method creates an empty framework request object. |
| [WdfRequestWdmFormatUsingStackLocation function](..\wdfrequest\nf-wdfrequest-wdfrequestwdmformatusingstacklocation.md) | The WdfRequestWdmFormatUsingStackLocation method formats an I/O request by copying the contents of a specified WDM I/O stack location structure to the next stack location in the request. |
| [WdfRequestChangeTarget function](..\wdfrequest\nf-wdfrequest-wdfrequestchangetarget.md) | The WdfRequestChangeTarget method verifies that a specified I/O request can be sent to a specified I/O target. |
| [WdfRequestRetrieveOutputBuffer function](..\wdfrequest\nf-wdfrequest-wdfrequestretrieveoutputbuffer.md) | The WdfRequestRetrieveOutputBuffer method retrieves an I/O request's output buffer. |
| [WdfRequestStopAcknowledge function](..\wdfrequest\nf-wdfrequest-wdfrequeststopacknowledge.md) | The WdfRequestStopAcknowledge method informs the framework that the driver has stopped processing a specified I/O request. |
| [WdfRequestMarkCancelable function](..\wdfrequest\nf-wdfrequest-wdfrequestmarkcancelable.md) | The WdfRequestMarkCancelable method enables cancellation of a specified I/O request. |
| [WdfRequestGetCompletionParams function](..\wdfrequest\nf-wdfrequest-wdfrequestgetcompletionparams.md) | The WdfRequestGetCompletionParams method retrieves the I/O completion parameters that are associated with a specified framework request object. |
| [WdfRequestGetIoQueue function](..\wdfrequest\nf-wdfrequest-wdfrequestgetioqueue.md) | The WdfRequestGetIoQueue method returns a handle to the framework queue object from which a specified I/O request was delivered. |
| [WdfRequestRequeue function](..\wdfrequest\nf-wdfrequest-wdfrequestrequeue.md) | The WdfRequestRequeue method returns an I/O request to the head of the I/O queue from which it was delivered to the driver. |
| [WdfRequestUnmarkCancelable function](..\wdfrequest\nf-wdfrequest-wdfrequestunmarkcancelable.md) | The WdfRequestUnmarkCancelable method disables cancellation of a specified I/O request. |
| [WdfRequestCompleteWithPriorityBoost function](..\wdfrequest\nf-wdfrequest-wdfrequestcompletewithpriorityboost.md) | The WdfRequestCompleteWithPriorityBoost method completes a specified I/O request and supplies a completion status. It also specifies a value that the system can use to boost the run-time priority of the thread that requested the I/O operation. |
| [WdfRequestCancelSentRequest function](..\wdfrequest\nf-wdfrequest-wdfrequestcancelsentrequest.md) | The WdfRequestCancelSentRequest method attempts to cancel an I/O request that the caller previously submitted to an I/O target. |
| [WdfRequestComplete function](..\wdfrequest\nf-wdfrequest-wdfrequestcomplete.md) | The WdfRequestComplete method completes a specified I/O request and supplies a completion status. |
| [WdfRequestIsCanceled function](..\wdfrequest\nf-wdfrequest-wdfrequestiscanceled.md) | The WdfRequestIsCanceled method determines whether the I/O manager has attempted to cancel a specified I/O request. |
| [WdfRequestGetEffectiveIoType function](..\wdfrequest\nf-wdfrequest-wdfrequestgeteffectiveiotype.md) | The WdfRequestGetEffectiveIoType method returns the buffer access method that UMDF is using for the data buffers of the specified I/O request. |
| [WdfRequestIsReserved function](..\wdfrequest\nf-wdfrequest-wdfrequestisreserved.md) | The WdfRequestIsReserved method determines whether a specified request object is one that the framework reserved to support guaranteed forward progress during low-memory situations. |
| [WdfRequestRetrieveActivityId function](..\wdfrequest\nf-wdfrequest-wdfrequestretrieveactivityid.md) | The WdfRequestRetrieveActivityId method retrieves the current activity identifier associated with an I/O request. |
| [WdfRequestSend function](..\wdfrequest\nf-wdfrequest-wdfrequestsend.md) | The WdfRequestSend method sends a specified I/O request to a specified I/O target. |
| [WdfRequestRetrieveOutputMemory function](..\wdfrequest\nf-wdfrequest-wdfrequestretrieveoutputmemory.md) | The WdfRequestRetrieveOutputMemory method retrieves a handle to a framework memory object that represents an I/O request's output buffer. |
| [WdfRequestSetInformation function](..\wdfrequest\nf-wdfrequest-wdfrequestsetinformation.md) | The WdfRequestSetInformation method sets completion status information for a specified I/O request. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_WDF_REQUEST_CANCEL callback](..\wdfrequest\nc-wdfrequest-evt-wdf-request-cancel.md) | A driver's EvtRequestCancel event callback function handles operations that must be performed when an I/O request is canceled. |
| [EVT_WDF_REQUEST_IMPERSONATE callback](..\wdfrequest\nc-wdfrequest-evt-wdf-request-impersonate.md) | A driver's EvtRequestImpersonate event callback function performs tasks at the requested impersonation level, such as opening a protected file. |
| [EVT_WDF_REQUEST_COMPLETION_ROUTINE callback](..\wdfrequest\nc-wdfrequest-evt-wdf-request-completion-routine.md) | A driver's CompletionRoutine event callback function executes when another driver completes a specified I/O request. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_REQUEST_FORWARD_OPTIONS_FLAGS enumeration](..\wdfrequest\ne-wdfrequest--wdf-request-forward-options-flags.md) | The WDF_REQUEST_FORWARD_OPTIONS_FLAGS enumeration type defines flags that are used in a driver's WDF_REQUEST_FORWARD_OPTIONS structure. |
| [WDF_REQUEST_SEND_OPTIONS_FLAGS enumeration](..\wdfrequest\ne-wdfrequest--wdf-request-send-options-flags.md) | The WDF_REQUEST_SEND_OPTIONS_FLAGS enumeration type defines flags that are used in a driver's WDF_REQUEST_SEND_OPTIONS structure. |
| [WDF_REQUEST_TYPE enumeration](..\wdfrequest\ne-wdfrequest--wdf-request-type.md) | The WDF_REQUEST_TYPE enumeration type identifies types of requests that a framework request object might contain. |
| [WDF_REQUEST_STOP_ACTION_FLAGS enumeration](..\wdfrequest\ne-wdfrequest--wdf-request-stop-action-flags.md) | The WDF_REQUEST_STOP_ACTION_FLAGS enumeration type defines flags that the framework passes to a driver's EvtIoStop callback function. |
| [WDF_REQUEST_REUSE_FLAGS enumeration](..\wdfrequest\ne-wdfrequest--wdf-request-reuse-flags.md) | The WDF_REQUEST_REUSE_FLAGS enumeration type defines flags that are used in a driver's WDF_REQUEST_REUSE_PARAMS structure. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfIoResourceRequirementsListGetIoResList function](..\wdfresource\nf-wdfresource-wdfioresourcerequirementslistgetioreslist.md) | The WdfIoResourceRequirementsListGetIoResList method returns a handle to the framework resource-range-list object that represents a specified logical configuration in a specified resource requirements list. |
| [WdfIoResourceRequirementsListSetSlotNumber function](..\wdfresource\nf-wdfresource-wdfioresourcerequirementslistsetslotnumber.md) | The WdfIoResourceRequirementsListSetSlotNumber method assigns a slot number to a resource requirements list. |
| [WdfCmResourceListGetDescriptor function](..\wdfresource\nf-wdfresource-wdfcmresourcelistgetdescriptor.md) | The WdfCmResourceListGetDescriptor method returns a pointer to a resource descriptor that is contained in a specified resource list. |
| [WdfCmResourceListAppendDescriptor function](..\wdfresource\nf-wdfresource-wdfcmresourcelistappenddescriptor.md) | The WdfCmResourceListAppendDescriptor method adds a resource descriptor to the end of a specified resource list. |
| [WdfIoResourceListRemoveByDescriptor function](..\wdfresource\nf-wdfresource-wdfioresourcelistremovebydescriptor.md) | The WdfIoResourceListRemoveByDescriptor method removes a resource descriptor from a resource requirement list's logical configuration. |
| [WdfIoResourceRequirementsListInsertIoResList function](..\wdfresource\nf-wdfresource-wdfioresourcerequirementslistinsertioreslist.md) | The WdfIoResourceRequirementsListInsertIoResList method inserts a logical configuration into a resource requirements list. |
| [WdfCmResourceListGetCount function](..\wdfresource\nf-wdfresource-wdfcmresourcelistgetcount.md) | The WdfCmResourceListGetCount method returns the number of resource descriptors that are contained in a specified resource list. |
| [WdfIoResourceListCreate function](..\wdfresource\nf-wdfresource-wdfioresourcelistcreate.md) | The WdfIoResourceListCreate method creates an empty logical configuration, which can be populated and added to a resource requirements list. |
| [WdfIoResourceListRemove function](..\wdfresource\nf-wdfresource-wdfioresourcelistremove.md) | The WdfIoResourceListRemove method removes a resource descriptor from a resource requirements list's logical configuration. |
| [WdfCmResourceListRemove function](..\wdfresource\nf-wdfresource-wdfcmresourcelistremove.md) | The WdfCmResourceListRemove method removes a resource descriptor from a specified resource list. |
| [WdfIoResourceListGetDescriptor function](..\wdfresource\nf-wdfresource-wdfioresourcelistgetdescriptor.md) | The WdfIoResourceListGetDescriptor method returns a pointer to a resource descriptor that is contained in a resource requirements list's logical configuration. |
| [WdfCmResourceListRemoveByDescriptor function](..\wdfresource\nf-wdfresource-wdfcmresourcelistremovebydescriptor.md) | The WdfCmResourceListRemoveByDescriptor method removes a specified resource descriptor from a specified resource list. |
| [WdfIoResourceListGetCount function](..\wdfresource\nf-wdfresource-wdfioresourcelistgetcount.md) | The WdfIoResourceListGetCount method returns the number of resource descriptors that are contained in a resource requirements list's logical configuration. |
| [WdfIoResourceRequirementsListGetCount function](..\wdfresource\nf-wdfresource-wdfioresourcerequirementslistgetcount.md) | The WdfIoResourceRequirementsListGetCount method returns the number of logical configurations that are contained in a resource requirements list. |
| [WdfIoResourceListAppendDescriptor function](..\wdfresource\nf-wdfresource-wdfioresourcelistappenddescriptor.md) | The WdfIoResourceListAppendDescriptor method adds a resource descriptor to the end of a resource requirements list's logical configuration. |
| [WdfIoResourceRequirementsListAppendIoResList function](..\wdfresource\nf-wdfresource-wdfioresourcerequirementslistappendioreslist.md) | The WdfIoResourceRequirementsListAppendIoResList method adds a logical configuration to the end of a resource requirements list. |
| [WdfIoResourceListInsertDescriptor function](..\wdfresource\nf-wdfresource-wdfioresourcelistinsertdescriptor.md) | The WdfIoResourceListInsertDescriptor method inserts a resource descriptor into a resource requirements list's logical configuration. |
| [WdfCmResourceListInsertDescriptor function](..\wdfresource\nf-wdfresource-wdfcmresourcelistinsertdescriptor.md) | The WdfCmResourceListInsertDescriptor method inserts a resource descriptor into a specified resource list. |
| [WdfIoResourceRequirementsListRemoveByIoResList function](..\wdfresource\nf-wdfresource-wdfioresourcerequirementslistremovebyioreslist.md) | The WdfIoResourceRequirementsListRemoveByIoResList method removes a logical configuration from a resource requirements list. |
| [WdfIoResourceRequirementsListSetInterfaceType function](..\wdfresource\nf-wdfresource-wdfioresourcerequirementslistsetinterfacetype.md) | The WdfIoResourceRequirementsListSetInterfaceType method assigns a bus type to a resource requirements list. |
| [WdfIoResourceListUpdateDescriptor function](..\wdfresource\nf-wdfresource-wdfioresourcelistupdatedescriptor.md) | The WdfIoResourceListUpdateDescriptor method updates a resource descriptor in a resource requirements list's logical configuration. |
| [WdfIoResourceRequirementsListRemove function](..\wdfresource\nf-wdfresource-wdfioresourcerequirementslistremove.md) | The WdfIoResourceRequirementsListRemove method removes a logical configuration from a resource requirements list. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfStringGetUnicodeString function](..\wdfstring\nf-wdfstring-wdfstringgetunicodestring.md) | The WdfStringGetUnicodeString method retrieves the Unicode string that is assigned to a specified framework string object. |
| [WdfStringCreate function](..\wdfstring\nf-wdfstring-wdfstringcreate.md) | The WdfStringCreate method creates a framework string object and optionally assigns a specified Unicode string to the object. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfWaitLockAcquire function](..\wdfsync\nf-wdfsync-wdfwaitlockacquire.md) | The WdfWaitLockAcquire method acquires a specified wait lock. |
| [WdfSpinLockCreate function](..\wdfsync\nf-wdfsync-wdfspinlockcreate.md) | The WdfSpinLockCreate method creates a framework spin-lock object. |
| [WdfWaitLockCreate function](..\wdfsync\nf-wdfsync-wdfwaitlockcreate.md) | The WdfWaitLockCreate method creates a framework wait-lock object. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfTimerStart function](..\wdftimer\nf-wdftimer-wdftimerstart.md) | The WdfTimerStart method starts a timer's clock. |
| [WdfTimerGetParentObject function](..\wdftimer\nf-wdftimer-wdftimergetparentobject.md) | The WdfTimerGetParentObject method returns a handle to the parent object of a specified framework timer object. |
| [WdfTimerStop function](..\wdftimer\nf-wdftimer-wdftimerstop.md) | The WdfTimerStop method stops a timer's clock. |
| [WdfTimerCreate function](..\wdftimer\nf-wdftimer-wdftimercreate.md) | The WdfTimerCreate method creates a framework timer object. |
| [WDF_TIMER_CONFIG_INIT function](..\wdftimer\nf-wdftimer-wdf-timer-config-init.md) | The WDF_TIMER_CONFIG_INIT function initializes a WDF_TIMER_CONFIG structure for a timer that will use a single due time. |
| [WDF_TIMER_CONFIG_INIT_PERIODIC function](..\wdftimer\nf-wdftimer-wdf-timer-config-init-periodic.md) | The WDF_TIMER_CONFIG_INIT_PERIODIC function initializes a WDF_TIMER_CONFIG structure for a periodic timer. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_TIMER_CONFIG structure](..\wdftimer\ns-wdftimer--wdf-timer-config.md) | The WDF_TIMER_CONFIG structure contains configuration information for a framework timer object. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_TRI_STATE enumeration](..\wdftypes\ne-wdftypes--wdf-tri-state.md) | The WDF_TRI_STATE enumeration type defines three values that the framework uses for some structure members and function parameters. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfUsbInterfaceGetEndpointInformation function](..\wdfusb\nf-wdfusb-wdfusbinterfacegetendpointinformation.md) | The WdfUsbInterfaceGetEndpointInformation method retrieves information about a specified USB device endpoint and its associated pipe. |
| [WdfUsbTargetDeviceCyclePortSynchronously function](..\wdfusb\nf-wdfusb-wdfusbtargetdevicecycleportsynchronously.md) | The WdfUsbTargetDeviceCyclePortSynchronously method power-cycles the USB port to which a specified device is attached. |
| [WdfUsbTargetPipeFormatRequestForReset function](..\wdfusb\nf-wdfusb-wdfusbtargetpipeformatrequestforreset.md) | The WdfUsbTargetPipeFormatRequestForReset method builds a reset request for a specified USB pipe, but it does not send the request. |
| [WdfUsbTargetPipeGetIoTarget function](..\wdfusb\nf-wdfusb-wdfusbtargetpipegetiotarget.md) | The WdfUsbTargetPipeGetIoTarget method returns a handle to the I/O target object that is associated with a specified USB pipe. |
| [WdfUsbTargetDeviceResetPortSynchronously function](..\wdfusb\nf-wdfusb-wdfusbtargetdeviceresetportsynchronously.md) | The WdfUsbTargetDeviceResetPortSynchronously method resets the USB port that is associated with the specified USB device. |
| [WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_DESCRIPTOR function](..\wdfusb\nf-wdfusb-wdf-usb-interface-select-setting-params-init-descriptor.md) | The WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_DESCRIPTOR function initializes a WDF_USB_INTERFACE_SELECT_SETTING_PARAMS structure so that a driver can select a USB interface by specifying an interface descriptor. |
| [WdfUsbTargetPipeGetInformation function](..\wdfusb\nf-wdfusb-wdfusbtargetpipegetinformation.md) | The WdfUsbTargetPipeGetInformation method retrieves information about a USB pipe and its endpoint. |
| [WdfUsbTargetDeviceFormatRequestForControlTransfer function](..\wdfusb\nf-wdfusb-wdfusbtargetdeviceformatrequestforcontroltransfer.md) | The WdfUsbTargetDeviceFormatRequestForControlTransfer method builds a USB control transfer request, but it does not send the request. |
| [WdfUsbInterfaceGetConfiguredPipe function](..\wdfusb\nf-wdfusb-wdfusbinterfacegetconfiguredpipe.md) | The WdfUsbInterfaceGetConfiguredPipe method returns a handle to the framework pipe object that is associated with a specified USB device interface and pipe index. Optionally, the method also returns information about the pipe. |
| [WdfUsbTargetDeviceRetrieveCurrentFrameNumber function](..\wdfusb\nf-wdfusb-wdfusbtargetdeviceretrievecurrentframenumber.md) | The WdfUsbTargetDeviceRetrieveCurrentFrameNumber method retrieves the current USB frame number. |
| [WdfUsbTargetPipeIsOutEndpoint function](..\wdfusb\nf-wdfusb-wdfusbtargetpipeisoutendpoint.md) | The WdfUsbTargetPipeIsOutEndpoint method determines whether a specified USB pipe is connected to an output endpoint. |
| [WdfUsbTargetDeviceGetInterface function](..\wdfusb\nf-wdfusb-wdfusbtargetdevicegetinterface.md) | The WdfUsbTargetDeviceGetInterface method returns a handle to the framework USB interface object that is associated with a specified interface index. |
| [WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_SINGLE_INTERFACE function](..\wdfusb\nf-wdfusb-wdf-usb-device-select-config-params-init-single-interface.md) | The WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_SINGLE_INTERFACE function initializes a WDF_USB_DEVICE_SELECT_CONFIG_PARAMS structure so that a driver can configure a device to use a single, specified interface. |
| [WdfUsbTargetDeviceGetDeviceDescriptor function](..\wdfusb\nf-wdfusb-wdfusbtargetdevicegetdevicedescriptor.md) | The WdfUsbTargetDeviceGetDeviceDescriptor method retrieves the USB device descriptor for the USB device that is associated with a specified framework USB device object. |
| [WdfUsbInterfaceGetNumEndpoints function](..\wdfusb\nf-wdfusb-wdfusbinterfacegetnumendpoints.md) | The WdfUsbInterfaceGetNumEndpoints method returns the number of endpoints that are associated with a specified alternate setting of a specified USB interface. |
| [WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS function](..\wdfusb\nf-wdfusb-wdf-usb-device-select-config-params-init-interfaces-descriptors.md) | The WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_INTERFACES_DESCRIPTORS function initializes a WDF_USB_DEVICE_SELECT_CONFIG_PARAMS structure so that a driver can specify a configuration by using USB descriptors. |
| [WdfUsbTargetDeviceGetNumInterfaces function](..\wdfusb\nf-wdfusb-wdfusbtargetdevicegetnuminterfaces.md) | The WdfUsbTargetDeviceGetNumInterfaces method returns the number of USB device interfaces that are supported by a specified USB device. |
| [WdfUsbTargetDeviceSelectConfig function](..\wdfusb\nf-wdfusb-wdfusbtargetdeviceselectconfig.md) | The WdfUsbTargetDeviceSelectConfig method selects a USB configuration for a device, or it deconfigures the device. |
| [WdfUsbTargetDeviceCreateIsochUrb function](..\wdfusb\nf-wdfusb-wdfusbtargetdevicecreateisochurb.md) | The WdfUsbTargetDeviceCreateIsochUrb method allocates an isochronous USB request block (URB). |
| [WdfUsbTargetDeviceAllocAndQueryString function](..\wdfusb\nf-wdfusb-wdfusbtargetdeviceallocandquerystring.md) | The WdfUsbTargetDeviceAllocAndQueryString method allocates a buffer, then it retrieves the Unicode string that is associated with a specified USB device and descriptor index value. |
| [WdfUsbTargetDeviceCreateWithParameters function](..\wdfusb\nf-wdfusb-wdfusbtargetdevicecreatewithparameters.md) | The WdfUsbTargetDeviceCreateWithParameters method creates a framework USB device object for a specified framework device object and opens the USB device for I/O operations. |
| [WdfUsbTargetPipeAbortSynchronously function](..\wdfusb\nf-wdfusb-wdfusbtargetpipeabortsynchronously.md) | The WdfUsbTargetPipeAbortSynchronously method builds an abort request and sends it synchronously to a specified USB pipe. |
| [WdfUsbTargetPipeFormatRequestForRead function](..\wdfusb\nf-wdfusb-wdfusbtargetpipeformatrequestforread.md) | The WdfUsbTargetPipeFormatRequestForRead method builds a read request for a USB input pipe, but it does not send the request. |
| [WdfUsbTargetDeviceSendUrbSynchronously function](..\wdfusb\nf-wdfusb-wdfusbtargetdevicesendurbsynchronously.md) | The WdfUsbTargetDeviceSendUrbSynchronously method sends a USB request synchronously to a specified USB device, using request parameters that are described by a URB. |
| [WdfUsbTargetDeviceCreateUrb function](..\wdfusb\nf-wdfusb-wdfusbtargetdevicecreateurb.md) | The WdfUsbTargetDeviceCreateUrb method allocates a USB request block (URB). |
| [WdfUsbInterfaceGetDescriptor function](..\wdfusb\nf-wdfusb-wdfusbinterfacegetdescriptor.md) | The WdfUsbInterfaceGetDescriptor method retrieves the USB interface descriptor that is associated with a specified alternate setting of a specified USB interface. |
| [WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_SETTING function](..\wdfusb\nf-wdfusb-wdf-usb-interface-select-setting-params-init-setting.md) | The WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_SETTING function initializes a WDF_USB_INTERFACE_SELECT_SETTING_PARAMS structure so that a driver can select a USB interface by specifying a handle to an interface object and an alternate setting for the interface. |
| [WdfUsbTargetDeviceWdmGetConfigurationHandle function](..\wdfusb\nf-wdfusb-wdfusbtargetdevicewdmgetconfigurationhandle.md) | The WdfUsbTargetDeviceWdmGetConfigurationHandle method returns the USBD_CONFIGURATION_HANDLE-typed handle that is associated with the current configuration of a specified USB device. |
| [WdfUsbTargetPipeSetNoMaximumPacketSizeCheck function](..\wdfusb\nf-wdfusb-wdfusbtargetpipesetnomaximumpacketsizecheck.md) | The WdfUsbTargetPipeSetNoMaximumPacketSizeCheck method disables the framework's test of whether the size of a driver's read buffer is a multiple of a USB pipe's maximum packet size. |
| [WdfUsbTargetDeviceCreate function](..\wdfusb\nf-wdfusb-wdfusbtargetdevicecreate.md) | The WdfUsbTargetDeviceCreate method creates a framework USB device object for a specified framework device object and opens the USB device for I/O operations. |
| [WdfUsbTargetDeviceIsConnectedSynchronous function](..\wdfusb\nf-wdfusb-wdfusbtargetdeviceisconnectedsynchronous.md) | The WdfUsbTargetDeviceIsConnectedSynchronous method determines if the specified USB device is connected. |
| [WdfUsbInterfaceGetNumSettings function](..\wdfusb\nf-wdfusb-wdfusbinterfacegetnumsettings.md) | The WdfUsbInterfaceGetNumSettings method returns the number of alternate settings that a specified USB interface supports. |
| [WdfUsbTargetDeviceFormatRequestForString function](..\wdfusb\nf-wdfusb-wdfusbtargetdeviceformatrequestforstring.md) | The WdfUsbTargetDeviceFormatRequestForString method builds a request for the USB string descriptor that is associated with a USB device's string index value. |
| [WdfUsbInterfaceGetNumConfiguredPipes function](..\wdfusb\nf-wdfusb-wdfusbinterfacegetnumconfiguredpipes.md) | The WdfUsbInterfaceGetNumConfiguredPipes method returns the number of pipes that are configured for a specified USB device interface. |
| [WdfUsbTargetDeviceRetrieveInformation function](..\wdfusb\nf-wdfusb-wdfusbtargetdeviceretrieveinformation.md) | The WdfUsbTargetDeviceRetrieveInformation method retrieves information about the USB device that is associated with a specified framework USB device object. |
| [WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_URB function](..\wdfusb\nf-wdfusb-wdf-usb-interface-select-setting-params-init-urb.md) | The WDF_USB_INTERFACE_SELECT_SETTING_PARAMS_INIT_URB function initializes a WDF_USB_INTERFACE_SELECT_SETTING_PARAMS structure so that a driver can select a USB interface by specifying a URB. |
| [WdfUsbTargetDeviceGetIoTarget function](..\wdfusb\nf-wdfusb-wdfusbtargetdevicegetiotarget.md) | The WdfUsbTargetDeviceGetIoTarget method returns a handle to the I/O target object that is associated with a specified USB device. |
| [WDF_USB_CONTINUOUS_READER_CONFIG_INIT function](..\wdfusb\nf-wdfusb-wdf-usb-continuous-reader-config-init.md) | The WDF_USB_CONTINUOUS_READER_CONFIG_INIT function initializes a WDF_USB_CONTINUOUS_READER_CONFIG structure. |
| [WdfUsbTargetDeviceQueryUsbCapability function](..\wdfusb\nf-wdfusb-wdfusbtargetdevicequeryusbcapability.md) | The WdfUsbTargetDeviceQueryUsbCapability method determines whether the host controller and USB driver stack support a specific capability. |
| [WDF_USB_PIPE_DIRECTION_OUT function](..\wdfusb\nf-wdfusb-wdf-usb-pipe-direction-out.md) | The WDF_USB_PIPE_DIRECTION_OUT function determines whether a specified USB endpoint is an output endpoint. |
| [WdfUsbTargetPipeWriteSynchronously function](..\wdfusb\nf-wdfusb-wdfusbtargetpipewritesynchronously.md) | The WdfUsbTargetPipeWriteSynchronously method builds a write request and sends it synchronously to a specified USB output pipe. |
| [WdfUsbTargetPipeIsInEndpoint function](..\wdfusb\nf-wdfusb-wdfusbtargetpipeisinendpoint.md) | The WdfUsbTargetPipeIsInEndpoint method determines whether a specified USB pipe is connected to an input endpoint. |
| [WdfUsbTargetDeviceRetrieveConfigDescriptor function](..\wdfusb\nf-wdfusb-wdfusbtargetdeviceretrieveconfigdescriptor.md) | The WdfUsbTargetDeviceRetrieveConfigDescriptor method retrieves the USB configuration descriptor for the USB device that is associated with a specified framework USB device object. |
| [WDF_USB_PIPE_INFORMATION_INIT function](..\wdfusb\nf-wdfusb-wdf-usb-pipe-information-init.md) | The WDF_USB_PIPE_INFORMATION_INIT function initializes a WDF_USB_PIPE_INFORMATION structure. |
| [WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_URB function](..\wdfusb\nf-wdfusb-wdf-usb-device-select-config-params-init-urb.md) | The WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_URB function initializes a WDF_USB_DEVICE_SELECT_CONFIG_PARAMS structure so that a driver can specify a configuration by using a URB. |
| [WdfUsbTargetPipeConfigContinuousReader function](..\wdfusb\nf-wdfusb-wdfusbtargetpipeconfigcontinuousreader.md) | The WdfUsbTargetPipeConfigContinuousReader method configures the framework to continuously read from a specified USB pipe. |
| [WdfUsbTargetDeviceSendControlTransferSynchronously function](..\wdfusb\nf-wdfusb-wdfusbtargetdevicesendcontroltransfersynchronously.md) | The WdfUsbTargetDeviceSendControlTransferSynchronously method builds a USB control transfer request and sends it synchronously to an I/O target. |
| [WDF_USB_CONTROL_SETUP_PACKET_INIT function](..\wdfusb\nf-wdfusb-wdf-usb-control-setup-packet-init.md) | The WDF_USB_CONTROL_SETUP_PACKET_INIT function initializes a WDF_USB_CONTROL_SETUP_PACKET structure for a standard USB control transfer. |
| [WdfUsbTargetPipeFormatRequestForUrb function](..\wdfusb\nf-wdfusb-wdfusbtargetpipeformatrequestforurb.md) | The WdfUsbTargetPipeFormatRequestForUrb method builds an USB request for a specified USB pipe, using request parameters that a specified URB describes, but it does not send the request. |
| [WdfUsbInterfaceGetInterfaceNumber function](..\wdfusb\nf-wdfusb-wdfusbinterfacegetinterfacenumber.md) | The WdfUsbInterfaceGetInterfaceNumber method returns the interface number of a specified USB interface object. |
| [WdfUsbInterfaceGetConfiguredSettingIndex function](..\wdfusb\nf-wdfusb-wdfusbinterfacegetconfiguredsettingindex.md) | The WdfUsbInterfaceGetConfiguredSettingIndex method returns the alternate setting index that is currently selected for a specified USB device interface. |
| [WdfUsbTargetDeviceQueryString function](..\wdfusb\nf-wdfusb-wdfusbtargetdevicequerystring.md) | The WdfUsbTargetDeviceQueryString method retrieves the Unicode string that is associated with a specified USB device and descriptor index value. |
| [WdfUsbTargetPipeSendUrbSynchronously function](..\wdfusb\nf-wdfusb-wdfusbtargetpipesendurbsynchronously.md) | The WdfUsbTargetPipeSendUrbSynchronously method builds an USB request for a specified USB pipe, using request parameters that a specified URB describes. |
| [WDF_USB_CONTROL_SETUP_PACKET_INIT_CLASS function](..\wdfusb\nf-wdfusb-wdf-usb-control-setup-packet-init-class.md) | The WDF_USB_CONTROL_SETUP_PACKET_INIT_CLASS function initializes a WDF_USB_CONTROL_SETUP_PACKET structure for a device class-specific USB control transfer. |
| [WDF_USB_CONTROL_SETUP_PACKET_INIT_VENDOR function](..\wdfusb\nf-wdfusb-wdf-usb-control-setup-packet-init-vendor.md) | The WDF_USB_CONTROL_SETUP_PACKET_INIT_VENDOR function initializes a WDF_USB_CONTROL_SETUP_PACKET structure for a vendor-specific USB control transfer. |
| [WDF_USB_DEVICE_INFORMATION_INIT function](..\wdfusb\nf-wdfusb-wdf-usb-device-information-init.md) | The WDF_USB_DEVICE_INFORMATION_INIT function initializes a driver's WDF_USB_DEVICE_INFORMATION structure. |
| [WDF_USB_PIPE_DIRECTION_IN function](..\wdfusb\nf-wdfusb-wdf-usb-pipe-direction-in.md) | The WDF_USB_PIPE_DIRECTION_IN function determines whether a specified USB endpoint is an input endpoint. |
| [WDF_USB_CONTROL_SETUP_PACKET_INIT_GET_STATUS function](..\wdfusb\nf-wdfusb-wdf-usb-control-setup-packet-init-get-status.md) | The WDF_USB_CONTROL_SETUP_PACKET_INIT_GET_STATUS function initializes a WDF_USB_CONTROL_SETUP_PACKET structure for a USB control transfer that obtains device status. |
| [WdfUsbTargetPipeGetType function](..\wdfusb\nf-wdfusb-wdfusbtargetpipegettype.md) | The WdfUsbTargetPipeGetType method returns the type of a specified USB pipe. |
| [WDF_USB_DEVICE_CREATE_CONFIG_INIT function](..\wdfusb\nf-wdfusb-wdf-usb-device-create-config-init.md) | The WDF_USB_DEVICE_CREATE_CONFIG_INIT function initializes a WDF_USB_DEVICE_CREATE_CONFIG structure. |
| [WdfUsbTargetDeviceFormatRequestForCyclePort function](..\wdfusb\nf-wdfusb-wdfusbtargetdeviceformatrequestforcycleport.md) | The WdfUsbTargetDeviceFormatRequestForCyclePort method builds a power-cycle request for the port to which a specified device is attached, but it does not send the request. |
| [WdfUsbTargetPipeWdmGetPipeHandle function](..\wdfusb\nf-wdfusb-wdfusbtargetpipewdmgetpipehandle.md) | The WdfUsbTargetPipeWdmGetPipeHandle method returns the USBD_PIPE_HANDLE-typed handle that is associated with a specified framework pipe object. |
| [WdfUsbTargetPipeReadSynchronously function](..\wdfusb\nf-wdfusb-wdfusbtargetpipereadsynchronously.md) | The WdfUsbTargetPipeReadSynchronously method builds a read request and sends it synchronously to a specified USB input pipe. |
| [WdfUsbInterfaceSelectSetting function](..\wdfusb\nf-wdfusb-wdfusbinterfaceselectsetting.md) | The WdfUsbInterfaceSelectSetting method selects a specified alternate setting for a specified USB interface. |
| [WdfUsbTargetPipeFormatRequestForAbort function](..\wdfusb\nf-wdfusb-wdfusbtargetpipeformatrequestforabort.md) | The WdfUsbTargetPipeFormatRequestForAbort method builds an abort request for a specified USB pipe, but it does not send the request. |
| [WdfUsbTargetPipeResetSynchronously function](..\wdfusb\nf-wdfusb-wdfusbtargetpiperesetsynchronously.md) | The WdfUsbTargetPipeResetSynchronously method builds a reset request and sends it synchronously to a specified USB pipe. |
| [WdfUsbTargetDeviceFormatRequestForUrb function](..\wdfusb\nf-wdfusb-wdfusbtargetdeviceformatrequestforurb.md) | The WdfUsbTargetDeviceFormatRequestForUrb method builds an USB request for a specified USB device, using request parameters that are described by a URB, but it does not send the request. |
| [WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_MULTIPLE_INTERFACES function](..\wdfusb\nf-wdfusb-wdf-usb-device-select-config-params-init-multiple-interfaces.md) | The WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_MULTIPLE_INTERFACES function initializes a WDF_USB_DEVICE_SELECT_CONFIG_PARAMS structure so that a driver can configure a device to use multiple interfaces. |
| [WdfUsbTargetPipeFormatRequestForWrite function](..\wdfusb\nf-wdfusb-wdfusbtargetpipeformatrequestforwrite.md) | The WdfUsbTargetPipeFormatRequestForWrite method builds a write request for a USB output pipe, but it does not send the request. |
| [WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_DECONFIG function](..\wdfusb\nf-wdfusb-wdf-usb-device-select-config-params-init-deconfig.md) | The WDF_USB_DEVICE_SELECT_CONFIG_PARAMS_INIT_DECONFIG function initializes a WDF_USB_DEVICE_SELECT_CONFIG_PARAMS structure so that a driver can deconfigure a USB device. |
| [WDF_USB_CONTROL_SETUP_PACKET_INIT_FEATURE function](..\wdfusb\nf-wdfusb-wdf-usb-control-setup-packet-init-feature.md) | The WDF_USB_CONTROL_SETUP_PACKET_INIT_FEATURE function initializes a WDF_USB_CONTROL_SETUP_PACKET structure for a USB control transfer that sets or clears a device feature. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_USB_CONTROL_SETUP_PACKET structure](..\wdfusb\ns-wdfusb--wdf-usb-control-setup-packet.md) | The WDF_USB_CONTROL_SETUP_PACKET structure describes a setup packet for a USB control transfer. |
| [WDF_USB_INTERFACE_SETTING_PAIR structure](..\wdfusb\ns-wdfusb--wdf-usb-interface-setting-pair.md) | The WDF_USB_INTERFACE_SETTING_PAIR structure specifies an alternate setting for a specified USB interface. |
| [WDF_USB_DEVICE_CREATE_CONFIG structure](..\wdfusb\ns-wdfusb--wdf-usb-device-create-config.md) | The WDF_USB_DEVICE_CREATE_CONFIG structure contains information that the framework uses to configure a framework USB device object. |
| [WDF_USB_REQUEST_COMPLETION_PARAMS structure](..\wdfusb\ns-wdfusb--wdf-usb-request-completion-params.md) | The WDF_USB_REQUEST_COMPLETION_PARAMS structure contains parameters that are associated with the completion of an I/O request for a USB device. |
| [WDF_USB_PIPE_INFORMATION structure](..\wdfusb\ns-wdfusb--wdf-usb-pipe-information.md) | The WDF_USB_PIPE_INFORMATION structure contains information about a USB pipe and its endpoint. |
| [WDF_USB_CONTINUOUS_READER_CONFIG structure](..\wdfusb\ns-wdfusb--wdf-usb-continuous-reader-config.md) | The WDF_USB_CONTINUOUS_READER_CONFIG structure contains information that the framework uses to configure a continuous reader for a USB pipe. |
| [WDF_USB_DEVICE_INFORMATION structure](..\wdfusb\ns-wdfusb--wdf-usb-device-information.md) | The WDF_USB_DEVICE_INFORMATION structure contains version and capability information for a USB device. |
| [WDF_USB_INTERFACE_SELECT_SETTING_PARAMS structure](..\wdfusb\ns-wdfusb--wdf-usb-interface-select-setting-params.md) | The WDF_USB_INTERFACE_SELECT_SETTING_PARAMS structure contains selection information for a USB interface. |
| [WDF_USB_DEVICE_SELECT_CONFIG_PARAMS structure](..\wdfusb\ns-wdfusb--wdf-usb-device-select-config-params.md) | The WDF_USB_DEVICE_SELECT_CONFIG_PARAMS structure specifies USB device configuration parameters. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_WDF_USB_READERS_FAILED callback](..\wdfusb\nc-wdfusb-evt-wdf-usb-readers-failed.md) | A driver's EvtUsbTargetPipeReadersFailed event callback function informs the driver that a continuous reader has reported an error while processing a read request. |
| [EVT_WDF_USB_READER_COMPLETION_ROUTINE callback](..\wdfusb\nc-wdfusb-evt-wdf-usb-reader-completion-routine.md) | A driver's EvtUsbTargetPipeReadComplete event callback function informs the driver that a continuous reader has successfully completed a read request. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_USB_REQUEST_TYPE enumeration](..\wdfusb\ne-wdfusb--wdf-usb-request-type.md) | The WDF_USB_REQUEST_TYPE enumeration identifies the types of USB requests that a framework-based driver can send to a USB I/O target. |
| [WdfUsbTargetDeviceSelectConfigType enumeration](..\wdfusb\ne-wdfusb--wdfusbtargetdeviceselectconfigtype.md) | The WdfUsbTargetDeviceSelectConfigType enumeration defines types of configuration operations for USB devices. |
| [WDF_USB_PIPE_TYPE enumeration](..\wdfusb\ne-wdfusb--wdf-usb-pipe-type.md) | The WDF_USB_PIPE_TYPE enumeration identifies the types of USB pipes. |
| [WDF_USB_DEVICE_TRAITS enumeration](..\wdfusb\ne-wdfusb--wdf-usb-device-traits.md) | The WDF_USB_DEVICE_TRAITS enumeration identifies USB device traits. |
| [WDF_USB_BMREQUEST_RECIPIENT enumeration](..\wdfusb\ne-wdfusb--wdf-usb-bmrequest-recipient.md) | The WDF_USB_BMREQUEST_RECIPIENT enumeration identifies the data transfer recipient for a USB control transfer. |
| [WDF_USB_BMREQUEST_TYPE enumeration](..\wdfusb\ne-wdfusb--wdf-usb-bmrequest-type.md) | The WDF_USB_BMREQUEST_TYPE enumeration identifies the data transfer type for a USB control transfer. |
| [WdfUsbTargetDeviceSelectSettingType enumeration](..\wdfusb\ne-wdfusb--wdfusbtargetdeviceselectsettingtype.md) | The WdfUsbTargetDeviceSelectSettingType enumeration defines techniques for specifying an alternate setting for a USB interface. |
| [WDF_USB_BMREQUEST_DIRECTION enumeration](..\wdfusb\ne-wdfusb--wdf-usb-bmrequest-direction.md) | The WDF_USB_BMREQUEST_DIRECTION enumeration identifies the data transfer direction for a USB control transfer. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfGetTriageInfo function](..\wdfverifier\nf-wdfverifier-wdfgettriageinfo.md) | The WdfGetTriageInfo method is reserved for internal use only. |
| [WdfVerifierKeBugCheck function](..\wdfverifier\nf-wdfverifier-wdfverifierkebugcheck.md) | The WdfVerifierKeBugCheck function creates a bug check. |
| [WdfVerifierDbgBreakPoint function](..\wdfverifier\nf-wdfverifier-wdfverifierdbgbreakpoint.md) | The WdfVerifierDbgBreakPoint function breaks into a kernel debugger, if a debugger is running. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_WMI_PROVIDER_FLAGS enumeration](..\wdfwmi\ne-wdfwmi--wdf-wmi-provider-flags.md) | The WDF_WMI_PROVIDER_FLAGS enumeration defines configuration flags for a driver's WMI data provider. |
| [WDF_WMI_PROVIDER_CONTROL enumeration](..\wdfwmi\ne-wdfwmi--wdf-wmi-provider-control.md) | The WDF_WMI_PROVIDER_CONTROL enumeration defines the type of control functions that a WMI data provider can support. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_WMI_BUFFER_APPEND_STRING function](..\wdfwmi\nf-wdfwmi-wdf-wmi-buffer-append-string.md) | The WDF_WMI_BUFFER_APPEND_STRING function copies a specified Unicode string into a specified buffer in the format that WMI requires. |
| [WdfWmiInstanceFireEvent function](..\wdfwmi\nf-wdfwmi-wdfwmiinstancefireevent.md) | The WdfWmiInstanceFireEvent method sends a WMI event to WMI clients that have registered to receive event notification. |
| [WdfWmiInstanceGetDevice function](..\wdfwmi\nf-wdfwmi-wdfwmiinstancegetdevice.md) | The WdfWmiInstanceGetDevice method returns a handle to the framework device object that is associated with a specified WMI instance object. |
| [WdfWmiInstanceGetProvider function](..\wdfwmi\nf-wdfwmi-wdfwmiinstancegetprovider.md) | The WdfWmiInstanceGetProvider method returns a handle to the WMI provider object that is the parent object of a specified WMI instance object. |
| [WDF_WMI_INSTANCE_CONFIG_INIT_PROVIDER function](..\wdfwmi\nf-wdfwmi-wdf-wmi-instance-config-init-provider.md) | The WDF_WMI_INSTANCE_CONFIG_INIT_PROVIDER function initializes a WDF_WMI_INSTANCE_CONFIG structure and stores a specified handle to a WMI provider object. |
| [WdfWmiInstanceCreate function](..\wdfwmi\nf-wdfwmi-wdfwmiinstancecreate.md) | The WdfWmiInstanceCreate method creates a WMI instance object that represents an instance of a WMI data provider. |
| [WdfWmiProviderGetDevice function](..\wdfwmi\nf-wdfwmi-wdfwmiprovidergetdevice.md) | The WdfWmiProviderGetDevice method returns a handle to the framework device object that is the parent of a specified WMI provider object. |
| [WdfWmiProviderCreate function](..\wdfwmi\nf-wdfwmi-wdfwmiprovidercreate.md) | The WdfWmiProviderCreate method creates a WMI provider object that represents a WMI data block. |
| [WdfWmiProviderGetTracingHandle function](..\wdfwmi\nf-wdfwmi-wdfwmiprovidergettracinghandle.md) | The WdfWmiProviderGetTracingHandle method returns a handle to the event logger of a WPP software tracing session. |
| [WDF_WMI_INSTANCE_CONFIG_INIT_PROVIDER_CONFIG function](..\wdfwmi\nf-wdfwmi-wdf-wmi-instance-config-init-provider-config.md) | The WDF_WMI_INSTANCE_CONFIG_INIT_PROVIDER_CONFIG function initializes a WDF_WMI_INSTANCE_CONFIG structure and stores a pointer to a specified WDF_WMI_PROVIDER_CONFIG structure. |
| [WdfWmiProviderIsEnabled function](..\wdfwmi\nf-wdfwmi-wdfwmiproviderisenabled.md) | The WdfWmiProviderIsEnabled method determines if either data collection or event notification is enabled for a specified WMI data provider. |
| [WdfWmiInstanceDeregister function](..\wdfwmi\nf-wdfwmi-wdfwmiinstancederegister.md) | The WdfWmiInstanceDeregister method deregisters a specified instance of a WMI data provider from the system's WMI service. |
| [WdfWmiInstanceRegister function](..\wdfwmi\nf-wdfwmi-wdfwmiinstanceregister.md) | The WdfWmiInstanceRegister method registers a specified instance of a WMI data provider with the system's WMI service. |
| [WDF_WMI_PROVIDER_CONFIG_INIT function](..\wdfwmi\nf-wdfwmi-wdf-wmi-provider-config-init.md) | The WDF_WMI_PROVIDER_CONFIG_INIT function initializes a WDF_WMI_PROVIDER_CONFIG structure. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_WDF_WMI_INSTANCE_SET_ITEM callback](..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-instance-set-item.md) | A driver's EvtWmiInstanceSetItem callback function sets a single item of a WMI data provider's instance data to a value that a WMI client supplies. |
| [EVT_WDF_WMI_PROVIDER_FUNCTION_CONTROL callback](..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-provider-function-control.md) | A driver's EvtWmiProviderFunctionControl callback function enables and disables the driver's support for collecting data and sending events for a specified WMI data provider. |
| [EVT_WDF_WMI_INSTANCE_SET_INSTANCE callback](..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-instance-set-instance.md) | A driver's EvtWmiInstanceSetInstance callback function sets all of a WMI data provider's instance data to values that a WMI client supplies. |
| [EVT_WDF_WMI_INSTANCE_EXECUTE_METHOD callback](..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-instance-execute-method.md) | A driver's EvtWmiInstanceExecuteMethod callback function executes a specified method that the driver provides for a WMI data provider's instance. |
| [EVT_WDF_WMI_INSTANCE_QUERY_INSTANCE callback](..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-instance-query-instance.md) | A driver's EvtWmiInstanceQueryInstance callback function copies a WMI provider's instance data into a buffer for delivery to a WMI client. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_WMI_INSTANCE_CONFIG structure](..\wdfwmi\ns-wdfwmi--wdf-wmi-instance-config.md) | The WDF_WMI_INSTANCE_CONFIG structure contains configuration information for an instance of a WMI data provider. |
| [WDF_WMI_PROVIDER_CONFIG structure](..\wdfwmi\ns-wdfwmi--wdf-wmi-provider-config.md) | The WDF_WMI_PROVIDER_CONFIG structure contains configuration information for a driver's WMI data block. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfWorkItemCreate function](..\wdfworkitem\nf-wdfworkitem-wdfworkitemcreate.md) | The WdfWorkItemCreate method creates a framework work-item object, which can subsequently be added to the system's work-item queue. |
| [WDF_WORKITEM_CONFIG_INIT function](..\wdfworkitem\nf-wdfworkitem-wdf-workitem-config-init.md) | The WDF_WORKITEM_CONFIG_INIT function initializes a driver's WDF_WORKITEM_CONFIG structure. |
| [WdfWorkItemGetParentObject function](..\wdfworkitem\nf-wdfworkitem-wdfworkitemgetparentobject.md) | The WdfWorkItemGetParentObject method returns the framework object that a specified work item is associated with. |
| [WdfWorkItemFlush function](..\wdfworkitem\nf-wdfworkitem-wdfworkitemflush.md) | The WdfWorkItemFlush method returns after a specified work item has been serviced. |
| [WdfWorkItemEnqueue function](..\wdfworkitem\nf-wdfworkitem-wdfworkitemenqueue.md) | The WdfWorkItemEnqueue method adds a specified framework work-item object to the system's work-item queue. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_WORKITEM_CONFIG structure](..\wdfworkitem\ns-wdfworkitem--wdf-workitem-config.md) | The WDF_WORKITEM_CONFIG structure contains information that is associated with a work item. |
Interface

| Title        | Description    |
| ------------- |:-------------:|
| [IWDFIoRequestCompletionParams interface](..\wudfddi\nn-wudfddi-iwdfiorequestcompletionparams.md) | The IWDFIoRequestCompletionParams interface exposes methods that drivers can use to obtain completion information about an I/O request. Drivers can call these methods after a synchronous or asynchronous I/O operation completes. |
| [IWDFPropertyStoreFactory interface](..\wudfddi\nn-wudfddi-iwdfpropertystorefactory.md) | The IWDFPropertyStoreFactory interface is a factory interface that is used to create a property store interface. |
| [IFileCallbackClose interface](..\wudfddi\nn-wudfddi-ifilecallbackclose~r1.md) | The framework can notify a driver when the driver should perform a close operation. The driver can handle the notification by registering the IFileCallbackClose interface. |
| [IImpersonateCallback interface](..\wudfddi\nn-wudfddi-iimpersonatecallback~r1.md) | The IImpersonateCallback interface contains a method that handles impersonation. |
| [IWDFIoTarget interface](..\wudfddi\nn-wudfddi-iwdfiotarget.md) | The IWDFIoTarget interface exposes the I/O target object that typically represents a lower driver in the stack. |
| [IRemoteInterfaceCallbackEvent interface](..\wudfddi\nn-wudfddi-iremoteinterfacecallbackevent.md) | The IRemoteInterfaceCallbackEvent interface provides a callback function that the framework calls to notify the driver about device events that are associated with a device interface. |
| [IDriverEntry interface](..\wudfddi\nn-wudfddi-idriverentry~r1.md) | The IDriverEntry interface exposes the user-mode driver's main entry and exit points. |
| [IQueueCallbackIoStop interface](..\wudfddi\nn-wudfddi-iqueuecallbackiostop.md) | The IQueueCallbackIoStop interface contains a method that stops the processing of an I/O request from a queue. |
| [IWDFCmResourceList interface](..\wudfddi\nn-wudfddi-iwdfcmresourcelist.md) | This interface represents a list of hardware resources for a device. |
| [IWDFFile interface](..\wudfddi\nn-wudfddi-iwdffile.md) | The IWDFFile interface exposes the file object that represents the HANDLE that is returned by the Microsoft Win32 CreateFile function. |
| [IWDFDriverCreatedFile interface](..\wudfddi\nn-wudfddi-iwdfdrivercreatedfile~r1.md) | The IWDFDriverCreatedFile interface exposes a UMDF driver-created-file object for the driver to use. |
| [IRemoteInterfaceCallbackRemoval interface](..\wudfddi\nn-wudfddi-iremoteinterfacecallbackremoval.md) | The IRemoteInterfaceCallbackRemoval provides a callback function that the framework calls to notify the driver about the removal of a device interface. |
| [IWDFNamedPropertyStore interface](..\wudfddi\nn-wudfddi-iwdfnamedpropertystore.md) | The IWDFNamedPropertyStore interface exposes a property-store object. |
| [IWDFObject interface](..\wudfddi\nn-wudfddi-iwdfobject~r1.md) | The IWDFObject interface exposes the framework base object that provides the basic functionality common across all framework object types. All framework objects are derived from this root object. |
| [IQueueCallbackIoCanceledOnQueue interface](..\wudfddi\nn-wudfddi-iqueuecallbackiocanceledonqueue~r1.md) | The IQueueCallbackIoCanceledOnQueue interface is optional. Your driver can provide this interface if you want UMDF to notify the driver when an I/O request is canceled while it is in the driver's I/O queue. |
| [IQueueCallbackWrite interface](..\wudfddi\nn-wudfddi-iqueuecallbackwrite.md) | An I/O queue object notifies a driver when a write request is available for the driver. |
| [IWDFFile3 interface](..\wudfddi\nn-wudfddi-iwdffile3.md) | Drivers obtain the IWDFFile3 interface by calling IWDFFile |
| [IFileCallbackCleanup interface](..\wudfddi\nn-wudfddi-ifilecallbackcleanup.md) | The framework can notify a driver when the driver should perform a cleanup operation. |
| [IPnpCallback interface](..\wudfddi\nn-wudfddi-ipnpcallback~r1.md) | The IPnpCallback interface is a Plug and Play (PnP) and power management (PM) interface. |
| [IRemoteInterfaceCallbackEvent interface](..\wudfddi\nn-wudfddi-iremoteinterfacecallbackevent~r1.md) | The IRemoteInterfaceCallbackEvent interface provides a callback function that the framework calls to notify the driver about device events that are associated with a device interface. |
| [IWDFDeviceInitialize2 interface](..\wudfddi\nn-wudfddi-iwdfdeviceinitialize2~r1.md) | The IWDFDeviceInitialize2 interface is a helper interface that allows a driver to specify a preferred buffer retrieval mode and buffer access method. |
| [IQueueCallbackDefaultIoHandler interface](..\wudfddi\nn-wudfddi-iqueuecallbackdefaultiohandler~r1.md) | The IQueueCallbackDefaultIoHandler interface contains a method that handles I/O requests that no other method is registered to handle. |
| [IWDFIoRequest3 interface](..\wudfddi\nn-wudfddi-iwdfiorequest3~r1.md) | To obtain the IWDFIoRequest3 interface, drivers call IWDFIoRequest |
| [IWDFUnifiedPropertyStoreFactory interface](..\wudfddi\nn-wudfddi-iwdfunifiedpropertystorefactory~r1.md) | The IWDFUnifiedPropertyStoreFactory interface is a factory interface that is used to create a unified property store interface. |
| [IWDFIoQueue interface](..\wudfddi\nn-wudfddi-iwdfioqueue.md) | The IWDFIoQueue interface exposes an I/O queue object. |
| [IPnpCallbackRemoteInterfaceNotification interface](..\wudfddi\nn-wudfddi-ipnpcallbackremoteinterfacenotification~r1.md) | A driver's IPnpCallbackRemoteInterfaceNotification interface provides a callback function that the framework calls to notify the driver when a device interface becomes available. |
| [IWDFIoRequest3 interface](..\wudfddi\nn-wudfddi-iwdfiorequest3.md) | To obtain the IWDFIoRequest3 interface, drivers call IWDFIoRequest |
| [IFileCallbackCleanup interface](..\wudfddi\nn-wudfddi-ifilecallbackcleanup~r1.md) | The framework can notify a driver when the driver should perform a cleanup operation. |
| [IQueueCallbackDefaultIoHandler interface](..\wudfddi\nn-wudfddi-iqueuecallbackdefaultiohandler.md) | The IQueueCallbackDefaultIoHandler interface contains a method that handles I/O requests that no other method is registered to handle. |
| [IWDFObject interface](..\wudfddi\nn-wudfddi-iwdfobject.md) | The IWDFObject interface exposes the framework base object that provides the basic functionality common across all framework object types. All framework objects are derived from this root object. |
| [IWDFInterrupt interface](..\wudfddi\nn-wudfddi-iwdfinterrupt~r1.md) | This interface exposes an interrupt object. |
| [IPnpCallbackSelfManagedIo interface](..\wudfddi\nn-wudfddi-ipnpcallbackselfmanagedio~r1.md) | The IPnpCallbackSelfManagedIo interface is a Plug and Play (PnP) and power management (PM) interface. |
| [IQueueCallbackWrite interface](..\wudfddi\nn-wudfddi-iqueuecallbackwrite~r1.md) | An I/O queue object notifies a driver when a write request is available for the driver. |
| [IPowerPolicyCallbackWakeFromS0 interface](..\wudfddi\nn-wudfddi-ipowerpolicycallbackwakefroms0~r1.md) | A driver's IPowerPolicyCallbackWakeFromS0 interface provides callback functions that the framework calls to notify the driver about wake events. |
| [IRequestCallbackCancel interface](..\wudfddi\nn-wudfddi-irequestcallbackcancel~r1.md) | A driver is notified when an I/O request that the driver is currently processing is to be canceled. |
| [IQueueCallbackStateChange interface](..\wudfddi\nn-wudfddi-iqueuecallbackstatechange~r1.md) | An I/O queue object raises an event when it changes state. A driver can consume the event by registering the IQueueCallbackStateChange interface. |
| [IWDFFile2 interface](..\wudfddi\nn-wudfddi-iwdffile2~r1.md) | Drivers obtain the IWDFFile2 interface by calling IWDFFile |
| [IWDFDriver interface](..\wudfddi\nn-wudfddi-iwdfdriver.md) | The IWDFDriver interface exposes the framework driver object that represents the driver image that is loaded in the host process. |
| [IWDFIoRequestCompletionParams interface](..\wudfddi\nn-wudfddi-iwdfiorequestcompletionparams~r1.md) | The IWDFIoRequestCompletionParams interface exposes methods that drivers can use to obtain completion information about an I/O request. Drivers can call these methods after a synchronous or asynchronous I/O operation completes. |
| [IWDFDeviceInitialize interface](..\wudfddi\nn-wudfddi-iwdfdeviceinitialize~r1.md) | The IWDFDeviceInitialize interface is a helper interface that the framework supplies as an input parameter to the driver's IDriverEntry |
| [IRequestCallbackRequestCompletion interface](..\wudfddi\nn-wudfddi-irequestcallbackrequestcompletion~r1.md) | A driver implements the IRequestCallbackRequestCompletion interface to complete a request object. |
| [IQueueCallbackIoStop interface](..\wudfddi\nn-wudfddi-iqueuecallbackiostop~r1.md) | The IQueueCallbackIoStop interface contains a method that stops the processing of an I/O request from a queue. |
| [IWDFRequestCompletionParams interface](..\wudfddi\nn-wudfddi-iwdfrequestcompletionparams~r1.md) | The IWDFRequestCompletionParams interface exposes methods that drivers can use to obtain completion information about an I/O request. Drivers can call these methods after a synchronous or an asynchronous I/O operation completes. |
| [IWDFNamedPropertyStore interface](..\wudfddi\nn-wudfddi-iwdfnamedpropertystore~r1.md) | The IWDFNamedPropertyStore interface exposes a property-store object. |
| [IWDFIoRequest interface](..\wudfddi\nn-wudfddi-iwdfiorequest.md) | The IWDFIoRequest interface exposes an I/O request object. |
| [IWDFFile3 interface](..\wudfddi\nn-wudfddi-iwdffile3~r1.md) | Drivers obtain the IWDFFile3 interface by calling IWDFFile |
| [IWDFRemoteInterfaceInitialize interface](..\wudfddi\nn-wudfddi-iwdfremoteinterfaceinitialize.md) | UMDF-based drivers receive the IWDFRemoteInterfaceInitialize interface as input to an IPnpCallbackRemoteInterfaceNotification |
| [IWDFIoRequest2 interface](..\wudfddi\nn-wudfddi-iwdfiorequest2.md) | To obtain the IWDFIoRequest2 interface, drivers call IWDFIoRequest |
| [IWDFRequestCompletionParams interface](..\wudfddi\nn-wudfddi-iwdfrequestcompletionparams.md) | The IWDFRequestCompletionParams interface exposes methods that drivers can use to obtain completion information about an I/O request. Drivers can call these methods after a synchronous or an asynchronous I/O operation completes. |
| [IWDFDevice interface](..\wudfddi\nn-wudfddi-iwdfdevice.md) | The IWDFDevice interface exposes a device object, which is a representation of a device on the system. |
| [IWDFDeviceInitialize2 interface](..\wudfddi\nn-wudfddi-iwdfdeviceinitialize2.md) | The IWDFDeviceInitialize2 interface is a helper interface that allows a driver to specify a preferred buffer retrieval mode and buffer access method. |
| [IWDFFile interface](..\wudfddi\nn-wudfddi-iwdffile~r1.md) | The IWDFFile interface exposes the file object that represents the HANDLE that is returned by the Microsoft Win32 CreateFile function. |
| [IWDFIoTargetStateManagement interface](..\wudfddi\nn-wudfddi-iwdfiotargetstatemanagement.md) | The IWDFIoTargetStateManagement interface exposes methods that manage and monitor the state of an I/O target object. |
| [IFileCallbackClose interface](..\wudfddi\nn-wudfddi-ifilecallbackclose.md) | The framework can notify a driver when the driver should perform a close operation. The driver can handle the notification by registering the IFileCallbackClose interface. |
| [IPnpCallbackHardware interface](..\wudfddi\nn-wudfddi-ipnpcallbackhardware~r1.md) | The IPnpCallbackHardware interface is a Plug and Play (PnP) and power management (PM) interface. |
| [IWDFUnifiedPropertyStore interface](..\wudfddi\nn-wudfddi-iwdfunifiedpropertystore~r1.md) | The IWDFUnifiedPropertyStore interface exposes a unified property store. |
| [IWDFUnifiedPropertyStore interface](..\wudfddi\nn-wudfddi-iwdfunifiedpropertystore.md) | The IWDFUnifiedPropertyStore interface exposes a unified property store. |
| [IRemoteTargetCallbackRemoval interface](..\wudfddi\nn-wudfddi-iremotetargetcallbackremoval.md) | The IRemoteTargetCallbackRemoval interface provides callback functions that the framework calls to notify the driver about events that are associated with the removal of a remote I/O target. |
| [IWDFRemoteInterfaceInitialize interface](..\wudfddi\nn-wudfddi-iwdfremoteinterfaceinitialize~r1.md) | UMDF-based drivers receive the IWDFRemoteInterfaceInitialize interface as input to an IPnpCallbackRemoteInterfaceNotification |
| [IQueueCallbackRead interface](..\wudfddi\nn-wudfddi-iqueuecallbackread~r1.md) | An I/O queue notifies a driver when a read request is available for the driver. |
| [IWDFFileHandleTargetFactory interface](..\wudfddi\nn-wudfddi-iwdffilehandletargetfactory.md) | The IWDFFileHandleTargetFactory interface is a factory interface that is used to create a file-handle-based target device object. |
| [IWDFIoRequest interface](..\wudfddi\nn-wudfddi-iwdfiorequest~r1.md) | The IWDFIoRequest interface exposes an I/O request object. |
| [IWDFIoTargetStateManagement interface](..\wudfddi\nn-wudfddi-iwdfiotargetstatemanagement~r1.md) | The IWDFIoTargetStateManagement interface exposes methods that manage and monitor the state of an I/O target object. |
| [IPowerPolicyCallbackWakeFromSx interface](..\wudfddi\nn-wudfddi-ipowerpolicycallbackwakefromsx~r1.md) | A driver's IPowerPolicyCallbackWakeFromSx interface provides callback functions that the framework calls to notify the driver about wake events. These events are related to a device's ability to wake both itself and the system from a low-power state. |
| [IWDFDriver interface](..\wudfddi\nn-wudfddi-iwdfdriver~r1.md) | The IWDFDriver interface exposes the framework driver object that represents the driver image that is loaded in the host process. |
| [IWDFIoTarget2 interface](..\wudfddi\nn-wudfddi-iwdfiotarget2.md) | To obtain the IWDFIoTarget2 interface, drivers call IWDFIoTarget |
| [IObjectCleanup interface](..\wudfddi\nn-wudfddi-iobjectcleanup~r1.md) | Any driver that stores a reference-counted COM interface to a WDF object must support the IObjectCleanup interface to prevent interface leakage. Note that drivers, in general, are not required to hold references to WDF objects. |
| [IWDFDevice3 interface](..\wudfddi\nn-wudfddi-iwdfdevice3.md) | To obtain the IWDFDevice3 interface, drivers call IWDFDevice |
| [IPnpCallbackRemoteInterfaceNotification interface](..\wudfddi\nn-wudfddi-ipnpcallbackremoteinterfacenotification.md) | A driver's IPnpCallbackRemoteInterfaceNotification interface provides a callback function that the framework calls to notify the driver when a device interface becomes available. |
| [IWDFIoTarget2 interface](..\wudfddi\nn-wudfddi-iwdfiotarget2~r1.md) | To obtain the IWDFIoTarget2 interface, drivers call IWDFIoTarget |
| [IImpersonateCallback interface](..\wudfddi\nn-wudfddi-iimpersonatecallback.md) | The IImpersonateCallback interface contains a method that handles impersonation. |
| [IRemoteInterfaceCallbackRemoval interface](..\wudfddi\nn-wudfddi-iremoteinterfacecallbackremoval~r1.md) | The IRemoteInterfaceCallbackRemoval provides a callback function that the framework calls to notify the driver about the removal of a device interface. |
| [IPnpCallbackHardware2 interface](..\wudfddi\nn-wudfddi-ipnpcallbackhardware2.md) | The IPnpCallbackHardware2 interface exposes callback methods related to hardware. |
| [IPnpCallbackSelfManagedIo interface](..\wudfddi\nn-wudfddi-ipnpcallbackselfmanagedio.md) | The IPnpCallbackSelfManagedIo interface is a Plug and Play (PnP) and power management (PM) interface. |
| [IWDFFileHandleTargetFactory interface](..\wudfddi\nn-wudfddi-iwdffilehandletargetfactory~r1.md) | The IWDFFileHandleTargetFactory interface is a factory interface that is used to create a file-handle-based target device object. |
| [IWDFFile2 interface](..\wudfddi\nn-wudfddi-iwdffile2.md) | Drivers obtain the IWDFFile2 interface by calling IWDFFile |
| [IWDFIoRequest2 interface](..\wudfddi\nn-wudfddi-iwdfiorequest2~r1.md) | To obtain the IWDFIoRequest2 interface, drivers call IWDFIoRequest |
| [IWDFMemory interface](..\wudfddi\nn-wudfddi-iwdfmemory~r1.md) | The IWDFMemory interface exposes the framework memory object that provides access to a memory block. |
| [IWDFRemoteTarget interface](..\wudfddi\nn-wudfddi-iwdfremotetarget.md) | To obtain the IWDFRemoteTarget interface, drivers call IWDFDevice2 |
| [IWDFCmResourceList interface](..\wudfddi\nn-wudfddi-iwdfcmresourcelist~r1.md) | This interface represents a list of hardware resources for a device. |
| [IPnpCallbackHardwareInterrupt interface](..\wudfddi\nn-wudfddi-ipnpcallbackhardwareinterrupt.md) | The IPnpCallbackHardwareInterrupt interface supports interrupt-related Plug and Play and power management callback methods. |
| [IObjectCleanup interface](..\wudfddi\nn-wudfddi-iobjectcleanup.md) | Any driver that stores a reference-counted COM interface to a WDF object must support the IObjectCleanup interface to prevent interface leakage. Note that drivers, in general, are not required to hold references to WDF objects. |
| [IWDFRemoteInterface interface](..\wudfddi\nn-wudfddi-iwdfremoteinterface.md) | UMDF drivers receive a pointer to this interface by calling the IWDFDevice2 |
| [IWDFWorkItem interface](..\wudfddi\nn-wudfddi-iwdfworkitem~r1.md) | This interface exposes a work item object. |
| [IPnpCallbackHardware2 interface](..\wudfddi\nn-wudfddi-ipnpcallbackhardware2~r1.md) | The IPnpCallbackHardware2 interface exposes callback methods related to hardware. |
| [IWDFMemory interface](..\wudfddi\nn-wudfddi-iwdfmemory.md) | The IWDFMemory interface exposes the framework memory object that provides access to a memory block. |
| [IWDFDevice2 interface](..\wudfddi\nn-wudfddi-iwdfdevice2.md) | Drivers obtain the IWDFDevice2 interface by calling IWDFDevice |
| [IWDFRemoteInterface interface](..\wudfddi\nn-wudfddi-iwdfremoteinterface~r1.md) | UMDF drivers receive a pointer to this interface by calling the IWDFDevice2 |
| [IWDFDevice3 interface](..\wudfddi\nn-wudfddi-iwdfdevice3~r1.md) | To obtain the IWDFDevice3 interface, drivers call IWDFDevice |
| [IPowerPolicyCallbackWakeFromS0 interface](..\wudfddi\nn-wudfddi-ipowerpolicycallbackwakefroms0.md) | A driver's IPowerPolicyCallbackWakeFromS0 interface provides callback functions that the framework calls to notify the driver about wake events. |
| [IWDFRemoteTarget interface](..\wudfddi\nn-wudfddi-iwdfremotetarget~r1.md) | To obtain the IWDFRemoteTarget interface, drivers call IWDFDevice2 |
| [IWDFNamedPropertyStore2 interface](..\wudfddi\nn-wudfddi-iwdfnamedpropertystore2.md) | Drivers obtain the IWDFNamedPropertyStore2 interface by calling IWDFPropertyStoreFactory |
| [IQueueCallbackIoResume interface](..\wudfddi\nn-wudfddi-iqueuecallbackioresume~r1.md) | The IQueueCallbackIoResume interface contains a method that resumes the processing of an I/O request from a queue. |
| [IWDFUnifiedPropertyStoreFactory interface](..\wudfddi\nn-wudfddi-iwdfunifiedpropertystorefactory.md) | The IWDFUnifiedPropertyStoreFactory interface is a factory interface that is used to create a unified property store interface. |
| [IQueueCallbackRead interface](..\wudfddi\nn-wudfddi-iqueuecallbackread.md) | An I/O queue notifies a driver when a read request is available for the driver. |
| [IQueueCallbackCreate interface](..\wudfddi\nn-wudfddi-iqueuecallbackcreate~r1.md) | An I/O queue notifies a driver when an open file request is available for the driver. |
| [IWDFDeviceInitialize interface](..\wudfddi\nn-wudfddi-iwdfdeviceinitialize.md) | The IWDFDeviceInitialize interface is a helper interface that the framework supplies as an input parameter to the driver's IDriverEntry |
| [IWDFWorkItem interface](..\wudfddi\nn-wudfddi-iwdfworkitem.md) | This interface exposes a work item object. |
| [IQueueCallbackStateChange interface](..\wudfddi\nn-wudfddi-iqueuecallbackstatechange.md) | An I/O queue object raises an event when it changes state. A driver can consume the event by registering the IQueueCallbackStateChange interface. |
| [IWDFDevice interface](..\wudfddi\nn-wudfddi-iwdfdevice~r1.md) | The IWDFDevice interface exposes a device object, which is a representation of a device on the system. |
| [IWDFIoQueue interface](..\wudfddi\nn-wudfddi-iwdfioqueue~r1.md) | The IWDFIoQueue interface exposes an I/O queue object. |
| [IQueueCallbackIoCanceledOnQueue interface](..\wudfddi\nn-wudfddi-iqueuecallbackiocanceledonqueue.md) | The IQueueCallbackIoCanceledOnQueue interface is optional. Your driver can provide this interface if you want UMDF to notify the driver when an I/O request is canceled while it is in the driver's I/O queue. |
| [IPnpCallbackHardwareInterrupt interface](..\wudfddi\nn-wudfddi-ipnpcallbackhardwareinterrupt~r1.md) | The IPnpCallbackHardwareInterrupt interface supports interrupt-related Plug and Play and power management callback methods. |
| [IQueueCallbackDeviceIoControl interface](..\wudfddi\nn-wudfddi-iqueuecallbackdeviceiocontrol.md) | An I/O queue object notifies a driver when a device I/O control request is available for the driver. |
| [IQueueCallbackDeviceIoControl interface](..\wudfddi\nn-wudfddi-iqueuecallbackdeviceiocontrol~r1.md) | An I/O queue object notifies a driver when a device I/O control request is available for the driver. |
| [IWDFPropertyStoreFactory interface](..\wudfddi\nn-wudfddi-iwdfpropertystorefactory~r1.md) | The IWDFPropertyStoreFactory interface is a factory interface that is used to create a property store interface. |
| [IPowerPolicyCallbackWakeFromSx interface](..\wudfddi\nn-wudfddi-ipowerpolicycallbackwakefromsx.md) | A driver's IPowerPolicyCallbackWakeFromSx interface provides callback functions that the framework calls to notify the driver about wake events. These events are related to a device's ability to wake both itself and the system from a low-power state. |
| [IQueueCallbackIoResume interface](..\wudfddi\nn-wudfddi-iqueuecallbackioresume.md) | The IQueueCallbackIoResume interface contains a method that resumes the processing of an I/O request from a queue. |
| [IPnpCallbackHardware interface](..\wudfddi\nn-wudfddi-ipnpcallbackhardware.md) | The IPnpCallbackHardware interface is a Plug and Play (PnP) and power management (PM) interface. |
| [IWDFInterrupt interface](..\wudfddi\nn-wudfddi-iwdfinterrupt.md) | This interface exposes an interrupt object. |
| [IQueueCallbackCreate interface](..\wudfddi\nn-wudfddi-iqueuecallbackcreate.md) | An I/O queue notifies a driver when an open file request is available for the driver. |
| [IWDFNamedPropertyStore2 interface](..\wudfddi\nn-wudfddi-iwdfnamedpropertystore2~r1.md) | Drivers obtain the IWDFNamedPropertyStore2 interface by calling IWDFPropertyStoreFactory |
| [IDriverEntry interface](..\wudfddi\nn-wudfddi-idriverentry.md) | The IDriverEntry interface exposes the user-mode driver's main entry and exit points. |
| [IPnpCallback interface](..\wudfddi\nn-wudfddi-ipnpcallback.md) | The IPnpCallback interface is a Plug and Play (PnP) and power management (PM) interface. |
| [IRemoteTargetCallbackRemoval interface](..\wudfddi\nn-wudfddi-iremotetargetcallbackremoval~r1.md) | The IRemoteTargetCallbackRemoval interface provides callback functions that the framework calls to notify the driver about events that are associated with the removal of a remote I/O target. |
| [IWDFDevice2 interface](..\wudfddi\nn-wudfddi-iwdfdevice2~r1.md) | Drivers obtain the IWDFDevice2 interface by calling IWDFDevice |
| [IWDFIoTarget interface](..\wudfddi\nn-wudfddi-iwdfiotarget~r1.md) | The IWDFIoTarget interface exposes the I/O target object that typically represents a lower driver in the stack. |
| [IRequestCallbackCancel interface](..\wudfddi\nn-wudfddi-irequestcallbackcancel.md) | A driver is notified when an I/O request that the driver is currently processing is to be canceled. |
| [IRequestCallbackRequestCompletion interface](..\wudfddi\nn-wudfddi-irequestcallbackrequestcompletion.md) | A driver implements the IRequestCallbackRequestCompletion interface to complete a request object. |
| [IWDFDriverCreatedFile interface](..\wudfddi\nn-wudfddi-iwdfdrivercreatedfile.md) | The IWDFDriverCreatedFile interface exposes a UMDF driver-created-file object for the driver to use. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [IWDFRemoteInterfaceInitialize::RetrieveSymbolicLink method](..\wudfddi\nf-wudfddi-iwdfremoteinterfaceinitialize-retrievesymboliclink.md) | The RetrieveSymbolicLink method retrieves the symbolic link name that the operating system assigned to a device interface. |
| [IWDFIoRequest::GetFileObject method](..\wudfddi\nf-wudfddi-iwdfiorequest-getfileobject.md) | The GetFileObject method retrieves a pointer to the IWDFFile interface that is associated with an I/O request. |
| [IWDFIoQueue::RetrieveNextRequest method](..\wudfddi\nf-wudfddi-iwdfioqueue-retrievenextrequest.md) | The RetrieveNextRequest method retrieves the next I/O request from an I/O queue. |
| [IWDFIoQueue::Purge method](..\wudfddi\nf-wudfddi-iwdfioqueue-purge.md) | The Purge method directs the framework to reject new incoming I/O requests and to cancel all outstanding requests. |
| [IWDFRemoteTarget::OpenFileByName method](..\wudfddi\nf-wudfddi-iwdfremotetarget-openfilebyname.md) | The OpenFileByName method opens a remote I/O target that is a file. |
| [IWDFIoQueue::Start method](..\wudfddi\nf-wudfddi-iwdfioqueue-start.md) | The Start method enables an I/O queue to start receiving new I/O requests and delivering them to a driver. |
| [IWDFIoTarget::FormatRequestForWrite method](..\wudfddi\nf-wudfddi-iwdfiotarget-formatrequestforwrite.md) | The FormatRequestForWrite method formats an I/O request object for a write operation. |
| [IWDFDevice3::GetHardwareRegisterMappedAddress method](..\wudfddi\nf-wudfddi-iwdfdevice3-gethardwareregistermappedaddress.md) | A driver calls GetHardwareRegisterMappedAddress to get the user-mode mapped address of the memory resource it earlier mapped using MapIoSpace. |
| [IRemoteInterfaceCallbackRemoval::OnRemoteInterfaceRemoval method](..\wudfddi\nf-wudfddi-iremoteinterfacecallbackremoval-onremoteinterfaceremoval.md) | A UMDF-based driver's OnRemoteInterfaceRemoval event callback function notifies the driver that it cannot use a device interface because the interface has been removed. |
| [IWDFObject::AcquireLock method](..\wudfddi\nf-wudfddi-iwdfobject-acquirelock.md) | The AcquireLock method prevents the framework from calling methods of interfaces that a driver registered. |
| [IWDFDeviceInitialize::SetPowerPolicyOwnership method](..\wudfddi\nf-wudfddi-iwdfdeviceinitialize-setpowerpolicyownership.md) | The SetPowerPolicyOwnership method sets the ownership of the power policy to a driver or removes ownership from the driver. |
| [IPowerPolicyCallbackWakeFromS0::OnDisarmWakeFromS0 method](..\wudfddi\nf-wudfddi-ipowerpolicycallbackwakefroms0-ondisarmwakefroms0.md) | A driver's OnDisarmWakeFromS0 event callback function disarms (that is, disables) a device's ability to trigger a wake signal while in a low-power device state, if the system remains in the system working state (S0). |
| [IWDFFile2::GetRelatedFileObject method](..\wudfddi\nf-wudfddi-iwdffile2-getrelatedfileobject.md) | The GetRelatedFileObject method retrieves the IWDFFile interface of a related file object, which is a file object that has a technology-specific relationship with another file object. |
| [IWDFIoQueue::GetDevice method](..\wudfddi\nf-wudfddi-iwdfioqueue-getdevice.md) | The GetDevice method retrieves the interface to the device that owns the I/O queue. |
| [IDriverEntry::OnInitialize method](..\wudfddi\nf-wudfddi-idriverentry-oninitialize.md) | The OnInitialize method performs any operations that are necessary to initialize a driver. |
| [IWDFDevice::GetDefaultIoTarget method](..\wudfddi\nf-wudfddi-iwdfdevice-getdefaultiotarget.md) | The GetDefaultIoTarget method retrieves the interface of the default I/O target for a device instance. |
| [IWDFDeviceInitialize2::SetIoTypePreference method](..\wudfddi\nf-wudfddi-iwdfdeviceinitialize2-setiotypepreference.md) | The SetIoTypePreference method specifies your preferences for how UMDF and the driver access the data buffers of a device's I/O requests. |
| [IWDFIoRequest::CompleteWithInformation method](..\wudfddi\nf-wudfddi-iwdfiorequest-completewithinformation.md) | The CompleteWithInformation method completes a request with the supplied information. |
| [IWDFDevice2::AssignSxWakeSettings method](..\wudfddi\nf-wudfddi-iwdfdevice2-assignsxwakesettings.md) | The AssignSxWakeSettings method provides driver-supplied information about a device's ability to trigger a wake signal while both the device and the system are in a low-power state. |
| [IWDFDevice3::CreateWorkItem method](..\wudfddi\nf-wudfddi-iwdfdevice3-createworkitem.md) | The CreateWorkItem method creates a framework work-item object, which can subsequently be added to the framework’s work-item queue. |
| [IWDFDevice::CreateIoQueue method](..\wudfddi\nf-wudfddi-iwdfdevice-createioqueue.md) | The CreateIoQueue method configures the default I/O queue that is associated with a device or creates a secondary I/O queue for the device. |
| [IWDFDevice2::GetSystemPowerAction method](..\wudfddi\nf-wudfddi-iwdfdevice2-getsystempoweraction.md) | The GetSystemPowerAction method returns the system power action, if any, that is currently occurring for the computer. |
| [IWDFIoRequest::GetInputMemory method](..\wudfddi\nf-wudfddi-iwdfiorequest-getinputmemory.md) | The GetInputMemory method retrieves the memory object that represents the input buffer in an I/O request. |
| [IWDFIoRequest::GetCreateParameters method](..\wudfddi\nf-wudfddi-iwdfiorequest-getcreateparameters.md) | The GetCreateParameters method retrieves the request parameters for a create-type request. |
| [IWDFDriver::IsVersionAvailable method](..\wudfddi\nf-wudfddi-iwdfdriver-isversionavailable.md) | The IsVersionAvailable method determines whether the specified version of the framework is available. |
| [IWDFDevice3::MapIoSpace method](..\wudfddi\nf-wudfddi-iwdfdevice3-mapiospace.md) | The MapIoSpace method maps the given physical address range to system address space and returns a pseudo base address. |
| [IWDFRemoteTarget::Reopen method](..\wudfddi\nf-wudfddi-iwdfremotetarget-reopen.md) | The Reopen method reopens a remote I/O target after it has been temporarily closed. |
| [IPowerPolicyCallbackWakeFromSx::OnDisarmWakeFromSx method](..\wudfddi\nf-wudfddi-ipowerpolicycallbackwakefromsx-ondisarmwakefromsx.md) | A driver's OnDisarmWakeFromSx event callback function disarms (that is, disables) a device's ability to trigger a wake signal while the device and system are in low-power states. |
| [IWDFRemoteTarget::CloseForQueryRemove method](..\wudfddi\nf-wudfddi-iwdfremotetarget-closeforqueryremove.md) | The CloseForQueryRemove method closes a remote I/O target because the operating system might allow the device to be removed. |
| [IPowerPolicyCallbackWakeFromS0::OnArmWakeFromS0 method](..\wudfddi\nf-wudfddi-ipowerpolicycallbackwakefroms0-onarmwakefroms0.md) | A driver's OnArmWakeFromS0 callback function arms (that is, enables) a device so that it can trigger a wake signal while in a low-power device state, if the system remains in the system working state (S0). |
| [IWDFDevice2::GetDeviceStackIoTypePreference method](..\wudfddi\nf-wudfddi-iwdfdevice2-getdevicestackiotypepreference.md) | The GetDeviceStackIoTypePreference method retrieves the buffer access methods that the framework is using for a device. |
| [IWDFIoRequest2::Requeue method](..\wudfddi\nf-wudfddi-iwdfiorequest2-requeue.md) | The Requeue method returns an I/O request to the head of the I/O queue from which it was delivered to the driver. |
| [IWDFDevice::CreateWdfFile method](..\wudfddi\nf-wudfddi-iwdfdevice-createwdffile.md) | The CreateWdfFile method creates a file object for a driver to use. |
| [IWDFIoQueue::Stop method](..\wudfddi\nf-wudfddi-iwdfioqueue-stop.md) | The Stop method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests. |
| [IWDFIoTargetStateManagement::GetState method](..\wudfddi\nf-wudfddi-iwdfiotargetstatemanagement-getstate.md) | The GetState method returns the current state of a local I/O target. |
| [IWDFRemoteInterfaceInitialize::GetInterfaceGuid method](..\wudfddi\nf-wudfddi-iwdfremoteinterfaceinitialize-getinterfaceguid.md) | The GetInterfaceGuid method retrieves the GUID that identifies a device interface. |
| [IWDFIoRequest3::SetUserModeDriverInitiatedIo method](..\wudfddi\nf-wudfddi-iwdfiorequest3-setusermodedriverinitiatedio.md) | The SetUserModeDriverInitiatedIo method indicates to kernel-mode drivers that sit below the UMDF driver in the same device stack that a particular request should be treated as though it came from a UMDF driver. |
| [IWDFIoTarget::GetTargetFile method](..\wudfddi\nf-wudfddi-iwdfiotarget-gettargetfile.md) | The GetTargetFile method retrieves the framework file object that is associated with the I/O target object. |
| [IQueueCallbackDefaultIoHandler::OnDefaultIoHandler method](..\wudfddi\nf-wudfddi-iqueuecallbackdefaultiohandler-ondefaultiohandler.md) | The OnDefaultIoHandler method handles I/O requests that no other method is registered to handle. |
| [IWDFMemory::CopyToBuffer method](..\wudfddi\nf-wudfddi-iwdfmemory-copytobuffer.md) | The CopyToBuffer method safely copies data from a memory object to the specified target buffer. |
| [IImpersonateCallback::OnImpersonate method](..\wudfddi\nf-wudfddi-iimpersonatecallback-onimpersonate.md) | The OnImpersonate method handles impersonation. |
| [IPnpCallbackSelfManagedIo::OnSelfManagedIoInit method](..\wudfddi\nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagedioinit.md) | The OnSelfManagedIoInit method initializes a device's self-managed I/O operations. |
| [IWDFRequestCompletionParams::GetCompletionStatus method](..\wudfddi\nf-wudfddi-iwdfrequestcompletionparams-getcompletionstatus.md) | The GetCompletionStatus method retrieves the completion status of an I/O request. |
| [IWDFIoRequest3::GetUserModeDriverInitiatedIo method](..\wudfddi\nf-wudfddi-iwdfiorequest3-getusermodedriverinitiatedio.md) | The GetUserModeDriverInitiatedIo method determines whether an I/O request is marked as initiated by a UMDF driver. |
| [IWDFDriver::CreateDevice method](..\wudfddi\nf-wudfddi-iwdfdriver-createdevice.md) | The CreateDevice method configures and creates a new framework device object. |
| [IWDFRemoteTarget::Stop method](..\wudfddi\nf-wudfddi-iwdfremotetarget-stop.md) | The Stop method temporarily stops a remote I/O target. |
| [IPnpCallbackHardware2::OnPrepareHardware method](..\wudfddi\nf-wudfddi-ipnpcallbackhardware2-onpreparehardware.md) | The OnPrepareHardware method performs any operations that are needed to make a device accessible to the driver. |
| [IPnpCallback::OnD0Exit method](..\wudfddi\nf-wudfddi-ipnpcallback-ond0exit.md) | The OnD0Exit method notifies a driver when a device exits the D0 power state so that the driver can perform necessary operations, such as disabling the device. |
| [IWDFRemoteTarget::GetState method](..\wudfddi\nf-wudfddi-iwdfremotetarget-getstate.md) | The GetState method returns the current state of a remote I/O target. |
| [IWDFIoRequest::Send method](..\wudfddi\nf-wudfddi-iwdfiorequest-send.md) | The Send method sends a request to the specified I/O target. |
| [IWDFWorkItem::Flush method](..\wudfddi\nf-wudfddi-iwdfworkitem-flush.md) | The Flush method returns after this interface's work item has been serviced. |
| [IRemoteTargetCallbackRemoval::OnRemoteTargetRemoveComplete method](..\wudfddi\nf-wudfddi-iremotetargetcallbackremoval-onremotetargetremovecomplete.md) | A UMDF-based driver's OnRemoteTargetRemoveComplete event callback function performs operations that are necessary after the operating system completes the removal of a remote I/O target's device. |
| [IWDFDevice::RetrieveDevicePropertyStore method](..\wudfddi\nf-wudfddi-iwdfdevice-retrievedevicepropertystore.md) | The RetrieveDevicePropertyStore method retrieves a property store interface that drivers can use to access the registry. |
| [IPnpCallbackHardware2::OnReleaseHardware method](..\wudfddi\nf-wudfddi-ipnpcallbackhardware2-onreleasehardware.md) | The OnReleaseHardware method performs operations that are needed when a device is no longer accessible. |
| [IWDFIoRequest2::GetQueryInformationParameters method](..\wudfddi\nf-wudfddi-iwdfiorequest2-getqueryinformationparameters.md) | The GetQueryInformationParameters method retrieves parameters that are associated with a WdfRequestQueryInformation-typed I/O request. |
| [IWDFRequestCompletionParams::GetCompletedRequestType method](..\wudfddi\nf-wudfddi-iwdfrequestcompletionparams-getcompletedrequesttype.md) | The GetCompletedRequestType method retrieves the type of operation that the request to be completed contains. |
| [IWDFIoRequest::GetCompletionParams method](..\wudfddi\nf-wudfddi-iwdfiorequest-getcompletionparams.md) | The GetCompletionParams method retrieves the parameters object for the completion of an I/O request object. |
| [IQueueCallbackIoStop::OnIoStop method](..\wudfddi\nf-wudfddi-iqueuecallbackiostop-oniostop.md) | The OnIoStop callback function stops the processing of the specified I/O request from the specified queue. |
| [IPnpCallbackHardware::OnPrepareHardware method](..\wudfddi\nf-wudfddi-ipnpcallbackhardware-onpreparehardware.md) | The OnPrepareHardware method notifies a driver to make the specified hardware accessible. |
| [IWDFDevice2::ResumeIdle method](..\wudfddi\nf-wudfddi-iwdfdevice2-resumeidle.md) | The ResumeIdle method informs the framework that the device is not in use and can be placed in a device low-power state if it remains idle. |
| [IWDFIoTarget2::FormatRequestForSetInformation method](..\wudfddi\nf-wudfddi-iwdfiotarget2-formatrequestforsetinformation.md) | The FormatRequestForSetInformation method formats an I/O request to set information about a file, but it does not send the request to an I/O target. |
| [IWDFDevice::PostEvent method](..\wudfddi\nf-wudfddi-iwdfdevice-postevent.md) | The PostEvent method asynchronously notifies applications that are waiting for the specified event from a driver. |
| [IWDFDevice3::UnmapIoSpace method](..\wudfddi\nf-wudfddi-iwdfdevice3-unmapiospace.md) | The UnmapIoSpace method unmaps a specified range of physical addresses previously mapped by MapIoSpace method. |
| [IWDFDevice::GetDriver method](..\wudfddi\nf-wudfddi-iwdfdevice-getdriver.md) | The GetDriver method retrieves the interface to the parent driver object of a device instance. |
| [IWDFDriverCreatedFile::Close method](..\wudfddi\nf-wudfddi-iwdfdrivercreatedfile-close.md) | The Close method closes an instance of a UMDF driver-created-file object that was created by calling the IWDFDevice |
| [IQueueCallbackDeviceIoControl::OnDeviceIoControl method](..\wudfddi\nf-wudfddi-iqueuecallbackdeviceiocontrol-ondeviceiocontrol.md) | The OnDeviceIoControl method is called to handle a device I/O control request when an application performs a specific operation on a device through the Microsoft Win32 OnDeviceIoControl function. |
| [IWDFDevice::AssignDeviceInterfaceState method](..\wudfddi\nf-wudfddi-iwdfdevice-assigndeviceinterfacestate.md) | The AssignDeviceInterfaceState method enables or disables the specified device interface instance for a device. |
| [IPnpCallback::OnSurpriseRemoval method](..\wudfddi\nf-wudfddi-ipnpcallback-onsurpriseremoval.md) | The OnSurpriseRemoval method notifies a driver after a device is removed from a computer unexpectedly so that the driver can perform necessary operations. |
| [IQueueCallbackCreate::OnCreateFile method](..\wudfddi\nf-wudfddi-iqueuecallbackcreate-oncreatefile.md) | The OnCreateFile method is called to handle an open file request when an application opens a device through the Microsoft Win32 CreateFile function. |
| [IWDFIoRequest::GetDeviceIoControlParameters method](..\wudfddi\nf-wudfddi-iwdfiorequest-getdeviceiocontrolparameters.md) | The GetDeviceIoControlParameters method retrieves the request parameters for a device I/O control-type request. |
| [IWDFRequestCompletionParams::GetInformation method](..\wudfddi\nf-wudfddi-iwdfrequestcompletionparams-getinformation.md) | The GetInformation method retrieves information that is associated with the completion of an I/O request. |
| [IWDFIoRequest2::RetrieveOutputBuffer method](..\wudfddi\nf-wudfddi-iwdfiorequest2-retrieveoutputbuffer.md) | The RequestRetrieveOutputBuffer method retrieves an I/O request's output buffer. |
| [IWDFNamedPropertyStore::GetNamedValue method](..\wudfddi\nf-wudfddi-iwdfnamedpropertystore-getnamedvalue.md) | The GetNamedValue method retrieves the value of a property. |
| [IWDFIoRequest::GetIoQueue method](..\wudfddi\nf-wudfddi-iwdfiorequest-getioqueue.md) | The GetIoQueue method retrieves the I/O queue object that is associated with an I/O request. |
| [IWDFIoRequest::GetOutputMemory method](..\wudfddi\nf-wudfddi-iwdfiorequest-getoutputmemory.md) | The GetOutputMemory method retrieves the memory object that represents the output buffer for an I/O request. |
| [IWDFDevice::SetPnpState method](..\wudfddi\nf-wudfddi-iwdfdevice-setpnpstate.md) | The SetPnpState method turns on or off (or sets to the default state) the specified Plug and Play (PnP) property of a device. |
| [IDriverEntry::OnDeviceAdd method](..\wudfddi\nf-wudfddi-idriverentry-ondeviceadd.md) | The OnDeviceAdd method adds a new device to a system. |
| [IWDFIoRequest::SetCompletionCallback method](..\wudfddi\nf-wudfddi-iwdfiorequest-setcompletioncallback.md) | The SetCompletionCallback method registers the interface for the OnCompletion method that the framework should call when an I/O request completes. |
| [IWDFIoRequest::IsFrom32BitProcess method](..\wudfddi\nf-wudfddi-iwdfiorequest-isfrom32bitprocess.md) | The IsFrom32BitProcess method determines whether a request originated from a 32-bit process. |
| [IWDFIoRequest::FormatUsingCurrentType method](..\wudfddi\nf-wudfddi-iwdfiorequest-formatusingcurrenttype.md) | The FormatUsingCurrentType method formats an I/O request so that the driver can forward it, unmodified, to the next-lower driver. |
| [IWDFPropertyStoreFactory::RetrieveDevicePropertyStore method](..\wudfddi\nf-wudfddi-iwdfpropertystorefactory-retrievedevicepropertystore.md) | The RetrieveDevicePropertyStore method retrieves a property store interface that drivers can use to access the registry. |
| [IWDFDevice2::CreateRemoteTarget method](..\wudfddi\nf-wudfddi-iwdfdevice2-createremotetarget.md) | The CreateRemoteTarget method creates a remote target object that represents a remote I/O target. |
| [IWDFInterrupt::QueueWorkItemForIsr method](..\wudfddi\nf-wudfddi-iwdfinterrupt-queueworkitemforisr.md) | The QueueWorkItemForIsr method queues a work item to process interrupt-related work outside of the interrupt service routine. |
| [IWDFDevice2::CreateRemoteInterface method](..\wudfddi\nf-wudfddi-iwdfdevice2-createremoteinterface.md) | The CreateRemoteInterface method creates a remote interface object that represents a device interface. |
| [IFileCallbackCleanup::OnCleanupFile method](..\wudfddi\nf-wudfddi-ifilecallbackcleanup-oncleanupfile.md) | The OnCleanupFile method cancels all I/O requests that a driver has pending in the framework queue. |
| [IWDFCmResourceList::GetCount method](..\wudfddi\nf-wudfddi-iwdfcmresourcelist-getcount.md) | The GetCount method returns the number of resource descriptors that are contained in this interface's resource list. |
| [IPowerPolicyCallbackWakeFromSx::OnWakeFromSxTriggered method](..\wudfddi\nf-wudfddi-ipowerpolicycallbackwakefromsx-onwakefromsxtriggered.md) | A driver's OnWakeFromSxTriggered event callback function informs the driver that its device, which had previously entered a low-power device state because system power was reduced, might have triggered a wake signal. |
| [IWDFDeviceInitialize::RetrieveDeviceInstanceId method](..\wudfddi\nf-wudfddi-iwdfdeviceinitialize-retrievedeviceinstanceid.md) | The RetrieveDeviceInstanceId method retrieves the identifier of an instance of a device. |
| [IWDFDevice::RetrieveDeviceInstanceId method](..\wudfddi\nf-wudfddi-iwdfdevice-retrievedeviceinstanceid.md) | The RetrieveDeviceInstanceId method retrieves the identifier of an instance of a device. |
| [IWDFIoRequest2::RetrieveInputBuffer method](..\wudfddi\nf-wudfddi-iwdfiorequest2-retrieveinputbuffer.md) | The RequestRetrieveInputBuffer method retrieves an I/O request's input buffer. |
| [IWDFRemoteTarget::OpenRemoteInterface method](..\wudfddi\nf-wudfddi-iwdfremotetarget-openremoteinterface.md) | The OpenRemoteInterface method opens a device interface so that the driver can send I/O requests to it. |
| [IWDFIoQueue::Drain method](..\wudfddi\nf-wudfddi-iwdfioqueue-drain.md) | The Drain method directs the queue to reject new incoming I/O requests and allow already-queued requests to be delivered to the driver for processing. |
| [IWDFIoTarget::FormatRequestForRead method](..\wudfddi\nf-wudfddi-iwdfiotarget-formatrequestforread.md) | The FormatRequestForRead method formats an I/O request object for a read operation. |
| [IPnpCallbackSelfManagedIo::OnSelfManagedIoFlush method](..\wudfddi\nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagedioflush.md) | The OnSelfManagedIoFlush method flushes the device for a device's self-managed I/O operations. |
| [IWDFIoRequest::GetType method](..\wudfddi\nf-wudfddi-iwdfiorequest-gettype.md) | The GetType method retrieves the type of operation that a request contains. |
| [IWDFWorkItem::Enqueue method](..\wudfddi\nf-wudfddi-iwdfworkitem-enqueue.md) | The Enqueue method adds this interface's framework work-item object to the system's work-item queue. |
| [IWDFFile2::RetrieveCountedFileName method](..\wudfddi\nf-wudfddi-iwdffile2-retrievecountedfilename.md) | The RetrieveCountedFileName method retrieves the full counted file name for a file that is associated with a device. |
| [IWDFDevice2::StopIdle method](..\wudfddi\nf-wudfddi-iwdfdevice2-stopidle.md) | The StopIdle method informs the framework that the device must be placed in its working (D0) power state. |
| [IWDFDevice::CommitPnpState method](..\wudfddi\nf-wudfddi-iwdfdevice-commitpnpstate.md) | The CommitPnpState method commits the state of the Plug and Play (PnP) property (that is, turns on, turns off, or sets to the default state) that the IWDFDevice |
| [IWDFIoRequest::MarkCancelable method](..\wudfddi\nf-wudfddi-iwdfiorequest-markcancelable.md) | The MarkCancelable method enables the canceling of the I/O request. |
| [IWDFInterrupt::TryToAcquireInterruptLock method](..\wudfddi\nf-wudfddi-iwdfinterrupt-trytoacquireinterruptlock.md) | The TryToAcquireInterruptLock method acquires the interrupt lock if no other thread has already acquired it. |
| [IWDFIoRequest::SetInformation method](..\wudfddi\nf-wudfddi-iwdfiorequest-setinformation.md) | The SetInformation method sets the size of information for a request. |
| [IWDFInterrupt::SetPolicy method](..\wudfddi\nf-wudfddi-iwdfinterrupt-setpolicy.md) | The SetPolicy method specifies the interrupt priority, processor affinity, and affinity policy for a specified interrupt. |
| [IWDFDeviceInitialize::SetFilter method](..\wudfddi\nf-wudfddi-iwdfdeviceinitialize-setfilter.md) | The SetFilter method sets the property that enables a device as a filter device. |
| [IWDFDeviceInitialize::AutoForwardCreateCleanupClose method](..\wudfddi\nf-wudfddi-iwdfdeviceinitialize-autoforwardcreatecleanupclose.md) | The AutoForwardCreateCleanupClose method controls when create, cleanup, and close notifications are forwarded to the next lower driver in the device stack. |
| [IWDFInterrupt::GetInfo method](..\wudfddi\nf-wudfddi-iwdfinterrupt-getinfo.md) | The GetInfo method retrieves information about a specified interrupt. |
| [IWDFDevice2::AssignS0IdleSettings method](..\wudfddi\nf-wudfddi-iwdfdevice2-assigns0idlesettings.md) | The AssignS0IdleSettings method provides driver-supplied information that the framework uses when a device is idle and the system is in its working (S0) state. |
| [IQueueCallbackStateChange::OnStateChange method](..\wudfddi\nf-wudfddi-iqueuecallbackstatechange-onstatechange.md) | The OnStateChange method is called when the state of the I/O queue object changes. |
| [IQueueCallbackRead::OnRead method](..\wudfddi\nf-wudfddi-iqueuecallbackread-onread.md) | The OnRead method is called to handle a read request when an application reads information from a device through the Microsoft Win32 ReadFile or ReadFileEx function. |
| [IWDFUnifiedPropertyStore::GetPropertyData method](..\wudfddi\nf-wudfddi-iwdfunifiedpropertystore-getpropertydata.md) | The GetPropertyData method retrieves the current setting for a device property. |
| [IWDFIoRequest::GetReadParameters method](..\wudfddi\nf-wudfddi-iwdfiorequest-getreadparameters.md) | The GetReadParameters method retrieves the request parameters for a read-type request. |
| [IWDFDevice::GetDefaultIoQueue method](..\wudfddi\nf-wudfddi-iwdfdevice-getdefaultioqueue.md) | The GetDefaultIoQueue method retrieves the interface of the default I/O queue for a device. |
| [IWDFIoRequestCompletionParams::GetReadParameters method](..\wudfddi\nf-wudfddi-iwdfiorequestcompletionparams-getreadparameters.md) | The GetReadParameters method retrieves parameters that are associated with the completion of a read request. |
| [IWDFObject::RetrieveContext method](..\wudfddi\nf-wudfddi-iwdfobject-retrievecontext.md) | The RetrieveContext method retrieves a context that was previously registered through the IWDFObject |
| [IWDFIoRequest2::GetEffectiveIoType method](..\wudfddi\nf-wudfddi-iwdfiorequest2-geteffectiveiotype.md) | The GetEffectiveIoType method returns the buffer access method that UMDF is using for the data buffers of the I/O request that the IWDFIoRequest2 interface represents. |
| [IWDFDeviceInitialize::SetLockingConstraint method](..\wudfddi\nf-wudfddi-iwdfdeviceinitialize-setlockingconstraint.md) | The SetLockingConstraint method sets the synchronization (or locking) model for callback functions into the driver. |
| [IWDFIoRequest2::StopAcknowledge method](..\wudfddi\nf-wudfddi-iwdfiorequest2-stopacknowledge.md) | The StopAcknowledge method informs the framework that the driver has stopped processing a specified I/O request. |
| [IDriverEntry::OnDeinitialize method](..\wudfddi\nf-wudfddi-idriverentry-ondeinitialize.md) | The OnDeinitialize method performs any operations that are necessary before a system unloads a driver. |
| [IWDFIoRequest2::GetRequestorMode method](..\wudfddi\nf-wudfddi-iwdfiorequest2-getrequestormode.md) | The GetRequestorMode method indicates whether an I/O request came from a kernel-mode driver or a user-mode component (either an application or a user-mode driver). |
| [IWDFFile::RetrieveFileName method](..\wudfddi\nf-wudfddi-iwdffile-retrievefilename.md) | The RetrieveFileName method retrieves the full name of the file that is associated with the underlying kernel-mode device. |
| [IWDFIoRequest2::Reuse method](..\wudfddi\nf-wudfddi-iwdfiorequest2-reuse.md) | The Reuse method reinitializes a framework request object so that it can be reused. |
| [IWDFIoTargetStateManagement::Stop method](..\wudfddi\nf-wudfddi-iwdfiotargetstatemanagement-stop.md) | The Stop method stops sending queued requests to a local I/O target. |
| [IRemoteTargetCallbackRemoval::OnRemoteTargetRemoveCanceled method](..\wudfddi\nf-wudfddi-iremotetargetcallbackremoval-onremotetargetremovecanceled.md) | A UMDF-based driver's OnRemoteTargetRemoveCanceled event callback function performs operations that are necessary when the operating system cancels the removal of a remote I/O target's device. |
| [IWDFNamedPropertyStore2::DeleteNamedValue method](..\wudfddi\nf-wudfddi-iwdfnamedpropertystore2-deletenamedvalue.md) | The DeleteNamedValue method deletes a value name from the registry. |
| [IWDFIoRequest2::RetrieveOutputMemory method](..\wudfddi\nf-wudfddi-iwdfiorequest2-retrieveoutputmemory.md) | The RetrieveOutputMemory method retrieves the IWDFMemory interface of a framework memory object that represents an I/O request's output buffer. |
| [IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival method](..\wudfddi\nf-wudfddi-ipnpcallbackremoteinterfacenotification-onremoteinterfacearrival.md) | A driver's OnRemoteInterfaceArrival event callback function informs the driver when a device interface is available. |
| [IWDFDevice::RetrieveDeviceName method](..\wudfddi\nf-wudfddi-iwdfdevice-retrievedevicename.md) | The RetrieveDeviceName method retrieves the name of an underlying kernel-mode device. |
| [IWDFDeviceInitialize::GetPnpCapability method](..\wudfddi\nf-wudfddi-iwdfdeviceinitialize-getpnpcapability.md) | The GetPnpCapability method determines the state of the specified Plug and Play (PnP) capability. |
| [IPnpCallback::OnQueryStop method](..\wudfddi\nf-wudfddi-ipnpcallback-onquerystop.md) | The OnQueryStop method notifies a driver before a device is stopped. |
| [IWDFNamedPropertyStore::GetNameAt method](..\wudfddi\nf-wudfddi-iwdfnamedpropertystore-getnameat.md) | The GetNameAt method retrieves the name of a property. |
| [IWDFDeviceInitialize::RetrieveDevicePropertyStore method](..\wudfddi\nf-wudfddi-iwdfdeviceinitialize-retrievedevicepropertystore.md) | The RetrieveDevicePropertyStore method retrieves a device property store that clients can read and write device properties through. |
| [IQueueCallbackIoCanceledOnQueue::OnIoCanceledOnQueue method](..\wudfddi\nf-wudfddi-iqueuecallbackiocanceledonqueue-oniocanceledonqueue.md) | A driver's OnIoCanceledOnQueue event callback function informs the driver that an I/O request was canceled while it was in an I/O queue. |
| [IWDFCmResourceList::GetDescriptor method](..\wudfddi\nf-wudfddi-iwdfcmresourcelist-getdescriptor.md) | The GetDescriptor method returns a pointer to a resource descriptor that is contained in this interface's resource list. |
| [IWDFDriver::CreateWdfMemory method](..\wudfddi\nf-wudfddi-iwdfdriver-createwdfmemory.md) | The CreateWdfMemory method creates a framework memory object and allocates, for the memory object, a data buffer of the specified nonzero size. |
| [IPnpCallbackSelfManagedIo::OnSelfManagedIoSuspend method](..\wudfddi\nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagediosuspend.md) | The OnSelfManagedIoSuspend method suspends a device's self-managed I/O operations. |
| [IPnpCallbackHardwareInterrupt::OnD0EntryPostInterruptsEnabled method](..\wudfddi\nf-wudfddi-ipnpcallbackhardwareinterrupt-ond0entrypostinterruptsenabled.md) | A driver's OnD0EntryPostInterruptsEnabled event callback function performs device-specific operations that are required when the driver enables the device's hardware interrupts. |
| [IWDFIoRequest2::GetSetInformationParameters method](..\wudfddi\nf-wudfddi-iwdfiorequest2-getsetinformationparameters.md) | The GetSetInformationParameters method retrieves parameters that are associated with a WdfRequestSetInformation-typed I/O request. |
| [IWDFIoRequest::Complete method](..\wudfddi\nf-wudfddi-iwdfiorequest-complete.md) | The Complete method completes an I/O request. |
| [IWDFIoTargetStateManagement::Remove method](..\wudfddi\nf-wudfddi-iwdfiotargetstatemanagement-remove.md) | The Remove method removes a local I/O target. |
| [IWDFDevice::GetPnpState method](..\wudfddi\nf-wudfddi-iwdfdevice-getpnpstate.md) | The GetPnpState method determines whether the given Plug and Play (PnP) property of a device is on or off (or set to the default state). |
| [IPnpCallbackSelfManagedIo::OnSelfManagedIoCleanup method](..\wudfddi\nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagediocleanup.md) | The OnSelfManagedIoCleanup method releases memory for a device's self-managed I/O operations, after the device is removed. |
| [IWDFDriver::CreatePreallocatedWdfMemory method](..\wudfddi\nf-wudfddi-iwdfdriver-createpreallocatedwdfmemory.md) | The CreatePreallocatedWdfMemory method creates a framework memory object for the specified buffer. |
| [IWDFInterrupt::ReleaseInterruptLock method](..\wudfddi\nf-wudfddi-iwdfinterrupt-releaseinterruptlock.md) | The ReleaseInterruptLock method ends a code sequence that executes while holding an interrupt object's lock. |
| [IWDFIoTarget::CancelSentRequestsForFile method](..\wudfddi\nf-wudfddi-iwdfiotarget-cancelsentrequestsforfile.md) | The CancelSentRequestsForFile method cancels all I/O requests that have been sent on behalf of the specified file object. |
| [IWDFIoRequest3::SetActivityId method](..\wudfddi\nf-wudfddi-iwdfiorequest3-setactivityid.md) | The SetActivityId method associates an activity identifier with an I/O request. |
| [IWDFDeviceInitialize::SetPnpCapability method](..\wudfddi\nf-wudfddi-iwdfdeviceinitialize-setpnpcapability.md) | The SetPnpCapability method sets the specified Plug and Play (PnP) capability of a device to the specified state. |
| [IWDFIoRequest::Impersonate method](..\wudfddi\nf-wudfddi-iwdfiorequest-impersonate.md) | The Impersonate method registers the interface for the method that the framework should call for impersonation. |
| [IWDFDevice3::AssignS0IdleSettingsEx method](..\wudfddi\nf-wudfddi-iwdfdevice3-assigns0idlesettingsex.md) | The AssignS0IdleSettingsEx method provides driver-supplied information that the framework uses when a device is idle and the system is in its working (S0) state. |
| [IPnpCallback::OnD0Entry method](..\wudfddi\nf-wudfddi-ipnpcallback-ond0entry.md) | The OnD0Entry method notifies a driver when a device enters the D0 power state so that the driver can perform necessary operations, such as enabling the device. |
| [IPowerPolicyCallbackWakeFromS0::OnWakeFromS0Triggered method](..\wudfddi\nf-wudfddi-ipowerpolicycallbackwakefroms0-onwakefroms0triggered.md) | A driver's OnWakeFromS0Triggered event callback function informs the driver that its device, which had previously entered a low-power device state while the system power state remained at S0, might have triggered a wake signal. |
| [IWDFNamedPropertyStore::SetNamedValue method](..\wudfddi\nf-wudfddi-iwdfnamedpropertystore-setnamedvalue.md) | The SetNamedValue method sets the value of a property. |
| [IWDFMemory::GetDataBuffer method](..\wudfddi\nf-wudfddi-iwdfmemory-getdatabuffer.md) | The GetDataBuffer method retrieves the data buffer that is associated with a memory object. |
| [IWDFDriver::CreateWdfObject method](..\wudfddi\nf-wudfddi-iwdfdriver-createwdfobject.md) | The CreateWdfObject method creates a custom (or user) WDF object from a parent WDF object. |
| [IWDFFileHandleTargetFactory::CreateFileHandleTarget method](..\wudfddi\nf-wudfddi-iwdffilehandletargetfactory-createfilehandletarget.md) | The CreateFileHandleTarget method creates a file-handle-based I/O target object. |
| [IWDFUnifiedPropertyStoreFactory::RetrieveUnifiedDevicePropertyStore method](..\wudfddi\nf-wudfddi-iwdfunifiedpropertystorefactory-retrieveunifieddevicepropertystore.md) | The RetrieveUnifiedDevicePropertyStore method retrieves a unified property store interface. |
| [IQueueCallbackIoResume::OnIoResume method](..\wudfddi\nf-wudfddi-iqueuecallbackioresume-onioresume.md) | The OnIoResume method resumes the processing of the specified I/O request from the specified queue. |
| [IWDFRemoteTarget::Start method](..\wudfddi\nf-wudfddi-iwdfremotetarget-start.md) | The IWDFRemoteTarget |
| [IRequestCallbackRequestCompletion::OnCompletion method](..\wudfddi\nf-wudfddi-irequestcallbackrequestcompletion-oncompletion.md) | The OnCompletion method completes the specified request. |
| [IWDFRemoteTarget::Close method](..\wudfddi\nf-wudfddi-iwdfremotetarget-close.md) | The Close method closes a remote I/O target. |
| [IWDFIoQueue::DrainSynchronously method](..\wudfddi\nf-wudfddi-iwdfioqueue-drainsynchronously.md) | The DrainSynchronously method directs the queue to reject new incoming I/O requests and allows already-queued requests to be delivered to the driver for processing. This method returns after all requests are completed or canceled. |
| [IWDFObject::DeleteWdfObject method](..\wudfddi\nf-wudfddi-iwdfobject-deletewdfobject.md) | The DeleteWdfObject method deletes a previously created Microsoft Windows Driver Frameworks (WDF) object. |
| [IWDFFile::GetDevice method](..\wudfddi\nf-wudfddi-iwdffile-getdevice.md) | The GetDevice method returns the interface to the device object that a file object is associated with. |
| [IObjectCleanup::OnCleanup method](..\wudfddi\nf-wudfddi-iobjectcleanup-oncleanup.md) | The OnCleanup method releases any references to a WDF object to prevent interface leakage. |
| [IWDFIoRequest::UnmarkCancelable method](..\wudfddi\nf-wudfddi-iwdfiorequest-unmarkcancelable.md) | The UnmarkCancelable method disables the canceling of an I/O request. |
| [IWDFObject::AssignContext method](..\wudfddi\nf-wudfddi-iwdfobject-assigncontext.md) | The AssignContext method registers a context and a driver-supplied cleanup callback function for the object. |
| [IRequestCallbackCancel::OnCancel method](..\wudfddi\nf-wudfddi-irequestcallbackcancel-oncancel.md) | The OnCancel method is called when an application cancels an I/O operation through the Microsoft Win32 CancelIo, CancelIoEx, or CancelSynchronousIo function. |
| [IWDFInterrupt::Enable method](..\wudfddi\nf-wudfddi-iwdfinterrupt-enable.md) | The Enable method enables a specified device interrupt by calling the driver's OnInterruptEnable callback function. |
| [IPowerPolicyCallbackWakeFromSx::OnArmWakeFromSx method](..\wudfddi\nf-wudfddi-ipowerpolicycallbackwakefromsx-onarmwakefromsx.md) | A driver's OnArmWakeFromSx event callback function arms (that is, enables) a device so that it can trigger a wake signal while in a low-power device state. |
| [IRemoteInterfaceCallbackEvent::OnRemoteInterfaceEvent method](..\wudfddi\nf-wudfddi-iremoteinterfacecallbackevent-onremoteinterfaceevent.md) | A UMDF-based driver's OnRemoteInterfaceEvent event callback function handles device events that are associated with a device interface. |
| [IWDFIoTarget2::FormatRequestForFlush method](..\wudfddi\nf-wudfddi-iwdfiotarget2-formatrequestforflush.md) | The FormatRequestForFlush method builds an I/O request for a flush operation but does not send the request to an I/O target. |
| [IWDFIoRequest::ForwardToIoQueue method](..\wudfddi\nf-wudfddi-iwdfiorequest-forwardtoioqueue.md) | The ForwardToIoQueue method forwards (that is, requeues) an I/O request to one of the calling driver's I/O queues. |
| [IWDFIoRequestCompletionParams::GetIoctlParameters method](..\wudfddi\nf-wudfddi-iwdfiorequestcompletionparams-getioctlparameters.md) | The GetIoctlParameters method retrieves parameters that are associated with the completion of a device I/O control request. |
| [IWDFDevice2::CreateSymbolicLinkWithReferenceString method](..\wudfddi\nf-wudfddi-iwdfdevice2-createsymboliclinkwithreferencestring.md) | TheCreateSymbolicLinkWithReferenceString method creates a symbolic link name, and optionally, a reference string, for a device. |
| [IWDFMemory::CopyFromMemory method](..\wudfddi\nf-wudfddi-iwdfmemory-copyfrommemory.md) | The CopyFromMemory method safely copies data from the specified source buffer and prevents overruns that the copy operation might otherwise cause. |
| [IWDFInterrupt::AcquireInterruptLock method](..\wudfddi\nf-wudfddi-iwdfinterrupt-acquireinterruptlock.md) | The AcquireInterruptLock method begins a code sequence that executes while holding an interrupt object's lock. |
| [IWDFInterrupt::GetDevice method](..\wudfddi\nf-wudfddi-iwdfinterrupt-getdevice.md) | The GetDevice method returns the framework device object interface for this interrupt object. |
| [IWDFIoRequest2::RetrieveInputMemory method](..\wudfddi\nf-wudfddi-iwdfiorequest2-retrieveinputmemory.md) | The RetrieveInputMemory method retrieves the IWDFMemory interface of a framework memory object that represents an I/O request's input buffer. |
| [IWDFDevice::CreateDeviceInterface method](..\wudfddi\nf-wudfddi-iwdfdevice-createdeviceinterface.md) | The CreateDeviceInterface method creates an instance of a device interface class. |
| [IWDFIoRequest2::IsFromUserModeDriver method](..\wudfddi\nf-wudfddi-iwdfiorequest2-isfromusermodedriver.md) | The IsFromUserModeDriver method indicates whether an I/O request came from a user-mode driver or an application. |
| [IWDFDevice2::RegisterRemoteInterfaceNotification method](..\wudfddi\nf-wudfddi-iwdfdevice2-registerremoteinterfacenotification.md) | The RegisterRemoteInterfaceNotification method registers a driver to receive a notification when a specified device interface becomes available. |
| [IWDFMemory::GetSize method](..\wudfddi\nf-wudfddi-iwdfmemory-getsize.md) | The GetSize method retrieves the size of the data buffer that is associated with a memory object. |
| [IWDFIoTarget::FormatRequestForIoctl method](..\wudfddi\nf-wudfddi-iwdfiotarget-formatrequestforioctl.md) | The FormatRequestForIoctl method formats an I/O request object for an I/O control operation. |
| [IWDFIoRequest3::RetrieveActivityId method](..\wudfddi\nf-wudfddi-iwdfiorequest3-retrieveactivityid.md) | The RetrieveActivityId method retrieves the current activity identifier associated with an I/O request. |
| [IPnpCallbackSelfManagedIo::OnSelfManagedIoStop method](..\wudfddi\nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagediostop.md) | The OnSelfManagedIoStop method is not used in the current version of the UMDF. |
| [IQueueCallbackWrite::OnWrite method](..\wudfddi\nf-wudfddi-iqueuecallbackwrite-onwrite.md) | The OnWrite method is called to handle a write request when an application writes information to a device through the Microsoft Win32 WriteFile or WriteFileEx function. |
| [IWDFIoRequest::CancelSentRequest method](..\wudfddi\nf-wudfddi-iwdfiorequest-cancelsentrequest.md) | The CancelSentRequest method attempts to cancel the I/O request that the driver previously submitted to an I/O target. |
| [IPnpCallback::OnQueryRemove method](..\wudfddi\nf-wudfddi-ipnpcallback-onqueryremove.md) | The OnQueryRemove method notifies a driver before a device is removed from a computer. |
| [IWDFIoRequest::GetWriteParameters method](..\wudfddi\nf-wudfddi-iwdfiorequest-getwriteparameters.md) | The GetWriteParameters method retrieves the request parameters for a write-type request. |
| [IWDFIoQueue::RetrieveNextRequestByFileObject method](..\wudfddi\nf-wudfddi-iwdfioqueue-retrievenextrequestbyfileobject.md) | The RetrieveNextRequestByFileObject method retrieves from an I/O queue the next I/O request whose file object matches the specified file object. |
| [IWDFDevice::CreateRequest method](..\wudfddi\nf-wudfddi-iwdfdevice-createrequest.md) | The CreateRequest method creates an unformatted request object. |
| [IWDFIoTargetStateManagement::Start method](..\wudfddi\nf-wudfddi-iwdfiotargetstatemanagement-start.md) | The Start method starts sending queued requests to a local I/O target. |
| [IWDFIoRequest2::GetCreateParametersEx method](..\wudfddi\nf-wudfddi-iwdfiorequest2-getcreateparametersex.md) | The GetCreateParametersEx method retrieves file creation parameters that are associated with a file that is being created or opened. |
| [IWDFIoQueue::StopSynchronously method](..\wudfddi\nf-wudfddi-iwdfioqueue-stopsynchronously.md) | The StopSynchronously method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests. The method returns after all delivered requests have been canceled or completed. |
| [IWDFIoRequestCompletionParams::GetWriteParameters method](..\wudfddi\nf-wudfddi-iwdfiorequestcompletionparams-getwriteparameters.md) | The GetWriteParameters method retrieves parameters that are associated with the completion of a write request. |
| [IWDFInterrupt::SetExtendedPolicy method](..\wudfddi\nf-wudfddi-iwdfinterrupt-setextendedpolicy.md) | The SetExtendedPolicy method specifies the interrupt priority, processor affinity, affinity policy, and processor group for a specified interrupt. |
| [IWDFDevice3::CreateInterrupt method](..\wudfddi\nf-wudfddi-iwdfdevice3-createinterrupt.md) | The CreateInterrupt method creates a framework interrupt object. |
| [IWDFIoQueue::GetState method](..\wudfddi\nf-wudfddi-iwdfioqueue-getstate.md) | The GetState method retrieves the state of an I/O queue. |
| [IWDFMemory::SetBuffer method](..\wudfddi\nf-wudfddi-iwdfmemory-setbuffer.md) | The SetBuffer method assigns a specified buffer to a memory object that a driver created by calling IWDFDriver |
| [IWDFIoQueue::PurgeSynchronously method](..\wudfddi\nf-wudfddi-iwdfioqueue-purgesynchronously.md) | The PurgeSynchronously method directs the framework to reject new incoming I/O requests and to cancel all outstanding requests. The method returns after all outstanding requests are canceled. |
| [IWDFIoRequest2::IsCanceled method](..\wudfddi\nf-wudfddi-iwdfiorequest2-iscanceled.md) | The IsCanceled method determines whether the I/O manager has attempted to cancel an I/O request. |
| [IWDFWorkItem::GetParentObject method](..\wudfddi\nf-wudfddi-iwdfworkitem-getparentobject.md) | The GetParentObject method returns the parent framework object of this interface's work item. |
| [IWDFMemory::CopyFromBuffer method](..\wudfddi\nf-wudfddi-iwdfmemory-copyfrombuffer.md) | The CopyFromBuffer method safely copies data from the specified source buffer to a memory object. |
| [IWDFIoQueue::ConfigureRequestDispatching method](..\wudfddi\nf-wudfddi-iwdfioqueue-configurerequestdispatching.md) | The ConfigureRequestDispatching method configures the queuing of I/O requests of the given type. |
| [IWDFIoRequest2::GetStatus method](..\wudfddi\nf-wudfddi-iwdfiorequest2-getstatus.md) | The GetStatus method returns the status of an I/O request. |
| [IPnpCallbackSelfManagedIo::OnSelfManagedIoRestart method](..\wudfddi\nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagediorestart.md) | The OnSelfManagedIoRestart method restarts a device's self-managed I/O operations. |
| [IWDFInterrupt::Disable method](..\wudfddi\nf-wudfddi-iwdfinterrupt-disable.md) | The Disable method disables a specified device interrupt by calling the driver's OnInterruptDisable callback function. |
| [IWDFFile3::GetInitiatorProcessId method](..\wudfddi\nf-wudfddi-iwdffile3-getinitiatorprocessid.md) | The GetInitiatorProcessId method retrieves the initiator process ID associated with an IWDFFile interface. |
| [IFileCallbackClose::OnCloseFile method](..\wudfddi\nf-wudfddi-ifilecallbackclose-onclosefile.md) | The OnCloseFile method is called when the last reference count on a file object goes down to zero and before the file object is released. |
| [IWDFNamedPropertyStore::GetNameCount method](..\wudfddi\nf-wudfddi-iwdfnamedpropertystore-getnamecount.md) | The GetNameCount method retrieves the number of properties in a property store. |
| [IWDFUnifiedPropertyStore::SetPropertyData method](..\wudfddi\nf-wudfddi-iwdfunifiedpropertystore-setpropertydata.md) | The SetPropertyData method modifies the current setting of a device property. |
| [IPnpCallbackHardwareInterrupt::OnD0ExitPreInterruptsDisabled method](..\wudfddi\nf-wudfddi-ipnpcallbackhardwareinterrupt-ond0exitpreinterruptsdisabled.md) | A driver's OnD0ExitPreInterruptsDisabled event callback function performs device-specific operations that are required before the driver disables the device's hardware interrupts. |
| [IWDFDriver::RetrieveVersionString method](..\wudfddi\nf-wudfddi-iwdfdriver-retrieveversionstring.md) | The RetrieveVersionString method retrieves the version of the framework. |
| [IWDFDevice::ConfigureRequestDispatching method](..\wudfddi\nf-wudfddi-iwdfdevice-configurerequestdispatching.md) | The ConfigureRequestDispatching method configures the queuing of I/O requests of the specified type to the specified I/O queue. |
| [IWDFIoTarget2::FormatRequestForQueryInformation method](..\wudfddi\nf-wudfddi-iwdfiotarget2-formatrequestforqueryinformation.md) | The FormatRequestForQueryInformation method formats an I/O request to obtain information about a file, but it does not send the request to an I/O target. |
| [IWDFObject::ReleaseLock method](..\wudfddi\nf-wudfddi-iwdfobject-releaselock.md) | The ReleaseLock method allows the framework to call methods of interfaces that are registered by the driver that the framework previously prevented from calling because the driver called the IWDFObject |
| [IWDFIoRequest::GetRequestorProcessId method](..\wudfddi\nf-wudfddi-iwdfiorequest-getrequestorprocessid.md) | The GetRequestorProcessId method retrieves the identifier of the process that sent an I/O request. |
| [IWDFDevice::CreateSymbolicLink method](..\wudfddi\nf-wudfddi-iwdfdevice-createsymboliclink.md) | The CreateSymbolicLink method creates a symbolic link for the device. |
| [IRemoteTargetCallbackRemoval::OnRemoteTargetQueryRemove method](..\wudfddi\nf-wudfddi-iremotetargetcallbackremoval-onremotetargetqueryremove.md) | A UMDF-based driver's OnRemoteTargetQueryRemove event callback function determines whether a remote I/O target's device can be stopped and removed. |
| [IPnpCallbackHardware::OnReleaseHardware method](..\wudfddi\nf-wudfddi-ipnpcallbackhardware-onreleasehardware.md) | The OnReleaseHardware method notifies a driver to perform operations that are necessary when the specified hardware is no longer accessible. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [SECURITY_IMPERSONATION_LEVEL enumeration](..\wudfddi\ne-wudfddi--security-impersonation-level.md) | The SECURITY_IMPERSONATION_LEVEL enumeration contains values that identify security impersonation levels. |
| [DEVICE_POWER_STATE enumeration](..\wudfddi\ne-wudfddi--device-power-state~r1.md) | The DEVICE_POWER_STATE enumeration identifies the device power states that a device can enter. |
| [DEVICE_POWER_STATE enumeration](..\wudfddi\ne-wudfddi--device-power-state.md) | The DEVICE_POWER_STATE enumeration identifies the device power states that a device can enter. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [UMDF_IO_TARGET_OPEN_PARAMS structure](..\wudfddi\ns-wudfddi--umdf-io-target-open-params.md) | The UMDF_IO_TARGET_OPEN_PARAMS structure contains file-open parameters. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WRITE_PORT_ULONG function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-write-port-ulong.md) | The WRITE_PORT_ULONG function writes a ULONG value to the specified port address. |
| [READ_PORT_UCHAR function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-read-port-uchar.md) | The READ_PORT_UCHAR function reads a byte from the specified port address. |
| [READ_REGISTER_UCHAR function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-read-register-uchar.md) | The READ_REGISTER_UCHAR function reads a byte from the specified register address. |
| [WRITE_REGISTER_BUFFER_UCHAR function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-write-register-buffer-uchar.md) | The WRITE_REGISTER_BUFFER_UCHAR function writes a number of bytes from a buffer to the specified register. |
| [WRITE_PORT_USHORT function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-write-port-ushort.md) | The WRITE_PORT_USHORT function writes a USHORT value to the specified port address. |
| [WRITE_PORT_BUFFER_USHORT function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-write-port-buffer-ushort.md) | The WRITE_PORT_BUFFER_USHORT function writes a number of USHORT values from a buffer to the specified port address. |
| [READ_PORT_BUFFER_USHORT function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-read-port-buffer-ushort.md) | The READ_PORT_BUFFER_USHORT function reads a number of USHORT values from the specified port address into a buffer. |
| [WRITE_REGISTER_BUFFER_USHORT function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-write-register-buffer-ushort.md) | The WRITE_REGISTER_BUFFER_USHORT routine writes a number of USHORT values from a buffer to the specified register. |
| [READ_REGISTER_BUFFER_UCHAR function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-read-register-buffer-uchar.md) | The READ_REGISTER_BUFFER_UCHAR function reads a number of bytes from the specified register address into a buffer. |
| [READ_REGISTER_ULONG function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-read-register-ulong.md) | The READ_REGISTER_ULONG function reads a ULONG value from the specified register address. |
| [READ_REGISTER_BUFFER_ULONG function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-read-register-buffer-ulong.md) | The READ_REGISTER_BUFFER_ULONG function reads a number of ULONG values from the specified register address into a buffer. |
| [WRITE_PORT_BUFFER_UCHAR function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-write-port-buffer-uchar.md) | The WRITE_PORT_BUFFER_UCHAR function writes a number of bytes from a buffer to the specified port. |
| [WRITE_REGISTER_BUFFER_ULONG function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-write-register-buffer-ulong.md) | The WRITE_REGISTER_BUFFER_ULONG function writes a number of ULONG values from a buffer to the specified register. |
| [READ_PORT_BUFFER_UCHAR function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-read-port-buffer-uchar.md) | The READ_PORT_BUFFER_UCHAR function reads a number of bytes from the specified port address into a buffer. |
| [READ_REGISTER_BUFFER_ULONG64 function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-read-register-buffer-ulong64.md) | The READ_REGISTER_BUFFER_ULONG64 function reads a number of ULONG64 values from the specified register address into a buffer. |
| [WRITE_REGISTER_BUFFER_ULONG64 function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-write-register-buffer-ulong64.md) | The WRITE_REGISTER_BUFFER_ULONG64 function writes a number of ULONG64 values from a buffer to the specified register. |
| [READ_REGISTER_ULONG64 function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-read-register-ulong64.md) | The READ_REGISTER_ULONG64 function reads a ULONG64 value from the specified register address. |
| [READ_PORT_ULONG function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-read-port-ulong.md) | The READ_PORT_ULONG function reads a ULONG value from the specified port address. |
| [READ_PORT_USHORT function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-read-port-ushort.md) | The READ_PORT_USHORT function reads a USHORT value from the specified port address. |
| [WRITE_PORT_UCHAR function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-write-port-uchar.md) | The WRITE_PORT_UCHAR function writes a byte to the specified port address. |
| [WRITE_REGISTER_ULONG function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-write-register-ulong.md) | The WRITE_REGISTER_ULONG routine writes a ULONG value to the specified address. |
| [WRITE_REGISTER_UCHAR function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-write-register-uchar.md) | The WRITE_REGISTER_UCHAR routine writes a byte to the specified address. |
| [WRITE_REGISTER_ULONG64 function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-write-register-ulong64.md) | The WRITE_REGISTER_ULONG64 function writes a ULONG64 value to the specified address. |
| [READ_REGISTER_BUFFER_USHORT function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-read-register-buffer-ushort.md) | The READ_REGISTER_BUFFER_USHORT function reads a number of USHORT values from the specified register address into a buffer. |
| [WRITE_PORT_BUFFER_ULONG function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-write-port-buffer-ulong.md) | The WRITE_PORT_BUFFER_ULONG function writes a number of ULONG values from a buffer to the specified port address. |
| [WRITE_REGISTER_USHORT function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-write-register-ushort.md) | The WRITE_REGISTER_USHORT routine writes a USHORT value to the specified address. |
| [READ_PORT_BUFFER_ULONG function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-read-port-buffer-ulong.md) | The READ_PORT_BUFFER_ULONG function reads a number of ULONG values from the specified port address into a buffer. |
| [READ_REGISTER_USHORT function](..\wudfddi_hwaccess\nf-wudfddi-hwaccess-read-register-ushort.md) | The READ_REGISTER_USHORT function reads a USHORT value from the specified register address. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_EVENT_TYPE enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-event-type.md) | The WDF_EVENT_TYPE enumeration specifies. |
| [WDF_DEVICE_HWACCESS_TARGET_SIZE enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-device-hwaccess-target-size.md) | The WDF_DEVICE_HWACCESS_TARGET_SIZE enumeration is used internally by the framework. Do not use. |
| [WDF_PROPERTY_STORE_ROOT_CLASS enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-property-store-root-class.md) | The WDF_PROPERTY_STORE_ROOT_CLASS enumeration identifies the registry keys that UMDF property stores represent. |
| [WDF_PNP_CAPABILITY enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-pnp-capability.md) | The WDF_PNP_CAPABILITY enumeration contains values that identify Plug and Play (PnP) capabilities for a device. |
| [WDF_DEVICE_IO_BUFFER_RETRIEVAL enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-device-io-buffer-retrieval.md) | The WDF_DEVICE_IO_BUFFER_RETRIEVAL enumeration is used to specify when UMDF makes an I/O request's buffers available to the driver. |
| [WDF_REQUEST_SEND_OPTIONS_FLAGS enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-request-send-options-flags.md) | The WDF_REQUEST_SEND_OPTIONS_FLAGS enumeration type defines flags that a driver can specify when it calls IWDFIoRequest |
| [WDF_IO_TARGET_STATE enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-io-target-state.md) | The WDF_IO_TARGET_STATE enumeration specifies the states that an I/O target can be in. |
| [WDF_IO_TARGET_SENT_IO_ACTION enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-io-target-sent-io-action.md) | The WDF_IO_TARGET_SENT_IO_ACTION enumeration identifies the actions that the framework can take when a driver calls IWDFIoTargetStateManagement |
| [WDF_POWER_DEVICE_STATE enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-power-device-state.md) | The WDF_POWER_DEVICE_STATE enumeration contains values that identify the power state that a device might support. |
| [WDF_POWER_POLICY_IDLE_TIMEOUT_CONSTANTS enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-power-policy-idle-timeout-constants.md) | The WDF_POWER_POLICY_IDLE_TIMEOUT_CONSTANTS enumeration is reserved for internal use. |
| [WDF_CALLBACK_CONSTRAINT enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-callback-constraint.md) | WDF_CALLBACK_CONSTRAINT enumeration |
| [WDF_TRI_STATE enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-tri-state.md) | The WDF_TRI_STATE enumeration type defines three values that the framework uses for some structure members and function parameters. |
| [WDF_DEVICE_HWACCESS_TARGET_TYPE enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-device-hwaccess-target-type.md) | The WDF_DEVICE_HWACCESS_TARGET_TYPE enumeration is used internally by the framework. Do not use. |
| [WDF_POWER_POLICY_S0_IDLE_CAPABILITIES enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-power-policy-s0-idle-capabilities.md) | The WDF_POWER_POLICY_S0_IDLE_CAPABILITIES enumeration identifies the capabilities that a device can support when it enters a low-power state while it is idling. |
| [WDF_REQUEST_TYPE enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-request-type.md) | The WDF_REQUEST_TYPE enumeration identifies the types of I/O requests that a UMDF request object can represent. |
| [WDF_KPROCESSOR_MODE enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-kprocessor-mode.md) | The WDF_KPROCESSOR_MODE enumeration type identifies the processor modes in which a thread can execute. |
| [WDF_IO_QUEUE_DISPATCH_TYPE enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-io-queue-dispatch-type.md) | The WDF_IO_QUEUE_DISPATCH_TYPE enumeration contains values that identify how a driver must receive requests from an I/O queue. |
| [WDF_PNP_STATE enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-pnp-state.md) | The WDF_PNP_STATE enumeration contains values that identify the status of Plug and Play (PnP) for a device. |
| [WDF_POWER_POLICY_S0_IDLE_USER_CONTROL enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-power-policy-s0-idle-user-control.md) | The WDF_POWER_POLICY_S0_IDLE_USER_CONTROL enumeration identifies whether a user can control a device's behavior when the device is idle and the system is in its working (S0) state. |
| [WDF_POWER_POLICY_SX_WAKE_USER_CONTROL enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-power-policy-sx-wake-user-control.md) | The WDF_POWER_POLICY_SX_WAKE_USER_CONTROL enumeration identifies whether a user can control a device's ability to wake the system from a low system power state. |
| [WDF_IO_QUEUE_STATE enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-io-queue-state.md) | The WDF_IO_QUEUE_STATE enumeration contains values that identify the state of an I/O queue. |
| [WDF_FILE_INFORMATION_CLASS enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-file-information-class.md) | The WDF_FILE_INFORMATION_CLASS enumeration identifies the types of file information that a driver can obtain or set. |
| [WDF_DEVICE_IO_TYPE enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-device-io-type.md) | The WDF_DEVICE_IO_TYPE enumeration is used to specify a method for accessing data buffers. |
| [WDF_PROPERTY_STORE_DISPOSITION enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-property-store-disposition.md) | The WDF_PROPERTY_STORE_DISPOSITION enumeration contains values that indicate whether a registry value was created or already existed when a driver obtained a property store interface. |
| [WDF_REQUEST_STOP_ACTION_FLAGS enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-request-stop-action-flags.md) | The WDF_REQUEST_STOP_ACTION_FLAGS enumeration contains values that identify the state of a stop action request in a call to the driver's IQueueCallbackIoStop |
| [WDF_PROPERTY_STORE_RETRIEVE_FLAGS enumeration](..\wudfddi_types\ne-wudfddi-types--wdf-property-store-retrieve-flags.md) | The WDF_PROPERTY_STORE_RETRIEVE_FLAGS enumeration contains values that indicate whether UMDF should create a registry key if the key does not already exist. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDFMEMORY_OFFSET structure](..\wudfddi_types\ns-wudfddi-types--wdfmemory-offset.md) | The WDFMEMORY_OFFSET structure describes the location and size of information that is accessed within a memory block. |
| [UMDF_VERSION_DATA structure](..\wudfddi_types\ns-wudfddi-types-umdf-version-data.md) | The UMDF_VERSION_DATA structure describes a version of the framework. |
| [WDF_PROPERTY_STORE_ROOT structure](..\wudfddi_types\ns-wudfddi-types--wdf-property-store-root.md) | The WDF_PROPERTY_STORE_ROOT structure contains information that identifies a UMDF property store. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WUDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT function](..\wudfdevice\nf-wudfdevice-wudf-device-power-policy-idle-settings-init.md) | The WUDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT function initializes a driver's WUDF_DEVICE_POWER_POLICY_IDLE_SETTINGS structure. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [WUDF_INTERRUPT_ENABLE callback](..\wudfinterrupt\nc-wudfinterrupt-wudf-interrupt-enable.md) | A driver's OnInterruptEnable event callback function enables a specified hardware interrupt. |
| [WUDF_INTERRUPT_DISABLE callback](..\wudfinterrupt\nc-wudfinterrupt-wudf-interrupt-disable.md) | A driver's OnInterruptDisable event callback function disables a specified hardware interrupt. |
| [WUDF_INTERRUPT_WORKITEM callback](..\wudfinterrupt\nc-wudfinterrupt-wudf-interrupt-workitem.md) | A driver's OnInterruptWorkItem event callback function processes interrupt information that the driver's OnInterruptIsr callback function has stored. |
| [WUDF_INTERRUPT_ISR callback](..\wudfinterrupt\nc-wudfinterrupt-wudf-interrupt-isr.md) | A driver's OnInterruptIsr event callback function services a hardware interrupt. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_INTERRUPT_POLICY enumeration](..\wudfinterrupt\ne-wudfinterrupt--wdf-interrupt-policy.md) | The WDF_INTERRUPT_POLICY enumeration type identifies the affinity policies that the Plug and Play (PnP) manager can use when it assigns a device's interrupts to the processors of a multiprocessor system. |
| [WDF_INTERRUPT_PRIORITY enumeration](..\wudfinterrupt\ne-wudfinterrupt--wdf-interrupt-priority.md) | The WDF_INTERRUPT_PRIORITY enumeration type identifies relative priorities for device interrupts. |
| [WDF_INTERRUPT_POLARITY enumeration](..\wudfinterrupt\ne-wudfinterrupt--wdf-interrupt-polarity.md) | The WDF_INTERRUPT_POLARITY enumeration type is used to specify an interrupt signal's polarity. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WUDF_INTERRUPT_CONFIG structure](..\wudfinterrupt\ns-wudfinterrupt--wudf-interrupt-config.md) | The WUDF_INTERRUPT_CONFIG structure contains configuration information for a device interrupt. |
| [WDF_INTERRUPT_EXTENDED_POLICY structure](..\wudfinterrupt\ns-wudfinterrupt--wdf-interrupt-extended-policy.md) | The WDF_INTERRUPT_EXTENDED_POLICY structure contains information about an interrupt's policy, priority, affinity, and group. |
| [WDF_INTERRUPT_INFO structure](..\wudfinterrupt\ns-wudfinterrupt--wdf-interrupt-info.md) | The WDF_INTERRUPT_INFO structure contains information about a device's interrupt resource. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_INTERRUPT_EXTENDED_POLICY_INIT function](..\wudfinterrupt\nf-wudfinterrupt-wdf-interrupt-extended-policy-init.md) | The WDF_INTERRUPT_EXTENDED_POLICY_INIT function initializes a WDF_INTERRUPT_EXTENDED_POLICY structure. |
| [WDF_INTERRUPT_INFO_INIT function](..\wudfinterrupt\nf-wudfinterrupt-wdf-interrupt-info-init.md) | The WDF_INTERRUPT_INFO_INIT function initializes a WDF_INTERRUPT_INFO structure. |
| [WUDF_INTERRUPT_CONFIG_INIT function](..\wudfinterrupt\nf-wudfinterrupt-wudf-interrupt-config-init.md) | The WUDF_INTERRUPT_CONFIG_INIT function initializes a WUDF_INTERRUPT_CONFIG structure. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [IWDFUsbInterface::RetrieveUsbPipeObject method](..\wudfusb\nf-wudfusb-iwdfusbinterface-retrieveusbpipeobject.md) | The RetrieveUsbPipeObject method retrieves a USB pipe object for the specified pipe index. |
| [IWDFUsbTargetPipe::IsInEndPoint method](..\wudfusb\nf-wudfusb-iwdfusbtargetpipe-isinendpoint.md) | The IsInEndPoint method determines whether a USB pipe (endpoint) is an IN pipe. |
| [IWDFUsbInterface::GetInterfaceDescriptor method](..\wudfusb\nf-wudfusb-iwdfusbinterface-getinterfacedescriptor.md) | The GetInterfaceDescriptor method retrieves a descriptor for a USB interface. |
| [IWDFUsbTargetDevice::GetWinUsbHandle method](..\wudfusb\nf-wudfusb-iwdfusbtargetdevice-getwinusbhandle.md) | The GetWinUsbHandle method retrieves the WinUsb interface handle that is associated with a I/O target device object. |
| [IWDFUsbTargetPipe::Reset method](..\wudfusb\nf-wudfusb-iwdfusbtargetpipe-reset.md) | The Reset method resets the data toggle and clears the stall condition on a USB pipe. |
| [IUsbTargetPipeContinuousReaderCallbackReadersFailed::OnReaderFailure method](..\wudfusb\nf-wudfusb-iusbtargetpipecontinuousreadercallbackreadersfailed-onreaderfailure.md) | A driver's OnReaderFailure event callback function informs the driver that a continuous reader has reported an error while processing a read request. |
| [IWDFUsbTargetPipe::Flush method](..\wudfusb\nf-wudfusb-iwdfusbtargetpipe-flush.md) | The Flush method discards any data that WinUsb saved when the device returned more data than the client requested. |
| [IWDFUsbTargetPipe::GetInformation method](..\wudfusb\nf-wudfusb-iwdfusbtargetpipe-getinformation.md) | The GetInformation method retrieves information about a USB pipe (endpoint). |
| [IWDFUsbRequestCompletionParams::GetCompletedUsbRequestType method](..\wudfusb\nf-wudfusb-iwdfusbrequestcompletionparams-getcompletedusbrequesttype.md) | The GetCompletedUsbRequestType method retrieves the type of operation that the request to be completed contains. |
| [IWDFUsbRequestCompletionParams::GetDeviceControlTransferParameters method](..\wudfusb\nf-wudfusb-iwdfusbrequestcompletionparams-getdevicecontroltransferparameters.md) | The GetDeviceControlTransferParameters method retrieves parameters that are associated with the completion of a device I/O control request. |
| [IWDFUsbTargetPipe::SetPipePolicy method](..\wudfusb\nf-wudfusb-iwdfusbtargetpipe-setpipepolicy.md) | The SetPipePolicy method sets the WinUsb pipe policy. |
| [IWDFUsbTargetPipe::GetType method](..\wudfusb\nf-wudfusb-iwdfusbtargetpipe-gettype.md) | The GetType method retrieves the type of a USB pipe. |
| [IWDFUsbRequestCompletionParams::GetPipeReadParameters method](..\wudfusb\nf-wudfusb-iwdfusbrequestcompletionparams-getpipereadparameters.md) | The GetPipeReadParameters method retrieves parameters that are associated with the completion of a read request. |
| [IWDFUsbTargetDevice::GetNumInterfaces method](..\wudfusb\nf-wudfusb-iwdfusbtargetdevice-getnuminterfaces.md) | The GetNumInterfaces method retrieves the number of USB interfaces for the USB device. |
| [IWDFUsbTargetPipe::IsOutEndPoint method](..\wudfusb\nf-wudfusb-iwdfusbtargetpipe-isoutendpoint.md) | The IsOutEndPoint method determines whether a USB pipe (endpoint) is an OUT pipe. |
| [IWDFUsbInterface::GetConfiguredSettingIndex method](..\wudfusb\nf-wudfusb-iwdfusbinterface-getconfiguredsettingindex.md) | The GetConfiguredSettingIndex method retrieves the current setting index for a USB interface. |
| [IWDFUsbTargetDevice::RetrievePowerPolicy method](..\wudfusb\nf-wudfusb-iwdfusbtargetdevice-retrievepowerpolicy.md) | The RetrievePowerPolicy method retrieves a WinUsb power policy. |
| [IWDFUsbTargetDevice::RetrieveUsbInterface method](..\wudfusb\nf-wudfusb-iwdfusbtargetdevice-retrieveusbinterface.md) | The RetrieveUsbInterface method retrieves the specified USB interface for a USB device. |
| [IWDFUsbInterface::GetNumEndPoints method](..\wudfusb\nf-wudfusb-iwdfusbinterface-getnumendpoints.md) | The GetNumEndPoints method retrieves the number of endpoints (pipes) on a USB interface. |
| [IUsbTargetPipeContinuousReaderCallbackReadComplete::OnReaderCompletion method](..\wudfusb\nf-wudfusb-iusbtargetpipecontinuousreadercallbackreadcomplete-onreadercompletion.md) | A driver's OnReaderCompletion event callback function informs the driver that a continuous reader has successfully completed a read request. |
| [IWDFUsbTargetDevice::RetrieveDeviceInformation method](..\wudfusb\nf-wudfusb-iwdfusbtargetdevice-retrievedeviceinformation.md) | The RetrieveDeviceInformation method retrieves device information of the specified type. |
| [IWDFUsbInterface::SelectSetting method](..\wudfusb\nf-wudfusb-iwdfusbinterface-selectsetting.md) | The SelectSetting method selects the specified alternate setting on a USB interface. |
| [IWDFUsbTargetDevice::RetrieveDescriptor method](..\wudfusb\nf-wudfusb-iwdfusbtargetdevice-retrievedescriptor.md) | The RetrieveDescriptor method retrieves a USB descriptor, which can describe a device, configuration, or string. |
| [IWDFUsbTargetPipe2::ConfigureContinuousReader method](..\wudfusb\nf-wudfusb-iwdfusbtargetpipe2-configurecontinuousreader.md) | The ConfigureContinuousReader method configures the framework to continuously read from a USB pipe. |
| [IWDFUsbTargetPipe::RetrievePipePolicy method](..\wudfusb\nf-wudfusb-iwdfusbtargetpipe-retrievepipepolicy.md) | The RetrievePipePolicy method retrieves a WinUsb pipe policy. |
| [IWDFUsbTargetDevice::SetPowerPolicy method](..\wudfusb\nf-wudfusb-iwdfusbtargetdevice-setpowerpolicy.md) | The SetPowerPolicy method sets the WinUsb power policy. |
| [IWDFUsbTargetPipe::Abort method](..\wudfusb\nf-wudfusb-iwdfusbtargetpipe-abort.md) | The Abort method aborts all pending transfers on a USB pipe. |
| [IWDFUsbInterface::GetWinUsbHandle method](..\wudfusb\nf-wudfusb-iwdfusbinterface-getwinusbhandle.md) | The GetWinUsbHandle method retrieves the WinUsb interface handle that is associated with a USB interface. |
| [IWDFUsbRequestCompletionParams::GetPipeWriteParameters method](..\wudfusb\nf-wudfusb-iwdfusbrequestcompletionparams-getpipewriteparameters.md) | The GetPipeWriteParameters method retrieves parameters that are associated with the completion of a write request. |
| [IWDFUsbInterface::GetInterfaceNumber method](..\wudfusb\nf-wudfusb-iwdfusbinterface-getinterfacenumber.md) | The GetInterfaceNumber method retrieves the index of a USB interface. |
| [IWDFUsbTargetFactory::CreateUsbTargetDevice method](..\wudfusb\nf-wudfusb-iwdfusbtargetfactory-createusbtargetdevice.md) | The CreateUsbTargetDevice method creates a USB device object that is also an I/O target. |
| [IWDFUsbTargetDevice::FormatRequestForControlTransfer method](..\wudfusb\nf-wudfusb-iwdfusbtargetdevice-formatrequestforcontroltransfer.md) | The FormatRequestForControlTransfer method formats an I/O request object for a USB control transfer. |
Interface

| Title        | Description    |
| ------------- |:-------------:|
| [IWDFUsbInterface interface](..\wudfusb\nn-wudfusb-iwdfusbinterface~r1.md) | The IWDFUsbInterface interface exposes a USB interface that a USB device exposes. |
| [IUsbTargetPipeContinuousReaderCallbackReadComplete interface](..\wudfusb\nn-wudfusb-iusbtargetpipecontinuousreadercallbackreadcomplete~r1.md) | IUsbTargetPipeContinuousReaderCallbackReadComplete is a driver-supplied interface. |
| [IUsbTargetPipeContinuousReaderCallbackReadersFailed interface](..\wudfusb\nn-wudfusb-iusbtargetpipecontinuousreadercallbackreadersfailed.md) | IUsbTargetPipeContinuousReaderCallbackReadersFailed is a driver-supplied interface. |
| [IWDFUsbInterface interface](..\wudfusb\nn-wudfusb-iwdfusbinterface.md) | The IWDFUsbInterface interface exposes a USB interface that a USB device exposes. |
| [IWDFUsbTargetPipe interface](..\wudfusb\nn-wudfusb-iwdfusbtargetpipe.md) | The IWDFUsbTargetPipe interface exposes a USB pipe (endpoint), which is also an I/O target. |
| [IWDFUsbTargetPipe interface](..\wudfusb\nn-wudfusb-iwdfusbtargetpipe~r1.md) | The IWDFUsbTargetPipe interface exposes a USB pipe (endpoint), which is also an I/O target. |
| [IWDFUsbRequestCompletionParams interface](..\wudfusb\nn-wudfusb-iwdfusbrequestcompletionparams~r1.md) | The IWDFUsbRequestCompletionParams interface exposes the parameters object for the completion of a USB request object. The parameters object is primarily required for asynchronous I/O and layered drivers. |
| [IWDFUsbRequestCompletionParams interface](..\wudfusb\nn-wudfusb-iwdfusbrequestcompletionparams.md) | The IWDFUsbRequestCompletionParams interface exposes the parameters object for the completion of a USB request object. The parameters object is primarily required for asynchronous I/O and layered drivers. |
| [IWDFUsbTargetFactory interface](..\wudfusb\nn-wudfusb-iwdfusbtargetfactory.md) | The IWDFUsbTargetFactory interface is a factory interface that is used to create a USB target device object. |
| [IWDFUsbTargetDevice interface](..\wudfusb\nn-wudfusb-iwdfusbtargetdevice~r1.md) | The IWDFUsbTargetDevice interface exposes a USB device I/O target object. |
| [IWDFUsbTargetDevice interface](..\wudfusb\nn-wudfusb-iwdfusbtargetdevice.md) | The IWDFUsbTargetDevice interface exposes a USB device I/O target object. |
| [IWDFUsbTargetPipe2 interface](..\wudfusb\nn-wudfusb-iwdfusbtargetpipe2.md) | The IWDFUsbTargetPipe2 interface exposes a USB pipe (endpoint), which is also an I/O target. |
| [IUsbTargetPipeContinuousReaderCallbackReadersFailed interface](..\wudfusb\nn-wudfusb-iusbtargetpipecontinuousreadercallbackreadersfailed~r1.md) | IUsbTargetPipeContinuousReaderCallbackReadersFailed is a driver-supplied interface. |
| [IUsbTargetPipeContinuousReaderCallbackReadComplete interface](..\wudfusb\nn-wudfusb-iusbtargetpipecontinuousreadercallbackreadcomplete.md) | IUsbTargetPipeContinuousReaderCallbackReadComplete is a driver-supplied interface. |
| [IWDFUsbTargetFactory interface](..\wudfusb\nn-wudfusb-iwdfusbtargetfactory~r1.md) | The IWDFUsbTargetFactory interface is a factory interface that is used to create a USB target device object. |
| [IWDFUsbTargetPipe2 interface](..\wudfusb\nn-wudfusb-iwdfusbtargetpipe2~r1.md) | The IWDFUsbTargetPipe2 interface exposes a USB pipe (endpoint), which is also an I/O target. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_USB_REQUEST_TYPE enumeration](..\wudfusb\ne-wudfusb--wdf-usb-request-type~r1.md) | The WDF_USB_REQUEST_TYPE enumeration contains values that identify a type of USB request object. |
| [WDF_USB_REQUEST_TYPE enumeration](..\wudfusb\ne-wudfusb--wdf-usb-request-type.md) | The WDF_USB_REQUEST_TYPE enumeration contains values that identify a type of USB request object. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WUDF_WORKITEM_CONFIG structure](..\wudfworkitem\ns-wudfworkitem--wudf-workitem-config.md) | The WUDF_WORKITEM_CONFIG structure contains information that is associated with a work item. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [WUDF_WORKITEM_CONFIG_INIT function](..\wudfworkitem\nf-wudfworkitem-wudf-workitem-config-init.md) | The WUDF_WORKITEM_CONFIG_INIT macro initializes a driver's WUDF_WORKITEM_CONFIG structure. |


This technology is in the following headers:


| Header        | 

| [wdf](..\wdf\~PORTAL~wdf.md) | 

| [wdfassert](..\wdfassert\~PORTAL~wdfassert.md) | 

| [wdfchildlist](..\wdfchildlist\~PORTAL~wdfchildlist.md) | 

| [wdfcollection](..\wdfcollection\~PORTAL~wdfcollection.md) | 

| [wdfcommonbuffer](..\wdfcommonbuffer\~PORTAL~wdfcommonbuffer.md) | 

| [wdfcompanion](..\wdfcompanion\~PORTAL~wdfcompanion.md) | 

| [wdfcompaniontarget](..\wdfcompaniontarget\~PORTAL~wdfcompaniontarget.md) | 

| [wdfcontrol](..\wdfcontrol\~PORTAL~wdfcontrol.md) | 

| [wdfcore](..\wdfcore\~PORTAL~wdfcore.md) | 

| [wdfdevice](..\wdfdevice\~PORTAL~wdfdevice.md) | 

| [wdfdmaenabler](..\wdfdmaenabler\~PORTAL~wdfdmaenabler.md) | 

| [wdfdmatransaction](..\wdfdmatransaction\~PORTAL~wdfdmatransaction.md) | 

| [wdfdpc](..\wdfdpc\~PORTAL~wdfdpc.md) | 

| [wdfdriver](..\wdfdriver\~PORTAL~wdfdriver.md) | 

| [wdffdo](..\wdffdo\~PORTAL~wdffdo.md) | 

| [wdffileobject](..\wdffileobject\~PORTAL~wdffileobject.md) | 

| [wdfhwaccess](..\wdfhwaccess\~PORTAL~wdfhwaccess.md) | 

| [wdfinstaller](..\wdfinstaller\~PORTAL~wdfinstaller.md) | 

| [wdfinterrupt](..\wdfinterrupt\~PORTAL~wdfinterrupt.md) | 

| [wdfio](..\wdfio\~PORTAL~wdfio.md) | 

| [wdfiotarget](..\wdfiotarget\~PORTAL~wdfiotarget.md) | 

| [wdfmemory](..\wdfmemory\~PORTAL~wdfmemory.md) | 

| [wdfminiport](..\wdfminiport\~PORTAL~wdfminiport.md) | 

| [wdfobject](..\wdfobject\~PORTAL~wdfobject.md) | 

| [wdfpdo](..\wdfpdo\~PORTAL~wdfpdo.md) | 

| [wdfqueryinterface](..\wdfqueryinterface\~PORTAL~wdfqueryinterface.md) | 

| [wdfregistry](..\wdfregistry\~PORTAL~wdfregistry.md) | 

| [wdfrequest](..\wdfrequest\~PORTAL~wdfrequest.md) | 

| [wdfresource](..\wdfresource\~PORTAL~wdfresource.md) | 

| [wdfstring](..\wdfstring\~PORTAL~wdfstring.md) | 

| [wdfsync](..\wdfsync\~PORTAL~wdfsync.md) | 

| [wdftimer](..\wdftimer\~PORTAL~wdftimer.md) | 

| [wdftypes](..\wdftypes\~PORTAL~wdftypes.md) | 

| [wdfusb](..\wdfusb\~PORTAL~wdfusb.md) | 

| [wdfverifier](..\wdfverifier\~PORTAL~wdfverifier.md) | 

| [wdfwmi](..\wdfwmi\~PORTAL~wdfwmi.md) | 

| [wdfworkitem](..\wdfworkitem\~PORTAL~wdfworkitem.md) | 

| [wudfddi](..\wudfddi\~PORTAL~wudfddi.md) | 

| [wudfddi_hwaccess](..\wudfddi_hwaccess\~PORTAL~wudfddi_hwaccess.md) | 

| [wudfddi_types](..\wudfddi_types\~PORTAL~wudfddi_types.md) | 

| [wudfdevice](..\wudfdevice\~PORTAL~wudfdevice.md) | 

| [wudfinterrupt](..\wudfinterrupt\~PORTAL~wudfinterrupt.md) | 

| [wudfusb](..\wudfusb\~PORTAL~wudfusb.md) | 

| [wudfworkitem](..\wudfworkitem\~PORTAL~wudfworkitem.md) | 
