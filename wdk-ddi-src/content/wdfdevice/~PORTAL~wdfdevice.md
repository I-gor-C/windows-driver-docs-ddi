# Declarations in the wdfdevice header
This header Wdfdevice contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfDeviceInitSetDeviceType function](nf-wdfdevice-wdfdeviceinitsetdevicetype.md) | The WdfDeviceInitSetDeviceType method sets the device type for a specified device. |
| [WdfDeviceSetFailed function](nf-wdfdevice-wdfdevicesetfailed.md) | The WdfDeviceSetFailed method informs the framework that the driver encountered a hardware or software error that is associated with a specified device. |
| [WdfDeviceIndicateWakeStatus function](nf-wdfdevice-wdfdeviceindicatewakestatus.md) | The WdfDeviceIndicateWakeStatus method informs the framework that the calling bus driver has stopped waiting for a specified device to trigger a wake signal on the bus. |
| [WdfDeviceSetPnpCapabilities function](nf-wdfdevice-wdfdevicesetpnpcapabilities.md) | The WdfDeviceSetPnpCapabilities method reports a device's Plug and Play capabilities. |
| [WdfDeviceGetDevicePowerPolicyState function](nf-wdfdevice-wdfdevicegetdevicepowerpolicystate.md) | The WdfDeviceGetDevicePowerPolicyState method returns the current state of the framework's power policy state machine, for a specified device. |
| [WdfDevStateNormalize function](nf-wdfdevice-wdfdevstatenormalize.md) | The WdfDevStateNormalize method removes extra bits from a specified framework state machine value so that the driver can use the value as an index into an array of machine states. |
| [WDF_DEVICE_STATE_INIT function](nf-wdfdevice-wdf-device-state-init.md) | The WDF_DEVICE_STATE_INIT function initializes a driver's WDF_DEVICE_STATE structure. |
| [WdfWdmDeviceGetWdfDeviceHandle function](nf-wdfdevice-wdfwdmdevicegetwdfdevicehandle.md) | The WdfWdmDeviceGetWdfDeviceHandle method returns a handle to the framework device object that is associated with a specified WDM device object. |
| [WdfDeviceGetFileObject function](nf-wdfdevice-wdfdevicegetfileobject.md) | The WdfDeviceGetFileObject method returns a handle to the framework file object that is associated with a specified WDM file object. |
| [WDF_DEVICE_INTERFACE_PROPERTY_DATA_INIT function](nf-wdfdevice-wdf-device-interface-property-data-init.md) | The WDF_DEVICE_INTERFACE_PROPERTY_DATA_INIT function initializes a driver's WDF_DEVICE_INTERFACE_PROPERTY_DATA structure. |
| [WdfDeviceWdmGetAttachedDevice function](nf-wdfdevice-wdfdevicewdmgetattacheddevice.md) | The WdfDeviceWdmGetAttachedDevice method returns the next-lower WDM device object in the device stack. |
| [WdfDeviceCreateDeviceInterface function](nf-wdfdevice-wdfdevicecreatedeviceinterface.md) | The WdfDeviceCreateDeviceInterface method creates a device interface for a specified device. |
| [WdfDeviceInitRegisterPowerStateChangeCallback function](nf-wdfdevice-wdfdeviceinitregisterpowerstatechangecallback.md) | The WdfDeviceInitRegisterPowerStateChangeCallback method registers a driver-supplied event callback function that the framework calls when a device's power state machine changes state. |
| [WdfDeviceInitSetPowerPolicyOwnership function](nf-wdfdevice-wdfdeviceinitsetpowerpolicyownership.md) | The WdfDeviceInitSetPowerPolicyOwnership method establishes whether the calling driver is, or is not, the power policy owner for a specified device. |
| [WdfDeviceResumeIdle function](nf-wdfdevice-wdfdeviceresumeidle.md) | The WdfDeviceResumeIdle method informs the framework that the specified device is not in use and can be placed in a device low-power state if it remains idle. |
| [WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS_INIT function](nf-wdfdevice-wdf-device-power-policy-wake-settings-init.md) | The WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS_INIT function initializes a driver's WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS structure. |
| [WdfDeviceInitSetIoTypeEx function](nf-wdfdevice-wdfdeviceinitsetiotypeex.md) | The WdfDeviceInitSetIoTypeEx method sets the method or preference for how a driver will access the data buffers that are included in read and write requests, as well as device I/O control requests, for a specified device. |
| [WdfDeviceInitSetPowerPolicyEventCallbacks function](nf-wdfdevice-wdfdeviceinitsetpowerpolicyeventcallbacks.md) | The WdfDeviceInitSetPowerPolicyEventCallbacks method registers a driver's power policy event callback functions. |
| [WdfDeviceInitSetPowerPageable function](nf-wdfdevice-wdfdeviceinitsetpowerpageable.md) | The WdfDeviceInitSetPowerPageable method informs the power manager that the driver must be able to access pageable data while the system is transitioning between a sleeping state and the working (S0) state. |
| [WdfDeviceGetDevicePnpState function](nf-wdfdevice-wdfdevicegetdevicepnpstate.md) | The WdfDeviceGetDevicePnpState method returns the current state of the framework's Plug and Play state machine for a specified device. |
| [WdfDeviceSetDeviceState function](nf-wdfdevice-wdfdevicesetdevicestate.md) | The WdfDeviceSetDeviceState method sets the device state for a specified device. |
| [WdfDeviceAddDependentUsageDeviceObject function](nf-wdfdevice-wdfdeviceadddependentusagedeviceobject.md) | The WdfDeviceAddDependentUsageDeviceObject method indicates that a specified device depends on another device when the specified device is used to store special files. |
| [WdfDeviceGetDeviceState function](nf-wdfdevice-wdfdevicegetdevicestate.md) | The WdfDeviceGetDeviceState method retrieves the device state for a specified device. |
| [WdfDeviceGetDevicePowerState function](nf-wdfdevice-wdfdevicegetdevicepowerstate.md) | The WdfDeviceGetDevicePowerState method returns the current state of the framework's power state machine, for a specified device. |
| [WDF_DEVICE_POWER_CAPABILITIES_INIT function](nf-wdfdevice-wdf-device-power-capabilities-init.md) | The WDF_DEVICE_POWER_CAPABILITIES_INIT function initializes a WDF_DEVICE_POWER_CAPABILITIES structure. |
| [WdfDeviceInitAssignWdmIrpPreprocessCallback function](nf-wdfdevice-wdfdeviceinitassignwdmirppreprocesscallback.md) | The WdfDeviceInitAssignWdmIrpPreprocessCallback method registers a callback function to handle an IRP major function code and, optionally, one or more minor function codes that are associated with the major function code. |
| [WdfDeviceInitAssignName function](nf-wdfdevice-wdfdeviceinitassignname.md) | The WdfDeviceInitAssignName method assigns a device name to a device's device object. |
| [WdfDeviceQueryInterfaceProperty function](nf-wdfdevice-wdfdevicequeryinterfaceproperty.md) | The WdfDeviceQueryInterfaceProperty method retrieves a specified device interface property. |
| [WdfDevStateIsNP function](nf-wdfdevice-wdfdevstateisnp.md) | The WdfDevStateIsNP method returns a Boolean value that indicates whether a specified power state or power policy state is a nonpageable state. |
| [WdfDeviceEnqueueRequest function](nf-wdfdevice-wdfdeviceenqueuerequest.md) | The WdfDeviceEnqueueRequest method delivers a specified I/O request to the framework, so that the framework can subsequently add the request to one of the I/O queues that the driver has created for the specified device. |
| [WdfDeviceResumeIdleWithTag function](nf-wdfdevice-wdfdeviceresumeidlewithtag.md) | TBD |
| [WdfDeviceRetrieveCompanionTarget function](nf-wdfdevice-wdfdeviceretrievecompaniontarget.md) | For internal use only. |
| [WdfDeviceInitFree function](nf-wdfdevice-wdfdeviceinitfree.md) | The WdfDeviceInitFree method deallocates a WDFDEVICE_INIT structure. |
| [WdfDeviceOpenRegistryKey function](nf-wdfdevice-wdfdeviceopenregistrykey.md) | The WdfDeviceOpenRegistryKey method opens a device's hardware key or a driver's software key in the registry and creates a framework registry-key object that represents the registry key. |
| [WDF_POWER_POLICY_EVENT_CALLBACKS_INIT function](nf-wdfdevice-wdf-power-policy-event-callbacks-init.md) | The WDF_POWER_POLICY_EVENT_CALLBACKS_INIT function initializes a driver's WDF_POWER_POLICY_EVENT_CALLBACKS structure. |
| [WdfDeviceSetDeviceInterfaceState function](nf-wdfdevice-wdfdevicesetdeviceinterfacestate.md) | The WdfDeviceSetDeviceInterfaceState method enables or disables a device interface for a specified device. |
| [WdfDeviceCreate function](nf-wdfdevice-wdfdevicecreate.md) | The WdfDeviceCreate method creates a framework device object. |
| [WdfDeviceWdmDispatchPreprocessedIrp function](nf-wdfdevice-wdfdevicewdmdispatchpreprocessedirp.md) | The WdfDeviceWdmDispatchPreprocessedIrp method returns a preprocessed IRP to the framework. |
| [WdfDeviceSetStaticStopRemove function](nf-wdfdevice-wdfdevicesetstaticstopremove.md) | The WdfDeviceSetStaticStopRemove method informs the framework whether a device can be stopped and removed. |
| [WDF_DEVICE_PNP_CAPABILITIES_INIT function](nf-wdfdevice-wdf-device-pnp-capabilities-init.md) | The WDF_DEVICE_PNP_CAPABILITIES_INIT function initializes a WDF_DEVICE_PNP_CAPABILITIES structure. |
| [WdfDeviceWriteToHardware function](nf-wdfdevice-wdfdevicewritetohardware.md) | The WdfDeviceWriteToHardware method is used internally by the framework. Do not use. |
| [WdfDeviceGetAlignmentRequirement function](nf-wdfdevice-wdfdevicegetalignmentrequirement.md) | The WdfDeviceGetAlignmentRequirement method retrieves a device's address alignment requirement for memory transfer operations. |
| [WdfDeviceInitSetExclusive function](nf-wdfdevice-wdfdeviceinitsetexclusive.md) | The WdfDeviceInitSetExclusive method indicates whether a specified device is an exclusive device. |
| [WdfDeviceResumeIdleNoTrack function](nf-wdfdevice-wdfdeviceresumeidlenotrack.md) | TBD |
| [WdfDeviceGetIoTarget function](nf-wdfdevice-wdfdevicegetiotarget.md) | The WdfDeviceGetIoTarget method returns a handle to a function or filter driver's local I/O target, for a specified device. |
| [WdfDeviceInitSetIoInCallerContextCallback function](nf-wdfdevice-wdfdeviceinitsetioincallercontextcallback.md) | The WdfDeviceInitSetIoInCallerContextCallback method registers a driver's EvtIoInCallerContext event callback function. |
| [WdfDeviceGetSystemPowerAction function](nf-wdfdevice-wdfdevicegetsystempoweraction.md) | The WdfDeviceGetSystemPowerAction method returns the system power action, if any, that is currently occurring for the computer. |
| [WdfDeviceRemoveRemovalRelationsPhysicalDevice function](nf-wdfdevice-wdfdeviceremoveremovalrelationsphysicaldevice.md) | The WdfDeviceRemoveRemovalRelationsPhysicalDevice method removes a specified device from the list of devices that must be removed when another specified device is removed. |
| [WdfDeviceQueryPropertyEx function](nf-wdfdevice-wdfdevicequerypropertyex.md) | The WdfDeviceQueryPropertyEx method retrieves a specified device property. |
| [WdfDeviceGetCharacteristics function](nf-wdfdevice-wdfdevicegetcharacteristics.md) | The WdfDeviceGetCharacteristics method returns device characteristics for a specified device. |
| [WdfDeviceInitSetRequestAttributes function](nf-wdfdevice-wdfdeviceinitsetrequestattributes.md) | The WdfDeviceInitSetRequestAttributes method sets object attributes that will be used for all of the framework request objects that the framework delivers to the driver from the device's I/O queues. |
| [WDF_FILEOBJECT_CONFIG_INIT function](nf-wdfdevice-wdf-fileobject-config-init.md) | The WDF_FILEOBJECT_CONFIG_INIT function initializes a driver's WDF_FILEOBJECT_CONFIG structure. |
| [WDF_POWER_FRAMEWORK_SETTINGS_INIT function](nf-wdfdevice-wdf-power-framework-settings-init.md) | The WDF_POWER_FRAMEWORK_SETTINGS_INIT function initializes a WDF_POWER_FRAMEWORK_SETTINGS structure. |
| [WdfDeviceGetDefaultQueue function](nf-wdfdevice-wdfdevicegetdefaultqueue.md) | The WdfDeviceGetDefaultQueue method returns a handle to a device's default I/O queue. |
| [WdfDeviceInitSetIoType function](nf-wdfdevice-wdfdeviceinitsetiotype.md) | The WdfDeviceInitSetIoType method sets the method or preference for how a driver will access the data buffers that are included in read and write requests for a specified device. |
| [WdfDeviceRetrieveDeviceInterfaceString function](nf-wdfdevice-wdfdeviceretrievedeviceinterfacestring.md) | The WdfDeviceRetrieveDeviceInterfaceString method retrieves the symbolic link name that the operating system assigned to a device interface that the driver registered for a specified device. |
| [WdfDeviceInitSetReleaseHardwareOrderOnFailure function](nf-wdfdevice-wdfdeviceinitsetreleasehardwareorderonfailure.md) | The WdfDeviceInitSetReleaseHardwareOrderOnFailure method specifies whether the framework calls the driver's EvtDeviceReleaseHardware callback function immediately after device failure, or waits until all child devices have been removed. |
| [WdfDeviceResumeIdleActual function](nf-wdfdevice-wdfdeviceresumeidleactual.md) | TBD |
| [WdfDeviceInitSetFileObjectConfig function](nf-wdfdevice-wdfdeviceinitsetfileobjectconfig.md) | The WdfDeviceInitSetFileObjectConfig method registers event callback functions and sets configuration information for the driver's framework file objects. |
| [WdfDeviceAllocAndQueryProperty function](nf-wdfdevice-wdfdeviceallocandqueryproperty.md) | The WdfDeviceAllocAndQueryProperty method allocates a buffer and retrieves a specified device property. |
| [WdfDeviceAssignProperty function](nf-wdfdevice-wdfdeviceassignproperty.md) | The WdfDeviceAssignProperty method modifies the current setting of a device property. |
| [WdfDeviceClearRemovalRelationsDevices function](nf-wdfdevice-wdfdeviceclearremovalrelationsdevices.md) | The WdfDeviceClearRemovalRelationsDevices method removes all devices from the list of devices that must be removed when a specified device is removed. |
| [WdfDeviceOpenDevicemapKey function](nf-wdfdevice-wdfdeviceopendevicemapkey.md) | The WdfDeviceOpenDevicemapKey method opens the DEVICEMAP key and creates a framework registry-key object that represents the registry key. |
| [WdfDeviceInitSetCharacteristics function](nf-wdfdevice-wdfdeviceinitsetcharacteristics.md) | The WdfDeviceInitSetCharacteristics method sets device characteristics for a specified device. |
| [WDF_REMOVE_LOCK_OPTIONS_INIT function](nf-wdfdevice-wdf-remove-lock-options-init.md) | The WDF_REMOVE_LOCK_OPTIONS_INIT function initializes a WDF_REMOVE_LOCK_OPTIONS structure. |
| [WdfDeviceQueryProperty function](nf-wdfdevice-wdfdevicequeryproperty.md) | The WdfDeviceQueryProperty method retrieves a specified device property. |
| [WdfDevicePostEvent function](nf-wdfdevice-wdfdevicepostevent.md) | The WdfDevicePostEvent method asynchronously notifies applications that are waiting for the specified event from a driver. |
| [WdfDeviceAllocAndQueryPropertyEx function](nf-wdfdevice-wdfdeviceallocandquerypropertyex.md) | The WdfDeviceAllocAndQueryPropertyEx method allocates a buffer and retrieves a specified device property. |
| [WDF_PNPPOWER_EVENT_CALLBACKS_INIT function](nf-wdfdevice-wdf-pnppower-event-callbacks-init.md) | The WDF_PNPPOWER_EVENT_CALLBACKS_INIT function initializes a driver's WDF_PNPPOWER_EVENT_CALLBACKS structure. |
| [WdfDeviceAssignInterfaceProperty function](nf-wdfdevice-wdfdeviceassigninterfaceproperty.md) | The WdfDeviceAssignInterfaceProperty method modifies the current value of a device interface property. |
| [WdfDeviceAllocAndQueryInterfaceProperty function](nf-wdfdevice-wdfdeviceallocandqueryinterfaceproperty.md) | The WdfDeviceAllocAndQueryInterfaceProperty method allocates a buffer and retrieves a specified device interface property. |
| [WdfDeviceStopIdle function](nf-wdfdevice-wdfdevicestopidle.md) | The WdfDeviceStopIdle method informs the framework that the specified device must be placed in its working (D0) power state. |
| [WdfDeviceConfigureRequestDispatching function](nf-wdfdevice-wdfdeviceconfigurerequestdispatching.md) | The WdfDeviceConfigureRequestDispatching method causes the framework to queue a specified type of I/O requests to a specified I/O queue. |
| [WdfDeviceWdmGetDeviceObject function](nf-wdfdevice-wdfdevicewdmgetdeviceobject.md) | The WdfDeviceWdmGetDeviceObject method returns the Windows Driver Model (WDM) device object that is associated with a specified framework device object. |
| [WdfDeviceWdmDispatchIrpToIoQueue function](nf-wdfdevice-wdfdevicewdmdispatchirptoioqueue.md) | The WdfDeviceWdmDispatchIrpToIoQueue method forwards the IRP to a specified I/O queue. |
| [WdfDeviceSetBusInformationForChildren function](nf-wdfdevice-wdfdevicesetbusinformationforchildren.md) | The WdfDeviceSetBusInformationForChildren method sets information about a bus that a bus driver supports. This information is available to the bus's child devices. |
| [WdfDeviceWdmAssignPowerFrameworkSettings function](nf-wdfdevice-wdfdevicewdmassignpowerframeworksettings.md) | The WdfDeviceWdmAssignPowerFrameworkSettings method registers power management framework (PoFx) settings for single-component devices. |
| [WdfDeviceInitSetRemoveLockOptions function](nf-wdfdevice-wdfdeviceinitsetremovelockoptions.md) | The WdfDeviceInitSetRemoveLockOptions method causes the framework to acquire a remove lock before delivering an IRP of any type to the driver. |
| [WdfDeviceAssignSxWakeSettings function](nf-wdfdevice-wdfdeviceassignsxwakesettings.md) | The WdfDeviceAssignSxWakeSettings method provides driver-supplied information about a device's ability to trigger a wake signal while both the device and the system are in a low-power state. |
| [WdfDeviceRemoveDependentUsageDeviceObject function](nf-wdfdevice-wdfdeviceremovedependentusagedeviceobject.md) | The WdfDeviceRemoveDependentUsageDeviceObject method indicates that a specified device no longer depends on another device when the specified device is used to store special files. |
| [WdfDeviceInitSetPowerNotPageable function](nf-wdfdevice-wdfdeviceinitsetpowernotpageable.md) | The WdfDeviceInitSetPowerNotPageable method informs the power manager that the driver will not access pageable data while the system is transitioning between a sleeping state and the working (S0) state. |
| [WdfDeviceInitAssignSDDLString function](nf-wdfdevice-wdfdeviceinitassignsddlstring.md) | The WdfDeviceInitAssignSDDLString method assigns a security setting for a device. |
| [WdfDeviceInitSetDeviceClass function](nf-wdfdevice-wdfdeviceinitsetdeviceclass.md) | The WdfDeviceInitSetDeviceClass method specifies a GUID that identifies the device's device setup class. |
| [WdfDeviceSetSpecialFileSupport function](nf-wdfdevice-wdfdevicesetspecialfilesupport.md) | The WdfDeviceSetSpecialFileSupport method enables or disables a function driver's support for special files, for the specified device. |
| [WdfDeviceMapIoSpace function](nf-wdfdevice-wdfdevicemapiospace.md) | The WdfDeviceMapIoSpace function maps the given physical address range to system address space and returns a pseudo base address. |
| [WdfDeviceStopIdleWithTag function](nf-wdfdevice-wdfdevicestopidlewithtag.md) | TBD |
| [WdfDeviceInitRegisterPowerPolicyStateChangeCallback function](nf-wdfdevice-wdfdeviceinitregisterpowerpolicystatechangecallback.md) | The WdfDeviceInitRegisterPowerPolicyStateChangeCallback method registers a driver-supplied event callback function that the framework calls when a device's power policy state machine changes state. |
| [WdfDeviceSetCharacteristics function](nf-wdfdevice-wdfdevicesetcharacteristics.md) | The WdfDeviceSetCharacteristics method sets device characteristics for a specified device. |
| [WdfDeviceStopIdleNoTrack function](nf-wdfdevice-wdfdevicestopidlenotrack.md) | TBD |
| [WdfDeviceInitSetPnpPowerEventCallbacks function](nf-wdfdevice-wdfdeviceinitsetpnppowereventcallbacks.md) | The WdfDeviceInitSetPnpPowerEventCallbacks method registers a driver's Plug and Play and power management event callback functions. |
| [WdfDeviceAddRemovalRelationsPhysicalDevice function](nf-wdfdevice-wdfdeviceaddremovalrelationsphysicaldevice.md) | The WdfDeviceAddRemovalRelationsPhysicalDevice method indicates that a specified device must be removed when another specified device is removed. |
| [WdfDeviceSetAlignmentRequirement function](nf-wdfdevice-wdfdevicesetalignmentrequirement.md) | The WdfDeviceSetAlignmentRequirement method registers the driver's preferred address alignment for the data buffers that the device uses during memory transfer operations. |
| [WdfDeviceReadFromHardware function](nf-wdfdevice-wdfdevicereadfromhardware.md) | The WdfDeviceReadFromHardware method is used internally by the framework. Do not use. |
| [WdfDeviceSetPowerCapabilities function](nf-wdfdevice-wdfdevicesetpowercapabilities.md) | The WdfDeviceSetPowerCapabilities method reports a device's power capabilities. |
| [WdfDeviceInitRegisterPnpStateChangeCallback function](nf-wdfdevice-wdfdeviceinitregisterpnpstatechangecallback.md) | The WdfDeviceInitRegisterPnpStateChangeCallback method registers a driver-supplied event callback function that the framework calls when a device's Plug and Play state machine changes state. |
| [WdfDeviceAssignMofResourceName function](nf-wdfdevice-wdfdeviceassignmofresourcename.md) | The WdfDeviceAssignMofResourceName method registers a MOF resource name for a specified device. |
| [WdfDeviceAssignS0IdleSettings function](nf-wdfdevice-wdfdeviceassigns0idlesettings.md) | The WdfDeviceAssignS0IdleSettings method provides driver-supplied information that the framework uses when a device is idle and the system is in its working (S0) state. |
| [WdfDeviceGetDeviceStackIoType function](nf-wdfdevice-wdfdevicegetdevicestackiotype.md) | The WdfDeviceGetDeviceStackIoType method retrieves the buffer access methods that the framework is using for a device. |
| [WdfDeviceWdmGetPhysicalDevice function](nf-wdfdevice-wdfdevicewdmgetphysicaldevice.md) | The WdfDeviceWdmGetPhysicalDevice method retrieves the physical device's WDM PDO from the device stack. |
| [WdfDeviceWdmDispatchIrp function](nf-wdfdevice-wdfdevicewdmdispatchirp.md) | The WdfDeviceWdmDispatchIrp method returns a dispatched IRP to the framework from EvtDeviceWdmIrpDispatch. |
| [WdfDeviceRetrieveDeviceName function](nf-wdfdevice-wdfdeviceretrievedevicename.md) | The WdfDeviceRetrieveDeviceName method returns the device name for a specified device. |
| [WdfDeviceGetDriver function](nf-wdfdevice-wdfdevicegetdriver.md) | The WdfDeviceGetDriver method returns a handle to the framework driver object that is associated with a specified framework device object. |
| [WdfDeviceStopIdleActual function](nf-wdfdevice-wdfdevicestopidleactual.md) | TBD |
| [WdfDeviceConfigureWdmIrpDispatchCallback function](nf-wdfdevice-wdfdeviceconfigurewdmirpdispatchcallback.md) | The WdfDeviceConfigureWdmIrpDispatchCallback method registers a driver's EvtDeviceWdmIrpDispatch callback function. |
| [WdfDeviceGetHardwareRegisterMappedAddress function](nf-wdfdevice-wdfdevicegethardwareregistermappedaddress.md) | A driver calls WdfDeviceGetHardwareRegisterMappedAddress to get the user-mode mapped address of the memory resource it mapped previously using WdfDeviceMapIoSpace. |
| [WdfDeviceCreateSymbolicLink function](nf-wdfdevice-wdfdevicecreatesymboliclink.md) | The WdfDeviceCreateSymbolicLink method creates a symbolic link to a specified device. |
| [WdfDeviceInitSetPowerInrush function](nf-wdfdevice-wdfdeviceinitsetpowerinrush.md) | The WdfDeviceInitSetPowerInrush method informs the power manager that the specified device requires an inrush of current when it starts. |
| [WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT function](nf-wdfdevice-wdf-device-power-policy-idle-settings-init.md) | The WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS_INIT function initializes a driver's WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS structure. |
| [WdfDeviceUnmapIoSpace function](nf-wdfdevice-wdfdeviceunmapiospace.md) | The WdfDeviceUnmapIoSpace function unmaps a specified range of physical addresses previously mapped by the WdfDeviceMapIoSpace function. |
| [WDF_IO_TYPE_CONFIG_INIT function](nf-wdfdevice-wdf-io-type-config-init.md) | The WDF_IO_TYPE_CONFIG_INIT function initializes a driver's WDF_IO_TYPE_CONFIG structure. |
| [WDF_DEVICE_PROPERTY_DATA_INIT function](nf-wdfdevice-wdf-device-property-data-init.md) | The WDF_DEVICE_PROPERTY_DATA_INIT function initializes a driver's WDF_DEVICE_PROPERTY_DATA structure. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_WDFDEVICEWRITETOHARDWARE callback function](nc-wdfdevice-pfn-wdfdevicewritetohardware.md) | TBD |
| [EVT_WDF_DEVICE_USAGE_NOTIFICATION callback](nc-wdfdevice-evt-wdf-device-usage-notification.md) | A driver's EvtDeviceUsageNotification event callback function informs the driver when a device is being used for special files. |
| [PFN_WDFDEVICEALLOCANDQUERYPROPERTYEX callback function](nc-wdfdevice-pfn-wdfdeviceallocandquerypropertyex.md) | TBD |
| [PFN_WDFDEVICEREMOVEDEPENDENTUSAGEDEVICEOBJECT callback function](nc-wdfdevice-pfn-wdfdeviceremovedependentusagedeviceobject.md) | TBD |
| [PFN_WDFDEVICESETFAILED callback function](nc-wdfdevice-pfn-wdfdevicesetfailed.md) | TBD |
| [PFN_WDFDEVICESETBUSINFORMATIONFORCHILDREN callback function](nc-wdfdevice-pfn-wdfdevicesetbusinformationforchildren.md) | TBD |
| [PFN_WDFDEVICEASSIGNPROPERTY callback function](nc-wdfdevice-pfn-wdfdeviceassignproperty.md) | TBD |
| [PFN_WDFDEVICEWDMDISPATCHIRP callback function](nc-wdfdevice-pfn-wdfdevicewdmdispatchirp.md) | TBD |
| [PFN_WDFDEVICEWDMGETATTACHEDDEVICE callback function](nc-wdfdevice-pfn-wdfdevicewdmgetattacheddevice.md) | TBD |
| [EVT_WDF_DEVICE_SELF_MANAGED_IO_FLUSH callback](nc-wdfdevice-evt-wdf-device-self-managed-io-flush.md) | A driver's EvtDeviceSelfManagedIoFlush event callback function handles flush activity for the device's self-managed I/O operations. |
| [EVT_WDF_FILE_CLOSE callback](nc-wdfdevice-evt-wdf-file-close.md) | A driver's EvtFileClose callback function handles operations that must be performed when all of an application's accesses to a device have been closed. |
| [PFN_WDFDEVICEINITREGISTERPOWERSTATECHANGECALLBACK callback function](nc-wdfdevice-pfn-wdfdeviceinitregisterpowerstatechangecallback.md) | TBD |
| [PFN_WDFWDMDEVICEGETWDFDEVICEHANDLE callback function](nc-wdfdevice-pfn-wdfwdmdevicegetwdfdevicehandle.md) | TBD |
| [EVT_WDFDEVICE_WDM_PRE_PO_FX_UNREGISTER_DEVICE callback](nc-wdfdevice-evt-wdfdevice-wdm-pre-po-fx-unregister-device.md) | The EvtDeviceWdmPrePoFxUnregisterDevice callback function performs device-specific operations before the framework deletes a specified registration with the power framework. |
| [PFN_WDFDEVICEGETDEVICESTATE callback function](nc-wdfdevice-pfn-wdfdevicegetdevicestate.md) | TBD |
| [PFN_WDFDEVICEASSIGNSXWAKESETTINGS callback function](nc-wdfdevice-pfn-wdfdeviceassignsxwakesettings.md) | TBD |
| [EVT_WDF_DEVICE_POWER_POLICY_STATE_CHANGE_NOTIFICATION callback](nc-wdfdevice-evt-wdf-device-power-policy-state-change-notification.md) | A driver's EvtDevicePowerPolicyStateChange event callback function informs the driver that a device's power policy state machine is moving from one state to another. |
| [PFN_WDFDEVICEINITREGISTERPOWERPOLICYSTATECHANGECALLBACK callback function](nc-wdfdevice-pfn-wdfdeviceinitregisterpowerpolicystatechangecallback.md) | TBD |
| [EVT_WDF_DEVICE_POWER_STATE_CHANGE_NOTIFICATION callback](nc-wdfdevice-evt-wdf-device-power-state-change-notification.md) | A driver's EvtDevicePowerStateChange event callback function informs the driver that a device's power state machine is moving from one state to another. |
| [PFN_WDFDEVICEINITSETFILEOBJECTCONFIG callback function](nc-wdfdevice-pfn-wdfdeviceinitsetfileobjectconfig.md) | TBD |
| [PFN_WDFDEVICEINITSETRELEASEHARDWAREORDERONFAILURE callback function](nc-wdfdevice-pfn-wdfdeviceinitsetreleasehardwareorderonfailure.md) | TBD |
| [PFN_WDFDEVICECREATE callback function](nc-wdfdevice-pfn-wdfdevicecreate.md) | TBD |
| [PFN_WDFDEVICESETSTATICSTOPREMOVE callback function](nc-wdfdevice-pfn-wdfdevicesetstaticstopremove.md) | TBD |
| [PFN_WDFDEVICECONFIGUREWDMIRPDISPATCHCALLBACK callback function](nc-wdfdevice-pfn-wdfdeviceconfigurewdmirpdispatchcallback.md) | TBD |
| [PFN_WDFDEVICEGETSYSTEMPOWERACTION callback function](nc-wdfdevice-pfn-wdfdevicegetsystempoweraction.md) | TBD |
| [PFN_WDFDEVICEINITSETPOWERPOLICYEVENTCALLBACKS callback function](nc-wdfdevice-pfn-wdfdeviceinitsetpowerpolicyeventcallbacks.md) | TBD |
| [PFN_WDFDEVICERESUMEIDLEACTUAL callback function](nc-wdfdevice-pfn-wdfdeviceresumeidleactual.md) | TBD |
| [EVT_WDF_DEVICE_WAKE_FROM_SX_TRIGGERED callback](nc-wdfdevice-evt-wdf-device-wake-from-sx-triggered.md) | A driver's EvtDeviceWakeFromSxTriggered event callback function informs the driver that its device, which had previously entered a low-power device state because system power was reduced, might have triggered a wake signal. |
| [PFN_WDFDEVICEPOSTEVENT callback function](nc-wdfdevice-pfn-wdfdevicepostevent.md) | TBD |
| [PFN_WDFDEVICEQUERYPROPERTY callback function](nc-wdfdevice-pfn-wdfdevicequeryproperty.md) | TBD |
| [PFN_WDFDEVICECONFIGUREREQUESTDISPATCHING callback function](nc-wdfdevice-pfn-wdfdeviceconfigurerequestdispatching.md) | TBD |
| [PFN_WDFDEVICEREMOVEREMOVALRELATIONSPHYSICALDEVICE callback function](nc-wdfdevice-pfn-wdfdeviceremoveremovalrelationsphysicaldevice.md) | TBD |
| [PFN_WDFDEVICEGETFILEOBJECT callback function](nc-wdfdevice-pfn-wdfdevicegetfileobject.md) | TBD |
| [PFN_WDFDEVICEINITASSIGNNAME callback function](nc-wdfdevice-pfn-wdfdeviceinitassignname.md) | TBD |
| [PFN_WDFDEVICEWDMDISPATCHPREPROCESSEDIRP callback function](nc-wdfdevice-pfn-wdfdevicewdmdispatchpreprocessedirp.md) | TBD |
| [PFN_WDFDEVICEALLOCANDQUERYPROPERTY callback function](nc-wdfdevice-pfn-wdfdeviceallocandqueryproperty.md) | TBD |
| [PFN_WDFDEVICEWDMGETDEVICEOBJECT callback function](nc-wdfdevice-pfn-wdfdevicewdmgetdeviceobject.md) | TBD |
| [PFN_WDFDEVICERETRIEVEDEVICENAME callback function](nc-wdfdevice-pfn-wdfdeviceretrievedevicename.md) | TBD |
| [PFN_WDFDEVICEINITSETCHARACTERISTICS callback function](nc-wdfdevice-pfn-wdfdeviceinitsetcharacteristics.md) | TBD |
| [PFN_WDFDEVICEGETIOTARGET callback function](nc-wdfdevice-pfn-wdfdevicegetiotarget.md) | TBD |
| [PFN_WDFDEVICEINDICATEWAKESTATUS callback function](nc-wdfdevice-pfn-wdfdeviceindicatewakestatus.md) | TBD |
| [PFN_WDFDEVICESETCHARACTERISTICS callback function](nc-wdfdevice-pfn-wdfdevicesetcharacteristics.md) | TBD |
| [EVT_WDF_DEVICE_PREPARE_HARDWARE callback](nc-wdfdevice-evt-wdf-device-prepare-hardware.md) | A driver's EvtDevicePrepareHardware event callback function performs any operations that are needed to make a device accessible to the driver. |
| [PFN_WDFDEVICERETRIEVEDEVICEINTERFACESTRING callback function](nc-wdfdevice-pfn-wdfdeviceretrievedeviceinterfacestring.md) | TBD |
| [PFN_WDFDEVICEOPENDEVICEMAPKEY callback function](nc-wdfdevice-pfn-wdfdeviceopendevicemapkey.md) | TBD |
| [PFN_WDFDEVICEINITASSIGNWDMIRPPREPROCESSCALLBACK callback function](nc-wdfdevice-pfn-wdfdeviceinitassignwdmirppreprocesscallback.md) | TBD |
| [PFN_WDFDEVICEINITSETPOWERINRUSH callback function](nc-wdfdevice-pfn-wdfdeviceinitsetpowerinrush.md) | TBD |
| [EVT_WDFDEVICE_WDM_IRP_PREPROCESS callback](nc-wdfdevice-evt-wdfdevice-wdm-irp-preprocess.md) | A driver's EvtDeviceWdmIrpPreprocess event callback function receives an IRP before the framework processes the IRP. |
| [PFN_WDFDEVICECLEARREMOVALRELATIONSDEVICES callback function](nc-wdfdevice-pfn-wdfdeviceclearremovalrelationsdevices.md) | TBD |
| [PFN_WDFDEVICERETRIEVECOMPANIONTARGET callback function](nc-wdfdevice-pfn-wdfdeviceretrievecompaniontarget.md) | TBD |
| [PFN_WDFDEVICESETPOWERCAPABILITIES callback function](nc-wdfdevice-pfn-wdfdevicesetpowercapabilities.md) | TBD |
| [PFN_WDFDEVICEINITSETREQUESTATTRIBUTES callback function](nc-wdfdevice-pfn-wdfdeviceinitsetrequestattributes.md) | TBD |
| [PFN_WDFDEVICEOPENREGISTRYKEY callback function](nc-wdfdevice-pfn-wdfdeviceopenregistrykey.md) | TBD |
| [PFN_WDFDEVICEADDREMOVALRELATIONSPHYSICALDEVICE callback function](nc-wdfdevice-pfn-wdfdeviceaddremovalrelationsphysicaldevice.md) | TBD |
| [PFN_WDFDEVICEGETDEVICEPOWERSTATE callback function](nc-wdfdevice-pfn-wdfdevicegetdevicepowerstate.md) | TBD |
| [PFN_WDFDEVICEINITSETDEVICECLASS callback function](nc-wdfdevice-pfn-wdfdeviceinitsetdeviceclass.md) | TBD |
| [PFN_WDFDEVICEASSIGNMOFRESOURCENAME callback function](nc-wdfdevice-pfn-wdfdeviceassignmofresourcename.md) | TBD |
| [PFN_WDFDEVICEINITFREE callback function](nc-wdfdevice-pfn-wdfdeviceinitfree.md) | TBD |
| [PFN_WDFDEVICEINITSETPOWERPOLICYOWNERSHIP callback function](nc-wdfdevice-pfn-wdfdeviceinitsetpowerpolicyownership.md) | TBD |
| [PFN_WDFDEVICESETPNPCAPABILITIES callback function](nc-wdfdevice-pfn-wdfdevicesetpnpcapabilities.md) | TBD |
| [PFN_WDFDEVICEADDDEPENDENTUSAGEDEVICEOBJECT callback function](nc-wdfdevice-pfn-wdfdeviceadddependentusagedeviceobject.md) | TBD |
| [EVT_WDF_DEVICE_D0_ENTRY_POST_INTERRUPTS_ENABLED callback](nc-wdfdevice-evt-wdf-device-d0-entry-post-interrupts-enabled.md) | A driver's EvtDeviceD0EntryPostInterruptsEnabled event callback function performs device-specific operations that are required after the driver has enabled the device's hardware interrupts. |
| [EVT_WDF_DEVICE_SELF_MANAGED_IO_RESTART callback](nc-wdfdevice-evt-wdf-device-self-managed-io-restart.md) | A driver's EvtDeviceSelfManagedIoRestart event callback function restarts a device's self-managed I/O operations. |
| [EVT_WDF_DEVICE_SELF_MANAGED_IO_INIT callback](nc-wdfdevice-evt-wdf-device-self-managed-io-init.md) | A driver's EvtDeviceSelfManagedIoInit event callback function initializes and starts the device's self-managed I/O operations. |
| [PFN_WDFDEVICEQUERYPROPERTYEX callback function](nc-wdfdevice-pfn-wdfdevicequerypropertyex.md) | TBD |
| [PFN_WDFDEVICEWDMASSIGNPOWERFRAMEWORKSETTINGS callback function](nc-wdfdevice-pfn-wdfdevicewdmassignpowerframeworksettings.md) | TBD |
| [PFN_WDFDEVICEINITSETREMOVELOCKOPTIONS callback function](nc-wdfdevice-pfn-wdfdeviceinitsetremovelockoptions.md) | TBD |
| [EVT_WDF_DEVICE_ARM_WAKE_FROM_SX_WITH_REASON callback](nc-wdfdevice-evt-wdf-device-arm-wake-from-sx-with-reason.md) | A driver's EvtDeviceArmWakeFromSxWithReason event callback function arms (that is, enables) a device so that it can trigger a wake signal while in a low-power device state. |
| [EVT_WDF_DEVICE_ARM_WAKE_FROM_S0 callback](nc-wdfdevice-evt-wdf-device-arm-wake-from-s0.md) | A driver's EvtDeviceArmWakeFromS0 event callback function arms (that is, enables) a device so that it can trigger a wake signal while in a low-power device state, if the system remains in the system working state (S0). |
| [EVT_WDF_DEVICE_QUERY_REMOVE callback](nc-wdfdevice-evt-wdf-device-query-remove.md) | A driver's EvtDeviceQueryRemove event callback function determines whether a specified device can be stopped and removed. |
| [PFN_WDFDEVICEGETCHARACTERISTICS callback function](nc-wdfdevice-pfn-wdfdevicegetcharacteristics.md) | TBD |
| [PFN_WDFDEVICEWDMGETPHYSICALDEVICE callback function](nc-wdfdevice-pfn-wdfdevicewdmgetphysicaldevice.md) | TBD |
| [PFN_WDFDEVICEINITSETIOTYPEEX callback function](nc-wdfdevice-pfn-wdfdeviceinitsetiotypeex.md) | TBD |
| [PFN_WDFDEVICEENQUEUEREQUEST callback function](nc-wdfdevice-pfn-wdfdeviceenqueuerequest.md) | TBD |
| [EVT_WDF_DEVICE_SELF_MANAGED_IO_SUSPEND callback](nc-wdfdevice-evt-wdf-device-self-managed-io-suspend.md) | A driver's EvtDeviceSelfManagedIoSuspend event callback function suspends a device's self-managed I/O operations. |
| [PFN_WDFDEVICEGETHARDWAREREGISTERMAPPEDADDRESS callback function](nc-wdfdevice-pfn-wdfdevicegethardwareregistermappedaddress.md) | TBD |
| [PFN_WDFDEVICECREATESYMBOLICLINK callback function](nc-wdfdevice-pfn-wdfdevicecreatesymboliclink.md) | TBD |
| [EVT_WDF_DEVICE_WAKE_FROM_S0_TRIGGERED callback](nc-wdfdevice-evt-wdf-device-wake-from-s0-triggered.md) | A driver's EvtDeviceWakeFromS0Triggered event callback function informs the driver that its device, which had previously entered a low-power device state while the system power state remained at S0, might have triggered a wake signal. |
| [EVT_WDFDEVICE_WDM_POST_PO_FX_REGISTER_DEVICE callback](nc-wdfdevice-evt-wdfdevice-wdm-post-po-fx-register-device.md) | The EvtDeviceWdmPostPoFxRegisterDevice callback function performs device-specific operations after the framework has registered with the power framework. |
| [PFN_WDFDEVICEINITSETEXCLUSIVE callback function](nc-wdfdevice-pfn-wdfdeviceinitsetexclusive.md) | TBD |
| [PFN_WDFDEVICEINITREGISTERPNPSTATECHANGECALLBACK callback function](nc-wdfdevice-pfn-wdfdeviceinitregisterpnpstatechangecallback.md) | TBD |
| [EVT_WDF_IO_IN_CALLER_CONTEXT callback](nc-wdfdevice-evt-wdf-io-in-caller-context.md) | A driver's EvtIoInCallerContext event callback function preprocesses an I/O request before the framework places it into an I/O queue. |
| [PFN_WDFDEVICEASSIGNS0IDLESETTINGS callback function](nc-wdfdevice-pfn-wdfdeviceassigns0idlesettings.md) | TBD |
| [PFN_WDFDEVICEREADFROMHARDWARE callback function](nc-wdfdevice-pfn-wdfdevicereadfromhardware.md) | TBD |
| [PFN_WDFDEVICEALLOCANDQUERYINTERFACEPROPERTY callback function](nc-wdfdevice-pfn-wdfdeviceallocandqueryinterfaceproperty.md) | TBD |
| [EVT_WDF_DEVICE_D0_EXIT callback](nc-wdfdevice-evt-wdf-device-d0-exit.md) | A driver's EvtDeviceD0Exit event callback function performs operations that are needed when the driver's device leaves the D0 power state. |
| [PFN_WDFDEVICEINITSETPNPPOWEREVENTCALLBACKS callback function](nc-wdfdevice-pfn-wdfdeviceinitsetpnppowereventcallbacks.md) | TBD |
| [PFN_WDFDEVICERESUMEIDLENOTRACK callback function](nc-wdfdevice-pfn-wdfdeviceresumeidlenotrack.md) | TBD |
| [PFN_WDFDEVICEASSIGNINTERFACEPROPERTY callback function](nc-wdfdevice-pfn-wdfdeviceassigninterfaceproperty.md) | TBD |
| [EVT_WDF_DEVICE_DISARM_WAKE_FROM_SX callback](nc-wdfdevice-evt-wdf-device-disarm-wake-from-sx.md) | A driver's EvtDeviceDisarmWakeFromSx event callback function disarms (that is, disables) a device's ability to trigger a wake signal while the device and system are in low-power states. |
| [PFN_WDFDEVICEGETALIGNMENTREQUIREMENT callback function](nc-wdfdevice-pfn-wdfdevicegetalignmentrequirement.md) | TBD |
| [PFN_WDFDEVICESETSPECIALFILESUPPORT callback function](nc-wdfdevice-pfn-wdfdevicesetspecialfilesupport.md) | TBD |
| [PFN_WDFDEVICEINITSETPOWERPAGEABLE callback function](nc-wdfdevice-pfn-wdfdeviceinitsetpowerpageable.md) | TBD |
| [PFN_WDFDEVICESETALIGNMENTREQUIREMENT callback function](nc-wdfdevice-pfn-wdfdevicesetalignmentrequirement.md) | TBD |
| [EVT_WDF_DEVICE_RELATIONS_QUERY callback](nc-wdfdevice-evt-wdf-device-relations-query.md) | A driver's EvtDeviceRelationsQuery event callback reports changes in the relationships among devices that are supported by the driver. |
| [EVT_WDF_DEVICE_SURPRISE_REMOVAL callback](nc-wdfdevice-evt-wdf-device-surprise-removal.md) | A driver's EvtDeviceSurpriseRemoval event callback function performs any operations that are needed after a device has been unexpectedly removed from the system or after a driver reports that the device has failed. |
| [EVT_WDF_FILE_CLEANUP callback](nc-wdfdevice-evt-wdf-file-cleanup.md) | A driver's EvtFileCleanup callback function handles operations that must be performed when an application is closing all accesses to a device. |
| [PFN_WDFDEVICEGETDEVICESTACKIOTYPE callback function](nc-wdfdevice-pfn-wdfdevicegetdevicestackiotype.md) | TBD |
| [EVT_WDF_DEVICE_SELF_MANAGED_IO_CLEANUP callback](nc-wdfdevice-evt-wdf-device-self-managed-io-cleanup.md) | A driver's EvtDeviceSelfManagedIoCleanup event callback function handles deallocation activity for the device's self-managed I/O operations, after a device has been removed. |
| [EVT_WDF_DEVICE_D0_EXIT_PRE_INTERRUPTS_DISABLED callback](nc-wdfdevice-evt-wdf-device-d0-exit-pre-interrupts-disabled.md) | A driver's EvtDeviceD0ExitPreInterruptsDisabled event callback function performs device-specific operations that are required before the driver disables the device's hardware interrupts. |
| [PFN_WDFDEVICEGETDEFAULTQUEUE callback function](nc-wdfdevice-pfn-wdfdevicegetdefaultqueue.md) | TBD |
| [PFN_WDFDEVICEGETDRIVER callback function](nc-wdfdevice-pfn-wdfdevicegetdriver.md) | TBD |
| [*PFN_WDFDEVICESTOPIDLEACTUAL callback function](nc-wdfdevice-pfn-wdfdevicestopidleactual.md) | TBD |
| [EVT_WDFDEVICE_WDM_IRP_DISPATCH callback](nc-wdfdevice-evt-wdfdevice-wdm-irp-dispatch.md) | A driver's EvtDeviceWdmIrpDispatch event callback function receives an IRP before the framework processes the IRP. |
| [EVT_WDF_DEVICE_ARM_WAKE_FROM_SX callback](nc-wdfdevice-evt-wdf-device-arm-wake-from-sx.md) | A driver's EvtDeviceArmWakeFromSx event callback function arms (that is, enables) a device so that it can trigger a wake signal while in a low-power device state. |
| [PFN_WDFDEVICEUNMAPIOSPACE callback function](nc-wdfdevice-pfn-wdfdeviceunmapiospace.md) | TBD |
| [PFN_WDFDEVICEQUERYINTERFACEPROPERTY callback function](nc-wdfdevice-pfn-wdfdevicequeryinterfaceproperty.md) | TBD |
| [*PFN_WDFDEVICESTOPIDLENOTRACK callback function](nc-wdfdevice-pfn-wdfdevicestopidlenotrack.md) | TBD |
| [PFN_WDFDEVICEGETDEVICEPOWERPOLICYSTATE callback function](nc-wdfdevice-pfn-wdfdevicegetdevicepowerpolicystate.md) | TBD |
| [EVT_WDF_DEVICE_USAGE_NOTIFICATION_EX callback](nc-wdfdevice-evt-wdf-device-usage-notification-ex.md) | A driver's EvtDeviceUsageNotificationEx event callback function determines whether a device can support a special file type. |
| [PFN_WDFDEVICEINITSETPOWERNOTPAGEABLE callback function](nc-wdfdevice-pfn-wdfdeviceinitsetpowernotpageable.md) | TBD |
| [EVT_WDF_DEVICE_DISARM_WAKE_FROM_S0 callback](nc-wdfdevice-evt-wdf-device-disarm-wake-from-s0.md) | A driver's EvtDeviceDisarmWakeFromS0 event callback function disarms (that is, disables) a device's ability to trigger a wake signal while in a low-power device state, if the system remains in the system working state (S0). |
| [PFN_WDFDEVICESETDEVICESTATE callback function](nc-wdfdevice-pfn-wdfdevicesetdevicestate.md) | TBD |
| [PFN_WDFDEVICEINITASSIGNSDDLSTRING callback function](nc-wdfdevice-pfn-wdfdeviceinitassignsddlstring.md) | TBD |
| [PFN_WDFDEVICEINITSETIOINCALLERCONTEXTCALLBACK callback function](nc-wdfdevice-pfn-wdfdeviceinitsetioincallercontextcallback.md) | TBD |
| [PFN_WDFDEVICEINITSETIOTYPE callback function](nc-wdfdevice-pfn-wdfdeviceinitsetiotype.md) | TBD |
| [EVT_WDF_DEVICE_PNP_STATE_CHANGE_NOTIFICATION callback](nc-wdfdevice-evt-wdf-device-pnp-state-change-notification.md) | A driver's EvtDevicePnpStateChange event callback function informs the driver that a device's Plug and Play (PnP) state machine is moving from one state to another. |
| [PFN_WDFDEVICEINITSETDEVICETYPE callback function](nc-wdfdevice-pfn-wdfdeviceinitsetdevicetype.md) | TBD |
| [EVT_WDF_DEVICE_RELEASE_HARDWARE callback](nc-wdfdevice-evt-wdf-device-release-hardware.md) | A driver's EvtDeviceReleaseHardware event callback function performs operations that are needed when a device is no longer accessible. |
| [PFN_WDFDEVICEGETDEVICEPNPSTATE callback function](nc-wdfdevice-pfn-wdfdevicegetdevicepnpstate.md) | TBD |
| [EVT_WDF_DEVICE_FILE_CREATE callback](nc-wdfdevice-evt-wdf-device-file-create.md) | A driver's EvtDeviceFileCreate callback function handles operations that must be performed when an application requests access to a device. |
| [PFN_WDFDEVICECREATEDEVICEINTERFACE callback function](nc-wdfdevice-pfn-wdfdevicecreatedeviceinterface.md) | TBD |
| [EVT_WDF_DEVICE_D0_ENTRY callback](nc-wdfdevice-evt-wdf-device-d0-entry.md) | A driver's EvtDeviceD0Entry event callback function performs operations that are needed when the driver's device enters the D0 power state. |
| [PFN_WDFDEVICEMAPIOSPACE callback function](nc-wdfdevice-pfn-wdfdevicemapiospace.md) | TBD |
| [PFN_WDFDEVICEWDMDISPATCHIRPTOIOQUEUE callback function](nc-wdfdevice-pfn-wdfdevicewdmdispatchirptoioqueue.md) | TBD |
| [EVT_WDF_DEVICE_QUERY_STOP callback](nc-wdfdevice-evt-wdf-device-query-stop.md) | A driver's EvtDeviceQueryStop event callback function determines whether a specified device can be stopped so that the PnP manager can redistribute system hardware resources. |
| [PFN_WDFDEVICESETDEVICEINTERFACESTATE callback function](nc-wdfdevice-pfn-wdfdevicesetdeviceinterfacestate.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_POWER_POLICY_IDLE_TIMEOUT_CONSTANTS enumeration](ne-wdfdevice--wdf-power-policy-idle-timeout-constants.md) | The WDF_POWER_POLICY_IDLE_TIMEOUT_CONSTANTS enumeration is reserved for internal use. |
| [WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE enumeration](ne-wdfdevice--wdf-power-policy-idle-timeout-type.md) | The WDF_POWER_POLICY_IDLE_TIMEOUT_TYPE enumeration identifies how the idle timeout for a device is determined. |
| [WDF_DEVICE_PNP_STATE enumeration](ne-wdfdevice--wdf-device-pnp-state.md) | The WDF_DEVICE_PNP_STATE enumeration identifies all of the states that the framework's Plug and Play state machine can enter. |
| [WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE enumeration](ne-wdfdevice--wdf-release-hardware-order-on-failure.md) | The WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE enumeration specifies when the framework calls a driver's EvtDeviceReleaseHardware callback function. |
| [WDF_DEVICE_HWACCESS_TARGET_TYPE enumeration](ne-wdfdevice--wdf-device-hwaccess-target-type.md) | The WDF_DEVICE_HWACCESS_TARGET_TYPE enumeration is used internally by the framework. Do not use. |
| [WDF_REQUEST_TYPE enumeration](ne-wdfdevice--wdf-request-type.md) | TBD |
| [WDF_DEVICE_POWER_POLICY_STATE enumeration](ne-wdfdevice--wdf-device-power-policy-state.md) | The WDF_DEVICE_POWER_POLICY_STATE enumeration identifies all of the states that the framework's power policy state machine can enter. |
| [WDF_SPECIAL_FILE_TYPE enumeration](ne-wdfdevice--wdf-special-file-type.md) | The WDF_SPECIAL_FILE_TYPE enumeration identifies special file types that a device can support. |
| [WDF_DEVICE_POWER_STATE enumeration](ne-wdfdevice--wdf-device-power-state.md) | The WDF_DEVICE_POWER_STATE enumeration identifies all of the states that the framework's power state machine can enter. |
| [WDF_EVENT_TYPE enumeration](ne-wdfdevice--wdf-event-type.md) | The WDF_EVENT_TYPE enumeration specifies. |
| [WDF_DEVICE_STATE_FLAGS enumeration](ne-wdfdevice--wdf-device-state-flags.md) | TBD |
| [WDF_POWER_POLICY_SX_WAKE_USER_CONTROL enumeration](ne-wdfdevice--wdf-power-policy-sx-wake-user-control.md) | The WDF_POWER_POLICY_SX_WAKE_USER_CONTROL enumeration identifies whether a user can control a device's ability to wake the system from a low system power state. |
| [WDF_REMOVE_LOCK_OPTIONS_FLAGS enumeration](ne-wdfdevice--wdf-remove-lock-options-flags.md) | The WDF_REMOVE_LOCK_OPTIONS_FLAGS enumeration type defines flags that are used in a driver's WDF_REMOVE_LOCK_OPTIONS structure. |
| [WDF_DEVICE_IO_TYPE enumeration](ne-wdfdevice--wdf-device-io-type.md) | The WDF_DEVICE_IO_TYPE enumeration is used to specify a method for accessing data buffers. |
| [WDF_POWER_POLICY_S0_IDLE_CAPABILITIES enumeration](ne-wdfdevice--wdf-power-policy-s0-idle-capabilities.md) | The WDF_POWER_POLICY_S0_IDLE_CAPABILITIES enumeration identifies the capabilities that a device can support when it enters a low-power state while it is idling. |
| [WDF_DEVICE_HWACCESS_TARGET_SIZE enumeration](ne-wdfdevice--wdf-device-hwaccess-target-size.md) | The WDF_DEVICE_HWACCESS_TARGET_SIZE enumeration is used internally by the framework. Do not use. |
| [WDF_FILEOBJECT_CLASS enumeration](ne-wdfdevice--wdf-fileobject-class.md) | The WDF_FILEOBJECT_CLASS enumeration defines values that identify whether a driver requires a framework file object to represent a file that an application or another driver is attempting to create or open. |
| [WDF_DISPATCH_IRP_TO_IO_QUEUE_FLAGS enumeration](ne-wdfdevice--wdf-dispatch-irp-to-io-queue-flags.md) | The WDF_DISPATCH_IRP_TO_IO_QUEUE_FLAGS enumeration type defines flags that the driver can specify when it calls WdfDeviceWdmDispatchIrpToIoQueue. |
| [WDF_DEVICE_FAILED_ACTION enumeration](ne-wdfdevice--wdf-device-failed-action.md) | The WDF_DEVICE_FAILED_ACTION enumeration identifies the action that the framework will take when a driver reports an unrecoverable software or hardware failure. |
| [WDF_STATE_NOTIFICATION_TYPE enumeration](ne-wdfdevice--wdf-state-notification-type.md) | The WDF_STATE_NOTIFICATION_TYPE enumeration identifies the type of Plug and Play, power, or power policy notification that a framework-based driver will receive. |
| [WDF_POWER_POLICY_S0_IDLE_USER_CONTROL enumeration](ne-wdfdevice--wdf-power-policy-s0-idle-user-control.md) | The WDF_POWER_POLICY_S0_IDLE_USER_CONTROL enumeration identifies whether a user can control a device's behavior when the device is idle and the system is in its working (S0) state. |
| [WDF_POWER_DEVICE_STATE enumeration](ne-wdfdevice--wdf-power-device-state.md) | The WDF_POWER_DEVICE_STATE enumeration identifies the device power states that a device might support. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA structure](ns-wdfdevice--wdf-device-power-policy-notification-data.md) | The WDF_DEVICE_POWER_POLICY_NOTIFICATION_DATA structure describes a state change within a device's power policy state machine. |
| [WDF_DEVICE_PNP_NOTIFICATION_DATA structure](ns-wdfdevice--wdf-device-pnp-notification-data.md) | The WDF_DEVICE_PNP_NOTIFICATION_DATA structure describes a state change within a device's Plug and Play state machine. |
| [WDF_DEVICE_STATE structure](ns-wdfdevice--wdf-device-state.md) | The WDF_DEVICE_STATE structure specifies a device's Plug and Play state. |
| [WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS structure](ns-wdfdevice--wdf-device-power-policy-idle-settings.md) | The WDF_DEVICE_POWER_POLICY_IDLE_SETTINGS structure contains driver-supplied information that the framework uses when a device is idle and the system is in the system working state (S0). |
| [WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS structure](ns-wdfdevice--wdf-device-power-policy-wake-settings.md) | The WDF_DEVICE_POWER_POLICY_WAKE_SETTINGS structure contains driver-supplied information about a device's ability to wake itself and the system, when both are in a low-power state. |
| [WDF_IO_TYPE_CONFIG structure](ns-wdfdevice--wdf-io-type-config.md) | The WDF_IO_TYPE_CONFIG structure specifies the driver's preferred buffer access method for read and write requests, and for device I/O control requests. |
| [WDF_DEVICE_POWER_NOTIFICATION_DATA structure](ns-wdfdevice--wdf-device-power-notification-data.md) | The WDF_DEVICE_POWER_NOTIFICATION_DATA structure describes a state change within a device's power state machine. |
| [WDF_DEVICE_INTERFACE_PROPERTY_DATA structure](ns-wdfdevice--wdf-device-interface-property-data.md) | The WDF_DEVICE_INTERFACE_PROPERTY_DATA structure describes a device interface property. |
| [WDF_DEVICE_POWER_CAPABILITIES structure](ns-wdfdevice--wdf-device-power-capabilities.md) | The WDF_DEVICE_POWER_CAPABILITIES structure describes a device's power capabilities. |
| [WDF_DEVICE_PROPERTY_DATA structure](ns-wdfdevice--wdf-device-property-data.md) | The WDF_DEVICE_PROPERTY_DATA structure describes a device property. |
| [WDF_PNPPOWER_EVENT_CALLBACKS structure](ns-wdfdevice--wdf-pnppower-event-callbacks.md) | The WDF_PNPPOWER_EVENT_CALLBACKS structure contains pointers to a driver's Plug and Play and power event callback functions. |
| [WDF_POWER_POLICY_EVENT_CALLBACKS structure](ns-wdfdevice--wdf-power-policy-event-callbacks.md) | The WDF_POWER_POLICY_EVENT_CALLBACKS structure contains pointers to a driver's power policy event callback functions. |
| [WDF_REMOVE_LOCK_OPTIONS structure](ns-wdfdevice--wdf-remove-lock-options.md) | The WDF_REMOVE_LOCK_OPTIONS structure specifies options for acquiring a remove lock before delivering an IRP to the driver. |
| [WDF_POWER_FRAMEWORK_SETTINGS structure](ns-wdfdevice--wdf-power-framework-settings.md) | The WDF_POWER_FRAMEWORK_SETTINGS structure describes power management framework (PoFx) settings for single-component devices. |
| [WDF_FILEOBJECT_CONFIG structure](ns-wdfdevice--wdf-fileobject-config.md) | The WDF_FILEOBJECT_CONFIG structure contains configuration information of a driver's framework file objects. |
| [WDF_DEVICE_PNP_CAPABILITIES structure](ns-wdfdevice--wdf-device-pnp-capabilities.md) | The WDF_DEVICE_PNP_CAPABILITIES structure describes a device's Plug and Play capabilities. |

This header is used in these topics:

- [wdf](..content/_wdf)
