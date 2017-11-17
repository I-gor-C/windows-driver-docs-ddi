# Declarations in the usbdlib header
This header Usbdlib contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [UsbBuildVendorRequest function](nf-usbdlib-usbbuildvendorrequest.md) | TBD |
| [GET_USBD_INTERFACE_SIZE function](nf-usbdlib-get-usbd-interface-size.md) | TBD |
| [UsbBuildSelectConfigurationRequest function](nf-usbdlib-usbbuildselectconfigurationrequest.md) | TBD |
| [URB_STATUS function](nf-usbdlib-urb-status.md) | TBD |
| [USBD_CreateHandle function](nf-usbdlib-usbd-createhandle.md) | The USBD_CreateHandle routine is called by a WDM USB client driver to obtain a USBD handle. The routine registers the client driver with the underlying USB driver stack. |
| [USBD_GetPdoRegistryParameter function](nf-usbdlib-usbd-getpdoregistryparameter.md) | The USBD_GetPdoRegistryParameter routine retrieves the value from the specified key in the USB device's hardware registry. |
| [USBD_QueryBusTime function](nf-usbdlib-usbd-querybustime.md) | The USBD_QueryBusTime routine has been deprecated in Windows XP and later operating systems. Do not use. |
| [USBD_ParseConfigurationDescriptor function](nf-usbdlib-usbd-parseconfigurationdescriptor.md) | The USBD_ParseConfigurationDescriptor routine has been deprecated. Use USBD_ParseConfigurationDescriptorEx instead. |
| [COMPOSITE_DEVICE_CAPABILITIES_INIT function](nf-usbdlib-composite-device-capabilities-init.md) | The COMPOSITE_DEVICE_CAPABILITIES_INIT macro initializes the COMPOSITE_DEVICE_CAPABILITIES structure. |
| [UsbBuildGetStatusRequest function](nf-usbdlib-usbbuildgetstatusrequest.md) | The UsbBuildGetStatusRequest macro formats an URB to obtain status from a device, interface, endpoint, or other device-defined target on a USB device. |
| [USBD_CreateConfigurationRequest function](nf-usbdlib-usbd-createconfigurationrequest.md) | The USBD_CreateConfigurationRequest routine has been deprecated. Use USBD_CreateConfigurationRequestEx instead. |
| [UsbBuildSelectInterfaceRequest function](nf-usbdlib-usbbuildselectinterfacerequest.md) | TBD |
| [USBD_CreateConfigurationRequestEx function](nf-usbdlib-usbd-createconfigurationrequestex.md) | The USBD_CreateConfigurationRequestEx routine allocates and formats a URB to select a configuration for a USB device.USBD_CreateConfigurationRequestEx replaces USBD_CreateConfigurationRequest. |
| [USBD_UrbFree function](nf-usbdlib-usbd-urbfree.md) | The USBD_UrbFree routine releases the URB that is allocated by USBD_UrbAllocate, USBD_IsochUrbAllocate, USBD_SelectConfigUrbAllocateAndBuild, or USBD_SelectInterfaceUrbAllocateAndBuild. |
| [USBD_ValidateConfigurationDescriptor function](nf-usbdlib-usbd-validateconfigurationdescriptor.md) | The USBD_ValidateConfigurationDescriptor routine validates all descriptors returned by a device in its response to a configuration descriptor request. |
| [USBD_ParseConfigurationDescriptorEx function](nf-usbdlib-usbd-parseconfigurationdescriptorex.md) | The USBD_ParseConfigurationDescriptorEx routine searches a given configuration descriptor and returns a pointer to an interface that matches the given search criteria. |
| [USBD_CalculateUsbBandwidth function](nf-usbdlib-usbd-calculateusbbandwidth.md) | The USBD_CalculateUsbBandwidth routine has been deprecated in Windows XP and later operating systems. Do not use. |
| [UsbBuildInterruptOrBulkTransferRequest function](nf-usbdlib-usbbuildinterruptorbulktransferrequest.md) | The UsbBuildInterruptOrBulkTransferRequest macro formats an URB to send or receive data on a bulk pipe, or to receive data from an interrupt pipe. |
| [GET_SELECT_INTERFACE_REQUEST_SIZE function](nf-usbdlib-get-select-interface-request-size.md) | TBD |
| [UsbBuildOsFeatureDescriptorRequest function](nf-usbdlib-usbbuildosfeaturedescriptorrequest.md) | TBD |
| [USBD_GetInterfaceLength function](nf-usbdlib-usbd-getinterfacelength.md) | The USBD_GetInterfaceLength routine obtains the length of a given interface descriptor, including the length of all endpoint descriptors contained within the interface. |
| [USBD_SelectConfigUrbAllocateAndBuild function](nf-usbdlib-usbd-selectconfigurballocateandbuild.md) | The USBD_SelectConfigUrbAllocateAndBuild routine allocates and formats a URB structure that is required to select a configuration for a USB device. |
| [GET_ISO_URB_SIZE function](nf-usbdlib-get-iso-urb-size.md) | TBD |
| [USBD_QueryUsbCapability function](nf-usbdlib-usbd-queryusbcapability.md) | TBD |
| [USBD_AssignUrbToIoStackLocation function](nf-usbdlib-usbd-assignurbtoiostacklocation.md) | The USBD_AssignUrbToIoStackLocation routine is called by a client driver to associate an URB with the IRP's next stack location. |
| [USBD_RegisterHcFilter function](nf-usbdlib-usbd-registerhcfilter.md) | The USBD_RegisterHcFilter routine has been deprecated in Windows XP and later operating systems. |
| [USBD_IsochUrbAllocate function](nf-usbdlib-usbd-isochurballocate.md) | The USBD_IsochUrbAllocate routine allocates and formats a URB structure for an isochronous transfer request. |
| [UsbBuildGetDescriptorRequest function](nf-usbdlib-usbbuildgetdescriptorrequest.md) | TBD |
| [USBD_BuildRegisterCompositeDevice function](nf-usbdlib-usbd-buildregistercompositedevice.md) | The USBD_BuildRegisterCompositeDevice routine is called by the driver of a USB multi-function device (composite driver) to initialize a REGISTER_COMPOSITE_DEVICE structure with the information required for registering the driver with the USB driver stack. |
| [UsbBuildFeatureRequest function](nf-usbdlib-usbbuildfeaturerequest.md) | TBD |
| [USBD_SelectInterfaceUrbAllocateAndBuild function](nf-usbdlib-usbd-selectinterfaceurballocateandbuild.md) | The USBD_SelectInterfaceUrbAllocateAndBuild routine allocates and formats a URB structure that is required for a request to select an interface or change its alternate setting. |
| [UsbBuildOpenStaticStreamsRequest function](nf-usbdlib-usbbuildopenstaticstreamsrequest.md) | The UsbBuildOpenStaticStreamsRequest inline function formats an URB structure for an open-streams request. The request opens streams associated with the specified bulk endpoint. |
| [USBD_GetUSBDIVersion function](nf-usbdlib-usbd-getusbdiversion.md) | The USBD_GetUSBDIVersion routine returns version information about the host controller driver (HCD) that controls the client's USB device.Note  USBD_IsInterfaceVersionSupported replaces the USBD_GetUSBDIVersion routine |
| [USBD_IsInterfaceVersionSupported function](nf-usbdlib-usbd-isinterfaceversionsupported.md) | The USBD_IsInterfaceVersionSupported routine is called by a USB client driver to check whether the underlying USB driver stack supports a particular USBD interface version. |
| [GET_SELECT_CONFIGURATION_REQUEST_SIZE function](nf-usbdlib-get-select-configuration-request-size.md) | TBD |
| [USBD_CloseHandle function](nf-usbdlib-usbd-closehandle.md) | The USBD_CloseHandle routine is called by a USB client driver to close a USBD handle and release all resources associated with the driver's registration. |
| [USBD_ParseDescriptors function](nf-usbdlib-usbd-parsedescriptors.md) | The USBD_ParseDescriptors routine searches a given configuration descriptor and returns a pointer to the first descriptor that matches the search criteria. |
| [USBD_UrbAllocate function](nf-usbdlib-usbd-urballocate.md) | The USBD_UrbAllocate routine allocates a USB Request Block (URB). |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [REQUEST_REMOTE_WAKE_NOTIFICATION structure](ns-usbdlib--request-remote-wake-notification.md) | The purpose of the REQUEST_REMOTE_WAKE_NOTIFICATION structure is to specify input parameters for the IOCTL_INTERNAL_USB_REQUEST_REMOTE_WAKE_NOTIFICATION I/O control request. |
| [USBD_INTERFACE_LIST_ENTRY structure](ns-usbdlib--usbd-interface-list-entry.md) | The USBD_INTERFACE_LIST_ENTRY structure is used by USB client drivers to create an array of interfaces to be inserted into a configuration request. |
| [COMPOSITE_DEVICE_CAPABILITIES structure](ns-usbdlib--composite-device-capabilities.md) | TBD |
| [REGISTER_COMPOSITE_DEVICE structure](ns-usbdlib--register-composite-device.md) | The REGISTER_COMPOSITE_DEVICE structure is used with the IOCTL_INTERNAL_USB_REGISTER_COMPOSITE_DEVICE I/O control request to register a parent driver of a Universal Serial Bus (USB) multi-function device (composite driver) with the USB driver stack. |

This header is used in these topics:

- [usbref](..content/_usbref)
