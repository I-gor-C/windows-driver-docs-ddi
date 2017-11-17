# Declarations in the hidsdi header
This header Hidsdi contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [HidD_GetManufacturerString function](nf-hidsdi-hidd-getmanufacturerstring.md) | The HidD_GetManufacturerString routine returns a top-level collection's embedded string that identifies the manufacturer. |
| [HidD_GetSerialNumberString function](nf-hidsdi-hidd-getserialnumberstring.md) | The HidD_GetSerialNumberString routine returns the embedded string of a top-level collection that identifies the serial number of the collection's physical device. |
| [HidD_GetMsGenreDescriptor function](nf-hidsdi-hidd-getmsgenredescriptor.md) | TBD |
| [HidD_GetNumInputBuffers function](nf-hidsdi-hidd-getnuminputbuffers.md) | The HidD_GetNumInputBuffers routine returns the current size, in number of reports, of the ring buffer that the HID class driver uses to queue input reports from a specified top-level collection. |
| [HidD_GetAttributes function](nf-hidsdi-hidd-getattributes.md) | The HidD_GetAttributes routine returns the attributes of a specified top-level collection. |
| [HidD_GetConfiguration function](nf-hidsdi-hidd-getconfiguration.md) | TBD |
| [HidD_GetHidGuid function](nf-hidsdi-hidd-gethidguid.md) | The HidD_GetHidGuid routine returns the device interfaceGUID for HIDClass devices. |
| [HidD_GetInputReport function](nf-hidsdi-hidd-getinputreport.md) | The HidD_GetInputReport routine returns an input reports from a top-level collection. |
| [HidD_FreePreparsedData function](nf-hidsdi-hidd-freepreparseddata.md) | The HidD_FreePreparsedData routine releases the resources that the HID class driver allocated to hold a top-level collection's preparsed data. |
| [HidD_SetConfiguration function](nf-hidsdi-hidd-setconfiguration.md) | TBD |
| [HidD_GetProductString function](nf-hidsdi-hidd-getproductstring.md) | The HidD_GetProductString routine returns the embedded string of a top-level collection that identifies the manufacturer's product. |
| [HidD_GetFeature function](nf-hidsdi-hidd-getfeature.md) | The HidD_GetFeature routine returns a feature report from a specified top-level collection. |
| [HidD_SetFeature function](nf-hidsdi-hidd-setfeature.md) | The HidD_SetFeature routine sends a feature report to a top-level collection. |
| [HidD_SetOutputReport function](nf-hidsdi-hidd-setoutputreport.md) | The HidD_SetOutputReport routine sends an output report to a top-level collection. |
| [HidD_FlushQueue function](nf-hidsdi-hidd-flushqueue.md) | The HidD_FlushQueue routine deletes all pending input reports in a top-level collection's input queue. |
| [HidD_GetIndexedString function](nf-hidsdi-hidd-getindexedstring.md) | The HidD_GetIndexedString routine returns a specified embedded string from a top-level collection. |
| [HidD_GetPreparsedData function](nf-hidsdi-hidd-getpreparseddata.md) | The HidD_GetPreparsedData routine returns a top-level collection's preparsed data. |
| [HidD_SetNumInputBuffers function](nf-hidsdi-hidd-setnuminputbuffers.md) | The HidD_SetNumInputBuffers routine sets the maximum number of input reports that the HID class driver ring buffer can hold for a specified top-level collection. |
| [HidD_GetPhysicalDescriptor function](nf-hidsdi-hidd-getphysicaldescriptor.md) | The HidD_GetPhysicalDescriptor routine returns the embedded string of a top-level collection that identifies the collection's physical device. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [HIDD_CONFIGURATION structure](ns-hidsdi--hidd-configuration.md) | TBD |
| [HIDD_ATTRIBUTES structure](ns-hidsdi--hidd-attributes.md) | The HIDD_ATTRIBUTES structure contains vendor information about a HIDClass device. |

This header is used in these topics:

- [hid](..content/_hid)
