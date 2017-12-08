# Human Interface Devices (HID)

Overview of the Human Interface Devices (HID) technology.

To develop Human Interface Devices (HID), you need these headers:

 * [hidclass.h](..\hidclass\index.md)
 * [hidpddi.h](..\hidpddi\index.md)
 * [hidpi.h](..\hidpi\index.md)
 * [hidport.h](..\hidport\index.md)
 * [hidsdi.h](..\hidsdi\index.md)
 * [kbdmou.h](..\kbdmou\index.md)
 * [ntdd8042.h](..\ntdd8042\index.md)
 * [vhf.h](..\vhf\index.md)

For the programming guide, see [Human Interface Devices (HID)](https://docs.microsoft.com/en-us/windows-hardware/drivers/hid).

## Functions

| Title   | Description   |
| ---- |:---- |
| [HidD_FlushQueue function](..\hidsdi\nf-hidsdi-hidd-flushqueue.md) | The HidD_FlushQueue routine deletes all pending input reports in a top-level collection's input queue. |
| [HidD_FreePreparsedData function](..\hidsdi\nf-hidsdi-hidd-freepreparseddata.md) | The HidD_FreePreparsedData routine releases the resources that the HID class driver allocated to hold a top-level collection's preparsed data. |
| [HidD_GetAttributes function](..\hidsdi\nf-hidsdi-hidd-getattributes.md) | The HidD_GetAttributes routine returns the attributes of a specified top-level collection. |
| [HidD_GetFeature function](..\hidsdi\nf-hidsdi-hidd-getfeature.md) | The HidD_GetFeature routine returns a feature report from a specified top-level collection. |
| [HidD_GetHidGuid function](..\hidsdi\nf-hidsdi-hidd-gethidguid.md) | The HidD_GetHidGuid routine returns the device interfaceGUID for HIDClass devices. |
| [HidD_GetIndexedString function](..\hidsdi\nf-hidsdi-hidd-getindexedstring.md) | The HidD_GetIndexedString routine returns a specified embedded string from a top-level collection. |
| [HidD_GetInputReport function](..\hidsdi\nf-hidsdi-hidd-getinputreport.md) | The HidD_GetInputReport routine returns an input reports from a top-level collection. |
| [HidD_GetManufacturerString function](..\hidsdi\nf-hidsdi-hidd-getmanufacturerstring.md) | The HidD_GetManufacturerString routine returns a top-level collection's embedded string that identifies the manufacturer. |
| [HidD_GetNumInputBuffers function](..\hidsdi\nf-hidsdi-hidd-getnuminputbuffers.md) | The HidD_GetNumInputBuffers routine returns the current size, in number of reports, of the ring buffer that the HID class driver uses to queue input reports from a specified top-level collection. |
| [HidD_GetPhysicalDescriptor function](..\hidsdi\nf-hidsdi-hidd-getphysicaldescriptor.md) | The HidD_GetPhysicalDescriptor routine returns the embedded string of a top-level collection that identifies the collection's physical device. |
| [HidD_GetPreparsedData function](..\hidsdi\nf-hidsdi-hidd-getpreparseddata.md) | The HidD_GetPreparsedData routine returns a top-level collection's preparsed data. |
| [HidD_GetProductString function](..\hidsdi\nf-hidsdi-hidd-getproductstring.md) | The HidD_GetProductString routine returns the embedded string of a top-level collection that identifies the manufacturer's product. |
| [HidD_GetSerialNumberString function](..\hidsdi\nf-hidsdi-hidd-getserialnumberstring.md) | The HidD_GetSerialNumberString routine returns the embedded string of a top-level collection that identifies the serial number of the collection's physical device. |
| [HidD_SetFeature function](..\hidsdi\nf-hidsdi-hidd-setfeature.md) | The HidD_SetFeature routine sends a feature report to a top-level collection. |
| [HidD_SetNumInputBuffers function](..\hidsdi\nf-hidsdi-hidd-setnuminputbuffers.md) | The HidD_SetNumInputBuffers routine sets the maximum number of input reports that the HID class driver ring buffer can hold for a specified top-level collection. |
| [HidD_SetOutputReport function](..\hidsdi\nf-hidsdi-hidd-setoutputreport.md) | The HidD_SetOutputReport routine sends an output report to a top-level collection. |
| [HidP_GetButtonCaps function](..\hidpi\nf-hidpi-hidp-getbuttoncaps.md) | The HidP_GetButtonCaps routine returns a button capability array that describes all the HID control buttons in a top-level collection for a specified type of HID report. |
| [HidP_GetCaps function](..\hidpi\nf-hidpi-hidp-getcaps.md) | The HidP_GetCaps routine returns a top-level collection's HIDP_CAPS structure. |
| [HidP_GetCollectionDescription function](..\hidpddi\nf-hidpddi-hidp-getcollectiondescription.md) | Fills a device description block with collection description and the corresponding report ID information for the specified report descriptor. |
| [HidP_GetData function](..\hidpi\nf-hidpi-hidp-getdata.md) | The HidP_GetData routine returns, for a specified report, an array of HIDP_DATA structures that identify the data indices of all HID control buttons that are currently set to ON (1), and the data indices and data associated with all HID control values. |
| [HidP_GetExtendedAttributes function](..\hidpi\nf-hidpi-hidp-getextendedattributes.md) | The HidP_GetExtendedAttributes routine returns the extended attributes of a HID control. |
| [HidP_GetLinkCollectionNodes function](..\hidpi\nf-hidpi-hidp-getlinkcollectionnodes.md) | The HidP_GetLinkCollectionNodes routine returns a top-level collection's link collection array. |
| [HidP_GetScaledUsageValue function](..\hidpi\nf-hidpi-hidp-getscaledusagevalue.md) | The HidP_GetScaledUsageValue routine returns the signed and scaled result of a HID control value extracted from a HID report. |
| [HidP_GetSpecificButtonCaps function](..\hidpi\nf-hidpi-hidp-getspecificbuttoncaps.md) | The HidP_GetSpecificButtonCaps routine returns a button capability array that describes all HID control buttons in a top-level collection that meet a specified selection criteria. |
| [HidP_GetSpecificValueCaps function](..\hidpi\nf-hidpi-hidp-getspecificvaluecaps.md) | The HidP_GetSpecificValueCaps routine returns a value capability array that describes all HID control values that meet a specified selection criteria. |
| [HidP_GetUsageValue function](..\hidpi\nf-hidpi-hidp-getusagevalue.md) | The HidP_GetUsageValue routine extracts the data associated with a HID control value that matches the selection criteria in a HID report. |
| [HidP_GetUsageValueArray function](..\hidpi\nf-hidpi-hidp-getusagevaluearray.md) | The HidP_GetUsageValueArray routine extracts the data associated with a HID control usage value array from a HID report. |
| [HidP_GetUsages function](..\hidpi\nf-hidpi-hidp-getusages.md) | The HidP_GetUsages routine returns a list of all the HID control button usages that are on a specified usage page and are set to ON in a HID report. |
| [HidP_GetUsagesEx function](..\hidpi\nf-hidpi-hidp-getusagesex.md) | The HidP_GetUsagesEx routine returns a list of the all the HID control button usages that are set to ON in a HID report. |
| [HidP_GetValueCaps function](..\hidpi\nf-hidpi-hidp-getvaluecaps.md) | The HidP_GetValueCaps routine returns a value capability array that describes all the HID control values in a top-level collection for a specified type of HID report. |
| [HidP_InitializeReportForID function](..\hidpi\nf-hidpi-hidp-initializereportforid.md) | The HidP_InitializeReportForID routine initializes a HID report. |
| [HidP_MaxDataListLength function](..\hidpi\nf-hidpi-hidp-maxdatalistlength.md) | The HidP_MaxDataListLength routine returns the maximum number of HIDP_DATA structures that HidP_GetData can return for a specified type of HID report and a specified top-level collection. |
| [HidP_MaxUsageListLength function](..\hidpi\nf-hidpi-hidp-maxusagelistlength.md) | The HidP_MaxUsageListLength routine returns the maximum number of HID usages that HidP_GetUsages can return for a specified type of HID report and a specified top-level collection. |
| [HidP_SetData function](..\hidpi\nf-hidpi-hidp-setdata.md) | The HidP_SetData routine sets a specified set of HID control button and value usages in a HID report. |
| [HidP_SetScaledUsageValue function](..\hidpi\nf-hidpi-hidp-setscaledusagevalue.md) | The HidP_SetScaledUsageValue routine converts a signed and scaled physical number to a HID usage's logical value, and sets the usage value in a specified HID report. |
| [HidP_SetUsageValue function](..\hidpi\nf-hidpi-hidp-setusagevalue.md) | The HidP_SetUsageValue routine sets a HID control value in a specified HID report. |
| [HidP_SetUsageValueArray function](..\hidpi\nf-hidpi-hidp-setusagevaluearray.md) | The HidP_SetUsageValueArray routine sets a HID control usage value array in a specified HID report. |
| [HidP_SetUsages function](..\hidpi\nf-hidpi-hidp-setusages.md) | The HidP_SetUsages routine sets specified HID control buttons ON (1) in a HID report. |
| [HidP_TranslateUsagesToI8042ScanCodes function](..\hidpi\nf-hidpi-hidp-translateusagestoi8042scancodes.md) | The HidP_TranslateUsagesToI8042ScanCodes routine maps a list of HID usages on the HID_USAGE_PAGE_KEYBOARD usage page to their respective PS/2 scan codes (Scan Code Set 1). |
| [HidP_UnsetUsages function](..\hidpi\nf-hidpi-hidp-unsetusages.md) | The HidP_UnsetUsages routine sets specified HID control button usages OFF (zero) in a HID report. |
| [HidP_UsageListDifference function](..\hidpi\nf-hidpi-hidp-usagelistdifference.md) | The HidP_UsageListDifference routine returns the differences between two arrays of HID usages. |
| [HidRegisterMinidriver function](..\hidport\nf-hidport-hidregisterminidriver.md) | The HidRegisterMinidriver routine is called by HID minidrivers, during their initialization, to register with the HID class driver. |
| [VHF_CONFIG_INIT function](..\vhf\nf-vhf-vhf-config-init.md) | Use the VHF_CONFIG_INIT function to initialize the required members of the VHF_CONFIG structure allocated by the HID source driver. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [EVT_VHF_ASYNC_OPERATION callback](..\vhf\nc-vhf-evt-vhf-async-operation.md) | The HID source driver implements this event callback if it wants to support one of the four asynchronous operation to get and set HID reports. |
| [EVT_VHF_CLEANUP callback](..\vhf\nc-vhf-evt-vhf-cleanup.md) | The HID source driver implements this event callback to free resources that might the driver allocated to the virtual HID device. |
| [EVT_VHF_READY_FOR_NEXT_READ_REPORT callback](..\vhf\nc-vhf-evt-vhf-ready-for-next-read-report.md) | The HID source driver implements this event call back function to use its buffering scheme for HID Input Reports, and wants to get notified when the next report can be submitted to VHF. |
| [PI8042_ISR_WRITE_PORT callback](..\ntdd8042\nc-ntdd8042-pi8042-isr-write-port.md) | The PI8042_ISR_WRITE_PORT-typed callback routine writes data to an i8042 port. I8042prt provides this callback. |
| [PI8042_KEYBOARD_INITIALIZATION_ROUTINE callback](..\ntdd8042\nc-ntdd8042-pi8042-keyboard-initialization-routine.md) | A PI8042_KEYBOARD_INITIALIZATION_ROUTINE-typed callback routine supplements the default initialization of a keyboard device by I8042prt. |
| [PI8042_KEYBOARD_ISR callback](..\ntdd8042\nc-ntdd8042-pi8042-keyboard-isr.md) | A PI8042_KEYBOARD_ISR-typed callback routine customizes the operation of the I8042prt keyboard ISR. |
| [PI8042_MOUSE_ISR callback](..\ntdd8042\nc-ntdd8042-pi8042-mouse-isr.md) | A PI8042_MOUSE_ISR-typed callback routine customizes the operation of the I8042prt mouse ISR. |
| [PI8042_QUEUE_PACKET callback](..\ntdd8042\nc-ntdd8042-pi8042-queue-packet.md) | The PI8042_QUEUE_PACKET-typed callback routine queues an input data packet for processing by the ISR DPC of a keyboard or mouse device. I8042prt provides this callback. |
| [PI8042_SYNCH_READ_PORT callback](..\ntdd8042\nc-ntdd8042-pi8042-synch-read-port.md) | The PI8042_SYNCH_READ_PORT-typed callback routine does a synchronized read from an i8042 port. I8042prt supplies this callback. |
| [PI8042_SYNCH_WRITE_PORT callback](..\ntdd8042\nc-ntdd8042-pi8042-synch-write-port.md) | The PI8042_SYNCH_READ_PORT-typed callback routine does a synchronized write to an i8042 port. I8042prt supplies this routine. |
| [PSERVICE_CALLBACK_ROUTINE callback](..\kbdmou\nc-kbdmou-pservice-callback-routine.md) | A function driver calls the class service callback in its ISR dispatch completion routine. The class service callback transfers input data from the input data buffer of a device to the class data queue. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [CONNECT_DATA structure](..\kbdmou\ns-kbdmou--connect-data.md) | CONNECT_DATA specifies information that Kbdclass and Mouclass use to connect to a keyboard or mouse port. |
| [HIDD_ATTRIBUTES structure](..\hidsdi\ns-hidsdi--hidd-attributes.md) | The HIDD_ATTRIBUTES structure contains vendor information about a HIDClass device. |
| [HIDP_BUTTON_CAPS structure](..\hidpi\ns-hidpi--hidp-button-caps.md) | The HIDP_BUTTON_CAPS structure contains information about the capability of a HID control button usage (or a set of buttons associated with a usage range). |
| [HIDP_CAPS structure](..\hidpi\ns-hidpi--hidp-caps.md) | The HIDP_CAPS structure contains information about a top-level collection's capability. |
| [HIDP_COLLECTION_DESC structure](..\hidpddi\ns-hidpddi--hidp-collection-desc.md) | Contains the information of a top-level-collection. This structure is used in the HidP_GetCollectionDescription call. |
| [HIDP_DATA structure](..\hidpi\ns-hidpi--hidp-data.md) | The HIDP_DATA structure contains information about a HID control's data index and value in a HID report. |
| [HIDP_DEVICE_DESC structure](..\hidpddi\ns-hidpddi--hidp-device-desc.md) | Contains the device description block filled in collection descriptions as linked lists. This structure is used by HidP_GetCollectionDescription. |
| [HIDP_EXTENDED_ATTRIBUTES structure](..\hidpi\ns-hidpi--hidp-extended-attributes.md) | The HIDP_EXTENDED_ATTRIBUTES structure contains information about the global items specified for a HID control that the HID parser did not recognize. |
| [HIDP_GETCOLDESC_DBG structure](..\hidpddi\ns-hidpddi--hidp-getcoldesc-dbg.md) | Contains the error code indicating the failure in parsing the report descriptor. This structure is used in the HidP_GetCollectionDescription call. |
| [HIDP_LINK_COLLECTION_NODE structure](..\hidpi\ns-hidpi--hidp-link-collection-node.md) | The HIDP_LINK_COLLECTION_NODE structure contains information about a link collection in a top-level collection's link collection array. |
| [HIDP_REPORT_IDS structure](..\hidpddi\ns-hidpddi--hidp-report-ids.md) | Contains report ID information for a top-level collection. |
| [HIDP_UNKNOWN_TOKEN structure](..\hidpi\ns-hidpi--hidp-unknown-token.md) | The HIDP_UNKNOWN_TOKEN structure contains information about a global item that the HID parser did not recognize. |
| [HIDP_VALUE_CAPS structure](..\hidpi\ns-hidpi--hidp-value-caps.md) | The HIDP_VALUE_CAPS structure contains information that describes the capability of a set of HID control values (either a single usage or a usage range). |
| [HID_COLLECTION_INFORMATION structure](..\hidclass\ns-hidclass--hid-collection-information.md) | The HID_COLLECTION_INFORMATION structure contains general information about a top-level collection. |
| [HID_DESCRIPTOR structure](..\hidport\ns-hidport--hid-descriptor.md) | The HID_DESCRIPTOR structure represents a HID descriptor for a HIDClass device. |
| [HID_DEVICE_ATTRIBUTES structure](..\hidport\ns-hidport--hid-device-attributes.md) | The HID_DEVICE_ATTRIBUTES structure contains information about a HIDClass device. |
| [HID_DEVICE_EXTENSION structure](..\hidport\ns-hidport--hid-device-extension.md) | The HID_DEVICE_EXTENSION structure is used by a HID minidriver as its layout for the device extension of a HIDClass device's functional device object. |
| [HID_MINIDRIVER_REGISTRATION structure](..\hidport\ns-hidport--hid-minidriver-registration.md) | The HID_MINIDRIVER_REGISTRATION structure contains registration information that a HID minidriver passes to the HID Client Drivers when the minidriver registers with the class driver. |
| [HID_XFER_PACKET structure](..\hidclass\ns-hidclass--hid-xfer-packet.md) | The HID_XFER_PACKET structure contains information about a HID report that the HID class driver uses with I/O requests to get or set a report. |
| [INTERNAL_I8042_HOOK_KEYBOARD structure](..\ntdd8042\ns-ntdd8042--internal-i8042-hook-keyboard.md) | INTERNAL_I8042_HOOK_KEYBOARD is used by I8042prt to connect optional callback routines that supplement keyboard initialization and the keyboard ISR. The callbacks can be supplied by an optional, vendor-supplied, upper-level filter driver. |
| [INTERNAL_I8042_HOOK_MOUSE structure](..\ntdd8042\ns-ntdd8042--internal-i8042-hook-mouse.md) | INTERNAL_I8042_HOOK_MOUSE is used by I8042prt to connect an optional callback routine that supplements the operation of the mouse ISR. The callback can be supplied by an optional, vendor-supplied, upper-level filter driver. |
| [INTERNAL_I8042_START_INFORMATION structure](..\ntdd8042\ns-ntdd8042--internal-i8042-start-information.md) | INTERNAL_I8042_START_INFORMATION specifies the interrupt object that an optional, vendor-supplied, upper-level filter device driver can use to synchronize its operation with an I8042prt ISR. |
| [OUTPUT_PACKET structure](..\ntdd8042\ns-ntdd8042--output-packet.md) | OUTPUT_PACKET contains information about the data that is being written to a keyboard or mouse device by I8042prt. |
| [USAGE_AND_PAGE structure](..\hidpi\ns-hidpi--usage-and-page.md) | The USAGE_AND_PAGE structure specifies the usage page and usage ID of a HID control. |
| [VHF_CONFIG structure](..\vhf\ns-vhf--vhf-config.md) | Contains initial configuration information that is provided by the HID source driver when it calls VhfCreate to create a virtual HID device. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [HIDP_REPORT_TYPE enumeration](..\hidpi\ne-hidpi--hidp-report-type.md) | The HIDP_REPORT_TYPE enumeration type is used to specify a HID report type. |
| [KEYBOARD_SCAN_STATE enumeration](..\ntdd8042\ne-ntdd8042--keyboard-scan-state.md) | The KEYBOARD_SCAN_STATE enumeration type indicates the scan state of an input byte from a keyboard. |
| [MOUSE_STATE enumeration](..\ntdd8042\ne-ntdd8042--mouse-state.md) | The MOUSE_STATE enumeration type identifies the current state of input from a mouse. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_GET_NUM_DEVICE_INPUT_BUFFERS IOCTL](..\hidclass\ni-hidclass-ioctl-get-num-device-input-buffers.md) | The IOCTL_GET_NUM_DEVICE_INPUT_BUFFERS request obtains the size of the input report queue for a top-level collection. |
| [IOCTL_GET_PHYSICAL_DESCRIPTOR IOCTL](..\hidclass\ni-hidclass-ioctl-get-physical-descriptor.md) | The IOCTL_GET_PHYSICAL_DESCRIPTOR request obtains the physical descriptor of a top-level collection. |
| [IOCTL_HID_ACTIVATE_DEVICE IOCTL](..\hidport\ni-hidport-ioctl-hid-activate-device.md) | The IOCTL_HID_ACTIVATE_DEVICE request activates a HIDClass device, which makes it ready for I/O operations. |
| [IOCTL_HID_DEACTIVATE_DEVICE IOCTL](..\hidport\ni-hidport-ioctl-hid-deactivate-device.md) | The IOCTL_HID_DEACTIVATE_DEVICE request deactivates a HIDClass device, which causes it to stop operations and terminate all outstanding I/O requests. |
| [IOCTL_HID_DEVICERESET_NOTIFICATION IOCTL](..\hidclass\ni-hidclass-ioctl-hid-devicereset-notification.md) | The IOCTL_HID_DEVICERESET_NOTIFICATION request is sent by the HID client driver to HID class driver to wait for a device-initiated reset event. |
| [IOCTL_HID_DISABLE_SECURE_READ IOCTL](..\hidclass\ni-hidclass-ioctl-hid-disable-secure-read.md) | The IOCTL_HID_DISABLE_SECURE_READ request cancels an IOCTL_HID_ENABLE_SECURE_READ request for a HID collection. |
| [IOCTL_HID_ENABLE_SECURE_READ IOCTL](..\hidclass\ni-hidclass-ioctl-hid-enable-secure-read.md) | The IOCTL_HID_ENABLE_SECURE_READ request enables a secure read for open files of a HID collection. |
| [IOCTL_HID_ENABLE_WAKE_ON_SX IOCTL](..\hidclass\ni-hidclass-ioctl-hid-enable-wake-on-sx.md) | The IOCTL_HID_ENABLE_WAKE_ON_SX request is used to indicate the requirement for a device to be able to wake from system sleep. |
| [IOCTL_HID_FLUSH_QUEUE IOCTL](..\hidclass\ni-hidclass-ioctl-hid-flush-queue.md) | The IOCTL_HID_FLUSH_QUEUE request dequeues all of the unparsed input reports from a top-level collection's input report queue. |
| [IOCTL_HID_GET_COLLECTION_DESCRIPTOR IOCTL](..\hidclass\ni-hidclass-ioctl-hid-get-collection-descriptor.md) | The IOCTL_HID_GET_COLLECTION_DESCRIPTOR request obtains a top-level collection's preparsed data, which the HID class driver extracted from the physical device's report descriptor during device initialization. |
| [IOCTL_HID_GET_COLLECTION_INFORMATION IOCTL](..\hidclass\ni-hidclass-ioctl-hid-get-collection-information.md) | The IOCTL_HID_GET_COLLECTION_INFORMATION request obtains a top-level collection's HID_COLLECTION_INFORMATION structure. |
| [IOCTL_HID_GET_DEVICE_ATTRIBUTES IOCTL](..\hidport\ni-hidport-ioctl-hid-get-device-attributes.md) | The IOCTL_HID_GET_DEVICE_ATTRIBUTES request obtains a HIDClass device's attributes in a HID_DEVICE_ATTRIBUTES structure. |
| [IOCTL_HID_GET_DEVICE_DESCRIPTOR IOCTL](..\hidport\ni-hidport-ioctl-hid-get-device-descriptor.md) | The IOCTL_HID_GET_DEVICE_DESCRIPTOR request obtains a HIDClass device's HID descriptor. |
| [IOCTL_HID_GET_DRIVER_CONFIG IOCTL](..\hidclass\ni-hidclass-ioctl-hid-get-driver-config.md) | The IOCTL_HID_GET_DRIVER_CONFIG request retrieves the driver configuration. |
| [IOCTL_HID_GET_FEATURE IOCTL](..\hidclass\ni-hidclass-ioctl-hid-get-feature.md) | The IOCTL_HID_GET_FEATURE request obtains a feature report from a HIDClass device. |
| [IOCTL_HID_GET_HARDWARE_ID IOCTL](..\hidclass\ni-hidclass-ioctl-hid-get-hardware-id.md) | The IOCTL_HID_GET_HARDWARE_ID request obtains the Plug and Play hardware ID of a top-level collection. |
| [IOCTL_HID_GET_INDEXED_STRING IOCTL](..\hidclass\ni-hidclass-ioctl-hid-get-indexed-string.md) | The IOCTL_HID_GET_INDEXED_STRING request obtains a specified embedded string for a top-level collection. |
| [IOCTL_HID_GET_INPUT_REPORT IOCTL](..\hidclass\ni-hidclass-ioctl-hid-get-input-report.md) | IOCTL_HID_GET_INPUT_REPORT returns an input report from a HID Class device. |
| [IOCTL_HID_GET_MANUFACTURER_STRING IOCTL](..\hidclass\ni-hidclass-ioctl-hid-get-manufacturer-string.md) | The IOCTL_HID_GET_MANUFACTURER_STRING request obtains a top-level collection's embedded string that identifies the manufacturer of the device. |
| [IOCTL_HID_GET_MS_GENRE_DESCRIPTOR IOCTL](..\hidclass\ni-hidclass-ioctl-hid-get-ms-genre-descriptor.md) | The IOCTL_HID_GET_MS_GENRE_DESCRIPTOR request is used for retrieving the genre descriptor for the device. |
| [IOCTL_HID_GET_POLL_FREQUENCY_MSEC IOCTL](..\hidclass\ni-hidclass-ioctl-hid-get-poll-frequency-msec.md) | The IOCTL_HID_GET_POLL_FREQUENCY_MSEC request obtains the current polling frequency, in milliseconds, of a top-level collection. |
| [IOCTL_HID_GET_PRODUCT_STRING IOCTL](..\hidclass\ni-hidclass-ioctl-hid-get-product-string.md) | The IOCTL_HID_GET_PRODUCT_STRING request obtains a top-level collection's embedded string that identifies the manufacturer's product. The retrieved string is a NULL-terminated wide character string in a human-readable format. |
| [IOCTL_HID_GET_REPORT_DESCRIPTOR IOCTL](..\hidport\ni-hidport-ioctl-hid-get-report-descriptor.md) | The IOCTL_HID_GET_REPORT_DESCRIPTOR request obtains the report descriptor for a HIDClass device. |
| [IOCTL_HID_GET_SERIALNUMBER_STRING IOCTL](..\hidclass\ni-hidclass-ioctl-hid-get-serialnumber-string.md) | The IOCTL_HID_GET_SERIALNUMBER_STRING request obtains a top-level collection's embedded string that identifies the device's serial number. |
| [IOCTL_HID_GET_STRING IOCTL](..\hidport\ni-hidport-ioctl-hid-get-string.md) | The IOCTL_HID_GET_STRING request obtains a manufacturer ID, product ID, or serial number for a top-level collection. The retrieved string is a NULL-terminated wide character string in a human-readable format. |
| [IOCTL_HID_READ_REPORT IOCTL](..\hidport\ni-hidport-ioctl-hid-read-report.md) | The IOCTL_HID_READ_REPORT request transfers an input report from a HIDClass device into the HID class driver's buffer. |
| [IOCTL_HID_SEND_IDLE_NOTIFICATION_REQUEST IOCTL](..\hidport\ni-hidport-ioctl-hid-send-idle-notification-request.md) | The IOCTL_HID_SEND_IDLE_NOTIFICATION_REQUEST control code is the IOCTL of the idle notification request IRP that HIDClass sends to HID mini drivers, such as HIDUSB, to inform the bus driver that the device is now idle. |
| [IOCTL_HID_SET_DRIVER_CONFIG IOCTL](..\hidclass\ni-hidclass-ioctl-hid-set-driver-config.md) | The IOCTL_HID_SET_DRIVER_CONFIG request sets the driver configuration. |
| [IOCTL_HID_SET_FEATURE IOCTL](..\hidclass\ni-hidclass-ioctl-hid-set-feature.md) | IOCTL_HID_SET_FEATURE sends a feature report to a HIDClass device. |
| [IOCTL_HID_SET_OUTPUT_REPORT IOCTL](..\hidclass\ni-hidclass-ioctl-hid-set-output-report.md) | The IOCTL_HID_SET_OUTPUT_REPORT request sends an output report to a top-level collection. |
| [IOCTL_HID_SET_POLL_FREQUENCY_MSEC IOCTL](..\hidclass\ni-hidclass-ioctl-hid-set-poll-frequency-msec.md) | The IOCTL_HID_SET_POLL_FREQUENCY_MSEC request sets the polling frequency, in milliseconds, for a top-level collection. |
| [IOCTL_HID_SET_S0_IDLE_TIMEOUT IOCTL](..\hidclass\ni-hidclass-ioctl-hid-set-s0-idle-timeout.md) | The IOCTL_HID_SET_S0_IDLE_TIMEOUT request is used by a client to inform the HID class driver about the client's preferred idle timeout value. |
| [IOCTL_HID_WRITE_REPORT IOCTL](..\hidport\ni-hidport-ioctl-hid-write-report.md) | The IOCTL_HID_WRITE_REPORT request sends a HID report to a HIDClass device. |
| [IOCTL_INTERNAL_I8042_CONTROLLER_WRITE_BUFFER IOCTL](..\ntdd8042\ni-ntdd8042-ioctl-internal-i8042-controller-write-buffer.md) | The IOCTL_INTERNAL_I8042_CONTROLLER_WRITE_BUFFER request is not supported. |
| [IOCTL_INTERNAL_I8042_HOOK_KEYBOARD IOCTL](..\ntdd8042\ni-ntdd8042-ioctl-internal-i8042-hook-keyboard.md) | The IOCTL_INTERNAL_I8042_HOOK_KEYBOARD request does the following |
| [IOCTL_INTERNAL_I8042_HOOK_MOUSE IOCTL](..\ntdd8042\ni-ntdd8042-ioctl-internal-i8042-hook-mouse.md) | The IOCTL_INTERNAL_I8042_HOOK_MOUSE request adds an ISR callback routine to the I8042prt mouse ISR. |
| [IOCTL_INTERNAL_I8042_KEYBOARD_START_INFORMATION IOCTL](..\ntdd8042\ni-ntdd8042-ioctl-internal-i8042-keyboard-start-information.md) | The IOCTL_INTERNAL_I8042_KEYBOARD_START_INFORMATION request passes a pointer to a keyboard interrupt object. |
| [IOCTL_INTERNAL_I8042_KEYBOARD_WRITE_BUFFER IOCTL](..\ntdd8042\ni-ntdd8042-ioctl-internal-i8042-keyboard-write-buffer.md) | The IOCTL_INTERNAL_I8042_KEYBOARD_WRITE_BUFFER request writes data to the i8042 port controller to control operation of a keyboard device. |
| [IOCTL_INTERNAL_I8042_MOUSE_START_INFORMATION IOCTL](..\ntdd8042\ni-ntdd8042-ioctl-internal-i8042-mouse-start-information.md) | The IOCTL_INTERNAL_I8042_MOUSE_START_INFORMATION request passes a pointer to a mouse interrupt object. |
| [IOCTL_INTERNAL_I8042_MOUSE_WRITE_BUFFER IOCTL](..\ntdd8042\ni-ntdd8042-ioctl-internal-i8042-mouse-write-buffer.md) | The IOCTL_INTERNAL_I8042_MOUSE_WRITE_BUFFER request writes data to the i8042 port controller to control operation of a mouse device. |
| [IOCTL_INTERNAL_KEYBOARD_CONNECT IOCTL](..\kbdmou\ni-kbdmou-ioctl-internal-keyboard-connect.md) | The IOCTL_INTERNAL_KEYBOARD_CONNECT request connects the Kbdclass service to the keyboard device. |
| [IOCTL_INTERNAL_KEYBOARD_DISCONNECT IOCTL](..\kbdmou\ni-kbdmou-ioctl-internal-keyboard-disconnect.md) | The IOCTL_INTERNAL_KEYBOARD_DISCONNECT request is completed with a status of STATUS_NOT_IMPLEMENTED. Note that a Plug and Play keyboard can be added or removed by the Plug and Play manager. |
| [IOCTL_INTERNAL_MOUSE_CONNECT IOCTL](..\kbdmou\ni-kbdmou-ioctl-internal-mouse-connect.md) | The IOCTL_INTERNAL_MOUSE_CONNECT request connects Mouclass service to a mouse device. |
| [IOCTL_INTERNAL_MOUSE_DISCONNECT IOCTL](..\kbdmou\ni-kbdmou-ioctl-internal-mouse-disconnect.md) | The IOCTL_INTERNAL_MOUSE_DISCONNECT request is completed by Moufiltr with an error status of STATUS_NOT_IMPLEMENTED. |
| [IOCTL_SET_NUM_DEVICE_INPUT_BUFFERS IOCTL](..\hidclass\ni-hidclass-ioctl-set-num-device-input-buffers.md) | The IOCTL_SET_NUM_DEVICE_INPUT_BUFFERS request sets the number of buffers for the input report queue of a top-level collection. |
| [IOCTL_UMDF_GET_PHYSICAL_DESCRIPTOR IOCTL](..\hidport\ni-hidport-ioctl-umdf-get-physical-descriptor.md) | The IOCTL_UMDF_GET_PHYSICAL_DESCRIPTOR control code obtains the physical descriptor of a HIDClass device. |
| [IOCTL_UMDF_HID_GET_FEATURE IOCTL](..\hidport\ni-hidport-ioctl-umdf-hid-get-feature.md) | The IOCTL_UMDF_HID_GET_FEATURE control code obtains a feature report from a HIDClass device. |
| [IOCTL_UMDF_HID_GET_INPUT_REPORT IOCTL](..\hidport\ni-hidport-ioctl-umdf-hid-get-input-report.md) | The IOCTL_UMDF_HID_GET_INPUT_REPORT control code returns an input report from a HIDClass device. |
| [IOCTL_UMDF_HID_SET_FEATURE IOCTL](..\hidport\ni-hidport-ioctl-umdf-hid-set-feature.md) | The IOCTL_UMDF_HID_GET_FEATURE control code sends a feature report to a HIDClass device. |
| [IOCTL_UMDF_HID_SET_OUTPUT_REPORT IOCTL](..\hidport\ni-hidport-ioctl-umdf-hid-set-output-report.md) | The IOCTL_UMDF_HID_SET_OUTPUT_REPORT control code sends an output report to a top-level collection. |
