# Declarations in the wudfddi header
This header Wudfddi contains these programming interfaces:

Interface

| Title        | Description    |
| ------------- |:-------------:|
| [IWDFIoRequestCompletionParams interface](nn-wudfddi-iwdfiorequestcompletionparams.md) | The IWDFIoRequestCompletionParams interface exposes methods that drivers can use to obtain completion information about an I/O request. Drivers can call these methods after a synchronous or asynchronous I/O operation completes. |
| [IWDFPropertyStoreFactory interface](nn-wudfddi-iwdfpropertystorefactory.md) | The IWDFPropertyStoreFactory interface is a factory interface that is used to create a property store interface. |
| [IFileCallbackClose interface](nn-wudfddi-ifilecallbackclose~r1.md) | The framework can notify a driver when the driver should perform a close operation. The driver can handle the notification by registering the IFileCallbackClose interface. |
| [IImpersonateCallback interface](nn-wudfddi-iimpersonatecallback~r1.md) | The IImpersonateCallback interface contains a method that handles impersonation. |
| [IWDFIoTarget interface](nn-wudfddi-iwdfiotarget.md) | The IWDFIoTarget interface exposes the I/O target object that typically represents a lower driver in the stack. |
| [IRemoteInterfaceCallbackEvent interface](nn-wudfddi-iremoteinterfacecallbackevent.md) | The IRemoteInterfaceCallbackEvent interface provides a callback function that the framework calls to notify the driver about device events that are associated with a device interface. |
| [IDriverEntry interface](nn-wudfddi-idriverentry~r1.md) | The IDriverEntry interface exposes the user-mode driver's main entry and exit points. |
| [IQueueCallbackIoStop interface](nn-wudfddi-iqueuecallbackiostop.md) | The IQueueCallbackIoStop interface contains a method that stops the processing of an I/O request from a queue. |
| [IWDFCmResourceList interface](nn-wudfddi-iwdfcmresourcelist.md) | This interface represents a list of hardware resources for a device. |
| [IWDFFile interface](nn-wudfddi-iwdffile.md) | The IWDFFile interface exposes the file object that represents the HANDLE that is returned by the Microsoft Win32 CreateFile function. |
| [IWDFDriverCreatedFile interface](nn-wudfddi-iwdfdrivercreatedfile~r1.md) | The IWDFDriverCreatedFile interface exposes a UMDF driver-created-file object for the driver to use. |
| [IRemoteInterfaceCallbackRemoval interface](nn-wudfddi-iremoteinterfacecallbackremoval.md) | The IRemoteInterfaceCallbackRemoval provides a callback function that the framework calls to notify the driver about the removal of a device interface. |
| [IWDFNamedPropertyStore interface](nn-wudfddi-iwdfnamedpropertystore.md) | The IWDFNamedPropertyStore interface exposes a property-store object. |
| [IWDFObject interface](nn-wudfddi-iwdfobject~r1.md) | The IWDFObject interface exposes the framework base object that provides the basic functionality common across all framework object types. All framework objects are derived from this root object. |
| [IQueueCallbackIoCanceledOnQueue interface](nn-wudfddi-iqueuecallbackiocanceledonqueue~r1.md) | The IQueueCallbackIoCanceledOnQueue interface is optional. Your driver can provide this interface if you want UMDF to notify the driver when an I/O request is canceled while it is in the driver's I/O queue. |
| [IQueueCallbackWrite interface](nn-wudfddi-iqueuecallbackwrite.md) | An I/O queue object notifies a driver when a write request is available for the driver. |
| [IWDFFile3 interface](nn-wudfddi-iwdffile3.md) | Drivers obtain the IWDFFile3 interface by calling IWDFFile |
| [IFileCallbackCleanup interface](nn-wudfddi-ifilecallbackcleanup.md) | The framework can notify a driver when the driver should perform a cleanup operation. |
| [IPnpCallback interface](nn-wudfddi-ipnpcallback~r1.md) | The IPnpCallback interface is a Plug and Play (PnP) and power management (PM) interface. |
| [IRemoteInterfaceCallbackEvent interface](nn-wudfddi-iremoteinterfacecallbackevent~r1.md) | The IRemoteInterfaceCallbackEvent interface provides a callback function that the framework calls to notify the driver about device events that are associated with a device interface. |
| [IWDFDeviceInitialize2 interface](nn-wudfddi-iwdfdeviceinitialize2~r1.md) | The IWDFDeviceInitialize2 interface is a helper interface that allows a driver to specify a preferred buffer retrieval mode and buffer access method. |
| [IQueueCallbackDefaultIoHandler interface](nn-wudfddi-iqueuecallbackdefaultiohandler~r1.md) | The IQueueCallbackDefaultIoHandler interface contains a method that handles I/O requests that no other method is registered to handle. |
| [IWDFIoRequest3 interface](nn-wudfddi-iwdfiorequest3~r1.md) | To obtain the IWDFIoRequest3 interface, drivers call IWDFIoRequest |
| [IWDFUnifiedPropertyStoreFactory interface](nn-wudfddi-iwdfunifiedpropertystorefactory~r1.md) | The IWDFUnifiedPropertyStoreFactory interface is a factory interface that is used to create a unified property store interface. |
| [IWDFIoQueue interface](nn-wudfddi-iwdfioqueue.md) | The IWDFIoQueue interface exposes an I/O queue object. |
| [IPnpCallbackRemoteInterfaceNotification interface](nn-wudfddi-ipnpcallbackremoteinterfacenotification~r1.md) | A driver's IPnpCallbackRemoteInterfaceNotification interface provides a callback function that the framework calls to notify the driver when a device interface becomes available. |
| [IWDFIoRequest3 interface](nn-wudfddi-iwdfiorequest3.md) | To obtain the IWDFIoRequest3 interface, drivers call IWDFIoRequest |
| [IFileCallbackCleanup interface](nn-wudfddi-ifilecallbackcleanup~r1.md) | The framework can notify a driver when the driver should perform a cleanup operation. |
| [IQueueCallbackDefaultIoHandler interface](nn-wudfddi-iqueuecallbackdefaultiohandler.md) | The IQueueCallbackDefaultIoHandler interface contains a method that handles I/O requests that no other method is registered to handle. |
| [IWDFObject interface](nn-wudfddi-iwdfobject.md) | The IWDFObject interface exposes the framework base object that provides the basic functionality common across all framework object types. All framework objects are derived from this root object. |
| [IWDFInterrupt interface](nn-wudfddi-iwdfinterrupt~r1.md) | This interface exposes an interrupt object. |
| [IPnpCallbackSelfManagedIo interface](nn-wudfddi-ipnpcallbackselfmanagedio~r1.md) | The IPnpCallbackSelfManagedIo interface is a Plug and Play (PnP) and power management (PM) interface. |
| [IQueueCallbackWrite interface](nn-wudfddi-iqueuecallbackwrite~r1.md) | An I/O queue object notifies a driver when a write request is available for the driver. |
| [IPowerPolicyCallbackWakeFromS0 interface](nn-wudfddi-ipowerpolicycallbackwakefroms0~r1.md) | A driver's IPowerPolicyCallbackWakeFromS0 interface provides callback functions that the framework calls to notify the driver about wake events. |
| [IRequestCallbackCancel interface](nn-wudfddi-irequestcallbackcancel~r1.md) | A driver is notified when an I/O request that the driver is currently processing is to be canceled. |
| [IQueueCallbackStateChange interface](nn-wudfddi-iqueuecallbackstatechange~r1.md) | An I/O queue object raises an event when it changes state. A driver can consume the event by registering the IQueueCallbackStateChange interface. |
| [IWDFFile2 interface](nn-wudfddi-iwdffile2~r1.md) | Drivers obtain the IWDFFile2 interface by calling IWDFFile |
| [IWDFDriver interface](nn-wudfddi-iwdfdriver.md) | The IWDFDriver interface exposes the framework driver object that represents the driver image that is loaded in the host process. |
| [IWDFIoRequestCompletionParams interface](nn-wudfddi-iwdfiorequestcompletionparams~r1.md) | The IWDFIoRequestCompletionParams interface exposes methods that drivers can use to obtain completion information about an I/O request. Drivers can call these methods after a synchronous or asynchronous I/O operation completes. |
| [IWDFDeviceInitialize interface](nn-wudfddi-iwdfdeviceinitialize~r1.md) | The IWDFDeviceInitialize interface is a helper interface that the framework supplies as an input parameter to the driver's IDriverEntry |
| [IRequestCallbackRequestCompletion interface](nn-wudfddi-irequestcallbackrequestcompletion~r1.md) | A driver implements the IRequestCallbackRequestCompletion interface to complete a request object. |
| [IQueueCallbackIoStop interface](nn-wudfddi-iqueuecallbackiostop~r1.md) | The IQueueCallbackIoStop interface contains a method that stops the processing of an I/O request from a queue. |
| [IWDFRequestCompletionParams interface](nn-wudfddi-iwdfrequestcompletionparams~r1.md) | The IWDFRequestCompletionParams interface exposes methods that drivers can use to obtain completion information about an I/O request. Drivers can call these methods after a synchronous or an asynchronous I/O operation completes. |
| [IWDFNamedPropertyStore interface](nn-wudfddi-iwdfnamedpropertystore~r1.md) | The IWDFNamedPropertyStore interface exposes a property-store object. |
| [IWDFIoRequest interface](nn-wudfddi-iwdfiorequest.md) | The IWDFIoRequest interface exposes an I/O request object. |
| [IWDFFile3 interface](nn-wudfddi-iwdffile3~r1.md) | Drivers obtain the IWDFFile3 interface by calling IWDFFile |
| [IWDFRemoteInterfaceInitialize interface](nn-wudfddi-iwdfremoteinterfaceinitialize.md) | UMDF-based drivers receive the IWDFRemoteInterfaceInitialize interface as input to an IPnpCallbackRemoteInterfaceNotification |
| [IWDFIoRequest2 interface](nn-wudfddi-iwdfiorequest2.md) | To obtain the IWDFIoRequest2 interface, drivers call IWDFIoRequest |
| [IWDFRequestCompletionParams interface](nn-wudfddi-iwdfrequestcompletionparams.md) | The IWDFRequestCompletionParams interface exposes methods that drivers can use to obtain completion information about an I/O request. Drivers can call these methods after a synchronous or an asynchronous I/O operation completes. |
| [IWDFDevice interface](nn-wudfddi-iwdfdevice.md) | The IWDFDevice interface exposes a device object, which is a representation of a device on the system. |
| [IWDFDeviceInitialize2 interface](nn-wudfddi-iwdfdeviceinitialize2.md) | The IWDFDeviceInitialize2 interface is a helper interface that allows a driver to specify a preferred buffer retrieval mode and buffer access method. |
| [IWDFFile interface](nn-wudfddi-iwdffile~r1.md) | The IWDFFile interface exposes the file object that represents the HANDLE that is returned by the Microsoft Win32 CreateFile function. |
| [IWDFIoTargetStateManagement interface](nn-wudfddi-iwdfiotargetstatemanagement.md) | The IWDFIoTargetStateManagement interface exposes methods that manage and monitor the state of an I/O target object. |
| [IFileCallbackClose interface](nn-wudfddi-ifilecallbackclose.md) | The framework can notify a driver when the driver should perform a close operation. The driver can handle the notification by registering the IFileCallbackClose interface. |
| [IPnpCallbackHardware interface](nn-wudfddi-ipnpcallbackhardware~r1.md) | The IPnpCallbackHardware interface is a Plug and Play (PnP) and power management (PM) interface. |
| [IWDFUnifiedPropertyStore interface](nn-wudfddi-iwdfunifiedpropertystore~r1.md) | The IWDFUnifiedPropertyStore interface exposes a unified property store. |
| [IWDFUnifiedPropertyStore interface](nn-wudfddi-iwdfunifiedpropertystore.md) | The IWDFUnifiedPropertyStore interface exposes a unified property store. |
| [IRemoteTargetCallbackRemoval interface](nn-wudfddi-iremotetargetcallbackremoval.md) | The IRemoteTargetCallbackRemoval interface provides callback functions that the framework calls to notify the driver about events that are associated with the removal of a remote I/O target. |
| [IWDFRemoteInterfaceInitialize interface](nn-wudfddi-iwdfremoteinterfaceinitialize~r1.md) | UMDF-based drivers receive the IWDFRemoteInterfaceInitialize interface as input to an IPnpCallbackRemoteInterfaceNotification |
| [IQueueCallbackRead interface](nn-wudfddi-iqueuecallbackread~r1.md) | An I/O queue notifies a driver when a read request is available for the driver. |
| [IWDFFileHandleTargetFactory interface](nn-wudfddi-iwdffilehandletargetfactory.md) | The IWDFFileHandleTargetFactory interface is a factory interface that is used to create a file-handle-based target device object. |
| [IWDFIoRequest interface](nn-wudfddi-iwdfiorequest~r1.md) | The IWDFIoRequest interface exposes an I/O request object. |
| [IWDFIoTargetStateManagement interface](nn-wudfddi-iwdfiotargetstatemanagement~r1.md) | The IWDFIoTargetStateManagement interface exposes methods that manage and monitor the state of an I/O target object. |
| [IPowerPolicyCallbackWakeFromSx interface](nn-wudfddi-ipowerpolicycallbackwakefromsx~r1.md) | A driver's IPowerPolicyCallbackWakeFromSx interface provides callback functions that the framework calls to notify the driver about wake events. These events are related to a device's ability to wake both itself and the system from a low-power state. |
| [IWDFDriver interface](nn-wudfddi-iwdfdriver~r1.md) | The IWDFDriver interface exposes the framework driver object that represents the driver image that is loaded in the host process. |
| [IWDFIoTarget2 interface](nn-wudfddi-iwdfiotarget2.md) | To obtain the IWDFIoTarget2 interface, drivers call IWDFIoTarget |
| [IObjectCleanup interface](nn-wudfddi-iobjectcleanup~r1.md) | Any driver that stores a reference-counted COM interface to a WDF object must support the IObjectCleanup interface to prevent interface leakage. Note that drivers, in general, are not required to hold references to WDF objects. |
| [IWDFDevice3 interface](nn-wudfddi-iwdfdevice3.md) | To obtain the IWDFDevice3 interface, drivers call IWDFDevice |
| [IPnpCallbackRemoteInterfaceNotification interface](nn-wudfddi-ipnpcallbackremoteinterfacenotification.md) | A driver's IPnpCallbackRemoteInterfaceNotification interface provides a callback function that the framework calls to notify the driver when a device interface becomes available. |
| [IWDFIoTarget2 interface](nn-wudfddi-iwdfiotarget2~r1.md) | To obtain the IWDFIoTarget2 interface, drivers call IWDFIoTarget |
| [IImpersonateCallback interface](nn-wudfddi-iimpersonatecallback.md) | The IImpersonateCallback interface contains a method that handles impersonation. |
| [IRemoteInterfaceCallbackRemoval interface](nn-wudfddi-iremoteinterfacecallbackremoval~r1.md) | The IRemoteInterfaceCallbackRemoval provides a callback function that the framework calls to notify the driver about the removal of a device interface. |
| [IPnpCallbackHardware2 interface](nn-wudfddi-ipnpcallbackhardware2.md) | The IPnpCallbackHardware2 interface exposes callback methods related to hardware. |
| [IPnpCallbackSelfManagedIo interface](nn-wudfddi-ipnpcallbackselfmanagedio.md) | The IPnpCallbackSelfManagedIo interface is a Plug and Play (PnP) and power management (PM) interface. |
| [IWDFFileHandleTargetFactory interface](nn-wudfddi-iwdffilehandletargetfactory~r1.md) | The IWDFFileHandleTargetFactory interface is a factory interface that is used to create a file-handle-based target device object. |
| [IWDFFile2 interface](nn-wudfddi-iwdffile2.md) | Drivers obtain the IWDFFile2 interface by calling IWDFFile |
| [IWDFIoRequest2 interface](nn-wudfddi-iwdfiorequest2~r1.md) | To obtain the IWDFIoRequest2 interface, drivers call IWDFIoRequest |
| [IWDFMemory interface](nn-wudfddi-iwdfmemory~r1.md) | The IWDFMemory interface exposes the framework memory object that provides access to a memory block. |
| [IWDFRemoteTarget interface](nn-wudfddi-iwdfremotetarget.md) | To obtain the IWDFRemoteTarget interface, drivers call IWDFDevice2 |
| [IWDFCmResourceList interface](nn-wudfddi-iwdfcmresourcelist~r1.md) | This interface represents a list of hardware resources for a device. |
| [IPnpCallbackHardwareInterrupt interface](nn-wudfddi-ipnpcallbackhardwareinterrupt.md) | The IPnpCallbackHardwareInterrupt interface supports interrupt-related Plug and Play and power management callback methods. |
| [IObjectCleanup interface](nn-wudfddi-iobjectcleanup.md) | Any driver that stores a reference-counted COM interface to a WDF object must support the IObjectCleanup interface to prevent interface leakage. Note that drivers, in general, are not required to hold references to WDF objects. |
| [IWDFRemoteInterface interface](nn-wudfddi-iwdfremoteinterface.md) | UMDF drivers receive a pointer to this interface by calling the IWDFDevice2 |
| [IWDFWorkItem interface](nn-wudfddi-iwdfworkitem~r1.md) | This interface exposes a work item object. |
| [IPnpCallbackHardware2 interface](nn-wudfddi-ipnpcallbackhardware2~r1.md) | The IPnpCallbackHardware2 interface exposes callback methods related to hardware. |
| [IWDFMemory interface](nn-wudfddi-iwdfmemory.md) | The IWDFMemory interface exposes the framework memory object that provides access to a memory block. |
| [IWDFDevice2 interface](nn-wudfddi-iwdfdevice2.md) | Drivers obtain the IWDFDevice2 interface by calling IWDFDevice |
| [IWDFRemoteInterface interface](nn-wudfddi-iwdfremoteinterface~r1.md) | UMDF drivers receive a pointer to this interface by calling the IWDFDevice2 |
| [IWDFDevice3 interface](nn-wudfddi-iwdfdevice3~r1.md) | To obtain the IWDFDevice3 interface, drivers call IWDFDevice |
| [IPowerPolicyCallbackWakeFromS0 interface](nn-wudfddi-ipowerpolicycallbackwakefroms0.md) | A driver's IPowerPolicyCallbackWakeFromS0 interface provides callback functions that the framework calls to notify the driver about wake events. |
| [IWDFRemoteTarget interface](nn-wudfddi-iwdfremotetarget~r1.md) | To obtain the IWDFRemoteTarget interface, drivers call IWDFDevice2 |
| [IWDFNamedPropertyStore2 interface](nn-wudfddi-iwdfnamedpropertystore2.md) | Drivers obtain the IWDFNamedPropertyStore2 interface by calling IWDFPropertyStoreFactory |
| [IQueueCallbackIoResume interface](nn-wudfddi-iqueuecallbackioresume~r1.md) | The IQueueCallbackIoResume interface contains a method that resumes the processing of an I/O request from a queue. |
| [IWDFUnifiedPropertyStoreFactory interface](nn-wudfddi-iwdfunifiedpropertystorefactory.md) | The IWDFUnifiedPropertyStoreFactory interface is a factory interface that is used to create a unified property store interface. |
| [IQueueCallbackRead interface](nn-wudfddi-iqueuecallbackread.md) | An I/O queue notifies a driver when a read request is available for the driver. |
| [IQueueCallbackCreate interface](nn-wudfddi-iqueuecallbackcreate~r1.md) | An I/O queue notifies a driver when an open file request is available for the driver. |
| [IWDFDeviceInitialize interface](nn-wudfddi-iwdfdeviceinitialize.md) | The IWDFDeviceInitialize interface is a helper interface that the framework supplies as an input parameter to the driver's IDriverEntry |
| [IWDFWorkItem interface](nn-wudfddi-iwdfworkitem.md) | This interface exposes a work item object. |
| [IQueueCallbackStateChange interface](nn-wudfddi-iqueuecallbackstatechange.md) | An I/O queue object raises an event when it changes state. A driver can consume the event by registering the IQueueCallbackStateChange interface. |
| [IWDFDevice interface](nn-wudfddi-iwdfdevice~r1.md) | The IWDFDevice interface exposes a device object, which is a representation of a device on the system. |
| [IWDFIoQueue interface](nn-wudfddi-iwdfioqueue~r1.md) | The IWDFIoQueue interface exposes an I/O queue object. |
| [IQueueCallbackIoCanceledOnQueue interface](nn-wudfddi-iqueuecallbackiocanceledonqueue.md) | The IQueueCallbackIoCanceledOnQueue interface is optional. Your driver can provide this interface if you want UMDF to notify the driver when an I/O request is canceled while it is in the driver's I/O queue. |
| [IPnpCallbackHardwareInterrupt interface](nn-wudfddi-ipnpcallbackhardwareinterrupt~r1.md) | The IPnpCallbackHardwareInterrupt interface supports interrupt-related Plug and Play and power management callback methods. |
| [IQueueCallbackDeviceIoControl interface](nn-wudfddi-iqueuecallbackdeviceiocontrol.md) | An I/O queue object notifies a driver when a device I/O control request is available for the driver. |
| [IQueueCallbackDeviceIoControl interface](nn-wudfddi-iqueuecallbackdeviceiocontrol~r1.md) | An I/O queue object notifies a driver when a device I/O control request is available for the driver. |
| [IWDFPropertyStoreFactory interface](nn-wudfddi-iwdfpropertystorefactory~r1.md) | The IWDFPropertyStoreFactory interface is a factory interface that is used to create a property store interface. |
| [IPowerPolicyCallbackWakeFromSx interface](nn-wudfddi-ipowerpolicycallbackwakefromsx.md) | A driver's IPowerPolicyCallbackWakeFromSx interface provides callback functions that the framework calls to notify the driver about wake events. These events are related to a device's ability to wake both itself and the system from a low-power state. |
| [IQueueCallbackIoResume interface](nn-wudfddi-iqueuecallbackioresume.md) | The IQueueCallbackIoResume interface contains a method that resumes the processing of an I/O request from a queue. |
| [IPnpCallbackHardware interface](nn-wudfddi-ipnpcallbackhardware.md) | The IPnpCallbackHardware interface is a Plug and Play (PnP) and power management (PM) interface. |
| [IWDFInterrupt interface](nn-wudfddi-iwdfinterrupt.md) | This interface exposes an interrupt object. |
| [IQueueCallbackCreate interface](nn-wudfddi-iqueuecallbackcreate.md) | An I/O queue notifies a driver when an open file request is available for the driver. |
| [IWDFNamedPropertyStore2 interface](nn-wudfddi-iwdfnamedpropertystore2~r1.md) | Drivers obtain the IWDFNamedPropertyStore2 interface by calling IWDFPropertyStoreFactory |
| [IDriverEntry interface](nn-wudfddi-idriverentry.md) | The IDriverEntry interface exposes the user-mode driver's main entry and exit points. |
| [IPnpCallback interface](nn-wudfddi-ipnpcallback.md) | The IPnpCallback interface is a Plug and Play (PnP) and power management (PM) interface. |
| [IRemoteTargetCallbackRemoval interface](nn-wudfddi-iremotetargetcallbackremoval~r1.md) | The IRemoteTargetCallbackRemoval interface provides callback functions that the framework calls to notify the driver about events that are associated with the removal of a remote I/O target. |
| [IWDFDevice2 interface](nn-wudfddi-iwdfdevice2~r1.md) | Drivers obtain the IWDFDevice2 interface by calling IWDFDevice |
| [IWDFIoTarget interface](nn-wudfddi-iwdfiotarget~r1.md) | The IWDFIoTarget interface exposes the I/O target object that typically represents a lower driver in the stack. |
| [IRequestCallbackCancel interface](nn-wudfddi-irequestcallbackcancel.md) | A driver is notified when an I/O request that the driver is currently processing is to be canceled. |
| [IRequestCallbackRequestCompletion interface](nn-wudfddi-irequestcallbackrequestcompletion.md) | A driver implements the IRequestCallbackRequestCompletion interface to complete a request object. |
| [IWDFDriverCreatedFile interface](nn-wudfddi-iwdfdrivercreatedfile.md) | The IWDFDriverCreatedFile interface exposes a UMDF driver-created-file object for the driver to use. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [IWDFRemoteInterfaceInitialize::RetrieveSymbolicLink method](nf-wudfddi-iwdfremoteinterfaceinitialize-retrievesymboliclink.md) | The RetrieveSymbolicLink method retrieves the symbolic link name that the operating system assigned to a device interface. |
| [IWDFIoRequest::GetFileObject method](nf-wudfddi-iwdfiorequest-getfileobject.md) | The GetFileObject method retrieves a pointer to the IWDFFile interface that is associated with an I/O request. |
| [IWDFIoQueue::RetrieveNextRequest method](nf-wudfddi-iwdfioqueue-retrievenextrequest.md) | The RetrieveNextRequest method retrieves the next I/O request from an I/O queue. |
| [IWDFIoQueue::Purge method](nf-wudfddi-iwdfioqueue-purge.md) | The Purge method directs the framework to reject new incoming I/O requests and to cancel all outstanding requests. |
| [IWDFRemoteTarget::OpenFileByName method](nf-wudfddi-iwdfremotetarget-openfilebyname.md) | The OpenFileByName method opens a remote I/O target that is a file. |
| [IWDFIoQueue::Start method](nf-wudfddi-iwdfioqueue-start.md) | The Start method enables an I/O queue to start receiving new I/O requests and delivering them to a driver. |
| [IWDFIoTarget::FormatRequestForWrite method](nf-wudfddi-iwdfiotarget-formatrequestforwrite.md) | The FormatRequestForWrite method formats an I/O request object for a write operation. |
| [IWDFDevice3::GetHardwareRegisterMappedAddress method](nf-wudfddi-iwdfdevice3-gethardwareregistermappedaddress.md) | A driver calls GetHardwareRegisterMappedAddress to get the user-mode mapped address of the memory resource it earlier mapped using MapIoSpace. |
| [IWDFIoQueue::ConfigureRequestDispatching method](nf-wudfddi-iwdfioqueue-configurerequestdispatching~r1.md) | TBD |
| [IRemoteInterfaceCallbackRemoval::OnRemoteInterfaceRemoval method](nf-wudfddi-iremoteinterfacecallbackremoval-onremoteinterfaceremoval.md) | A UMDF-based driver's OnRemoteInterfaceRemoval event callback function notifies the driver that it cannot use a device interface because the interface has been removed. |
| [IWDFObject::AcquireLock method](nf-wudfddi-iwdfobject-acquirelock.md) | The AcquireLock method prevents the framework from calling methods of interfaces that a driver registered. |
| [IWDFDeviceInitialize::SetPowerPolicyOwnership method](nf-wudfddi-iwdfdeviceinitialize-setpowerpolicyownership.md) | The SetPowerPolicyOwnership method sets the ownership of the power policy to a driver or removes ownership from the driver. |
| [IPowerPolicyCallbackWakeFromS0::OnDisarmWakeFromS0 method](nf-wudfddi-ipowerpolicycallbackwakefroms0-ondisarmwakefroms0.md) | A driver's OnDisarmWakeFromS0 event callback function disarms (that is, disables) a device's ability to trigger a wake signal while in a low-power device state, if the system remains in the system working state (S0). |
| [IWDFFile2::GetRelatedFileObject method](nf-wudfddi-iwdffile2-getrelatedfileobject.md) | The GetRelatedFileObject method retrieves the IWDFFile interface of a related file object, which is a file object that has a technology-specific relationship with another file object. |
| [IWDFIoQueue::GetDevice method](nf-wudfddi-iwdfioqueue-getdevice.md) | The GetDevice method retrieves the interface to the device that owns the I/O queue. |
| [IDriverEntry::OnInitialize method](nf-wudfddi-idriverentry-oninitialize.md) | The OnInitialize method performs any operations that are necessary to initialize a driver. |
| [IWDFDevice::GetDefaultIoTarget method](nf-wudfddi-iwdfdevice-getdefaultiotarget.md) | The GetDefaultIoTarget method retrieves the interface of the default I/O target for a device instance. |
| [IWDFDeviceInitialize2::SetIoTypePreference method](nf-wudfddi-iwdfdeviceinitialize2-setiotypepreference.md) | The SetIoTypePreference method specifies your preferences for how UMDF and the driver access the data buffers of a device's I/O requests. |
| [IWDFIoRequest::CompleteWithInformation method](nf-wudfddi-iwdfiorequest-completewithinformation.md) | The CompleteWithInformation method completes a request with the supplied information. |
| [IWDFDevice2::AssignSxWakeSettings method](nf-wudfddi-iwdfdevice2-assignsxwakesettings.md) | The AssignSxWakeSettings method provides driver-supplied information about a device's ability to trigger a wake signal while both the device and the system are in a low-power state. |
| [IWDFDevice3::CreateWorkItem method](nf-wudfddi-iwdfdevice3-createworkitem.md) | The CreateWorkItem method creates a framework work-item object, which can subsequently be added to the framework’s work-item queue. |
| [IWDFDevice::CreateIoQueue method](nf-wudfddi-iwdfdevice-createioqueue.md) | The CreateIoQueue method configures the default I/O queue that is associated with a device or creates a secondary I/O queue for the device. |
| [IWDFDevice2::GetSystemPowerAction method](nf-wudfddi-iwdfdevice2-getsystempoweraction.md) | The GetSystemPowerAction method returns the system power action, if any, that is currently occurring for the computer. |
| [IWDFIoRequest::GetInputMemory method](nf-wudfddi-iwdfiorequest-getinputmemory.md) | The GetInputMemory method retrieves the memory object that represents the input buffer in an I/O request. |
| [IWDFIoRequest::GetCreateParameters method](nf-wudfddi-iwdfiorequest-getcreateparameters.md) | The GetCreateParameters method retrieves the request parameters for a create-type request. |
| [IWDFDriver::IsVersionAvailable method](nf-wudfddi-iwdfdriver-isversionavailable.md) | The IsVersionAvailable method determines whether the specified version of the framework is available. |
| [IWDFDevice3::MapIoSpace method](nf-wudfddi-iwdfdevice3-mapiospace.md) | The MapIoSpace method maps the given physical address range to system address space and returns a pseudo base address. |
| [IWDFRemoteTarget::Reopen method](nf-wudfddi-iwdfremotetarget-reopen.md) | The Reopen method reopens a remote I/O target after it has been temporarily closed. |
| [IPowerPolicyCallbackWakeFromSx::OnDisarmWakeFromSx method](nf-wudfddi-ipowerpolicycallbackwakefromsx-ondisarmwakefromsx.md) | A driver's OnDisarmWakeFromSx event callback function disarms (that is, disables) a device's ability to trigger a wake signal while the device and system are in low-power states. |
| [IWDFRemoteTarget::CloseForQueryRemove method](nf-wudfddi-iwdfremotetarget-closeforqueryremove.md) | The CloseForQueryRemove method closes a remote I/O target because the operating system might allow the device to be removed. |
| [IPowerPolicyCallbackWakeFromS0::OnArmWakeFromS0 method](nf-wudfddi-ipowerpolicycallbackwakefroms0-onarmwakefroms0.md) | A driver's OnArmWakeFromS0 callback function arms (that is, enables) a device so that it can trigger a wake signal while in a low-power device state, if the system remains in the system working state (S0). |
| [IWDFIoRequestCompletionParams::GetReadParameters method](nf-wudfddi-iwdfiorequestcompletionparams-getreadparameters~r1.md) | TBD |
| [IWDFDevice2::GetDeviceStackIoTypePreference method](nf-wudfddi-iwdfdevice2-getdevicestackiotypepreference.md) | The GetDeviceStackIoTypePreference method retrieves the buffer access methods that the framework is using for a device. |
| [IWDFRemoteTarget::Start method](nf-wudfddi-iwdfremotetarget-start~r2.md) | TBD |
| [IWDFIoRequest2::Requeue method](nf-wudfddi-iwdfiorequest2-requeue.md) | The Requeue method returns an I/O request to the head of the I/O queue from which it was delivered to the driver. |
| [IWDFDevice::CreateWdfFile method](nf-wudfddi-iwdfdevice-createwdffile.md) | The CreateWdfFile method creates a file object for a driver to use. |
| [IWDFIoQueue::Stop method](nf-wudfddi-iwdfioqueue-stop.md) | The Stop method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests. |
| [IWDFIoTargetStateManagement::GetState method](nf-wudfddi-iwdfiotargetstatemanagement-getstate.md) | The GetState method returns the current state of a local I/O target. |
| [IWDFDevice::RetrieveDevicePropertyStore method](nf-wudfddi-iwdfdevice-retrievedevicepropertystore~r1.md) | TBD |
| [IWDFRemoteInterfaceInitialize::GetInterfaceGuid method](nf-wudfddi-iwdfremoteinterfaceinitialize-getinterfaceguid.md) | The GetInterfaceGuid method retrieves the GUID that identifies a device interface. |
| [IWDFIoRequest3::SetUserModeDriverInitiatedIo method](nf-wudfddi-iwdfiorequest3-setusermodedriverinitiatedio.md) | The SetUserModeDriverInitiatedIo method indicates to kernel-mode drivers that sit below the UMDF driver in the same device stack that a particular request should be treated as though it came from a UMDF driver. |
| [IWDFIoTarget::GetTargetFile method](nf-wudfddi-iwdfiotarget-gettargetfile.md) | The GetTargetFile method retrieves the framework file object that is associated with the I/O target object. |
| [IQueueCallbackDefaultIoHandler::OnDefaultIoHandler method](nf-wudfddi-iqueuecallbackdefaultiohandler-ondefaultiohandler.md) | The OnDefaultIoHandler method handles I/O requests that no other method is registered to handle. |
| [IWDFMemory::CopyToBuffer method](nf-wudfddi-iwdfmemory-copytobuffer.md) | The CopyToBuffer method safely copies data from a memory object to the specified target buffer. |
| [IWDFDevice::RetrieveDeviceInstanceId method](nf-wudfddi-iwdfdevice-retrievedeviceinstanceid~r1.md) | TBD |
| [IImpersonateCallback::OnImpersonate method](nf-wudfddi-iimpersonatecallback-onimpersonate.md) | The OnImpersonate method handles impersonation. |
| [IPnpCallbackSelfManagedIo::OnSelfManagedIoInit method](nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagedioinit.md) | The OnSelfManagedIoInit method initializes a device's self-managed I/O operations. |
| [IWDFRequestCompletionParams::GetCompletionStatus method](nf-wudfddi-iwdfrequestcompletionparams-getcompletionstatus.md) | The GetCompletionStatus method retrieves the completion status of an I/O request. |
| [IWDFDevice3::WriteToHardware method](nf-wudfddi-iwdfdevice3-writetohardware.md) | TBD |
| [IWDFIoRequest3::GetUserModeDriverInitiatedIo method](nf-wudfddi-iwdfiorequest3-getusermodedriverinitiatedio.md) | The GetUserModeDriverInitiatedIo method determines whether an I/O request is marked as initiated by a UMDF driver. |
| [IWDFDriver::CreateDevice method](nf-wudfddi-iwdfdriver-createdevice.md) | The CreateDevice method configures and creates a new framework device object. |
| [IWDFRemoteTarget::Stop method](nf-wudfddi-iwdfremotetarget-stop.md) | The Stop method temporarily stops a remote I/O target. |
| [IPnpCallbackHardware2::OnPrepareHardware method](nf-wudfddi-ipnpcallbackhardware2-onpreparehardware.md) | The OnPrepareHardware method performs any operations that are needed to make a device accessible to the driver. |
| [IPnpCallback::OnD0Exit method](nf-wudfddi-ipnpcallback-ond0exit.md) | The OnD0Exit method notifies a driver when a device exits the D0 power state so that the driver can perform necessary operations, such as disabling the device. |
| [IWDFRemoteTarget::GetState method](nf-wudfddi-iwdfremotetarget-getstate.md) | The GetState method returns the current state of a remote I/O target. |
| [IWDFIoRequest::Send method](nf-wudfddi-iwdfiorequest-send.md) | The Send method sends a request to the specified I/O target. |
| [IWDFWorkItem::Flush method](nf-wudfddi-iwdfworkitem-flush.md) | The Flush method returns after this interface's work item has been serviced. |
| [IRemoteTargetCallbackRemoval::OnRemoteTargetRemoveComplete method](nf-wudfddi-iremotetargetcallbackremoval-onremotetargetremovecomplete.md) | A UMDF-based driver's OnRemoteTargetRemoveComplete event callback function performs operations that are necessary after the operating system completes the removal of a remote I/O target's device. |
| [IWDFDevice::RetrieveDevicePropertyStore method](nf-wudfddi-iwdfdevice-retrievedevicepropertystore.md) | The RetrieveDevicePropertyStore method retrieves a property store interface that drivers can use to access the registry. |
| [IWDFRemoteTarget::GetState method](nf-wudfddi-iwdfremotetarget-getstate~r2.md) | TBD |
| [IPnpCallbackHardware2::OnReleaseHardware method](nf-wudfddi-ipnpcallbackhardware2-onreleasehardware.md) | The OnReleaseHardware method performs operations that are needed when a device is no longer accessible. |
| [IWDFIoRequest2::GetQueryInformationParameters method](nf-wudfddi-iwdfiorequest2-getqueryinformationparameters.md) | The GetQueryInformationParameters method retrieves parameters that are associated with a WdfRequestQueryInformation-typed I/O request. |
| [IWDFRequestCompletionParams::GetCompletedRequestType method](nf-wudfddi-iwdfrequestcompletionparams-getcompletedrequesttype.md) | The GetCompletedRequestType method retrieves the type of operation that the request to be completed contains. |
| [IWDFIoRequest::GetCompletionParams method](nf-wudfddi-iwdfiorequest-getcompletionparams.md) | The GetCompletionParams method retrieves the parameters object for the completion of an I/O request object. |
| [IQueueCallbackIoStop::OnIoStop method](nf-wudfddi-iqueuecallbackiostop-oniostop.md) | The OnIoStop callback function stops the processing of the specified I/O request from the specified queue. |
| [IPnpCallbackHardware::OnPrepareHardware method](nf-wudfddi-ipnpcallbackhardware-onpreparehardware.md) | The OnPrepareHardware method notifies a driver to make the specified hardware accessible. |
| [IWDFDevice2::ResumeIdle method](nf-wudfddi-iwdfdevice2-resumeidle.md) | The ResumeIdle method informs the framework that the device is not in use and can be placed in a device low-power state if it remains idle. |
| [IWDFIoTarget2::FormatRequestForSetInformation method](nf-wudfddi-iwdfiotarget2-formatrequestforsetinformation.md) | The FormatRequestForSetInformation method formats an I/O request to set information about a file, but it does not send the request to an I/O target. |
| [IWDFDevice::PostEvent method](nf-wudfddi-iwdfdevice-postevent.md) | The PostEvent method asynchronously notifies applications that are waiting for the specified event from a driver. |
| [IWDFDevice3::UnmapIoSpace method](nf-wudfddi-iwdfdevice3-unmapiospace.md) | The UnmapIoSpace method unmaps a specified range of physical addresses previously mapped by MapIoSpace method. |
| [IWDFDevice::GetDriver method](nf-wudfddi-iwdfdevice-getdriver.md) | The GetDriver method retrieves the interface to the parent driver object of a device instance. |
| [IWDFDriverCreatedFile::Close method](nf-wudfddi-iwdfdrivercreatedfile-close.md) | The Close method closes an instance of a UMDF driver-created-file object that was created by calling the IWDFDevice |
| [IQueueCallbackDeviceIoControl::OnDeviceIoControl method](nf-wudfddi-iqueuecallbackdeviceiocontrol-ondeviceiocontrol.md) | The OnDeviceIoControl method is called to handle a device I/O control request when an application performs a specific operation on a device through the Microsoft Win32 OnDeviceIoControl function. |
| [IWDFDevice::AssignDeviceInterfaceState method](nf-wudfddi-iwdfdevice-assigndeviceinterfacestate.md) | The AssignDeviceInterfaceState method enables or disables the specified device interface instance for a device. |
| [IWDFInterrupt::GetDevice method](nf-wudfddi-iwdfinterrupt-getdevice~r2.md) | TBD |
| [IPnpCallback::OnSurpriseRemoval method](nf-wudfddi-ipnpcallback-onsurpriseremoval.md) | The OnSurpriseRemoval method notifies a driver after a device is removed from a computer unexpectedly so that the driver can perform necessary operations. |
| [IWDFRemoteTarget::Stop method](nf-wudfddi-iwdfremotetarget-stop~r2.md) | TBD |
| [IQueueCallbackCreate::OnCreateFile method](nf-wudfddi-iqueuecallbackcreate-oncreatefile.md) | The OnCreateFile method is called to handle an open file request when an application opens a device through the Microsoft Win32 CreateFile function. |
| [IWDFIoRequest::GetDeviceIoControlParameters method](nf-wudfddi-iwdfiorequest-getdeviceiocontrolparameters.md) | The GetDeviceIoControlParameters method retrieves the request parameters for a device I/O control-type request. |
| [IWDFRequestCompletionParams::GetInformation method](nf-wudfddi-iwdfrequestcompletionparams-getinformation.md) | The GetInformation method retrieves information that is associated with the completion of an I/O request. |
| [IWDFIoRequest2::RetrieveOutputBuffer method](nf-wudfddi-iwdfiorequest2-retrieveoutputbuffer.md) | The RequestRetrieveOutputBuffer method retrieves an I/O request's output buffer. |
| [IWDFNamedPropertyStore::GetNamedValue method](nf-wudfddi-iwdfnamedpropertystore-getnamedvalue.md) | The GetNamedValue method retrieves the value of a property. |
| [IWDFIoRequest::GetIoQueue method](nf-wudfddi-iwdfiorequest-getioqueue.md) | The GetIoQueue method retrieves the I/O queue object that is associated with an I/O request. |
| [IWDFIoRequest::GetOutputMemory method](nf-wudfddi-iwdfiorequest-getoutputmemory.md) | The GetOutputMemory method retrieves the memory object that represents the output buffer for an I/O request. |
| [IWDFDevice::SetPnpState method](nf-wudfddi-iwdfdevice-setpnpstate.md) | The SetPnpState method turns on or off (or sets to the default state) the specified Plug and Play (PnP) property of a device. |
| [IDriverEntry::OnDeviceAdd method](nf-wudfddi-idriverentry-ondeviceadd.md) | The OnDeviceAdd method adds a new device to a system. |
| [IWDFIoRequest::SetCompletionCallback method](nf-wudfddi-iwdfiorequest-setcompletioncallback.md) | The SetCompletionCallback method registers the interface for the OnCompletion method that the framework should call when an I/O request completes. |
| [IWDFIoRequest::IsFrom32BitProcess method](nf-wudfddi-iwdfiorequest-isfrom32bitprocess.md) | The IsFrom32BitProcess method determines whether a request originated from a 32-bit process. |
| [IWDFIoRequest::FormatUsingCurrentType method](nf-wudfddi-iwdfiorequest-formatusingcurrenttype.md) | The FormatUsingCurrentType method formats an I/O request so that the driver can forward it, unmodified, to the next-lower driver. |
| [IWDFRemoteTarget::Close method](nf-wudfddi-iwdfremotetarget-close~r1.md) | TBD |
| [IWDFPropertyStoreFactory::RetrieveDevicePropertyStore method](nf-wudfddi-iwdfpropertystorefactory-retrievedevicepropertystore.md) | The RetrieveDevicePropertyStore method retrieves a property store interface that drivers can use to access the registry. |
| [IWDFDevice2::CreateRemoteTarget method](nf-wudfddi-iwdfdevice2-createremotetarget.md) | The CreateRemoteTarget method creates a remote target object that represents a remote I/O target. |
| [IWDFInterrupt::QueueWorkItemForIsr method](nf-wudfddi-iwdfinterrupt-queueworkitemforisr.md) | The QueueWorkItemForIsr method queues a work item to process interrupt-related work outside of the interrupt service routine. |
| [IWDFDevice2::CreateRemoteInterface method](nf-wudfddi-iwdfdevice2-createremoteinterface.md) | The CreateRemoteInterface method creates a remote interface object that represents a device interface. |
| [IPnpCallbackHardware2::OnReleaseHardware method](nf-wudfddi-ipnpcallbackhardware2-onreleasehardware~r1.md) | TBD |
| [IFileCallbackCleanup::OnCleanupFile method](nf-wudfddi-ifilecallbackcleanup-oncleanupfile.md) | The OnCleanupFile method cancels all I/O requests that a driver has pending in the framework queue. |
| [IWDFCmResourceList::GetCount method](nf-wudfddi-iwdfcmresourcelist-getcount.md) | The GetCount method returns the number of resource descriptors that are contained in this interface's resource list. |
| [IPowerPolicyCallbackWakeFromSx::OnWakeFromSxTriggered method](nf-wudfddi-ipowerpolicycallbackwakefromsx-onwakefromsxtriggered.md) | A driver's OnWakeFromSxTriggered event callback function informs the driver that its device, which had previously entered a low-power device state because system power was reduced, might have triggered a wake signal. |
| [IWDFDeviceInitialize::RetrieveDeviceInstanceId method](nf-wudfddi-iwdfdeviceinitialize-retrievedeviceinstanceid.md) | The RetrieveDeviceInstanceId method retrieves the identifier of an instance of a device. |
| [IWDFDevice::RetrieveDeviceInstanceId method](nf-wudfddi-iwdfdevice-retrievedeviceinstanceid.md) | The RetrieveDeviceInstanceId method retrieves the identifier of an instance of a device. |
| [IWDFIoRequest2::RetrieveInputBuffer method](nf-wudfddi-iwdfiorequest2-retrieveinputbuffer.md) | The RequestRetrieveInputBuffer method retrieves an I/O request's input buffer. |
| [IWDFRemoteTarget::OpenRemoteInterface method](nf-wudfddi-iwdfremotetarget-openremoteinterface.md) | The OpenRemoteInterface method opens a device interface so that the driver can send I/O requests to it. |
| [IWDFIoQueue::Drain method](nf-wudfddi-iwdfioqueue-drain.md) | The Drain method directs the queue to reject new incoming I/O requests and allow already-queued requests to be delivered to the driver for processing. |
| [IWDFIoTarget::FormatRequestForRead method](nf-wudfddi-iwdfiotarget-formatrequestforread.md) | The FormatRequestForRead method formats an I/O request object for a read operation. |
| [IPnpCallbackSelfManagedIo::OnSelfManagedIoFlush method](nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagedioflush.md) | The OnSelfManagedIoFlush method flushes the device for a device's self-managed I/O operations. |
| [IWDFIoRequest::GetType method](nf-wudfddi-iwdfiorequest-gettype.md) | The GetType method retrieves the type of operation that a request contains. |
| [IWDFWorkItem::Enqueue method](nf-wudfddi-iwdfworkitem-enqueue.md) | The Enqueue method adds this interface's framework work-item object to the system's work-item queue. |
| [IWDFFile2::RetrieveCountedFileName method](nf-wudfddi-iwdffile2-retrievecountedfilename.md) | The RetrieveCountedFileName method retrieves the full counted file name for a file that is associated with a device. |
| [IWDFDevice2::StopIdle method](nf-wudfddi-iwdfdevice2-stopidle.md) | The StopIdle method informs the framework that the device must be placed in its working (D0) power state. |
| [IWDFDevice::CommitPnpState method](nf-wudfddi-iwdfdevice-commitpnpstate.md) | The CommitPnpState method commits the state of the Plug and Play (PnP) property (that is, turns on, turns off, or sets to the default state) that the IWDFDevice |
| [IWDFIoRequest::MarkCancelable method](nf-wudfddi-iwdfiorequest-markcancelable.md) | The MarkCancelable method enables the canceling of the I/O request. |
| [IWDFInterrupt::TryToAcquireInterruptLock method](nf-wudfddi-iwdfinterrupt-trytoacquireinterruptlock.md) | The TryToAcquireInterruptLock method acquires the interrupt lock if no other thread has already acquired it. |
| [IWDFIoRequest::SetInformation method](nf-wudfddi-iwdfiorequest-setinformation.md) | The SetInformation method sets the size of information for a request. |
| [IWDFInterrupt::SetPolicy method](nf-wudfddi-iwdfinterrupt-setpolicy.md) | The SetPolicy method specifies the interrupt priority, processor affinity, and affinity policy for a specified interrupt. |
| [IWDFDeviceInitialize::SetFilter method](nf-wudfddi-iwdfdeviceinitialize-setfilter.md) | The SetFilter method sets the property that enables a device as a filter device. |
| [IWDFDeviceInitialize::AutoForwardCreateCleanupClose method](nf-wudfddi-iwdfdeviceinitialize-autoforwardcreatecleanupclose.md) | The AutoForwardCreateCleanupClose method controls when create, cleanup, and close notifications are forwarded to the next lower driver in the device stack. |
| [IWDFIoTargetStateManagement::Stop method](nf-wudfddi-iwdfiotargetstatemanagement-stop~r1.md) | TBD |
| [IWDFInterrupt::GetInfo method](nf-wudfddi-iwdfinterrupt-getinfo.md) | The GetInfo method retrieves information about a specified interrupt. |
| [IWDFDevice2::AssignS0IdleSettings method](nf-wudfddi-iwdfdevice2-assigns0idlesettings.md) | The AssignS0IdleSettings method provides driver-supplied information that the framework uses when a device is idle and the system is in its working (S0) state. |
| [IQueueCallbackStateChange::OnStateChange method](nf-wudfddi-iqueuecallbackstatechange-onstatechange.md) | The OnStateChange method is called when the state of the I/O queue object changes. |
| [IQueueCallbackRead::OnRead method](nf-wudfddi-iqueuecallbackread-onread.md) | The OnRead method is called to handle a read request when an application reads information from a device through the Microsoft Win32 ReadFile or ReadFileEx function. |
| [IWDFIoTargetStateManagement::GetState method](nf-wudfddi-iwdfiotargetstatemanagement-getstate~r1.md) | TBD |
| [IWDFUnifiedPropertyStore::GetPropertyData method](nf-wudfddi-iwdfunifiedpropertystore-getpropertydata.md) | The GetPropertyData method retrieves the current setting for a device property. |
| [IWDFIoRequest::GetReadParameters method](nf-wudfddi-iwdfiorequest-getreadparameters.md) | The GetReadParameters method retrieves the request parameters for a read-type request. |
| [IWDFDevice::GetDefaultIoQueue method](nf-wudfddi-iwdfdevice-getdefaultioqueue.md) | The GetDefaultIoQueue method retrieves the interface of the default I/O queue for a device. |
| [IPnpCallbackHardware2::OnPrepareHardware method](nf-wudfddi-ipnpcallbackhardware2-onpreparehardware~r1.md) | TBD |
| [IWDFIoRequestCompletionParams::GetReadParameters method](nf-wudfddi-iwdfiorequestcompletionparams-getreadparameters.md) | The GetReadParameters method retrieves parameters that are associated with the completion of a read request. |
| [IWDFObject::RetrieveContext method](nf-wudfddi-iwdfobject-retrievecontext.md) | The RetrieveContext method retrieves a context that was previously registered through the IWDFObject |
| [IWDFDevice3::ReadFromHardware method](nf-wudfddi-iwdfdevice3-readfromhardware.md) | TBD |
| [IWDFIoRequest2::GetEffectiveIoType method](nf-wudfddi-iwdfiorequest2-geteffectiveiotype.md) | The GetEffectiveIoType method returns the buffer access method that UMDF is using for the data buffers of the I/O request that the IWDFIoRequest2 interface represents. |
| [IWDFDeviceInitialize::SetLockingConstraint method](nf-wudfddi-iwdfdeviceinitialize-setlockingconstraint.md) | The SetLockingConstraint method sets the synchronization (or locking) model for callback functions into the driver. |
| [IWDFIoRequest2::StopAcknowledge method](nf-wudfddi-iwdfiorequest2-stopacknowledge.md) | The StopAcknowledge method informs the framework that the driver has stopped processing a specified I/O request. |
| [IDriverEntry::OnDeinitialize method](nf-wudfddi-idriverentry-ondeinitialize.md) | The OnDeinitialize method performs any operations that are necessary before a system unloads a driver. |
| [IWDFIoRequest2::GetRequestorMode method](nf-wudfddi-iwdfiorequest2-getrequestormode.md) | The GetRequestorMode method indicates whether an I/O request came from a kernel-mode driver or a user-mode component (either an application or a user-mode driver). |
| [IWDFFile::RetrieveFileName method](nf-wudfddi-iwdffile-retrievefilename.md) | The RetrieveFileName method retrieves the full name of the file that is associated with the underlying kernel-mode device. |
| [IWDFIoRequest2::Reuse method](nf-wudfddi-iwdfiorequest2-reuse.md) | The Reuse method reinitializes a framework request object so that it can be reused. |
| [IWDFIoTargetStateManagement::Stop method](nf-wudfddi-iwdfiotargetstatemanagement-stop.md) | The Stop method stops sending queued requests to a local I/O target. |
| [IRemoteTargetCallbackRemoval::OnRemoteTargetRemoveCanceled method](nf-wudfddi-iremotetargetcallbackremoval-onremotetargetremovecanceled.md) | A UMDF-based driver's OnRemoteTargetRemoveCanceled event callback function performs operations that are necessary when the operating system cancels the removal of a remote I/O target's device. |
| [IWDFNamedPropertyStore2::DeleteNamedValue method](nf-wudfddi-iwdfnamedpropertystore2-deletenamedvalue.md) | The DeleteNamedValue method deletes a value name from the registry. |
| [IWDFPropertyStoreFactory::RetrieveDevicePropertyStore method](nf-wudfddi-iwdfpropertystorefactory-retrievedevicepropertystore~r2.md) | TBD |
| [IWDFIoRequest2::RetrieveOutputMemory method](nf-wudfddi-iwdfiorequest2-retrieveoutputmemory.md) | The RetrieveOutputMemory method retrieves the IWDFMemory interface of a framework memory object that represents an I/O request's output buffer. |
| [IPnpCallbackRemoteInterfaceNotification::OnRemoteInterfaceArrival method](nf-wudfddi-ipnpcallbackremoteinterfacenotification-onremoteinterfacearrival.md) | A driver's OnRemoteInterfaceArrival event callback function informs the driver when a device interface is available. |
| [IWDFDevice::RetrieveDeviceName method](nf-wudfddi-iwdfdevice-retrievedevicename.md) | The RetrieveDeviceName method retrieves the name of an underlying kernel-mode device. |
| [IWDFDeviceInitialize::GetPnpCapability method](nf-wudfddi-iwdfdeviceinitialize-getpnpcapability.md) | The GetPnpCapability method determines the state of the specified Plug and Play (PnP) capability. |
| [IPnpCallback::OnQueryStop method](nf-wudfddi-ipnpcallback-onquerystop.md) | The OnQueryStop method notifies a driver before a device is stopped. |
| [IWDFNamedPropertyStore::GetNameAt method](nf-wudfddi-iwdfnamedpropertystore-getnameat.md) | The GetNameAt method retrieves the name of a property. |
| [IWDFDeviceInitialize::RetrieveDevicePropertyStore method](nf-wudfddi-iwdfdeviceinitialize-retrievedevicepropertystore.md) | The RetrieveDevicePropertyStore method retrieves a device property store that clients can read and write device properties through. |
| [IQueueCallbackIoCanceledOnQueue::OnIoCanceledOnQueue method](nf-wudfddi-iqueuecallbackiocanceledonqueue-oniocanceledonqueue.md) | A driver's OnIoCanceledOnQueue event callback function informs the driver that an I/O request was canceled while it was in an I/O queue. |
| [IWDFCmResourceList::GetDescriptor method](nf-wudfddi-iwdfcmresourcelist-getdescriptor.md) | The GetDescriptor method returns a pointer to a resource descriptor that is contained in this interface's resource list. |
| [IWDFDriver::CreateWdfMemory method](nf-wudfddi-iwdfdriver-createwdfmemory.md) | The CreateWdfMemory method creates a framework memory object and allocates, for the memory object, a data buffer of the specified nonzero size. |
| [IPnpCallbackSelfManagedIo::OnSelfManagedIoSuspend method](nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagediosuspend.md) | The OnSelfManagedIoSuspend method suspends a device's self-managed I/O operations. |
| [IPnpCallbackHardwareInterrupt::OnD0EntryPostInterruptsEnabled method](nf-wudfddi-ipnpcallbackhardwareinterrupt-ond0entrypostinterruptsenabled.md) | A driver's OnD0EntryPostInterruptsEnabled event callback function performs device-specific operations that are required when the driver enables the device's hardware interrupts. |
| [IWDFIoRequest2::GetSetInformationParameters method](nf-wudfddi-iwdfiorequest2-getsetinformationparameters.md) | The GetSetInformationParameters method retrieves parameters that are associated with a WdfRequestSetInformation-typed I/O request. |
| [IWDFIoRequest::Complete method](nf-wudfddi-iwdfiorequest-complete.md) | The Complete method completes an I/O request. |
| [IWDFIoTargetStateManagement::Remove method](nf-wudfddi-iwdfiotargetstatemanagement-remove.md) | The Remove method removes a local I/O target. |
| [IWDFDevice::GetPnpState method](nf-wudfddi-iwdfdevice-getpnpstate.md) | The GetPnpState method determines whether the given Plug and Play (PnP) property of a device is on or off (or set to the default state). |
| [IPnpCallbackSelfManagedIo::OnSelfManagedIoCleanup method](nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagediocleanup.md) | The OnSelfManagedIoCleanup method releases memory for a device's self-managed I/O operations, after the device is removed. |
| [IWDFDriver::CreatePreallocatedWdfMemory method](nf-wudfddi-iwdfdriver-createpreallocatedwdfmemory.md) | The CreatePreallocatedWdfMemory method creates a framework memory object for the specified buffer. |
| [IWDFInterrupt::ReleaseInterruptLock method](nf-wudfddi-iwdfinterrupt-releaseinterruptlock.md) | The ReleaseInterruptLock method ends a code sequence that executes while holding an interrupt object's lock. |
| [IWDFIoTarget::CancelSentRequestsForFile method](nf-wudfddi-iwdfiotarget-cancelsentrequestsforfile.md) | The CancelSentRequestsForFile method cancels all I/O requests that have been sent on behalf of the specified file object. |
| [IWDFIoRequest3::SetActivityId method](nf-wudfddi-iwdfiorequest3-setactivityid.md) | The SetActivityId method associates an activity identifier with an I/O request. |
| [IWDFDeviceInitialize::SetPnpCapability method](nf-wudfddi-iwdfdeviceinitialize-setpnpcapability.md) | The SetPnpCapability method sets the specified Plug and Play (PnP) capability of a device to the specified state. |
| [IWDFIoRequest::Impersonate method](nf-wudfddi-iwdfiorequest-impersonate.md) | The Impersonate method registers the interface for the method that the framework should call for impersonation. |
| [IWDFDevice3::AssignS0IdleSettingsEx method](nf-wudfddi-iwdfdevice3-assigns0idlesettingsex.md) | The AssignS0IdleSettingsEx method provides driver-supplied information that the framework uses when a device is idle and the system is in its working (S0) state. |
| [IPnpCallback::OnD0Entry method](nf-wudfddi-ipnpcallback-ond0entry.md) | The OnD0Entry method notifies a driver when a device enters the D0 power state so that the driver can perform necessary operations, such as enabling the device. |
| [IPowerPolicyCallbackWakeFromS0::OnWakeFromS0Triggered method](nf-wudfddi-ipowerpolicycallbackwakefroms0-onwakefroms0triggered.md) | A driver's OnWakeFromS0Triggered event callback function informs the driver that its device, which had previously entered a low-power device state while the system power state remained at S0, might have triggered a wake signal. |
| [IWDFNamedPropertyStore::SetNamedValue method](nf-wudfddi-iwdfnamedpropertystore-setnamedvalue.md) | The SetNamedValue method sets the value of a property. |
| [IWDFMemory::GetDataBuffer method](nf-wudfddi-iwdfmemory-getdatabuffer.md) | The GetDataBuffer method retrieves the data buffer that is associated with a memory object. |
| [IWDFDriver::CreateWdfObject method](nf-wudfddi-iwdfdriver-createwdfobject.md) | The CreateWdfObject method creates a custom (or user) WDF object from a parent WDF object. |
| [IWDFFileHandleTargetFactory::CreateFileHandleTarget method](nf-wudfddi-iwdffilehandletargetfactory-createfilehandletarget.md) | The CreateFileHandleTarget method creates a file-handle-based I/O target object. |
| [IWDFUnifiedPropertyStoreFactory::RetrieveUnifiedDevicePropertyStore method](nf-wudfddi-iwdfunifiedpropertystorefactory-retrieveunifieddevicepropertystore.md) | The RetrieveUnifiedDevicePropertyStore method retrieves a unified property store interface. |
| [IQueueCallbackIoResume::OnIoResume method](nf-wudfddi-iqueuecallbackioresume-onioresume.md) | The OnIoResume method resumes the processing of the specified I/O request from the specified queue. |
| [IWDFRemoteTarget::Start method](nf-wudfddi-iwdfremotetarget-start.md) | The IWDFRemoteTarget |
| [IRequestCallbackRequestCompletion::OnCompletion method](nf-wudfddi-irequestcallbackrequestcompletion-oncompletion.md) | The OnCompletion method completes the specified request. |
| [IWDFRemoteTarget::Close method](nf-wudfddi-iwdfremotetarget-close.md) | The Close method closes a remote I/O target. |
| [IWDFIoQueue::DrainSynchronously method](nf-wudfddi-iwdfioqueue-drainsynchronously.md) | The DrainSynchronously method directs the queue to reject new incoming I/O requests and allows already-queued requests to be delivered to the driver for processing. This method returns after all requests are completed or canceled. |
| [IWDFObject::DeleteWdfObject method](nf-wudfddi-iwdfobject-deletewdfobject.md) | The DeleteWdfObject method deletes a previously created Microsoft Windows Driver Frameworks (WDF) object. |
| [IWDFFile::GetDevice method](nf-wudfddi-iwdffile-getdevice.md) | The GetDevice method returns the interface to the device object that a file object is associated with. |
| [IObjectCleanup::OnCleanup method](nf-wudfddi-iobjectcleanup-oncleanup.md) | The OnCleanup method releases any references to a WDF object to prevent interface leakage. |
| [IWDFIoRequest::UnmarkCancelable method](nf-wudfddi-iwdfiorequest-unmarkcancelable.md) | The UnmarkCancelable method disables the canceling of an I/O request. |
| [IWDFObject::AssignContext method](nf-wudfddi-iwdfobject-assigncontext.md) | The AssignContext method registers a context and a driver-supplied cleanup callback function for the object. |
| [IRequestCallbackCancel::OnCancel method](nf-wudfddi-irequestcallbackcancel-oncancel.md) | The OnCancel method is called when an application cancels an I/O operation through the Microsoft Win32 CancelIo, CancelIoEx, or CancelSynchronousIo function. |
| [IWDFInterrupt::Enable method](nf-wudfddi-iwdfinterrupt-enable.md) | The Enable method enables a specified device interrupt by calling the driver's OnInterruptEnable callback function. |
| [IPowerPolicyCallbackWakeFromSx::OnArmWakeFromSx method](nf-wudfddi-ipowerpolicycallbackwakefromsx-onarmwakefromsx.md) | A driver's OnArmWakeFromSx event callback function arms (that is, enables) a device so that it can trigger a wake signal while in a low-power device state. |
| [IWDFFile::GetDevice method](nf-wudfddi-iwdffile-getdevice~r1.md) | TBD |
| [IRemoteInterfaceCallbackEvent::OnRemoteInterfaceEvent method](nf-wudfddi-iremoteinterfacecallbackevent-onremoteinterfaceevent.md) | A UMDF-based driver's OnRemoteInterfaceEvent event callback function handles device events that are associated with a device interface. |
| [IWDFIoTarget2::FormatRequestForFlush method](nf-wudfddi-iwdfiotarget2-formatrequestforflush.md) | The FormatRequestForFlush method builds an I/O request for a flush operation but does not send the request to an I/O target. |
| [IWDFIoRequest::ForwardToIoQueue method](nf-wudfddi-iwdfiorequest-forwardtoioqueue.md) | The ForwardToIoQueue method forwards (that is, requeues) an I/O request to one of the calling driver's I/O queues. |
| [IWDFIoRequestCompletionParams::GetIoctlParameters method](nf-wudfddi-iwdfiorequestcompletionparams-getioctlparameters.md) | The GetIoctlParameters method retrieves parameters that are associated with the completion of a device I/O control request. |
| [IWDFDevice2::CreateSymbolicLinkWithReferenceString method](nf-wudfddi-iwdfdevice2-createsymboliclinkwithreferencestring.md) | TheCreateSymbolicLinkWithReferenceString method creates a symbolic link name, and optionally, a reference string, for a device. |
| [IWDFMemory::CopyFromMemory method](nf-wudfddi-iwdfmemory-copyfrommemory.md) | The CopyFromMemory method safely copies data from the specified source buffer and prevents overruns that the copy operation might otherwise cause. |
| [IWDFInterrupt::AcquireInterruptLock method](nf-wudfddi-iwdfinterrupt-acquireinterruptlock.md) | The AcquireInterruptLock method begins a code sequence that executes while holding an interrupt object's lock. |
| [IWDFInterrupt::GetDevice method](nf-wudfddi-iwdfinterrupt-getdevice.md) | The GetDevice method returns the framework device object interface for this interrupt object. |
| [IWDFIoRequest2::RetrieveInputMemory method](nf-wudfddi-iwdfiorequest2-retrieveinputmemory.md) | The RetrieveInputMemory method retrieves the IWDFMemory interface of a framework memory object that represents an I/O request's input buffer. |
| [IWDFDevice::CreateDeviceInterface method](nf-wudfddi-iwdfdevice-createdeviceinterface.md) | The CreateDeviceInterface method creates an instance of a device interface class. |
| [IWDFIoRequest2::IsFromUserModeDriver method](nf-wudfddi-iwdfiorequest2-isfromusermodedriver.md) | The IsFromUserModeDriver method indicates whether an I/O request came from a user-mode driver or an application. |
| [IWDFDevice2::RegisterRemoteInterfaceNotification method](nf-wudfddi-iwdfdevice2-registerremoteinterfacenotification.md) | The RegisterRemoteInterfaceNotification method registers a driver to receive a notification when a specified device interface becomes available. |
| [IWDFMemory::GetSize method](nf-wudfddi-iwdfmemory-getsize.md) | The GetSize method retrieves the size of the data buffer that is associated with a memory object. |
| [IWDFIoTarget::FormatRequestForIoctl method](nf-wudfddi-iwdfiotarget-formatrequestforioctl.md) | The FormatRequestForIoctl method formats an I/O request object for an I/O control operation. |
| [IWDFIoRequest3::RetrieveActivityId method](nf-wudfddi-iwdfiorequest3-retrieveactivityid.md) | The RetrieveActivityId method retrieves the current activity identifier associated with an I/O request. |
| [IPnpCallbackSelfManagedIo::OnSelfManagedIoStop method](nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagediostop.md) | The OnSelfManagedIoStop method is not used in the current version of the UMDF. |
| [IQueueCallbackWrite::OnWrite method](nf-wudfddi-iqueuecallbackwrite-onwrite.md) | The OnWrite method is called to handle a write request when an application writes information to a device through the Microsoft Win32 WriteFile or WriteFileEx function. |
| [IWDFIoRequest::CancelSentRequest method](nf-wudfddi-iwdfiorequest-cancelsentrequest.md) | The CancelSentRequest method attempts to cancel the I/O request that the driver previously submitted to an I/O target. |
| [IPnpCallback::OnQueryRemove method](nf-wudfddi-ipnpcallback-onqueryremove.md) | The OnQueryRemove method notifies a driver before a device is removed from a computer. |
| [IWDFIoRequest::GetWriteParameters method](nf-wudfddi-iwdfiorequest-getwriteparameters.md) | The GetWriteParameters method retrieves the request parameters for a write-type request. |
| [IWDFIoQueue::RetrieveNextRequestByFileObject method](nf-wudfddi-iwdfioqueue-retrievenextrequestbyfileobject.md) | The RetrieveNextRequestByFileObject method retrieves from an I/O queue the next I/O request whose file object matches the specified file object. |
| [IWDFIoRequestCompletionParams::GetWriteParameters method](nf-wudfddi-iwdfiorequestcompletionparams-getwriteparameters~r1.md) | TBD |
| [IWDFDevice::CreateRequest method](nf-wudfddi-iwdfdevice-createrequest.md) | The CreateRequest method creates an unformatted request object. |
| [IWDFIoTargetStateManagement::Start method](nf-wudfddi-iwdfiotargetstatemanagement-start.md) | The Start method starts sending queued requests to a local I/O target. |
| [IWDFIoRequest2::GetCreateParametersEx method](nf-wudfddi-iwdfiorequest2-getcreateparametersex.md) | The GetCreateParametersEx method retrieves file creation parameters that are associated with a file that is being created or opened. |
| [IWDFIoQueue::StopSynchronously method](nf-wudfddi-iwdfioqueue-stopsynchronously.md) | The StopSynchronously method prevents an I/O queue from delivering I/O requests, but the queue receives and stores new requests. The method returns after all delivered requests have been canceled or completed. |
| [IWDFIoRequestCompletionParams::GetWriteParameters method](nf-wudfddi-iwdfiorequestcompletionparams-getwriteparameters.md) | The GetWriteParameters method retrieves parameters that are associated with the completion of a write request. |
| [IWDFIoTargetStateManagement::Start method](nf-wudfddi-iwdfiotargetstatemanagement-start~r1.md) | TBD |
| [IWDFInterrupt::SetExtendedPolicy method](nf-wudfddi-iwdfinterrupt-setextendedpolicy.md) | The SetExtendedPolicy method specifies the interrupt priority, processor affinity, affinity policy, and processor group for a specified interrupt. |
| [IWDFDevice3::CreateInterrupt method](nf-wudfddi-iwdfdevice3-createinterrupt.md) | The CreateInterrupt method creates a framework interrupt object. |
| [IWDFIoQueue::GetState method](nf-wudfddi-iwdfioqueue-getstate.md) | The GetState method retrieves the state of an I/O queue. |
| [IWDFMemory::SetBuffer method](nf-wudfddi-iwdfmemory-setbuffer.md) | The SetBuffer method assigns a specified buffer to a memory object that a driver created by calling IWDFDriver |
| [IWDFIoQueue::PurgeSynchronously method](nf-wudfddi-iwdfioqueue-purgesynchronously.md) | The PurgeSynchronously method directs the framework to reject new incoming I/O requests and to cancel all outstanding requests. The method returns after all outstanding requests are canceled. |
| [IWDFIoRequest2::IsCanceled method](nf-wudfddi-iwdfiorequest2-iscanceled.md) | The IsCanceled method determines whether the I/O manager has attempted to cancel an I/O request. |
| [IWDFWorkItem::GetParentObject method](nf-wudfddi-iwdfworkitem-getparentobject.md) | The GetParentObject method returns the parent framework object of this interface's work item. |
| [IWDFMemory::CopyFromBuffer method](nf-wudfddi-iwdfmemory-copyfrombuffer.md) | The CopyFromBuffer method safely copies data from the specified source buffer to a memory object. |
| [IWDFIoQueue::ConfigureRequestDispatching method](nf-wudfddi-iwdfioqueue-configurerequestdispatching.md) | The ConfigureRequestDispatching method configures the queuing of I/O requests of the given type. |
| [IWDFIoRequest2::GetStatus method](nf-wudfddi-iwdfiorequest2-getstatus.md) | The GetStatus method returns the status of an I/O request. |
| [IPnpCallbackSelfManagedIo::OnSelfManagedIoRestart method](nf-wudfddi-ipnpcallbackselfmanagedio-onselfmanagediorestart.md) | The OnSelfManagedIoRestart method restarts a device's self-managed I/O operations. |
| [IWDFInterrupt::Disable method](nf-wudfddi-iwdfinterrupt-disable.md) | The Disable method disables a specified device interrupt by calling the driver's OnInterruptDisable callback function. |
| [IWDFFile3::GetInitiatorProcessId method](nf-wudfddi-iwdffile3-getinitiatorprocessid.md) | The GetInitiatorProcessId method retrieves the initiator process ID associated with an IWDFFile interface. |
| [IFileCallbackClose::OnCloseFile method](nf-wudfddi-ifilecallbackclose-onclosefile.md) | The OnCloseFile method is called when the last reference count on a file object goes down to zero and before the file object is released. |
| [IWDFNamedPropertyStore::GetNameCount method](nf-wudfddi-iwdfnamedpropertystore-getnamecount.md) | The GetNameCount method retrieves the number of properties in a property store. |
| [IWDFUnifiedPropertyStore::SetPropertyData method](nf-wudfddi-iwdfunifiedpropertystore-setpropertydata.md) | The SetPropertyData method modifies the current setting of a device property. |
| [IPnpCallbackHardwareInterrupt::OnD0ExitPreInterruptsDisabled method](nf-wudfddi-ipnpcallbackhardwareinterrupt-ond0exitpreinterruptsdisabled.md) | A driver's OnD0ExitPreInterruptsDisabled event callback function performs device-specific operations that are required before the driver disables the device's hardware interrupts. |
| [IWDFDriver::RetrieveVersionString method](nf-wudfddi-iwdfdriver-retrieveversionstring.md) | The RetrieveVersionString method retrieves the version of the framework. |
| [IWDFDevice::ConfigureRequestDispatching method](nf-wudfddi-iwdfdevice-configurerequestdispatching.md) | The ConfigureRequestDispatching method configures the queuing of I/O requests of the specified type to the specified I/O queue. |
| [IWDFIoTarget2::FormatRequestForQueryInformation method](nf-wudfddi-iwdfiotarget2-formatrequestforqueryinformation.md) | The FormatRequestForQueryInformation method formats an I/O request to obtain information about a file, but it does not send the request to an I/O target. |
| [IWDFObject::ReleaseLock method](nf-wudfddi-iwdfobject-releaselock.md) | The ReleaseLock method allows the framework to call methods of interfaces that are registered by the driver that the framework previously prevented from calling because the driver called the IWDFObject |
| [IWDFIoRequest::GetRequestorProcessId method](nf-wudfddi-iwdfiorequest-getrequestorprocessid.md) | The GetRequestorProcessId method retrieves the identifier of the process that sent an I/O request. |
| [IWDFDevice::CreateSymbolicLink method](nf-wudfddi-iwdfdevice-createsymboliclink.md) | The CreateSymbolicLink method creates a symbolic link for the device. |
| [IRemoteTargetCallbackRemoval::OnRemoteTargetQueryRemove method](nf-wudfddi-iremotetargetcallbackremoval-onremotetargetqueryremove.md) | A UMDF-based driver's OnRemoteTargetQueryRemove event callback function determines whether a remote I/O target's device can be stopped and removed. |
| [IPnpCallbackHardware::OnReleaseHardware method](nf-wudfddi-ipnpcallbackhardware-onreleasehardware.md) | The OnReleaseHardware method notifies a driver to perform operations that are necessary when the specified hardware is no longer accessible. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [IWDFFile3Vtbl structure](ns-wudfddi-iwdffile3vtbl.md) | TBD |
| [IWDFNamedPropertyStore2Vtbl structure](ns-wudfddi-iwdfnamedpropertystore2vtbl.md) | TBD |
| [IWDFObjectVtbl structure](ns-wudfddi-iwdfobjectvtbl.md) | TBD |
| [IWDFUnifiedPropertyStoreFactoryVtbl structure](ns-wudfddi-iwdfunifiedpropertystorefactoryvtbl.md) | TBD |
| [IWDFDevice2Vtbl structure](ns-wudfddi-iwdfdevice2vtbl.md) | TBD |
| [IRequestCallbackCancelVtbl structure](ns-wudfddi-irequestcallbackcancelvtbl.md) | TBD |
| [IWDFMemoryVtbl structure](ns-wudfddi-iwdfmemoryvtbl.md) | TBD |
| [IPnpCallbackHardwareInterruptVtbl structure](ns-wudfddi-ipnpcallbackhardwareinterruptvtbl.md) | TBD |
| [IWDFIoRequest2Vtbl structure](ns-wudfddi-iwdfiorequest2vtbl.md) | TBD |
| [IWDFDevice3Vtbl structure](ns-wudfddi-iwdfdevice3vtbl.md) | TBD |
| [IWDFIoQueueVtbl structure](ns-wudfddi-iwdfioqueuevtbl.md) | TBD |
| [IDriverEntryVtbl structure](ns-wudfddi-idriverentryvtbl.md) | TBD |
| [IPnpCallbackHardware2Vtbl structure](ns-wudfddi-ipnpcallbackhardware2vtbl.md) | TBD |
| [IPnpCallbackVtbl structure](ns-wudfddi-ipnpcallbackvtbl.md) | TBD |
| [IPowerPolicyCallbackWakeFromS0Vtbl structure](ns-wudfddi-ipowerpolicycallbackwakefroms0vtbl.md) | TBD |
| [IWDFUnifiedPropertyStoreVtbl structure](ns-wudfddi-iwdfunifiedpropertystorevtbl.md) | TBD |
| [IWDFIoTargetVtbl structure](ns-wudfddi-iwdfiotargetvtbl.md) | TBD |
| [IImpersonateCallbackVtbl structure](ns-wudfddi-iimpersonatecallbackvtbl.md) | TBD |
| [IObjectCleanupVtbl structure](ns-wudfddi-iobjectcleanupvtbl.md) | TBD |
| [IQueueCallbackDefaultIoHandlerVtbl structure](ns-wudfddi-iqueuecallbackdefaultiohandlervtbl.md) | TBD |
| [IRemoteInterfaceCallbackRemovalVtbl structure](ns-wudfddi-iremoteinterfacecallbackremovalvtbl.md) | TBD |
| [IPowerPolicyCallbackWakeFromSxVtbl structure](ns-wudfddi-ipowerpolicycallbackwakefromsxvtbl.md) | TBD |
| [IWDFDeviceInitializeVtbl structure](ns-wudfddi-iwdfdeviceinitializevtbl.md) | TBD |
| [IQueueCallbackIoStopVtbl structure](ns-wudfddi-iqueuecallbackiostopvtbl.md) | TBD |
| [IWDFFileVtbl structure](ns-wudfddi-iwdffilevtbl.md) | TBD |
| [IQueueCallbackDeviceIoControlVtbl structure](ns-wudfddi-iqueuecallbackdeviceiocontrolvtbl.md) | TBD |
| [UMDF_IO_TARGET_OPEN_PARAMS structure](ns-wudfddi--umdf-io-target-open-params~r1.md) | TBD |
| [IPnpCallbackSelfManagedIoVtbl structure](ns-wudfddi-ipnpcallbackselfmanagediovtbl.md) | TBD |
| [IWDFDriverCreatedFileVtbl structure](ns-wudfddi-iwdfdrivercreatedfilevtbl.md) | TBD |
| [IWDFWorkItemVtbl structure](ns-wudfddi-iwdfworkitemvtbl.md) | TBD |
| [IWDFPropertyStoreFactoryVtbl structure](ns-wudfddi-iwdfpropertystorefactoryvtbl.md) | TBD |
| [IWDFDeviceVtbl structure](ns-wudfddi-iwdfdevicevtbl.md) | TBD |
| [IRequestCallbackRequestCompletionVtbl structure](ns-wudfddi-irequestcallbackrequestcompletionvtbl.md) | TBD |
| [IRemoteTargetCallbackRemovalVtbl structure](ns-wudfddi-iremotetargetcallbackremovalvtbl.md) | TBD |
| [IWDFIoRequest3Vtbl structure](ns-wudfddi-iwdfiorequest3vtbl.md) | TBD |
| [IWDFFileHandleTargetFactoryVtbl structure](ns-wudfddi-iwdffilehandletargetfactoryvtbl.md) | TBD |
| [IWDFInterruptVtbl structure](ns-wudfddi-iwdfinterruptvtbl.md) | TBD |
| [tagPROPVARIANT structure](ns-wudfddi-tagpropvariant.md) | TBD |
| [IWDFRemoteInterfaceInitializeVtbl structure](ns-wudfddi-iwdfremoteinterfaceinitializevtbl.md) | TBD |
| [IWDFRemoteTargetVtbl structure](ns-wudfddi-iwdfremotetargetvtbl.md) | TBD |
| [IWDFRequestCompletionParamsVtbl structure](ns-wudfddi-iwdfrequestcompletionparamsvtbl.md) | TBD |
| [IPnpCallbackRemoteInterfaceNotificationVtbl structure](ns-wudfddi-ipnpcallbackremoteinterfacenotificationvtbl.md) | TBD |
| [IWDFCmResourceListVtbl structure](ns-wudfddi-iwdfcmresourcelistvtbl.md) | TBD |
| [UMDF_IO_TARGET_OPEN_PARAMS structure](ns-wudfddi--umdf-io-target-open-params.md) | The UMDF_IO_TARGET_OPEN_PARAMS structure contains file-open parameters. |
| [IWDFIoTarget2Vtbl structure](ns-wudfddi-iwdfiotarget2vtbl.md) | TBD |
| [IQueueCallbackIoCanceledOnQueueVtbl structure](ns-wudfddi-iqueuecallbackiocanceledonqueuevtbl.md) | TBD |
| [IQueueCallbackIoResumeVtbl structure](ns-wudfddi-iqueuecallbackioresumevtbl.md) | TBD |
| [IWDFDeviceInitialize2Vtbl structure](ns-wudfddi-iwdfdeviceinitialize2vtbl.md) | TBD |
| [WUDFDDI structure](ns-wudfddi-wudfddi.md) | TBD |
| [IWDFDriverVtbl structure](ns-wudfddi-iwdfdrivervtbl.md) | TBD |
| [IWDFRemoteInterfaceVtbl structure](ns-wudfddi-iwdfremoteinterfacevtbl.md) | TBD |
| [IWDFIoRequestCompletionParamsVtbl structure](ns-wudfddi-iwdfiorequestcompletionparamsvtbl.md) | TBD |
| [IFileCallbackCloseVtbl structure](ns-wudfddi-ifilecallbackclosevtbl.md) | TBD |
| [IPnpCallbackHardwareVtbl structure](ns-wudfddi-ipnpcallbackhardwarevtbl.md) | TBD |
| [IFileCallbackCleanupVtbl structure](ns-wudfddi-ifilecallbackcleanupvtbl.md) | TBD |
| [IQueueCallbackReadVtbl structure](ns-wudfddi-iqueuecallbackreadvtbl.md) | TBD |
| [IQueueCallbackWriteVtbl structure](ns-wudfddi-iqueuecallbackwritevtbl.md) | TBD |
| [WUDFDDI structure](ns-wudfddi-wudfddi~r1.md) | TBD |
| [IQueueCallbackCreateVtbl structure](ns-wudfddi-iqueuecallbackcreatevtbl.md) | TBD |
| [IWDFFile2Vtbl structure](ns-wudfddi-iwdffile2vtbl.md) | TBD |
| [IQueueCallbackStateChangeVtbl structure](ns-wudfddi-iqueuecallbackstatechangevtbl.md) | TBD |
| [IRemoteInterfaceCallbackEventVtbl structure](ns-wudfddi-iremoteinterfacecallbackeventvtbl.md) | TBD |
| [IWDFIoTargetStateManagementVtbl structure](ns-wudfddi-iwdfiotargetstatemanagementvtbl.md) | TBD |
| [IWDFIoRequestVtbl structure](ns-wudfddi-iwdfiorequestvtbl.md) | TBD |
| [IWDFNamedPropertyStoreVtbl structure](ns-wudfddi-iwdfnamedpropertystorevtbl.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [SECURITY_IMPERSONATION_LEVEL enumeration](ne-wudfddi--security-impersonation-level.md) | The SECURITY_IMPERSONATION_LEVEL enumeration contains values that identify security impersonation levels. |
| [WDF_INTERRUPT_POLICY enumeration](ne-wudfddi--wdf-interrupt-policy~r1.md) | TBD |
| [WDF_INTERRUPT_POLICY enumeration](ne-wudfddi--wdf-interrupt-policy.md) | TBD |
| [DEVICE_POWER_STATE enumeration](ne-wudfddi--device-power-state~r1.md) | The DEVICE_POWER_STATE enumeration identifies the device power states that a device can enter. |
| [WDF_INTERRUPT_PRIORITY enumeration](ne-wudfddi--wdf-interrupt-priority~r1.md) | TBD |
| [WDF_INTERRUPT_PRIORITY enumeration](ne-wudfddi--wdf-interrupt-priority.md) | TBD |
| [MIDL___MIDL_itf_wudfddi_0000_0000_0001 enumeration](ne-wudfddi---midl---midl-itf-wudfddi-0000-0000-0001.md) | TBD |
| [DEVICE_POWER_STATE enumeration](ne-wudfddi--device-power-state.md) | The DEVICE_POWER_STATE enumeration identifies the device power states that a device can enter. |
| [MIDL___MIDL_itf_wudfddi_0000_0000_0001 enumeration](ne-wudfddi---midl---midl-itf-wudfddi-0000-0000-0001~r1.md) | TBD |

This header is used in these topics:

- [wdf](..content/_wdf)
