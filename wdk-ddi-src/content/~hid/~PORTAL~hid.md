# Declarations in the hid technology
This technology  contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [HIDP_REPORT_IDS structure](..\hidpddi\ns-hidpddi--hidp-report-ids.md) | Contains report ID information for a top-level collection. |
| [HIDP_COLLECTION_DESC structure](..\hidpddi\ns-hidpddi--hidp-collection-desc.md) | Contains the information of a top-level-collection. This structure is used in the HidP_GetCollectionDescription call. |
| [HIDP_GETCOLDESC_DBG structure](..\hidpddi\ns-hidpddi--hidp-getcoldesc-dbg.md) | Contains the error code indicating the failure in parsing the report descriptor. This structure is used in the HidP_GetCollectionDescription call. |
| [HIDP_DEVICE_DESC structure](..\hidpddi\ns-hidpddi--hidp-device-desc.md) | Contains the device description block filled in collection descriptions as linked lists. This structure is used by HidP_GetCollectionDescription. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [HidP_GetCollectionDescription function](..\hidpddi\nf-hidpddi-hidp-getcollectiondescription.md) | Fills a device description block with collection description and the corresponding report ID information for the specified report descriptor. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [HidP_GetLinkCollectionNodes function](..\hidpi\nf-hidpi-hidp-getlinkcollectionnodes.md) | The HidP_GetLinkCollectionNodes routine returns a top-level collection's link collection array. |
| [HidP_GetUsages function](..\hidpi\nf-hidpi-hidp-getusages.md) | The HidP_GetUsages routine returns a list of all the HID control button usages that are on a specified usage page and are set to ON in a HID report. |
| [HidP_GetCaps function](..\hidpi\nf-hidpi-hidp-getcaps.md) | The HidP_GetCaps routine returns a top-level collection's HIDP_CAPS structure. |
| [HidP_GetButtonCaps function](..\hidpi\nf-hidpi-hidp-getbuttoncaps.md) | The HidP_GetButtonCaps routine returns a button capability array that describes all the HID control buttons in a top-level collection for a specified type of HID report. |
| [HidP_SetUsages function](..\hidpi\nf-hidpi-hidp-setusages.md) | The HidP_SetUsages routine sets specified HID control buttons ON (1) in a HID report. |
| [HidP_GetValueCaps function](..\hidpi\nf-hidpi-hidp-getvaluecaps.md) | The HidP_GetValueCaps routine returns a value capability array that describes all the HID control values in a top-level collection for a specified type of HID report. |
| [HidP_GetExtendedAttributes function](..\hidpi\nf-hidpi-hidp-getextendedattributes.md) | The HidP_GetExtendedAttributes routine returns the extended attributes of a HID control. |
| [HidP_SetUsageValue function](..\hidpi\nf-hidpi-hidp-setusagevalue.md) | The HidP_SetUsageValue routine sets a HID control value in a specified HID report. |
| [HidP_GetUsageValue function](..\hidpi\nf-hidpi-hidp-getusagevalue.md) | The HidP_GetUsageValue routine extracts the data associated with a HID control value that matches the selection criteria in a HID report. |
| [HidP_UnsetUsages function](..\hidpi\nf-hidpi-hidp-unsetusages.md) | The HidP_UnsetUsages routine sets specified HID control button usages OFF (zero) in a HID report. |
| [HidP_GetData function](..\hidpi\nf-hidpi-hidp-getdata.md) | The HidP_GetData routine returns, for a specified report, an array of HIDP_DATA structures that identify the data indices of all HID control buttons that are currently set to ON (1), and the data indices and data associated with all HID control values. |
| [HidP_GetSpecificButtonCaps function](..\hidpi\nf-hidpi-hidp-getspecificbuttoncaps.md) | The HidP_GetSpecificButtonCaps routine returns a button capability array that describes all HID control buttons in a top-level collection that meet a specified selection criteria. |
| [HidP_TranslateUsagesToI8042ScanCodes function](..\hidpi\nf-hidpi-hidp-translateusagestoi8042scancodes.md) | The HidP_TranslateUsagesToI8042ScanCodes routine maps a list of HID usages on the HID_USAGE_PAGE_KEYBOARD usage page to their respective PS/2 scan codes (Scan Code Set 1). |
| [HidP_SetUsageValueArray function](..\hidpi\nf-hidpi-hidp-setusagevaluearray.md) | The HidP_SetUsageValueArray routine sets a HID control usage value array in a specified HID report. |
| [HidP_UsageListDifference function](..\hidpi\nf-hidpi-hidp-usagelistdifference.md) | The HidP_UsageListDifference routine returns the differences between two arrays of HID usages. |
| [HidP_SetScaledUsageValue function](..\hidpi\nf-hidpi-hidp-setscaledusagevalue.md) | The HidP_SetScaledUsageValue routine converts a signed and scaled physical number to a HID usage's logical value, and sets the usage value in a specified HID report. |
| [HidP_MaxUsageListLength function](..\hidpi\nf-hidpi-hidp-maxusagelistlength.md) | The HidP_MaxUsageListLength routine returns the maximum number of HID usages that HidP_GetUsages can return for a specified type of HID report and a specified top-level collection. |
| [HidP_GetScaledUsageValue function](..\hidpi\nf-hidpi-hidp-getscaledusagevalue.md) | The HidP_GetScaledUsageValue routine returns the signed and scaled result of a HID control value extracted from a HID report. |
| [HidP_MaxDataListLength function](..\hidpi\nf-hidpi-hidp-maxdatalistlength.md) | The HidP_MaxDataListLength routine returns the maximum number of HIDP_DATA structures that HidP_GetData can return for a specified type of HID report and a specified top-level collection. |
| [HidP_InitializeReportForID function](..\hidpi\nf-hidpi-hidp-initializereportforid.md) | The HidP_InitializeReportForID routine initializes a HID report. |
| [HidP_SetData function](..\hidpi\nf-hidpi-hidp-setdata.md) | The HidP_SetData routine sets a specified set of HID control button and value usages in a HID report. |
| [HidP_GetUsageValueArray function](..\hidpi\nf-hidpi-hidp-getusagevaluearray.md) | The HidP_GetUsageValueArray routine extracts the data associated with a HID control usage value array from a HID report. |
| [HidP_GetUsagesEx function](..\hidpi\nf-hidpi-hidp-getusagesex.md) | The HidP_GetUsagesEx routine returns a list of the all the HID control button usages that are set to ON in a HID report. |
| [HidP_GetSpecificValueCaps function](..\hidpi\nf-hidpi-hidp-getspecificvaluecaps.md) | The HidP_GetSpecificValueCaps routine returns a value capability array that describes all HID control values that meet a specified selection criteria. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [USAGE_AND_PAGE structure](..\hidpi\ns-hidpi--usage-and-page.md) | The USAGE_AND_PAGE structure specifies the usage page and usage ID of a HID control. |
| [HIDP_VALUE_CAPS structure](..\hidpi\ns-hidpi--hidp-value-caps.md) | The HIDP_VALUE_CAPS structure contains information that describes the capability of a set of HID control values (either a single usage or a usage range). |
| [HIDP_DATA structure](..\hidpi\ns-hidpi--hidp-data.md) | The HIDP_DATA structure contains information about a HID control's data index and value in a HID report. |
| [HIDP_CAPS structure](..\hidpi\ns-hidpi--hidp-caps.md) | The HIDP_CAPS structure contains information about a top-level collection's capability. |
| [HIDP_BUTTON_CAPS structure](..\hidpi\ns-hidpi--hidp-button-caps.md) | The HIDP_BUTTON_CAPS structure contains information about the capability of a HID control button usage (or a set of buttons associated with a usage range). |
| [HIDP_EXTENDED_ATTRIBUTES structure](..\hidpi\ns-hidpi--hidp-extended-attributes.md) | The HIDP_EXTENDED_ATTRIBUTES structure contains information about the global items specified for a HID control that the HID parser did not recognize. |
| [HIDP_UNKNOWN_TOKEN structure](..\hidpi\ns-hidpi--hidp-unknown-token.md) | The HIDP_UNKNOWN_TOKEN structure contains information about a global item that the HID parser did not recognize. |
| [HIDP_LINK_COLLECTION_NODE structure](..\hidpi\ns-hidpi--hidp-link-collection-node.md) | The HIDP_LINK_COLLECTION_NODE structure contains information about a link collection in a top-level collection's link collection array. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [HIDP_REPORT_TYPE enumeration](..\hidpi\ne-hidpi--hidp-report-type.md) | The HIDP_REPORT_TYPE enumeration type is used to specify a HID report type. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_HID_ACTIVATE_DEVICE IOCTL](..\hidport\ni-hidport-ioctl-hid-activate-device.md) | The IOCTL_HID_ACTIVATE_DEVICE request activates a HIDClass device, which makes it ready for I/O operations. |
| [IOCTL_HID_GET_DEVICE_ATTRIBUTES IOCTL](..\hidport\ni-hidport-ioctl-hid-get-device-attributes.md) | The IOCTL_HID_GET_DEVICE_ATTRIBUTES request obtains a HIDClass device's attributes in a HID_DEVICE_ATTRIBUTES structure. |
| [IOCTL_HID_GET_STRING IOCTL](..\hidport\ni-hidport-ioctl-hid-get-string.md) | The IOCTL_HID_GET_STRING request obtains a manufacturer ID, product ID, or serial number for a top-level collection. The retrieved string is a NULL-terminated wide character string in a human-readable format. |
| [IOCTL_HID_GET_DEVICE_DESCRIPTOR IOCTL](..\hidport\ni-hidport-ioctl-hid-get-device-descriptor.md) | The IOCTL_HID_GET_DEVICE_DESCRIPTOR request obtains a HIDClass device's HID descriptor. |
| [IOCTL_HID_SEND_IDLE_NOTIFICATION_REQUEST IOCTL](..\hidport\ni-hidport-ioctl-hid-send-idle-notification-request.md) | The IOCTL_HID_SEND_IDLE_NOTIFICATION_REQUEST control code is the IOCTL of the idle notification request IRP that HIDClass sends to HID mini drivers, such as HIDUSB, to inform the bus driver that the device is now idle. |
| [IOCTL_HID_DEACTIVATE_DEVICE IOCTL](..\hidport\ni-hidport-ioctl-hid-deactivate-device.md) | The IOCTL_HID_DEACTIVATE_DEVICE request deactivates a HIDClass device, which causes it to stop operations and terminate all outstanding I/O requests. |
| [IOCTL_HID_GET_REPORT_DESCRIPTOR IOCTL](..\hidport\ni-hidport-ioctl-hid-get-report-descriptor.md) | The IOCTL_HID_GET_REPORT_DESCRIPTOR request obtains the report descriptor for a HIDClass device. |
| [IOCTL_HID_READ_REPORT IOCTL](..\hidport\ni-hidport-ioctl-hid-read-report.md) | The IOCTL_HID_READ_REPORT request transfers an input report from a HIDClass device into the HID class driver's buffer. |
| [IOCTL_HID_WRITE_REPORT IOCTL](..\hidport\ni-hidport-ioctl-hid-write-report.md) | The IOCTL_HID_WRITE_REPORT request sends a HID report to a HIDClass device. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [HID_MINIDRIVER_REGISTRATION structure](..\hidport\ns-hidport--hid-minidriver-registration.md) | The HID_MINIDRIVER_REGISTRATION structure contains registration information that a HID minidriver passes to the HID Client Drivers when the minidriver registers with the class driver. |
| [HID_DEVICE_EXTENSION structure](..\hidport\ns-hidport--hid-device-extension.md) | The HID_DEVICE_EXTENSION structure is used by a HID minidriver as its layout for the device extension of a HIDClass device's functional device object. |
| [HID_DEVICE_ATTRIBUTES structure](..\hidport\ns-hidport--hid-device-attributes.md) | The HID_DEVICE_ATTRIBUTES structure contains information about a HIDClass device. |
| [HID_DESCRIPTOR structure](..\hidport\ns-hidport--hid-descriptor.md) | The HID_DESCRIPTOR structure represents a HID descriptor for a HIDClass device. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [HidRegisterMinidriver function](..\hidport\nf-hidport-hidregisterminidriver.md) | The HidRegisterMinidriver routine is called by HID minidrivers, during their initialization, to register with the HID class driver. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [HidD_GetManufacturerString function](..\hidsdi\nf-hidsdi-hidd-getmanufacturerstring.md) | The HidD_GetManufacturerString routine returns a top-level collection's embedded string that identifies the manufacturer. |
| [HidD_GetSerialNumberString function](..\hidsdi\nf-hidsdi-hidd-getserialnumberstring.md) | The HidD_GetSerialNumberString routine returns the embedded string of a top-level collection that identifies the serial number of the collection's physical device. |
| [HidD_GetNumInputBuffers function](..\hidsdi\nf-hidsdi-hidd-getnuminputbuffers.md) | The HidD_GetNumInputBuffers routine returns the current size, in number of reports, of the ring buffer that the HID class driver uses to queue input reports from a specified top-level collection. |
| [HidD_GetAttributes function](..\hidsdi\nf-hidsdi-hidd-getattributes.md) | The HidD_GetAttributes routine returns the attributes of a specified top-level collection. |
| [HidD_GetHidGuid function](..\hidsdi\nf-hidsdi-hidd-gethidguid.md) | The HidD_GetHidGuid routine returns the device interfaceGUID for HIDClass devices. |
| [HidD_GetInputReport function](..\hidsdi\nf-hidsdi-hidd-getinputreport.md) | The HidD_GetInputReport routine returns an input reports from a top-level collection. |
| [HidD_FreePreparsedData function](..\hidsdi\nf-hidsdi-hidd-freepreparseddata.md) | The HidD_FreePreparsedData routine releases the resources that the HID class driver allocated to hold a top-level collection's preparsed data. |
| [HidD_GetProductString function](..\hidsdi\nf-hidsdi-hidd-getproductstring.md) | The HidD_GetProductString routine returns the embedded string of a top-level collection that identifies the manufacturer's product. |
| [HidD_GetFeature function](..\hidsdi\nf-hidsdi-hidd-getfeature.md) | The HidD_GetFeature routine returns a feature report from a specified top-level collection. |
| [HidD_SetFeature function](..\hidsdi\nf-hidsdi-hidd-setfeature.md) | The HidD_SetFeature routine sends a feature report to a top-level collection. |
| [HidD_SetOutputReport function](..\hidsdi\nf-hidsdi-hidd-setoutputreport.md) | The HidD_SetOutputReport routine sends an output report to a top-level collection. |
| [HidD_FlushQueue function](..\hidsdi\nf-hidsdi-hidd-flushqueue.md) | The HidD_FlushQueue routine deletes all pending input reports in a top-level collection's input queue. |
| [HidD_GetIndexedString function](..\hidsdi\nf-hidsdi-hidd-getindexedstring.md) | The HidD_GetIndexedString routine returns a specified embedded string from a top-level collection. |
| [HidD_GetPreparsedData function](..\hidsdi\nf-hidsdi-hidd-getpreparseddata.md) | The HidD_GetPreparsedData routine returns a top-level collection's preparsed data. |
| [HidD_SetNumInputBuffers function](..\hidsdi\nf-hidsdi-hidd-setnuminputbuffers.md) | The HidD_SetNumInputBuffers routine sets the maximum number of input reports that the HID class driver ring buffer can hold for a specified top-level collection. |
| [HidD_GetPhysicalDescriptor function](..\hidsdi\nf-hidsdi-hidd-getphysicaldescriptor.md) | The HidD_GetPhysicalDescriptor routine returns the embedded string of a top-level collection that identifies the collection's physical device. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [HIDD_ATTRIBUTES structure](..\hidsdi\ns-hidsdi--hidd-attributes.md) | The HIDD_ATTRIBUTES structure contains vendor information about a HIDClass device. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PSERVICE_CALLBACK_ROUTINE callback](..\kbdmou\nc-kbdmou-pservice-callback-routine.md) | A function driver calls the class service callback in its ISR dispatch completion routine. The class service callback transfers input data from the input data buffer of a device to the class data queue. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_INTERNAL_MOUSE_CONNECT IOCTL](..\kbdmou\ni-kbdmou-ioctl-internal-mouse-connect.md) | The IOCTL_INTERNAL_MOUSE_CONNECT request connects Mouclass service to a mouse device. |
| [IOCTL_INTERNAL_KEYBOARD_DISCONNECT IOCTL](..\kbdmou\ni-kbdmou-ioctl-internal-keyboard-disconnect.md) | The IOCTL_INTERNAL_KEYBOARD_DISCONNECT request is completed with a status of STATUS_NOT_IMPLEMENTED. Note that a Plug and Play keyboard can be added or removed by the Plug and Play manager. |
| [IOCTL_INTERNAL_KEYBOARD_CONNECT IOCTL](..\kbdmou\ni-kbdmou-ioctl-internal-keyboard-connect.md) | The IOCTL_INTERNAL_KEYBOARD_CONNECT request connects the Kbdclass service to the keyboard device. |
| [IOCTL_INTERNAL_MOUSE_DISCONNECT IOCTL](..\kbdmou\ni-kbdmou-ioctl-internal-mouse-disconnect.md) | The IOCTL_INTERNAL_MOUSE_DISCONNECT request is completed by Moufiltr with an error status of STATUS_NOT_IMPLEMENTED. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [CONNECT_DATA structure](..\kbdmou\ns-kbdmou--connect-data.md) | CONNECT_DATA specifies information that Kbdclass and Mouclass use to connect to a keyboard or mouse port. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [KEYBOARD_SCAN_STATE enumeration](..\ntdd8042\ne-ntdd8042--keyboard-scan-state.md) | The KEYBOARD_SCAN_STATE enumeration type indicates the scan state of an input byte from a keyboard. |
| [MOUSE_STATE enumeration](..\ntdd8042\ne-ntdd8042--mouse-state.md) | The MOUSE_STATE enumeration type identifies the current state of input from a mouse. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [INTERNAL_I8042_HOOK_KEYBOARD structure](..\ntdd8042\ns-ntdd8042--internal-i8042-hook-keyboard.md) | INTERNAL_I8042_HOOK_KEYBOARD is used by I8042prt to connect optional callback routines that supplement keyboard initialization and the keyboard ISR. The callbacks can be supplied by an optional, vendor-supplied, upper-level filter driver. |
| [INTERNAL_I8042_START_INFORMATION structure](..\ntdd8042\ns-ntdd8042--internal-i8042-start-information.md) | INTERNAL_I8042_START_INFORMATION specifies the interrupt object that an optional, vendor-supplied, upper-level filter device driver can use to synchronize its operation with an I8042prt ISR. |
| [INTERNAL_I8042_HOOK_MOUSE structure](..\ntdd8042\ns-ntdd8042--internal-i8042-hook-mouse.md) | INTERNAL_I8042_HOOK_MOUSE is used by I8042prt to connect an optional callback routine that supplements the operation of the mouse ISR. The callback can be supplied by an optional, vendor-supplied, upper-level filter driver. |
| [OUTPUT_PACKET structure](..\ntdd8042\ns-ntdd8042--output-packet.md) | OUTPUT_PACKET contains information about the data that is being written to a keyboard or mouse device by I8042prt. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_INTERNAL_I8042_MOUSE_WRITE_BUFFER IOCTL](..\ntdd8042\ni-ntdd8042-ioctl-internal-i8042-mouse-write-buffer.md) | The IOCTL_INTERNAL_I8042_MOUSE_WRITE_BUFFER request writes data to the i8042 port controller to control operation of a mouse device. |
| [IOCTL_INTERNAL_I8042_HOOK_MOUSE IOCTL](..\ntdd8042\ni-ntdd8042-ioctl-internal-i8042-hook-mouse.md) | The IOCTL_INTERNAL_I8042_HOOK_MOUSE request adds an ISR callback routine to the I8042prt mouse ISR. |
| [IOCTL_INTERNAL_I8042_HOOK_KEYBOARD IOCTL](..\ntdd8042\ni-ntdd8042-ioctl-internal-i8042-hook-keyboard.md) | The IOCTL_INTERNAL_I8042_HOOK_KEYBOARD request does the following |
| [IOCTL_INTERNAL_I8042_MOUSE_START_INFORMATION IOCTL](..\ntdd8042\ni-ntdd8042-ioctl-internal-i8042-mouse-start-information.md) | The IOCTL_INTERNAL_I8042_MOUSE_START_INFORMATION request passes a pointer to a mouse interrupt object. |
| [IOCTL_INTERNAL_I8042_KEYBOARD_START_INFORMATION IOCTL](..\ntdd8042\ni-ntdd8042-ioctl-internal-i8042-keyboard-start-information.md) | The IOCTL_INTERNAL_I8042_KEYBOARD_START_INFORMATION request passes a pointer to a keyboard interrupt object. |
| [IOCTL_INTERNAL_I8042_KEYBOARD_WRITE_BUFFER IOCTL](..\ntdd8042\ni-ntdd8042-ioctl-internal-i8042-keyboard-write-buffer.md) | The IOCTL_INTERNAL_I8042_KEYBOARD_WRITE_BUFFER request writes data to the i8042 port controller to control operation of a keyboard device. |
| [IOCTL_INTERNAL_I8042_CONTROLLER_WRITE_BUFFER IOCTL](..\ntdd8042\ni-ntdd8042-ioctl-internal-i8042-controller-write-buffer.md) | The IOCTL_INTERNAL_I8042_CONTROLLER_WRITE_BUFFER request is not supported. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PI8042_SYNCH_READ_PORT callback](..\ntdd8042\nc-ntdd8042-pi8042-synch-read-port.md) | The PI8042_SYNCH_READ_PORT-typed callback routine does a synchronized read from an i8042 port. I8042prt supplies this callback. |
| [PI8042_QUEUE_PACKET callback](..\ntdd8042\nc-ntdd8042-pi8042-queue-packet.md) | The PI8042_QUEUE_PACKET-typed callback routine queues an input data packet for processing by the ISR DPC of a keyboard or mouse device. I8042prt provides this callback. |
| [PI8042_MOUSE_ISR callback](..\ntdd8042\nc-ntdd8042-pi8042-mouse-isr.md) | A PI8042_MOUSE_ISR-typed callback routine customizes the operation of the I8042prt mouse ISR. |
| [PI8042_KEYBOARD_INITIALIZATION_ROUTINE callback](..\ntdd8042\nc-ntdd8042-pi8042-keyboard-initialization-routine.md) | A PI8042_KEYBOARD_INITIALIZATION_ROUTINE-typed callback routine supplements the default initialization of a keyboard device by I8042prt. |
| [PI8042_KEYBOARD_ISR callback](..\ntdd8042\nc-ntdd8042-pi8042-keyboard-isr.md) | A PI8042_KEYBOARD_ISR-typed callback routine customizes the operation of the I8042prt keyboard ISR. |
| [PI8042_ISR_WRITE_PORT callback](..\ntdd8042\nc-ntdd8042-pi8042-isr-write-port.md) | The PI8042_ISR_WRITE_PORT-typed callback routine writes data to an i8042 port. I8042prt provides this callback. |
| [PI8042_SYNCH_WRITE_PORT callback](..\ntdd8042\nc-ntdd8042-pi8042-synch-write-port.md) | The PI8042_SYNCH_READ_PORT-typed callback routine does a synchronized write to an i8042 port. I8042prt supplies this routine. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_VHF_READY_FOR_NEXT_READ_REPORT callback](..\vhf\nc-vhf-evt-vhf-ready-for-next-read-report.md) | The HID source driver implements this event call back function to use its buffering scheme for HID Input Reports, and wants to get notified when the next report can be submitted to VHF. |
| [EVT_VHF_ASYNC_OPERATION callback](..\vhf\nc-vhf-evt-vhf-async-operation.md) | The HID source driver implements this event callback if it wants to support one of the four asynchronous operation to get and set HID reports. |
| [EVT_VHF_CLEANUP callback](..\vhf\nc-vhf-evt-vhf-cleanup.md) | The HID source driver implements this event callback to free resources that might the driver allocated to the virtual HID device. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [VHF_CONFIG_INIT function](..\vhf\nf-vhf-vhf-config-init.md) | Use the VHF_CONFIG_INIT function to initialize the required members of the VHF_CONFIG structure allocated by the HID source driver. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [VHF_CONFIG structure](..\vhf\ns-vhf--vhf-config.md) | Contains initial configuration information that is provided by the HID source driver when it calls VhfCreate to create a virtual HID device. |


This technology is in the following headers:


| Header        | 

| [hidpddi](..\hidpddi\~PORTAL~hidpddi.md) | 

| [hidpi](..\hidpi\~PORTAL~hidpi.md) | 

| [hidport](..\hidport\~PORTAL~hidport.md) | 

| [hidsdi](..\hidsdi\~PORTAL~hidsdi.md) | 

| [kbdmou](..\kbdmou\~PORTAL~kbdmou.md) | 

| [ntdd8042](..\ntdd8042\~PORTAL~ntdd8042.md) | 

| [sffprtcl](..\sffprtcl\~PORTAL~sffprtcl.md) | 

| [vhf](..\vhf\~PORTAL~vhf.md) | 
