---
UID: NA:ntddsd
ms.assetid: 580360eb-94b6-3837-bcf3-d877646901ac
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# ntddsd.h header



ntddsd.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [PSDBUS_ACKNOWLEDGE_INT_ROUTINE](nc-ntddsd-psdbus_acknowledge_int_routine.md) | The PSDBUS_ACKNOWLEDGE_INT_ROUTINE prototype declares the routine that a Secure Digital (SD) device driver must call to acknowledge to the bus driver that it has finished processing the interrupt. |
| [PSDBUS_INITIALIZE_INTERFACE_ROUTINE](nc-ntddsd-psdbus_initialize_interface_routine.md) | The PSDBUS_INITIALIZE_INTERFACE_ROUTINE prototype declares the routine that a Secure Digital (SD) device driver uses to initialize an interface instance that it creates with the SdBusOpenInterface routine. |
| [SDBUS_CALLBACK_ROUTINE](nc-ntddsd-sdbus_callback_routine.md) | The PSDBUS_CALLBACK_ROUTINE prototype declares the Secure Digital (SD) driver callback routine that the SD bus driver uses to report device interrupts to the driver. |
| [SdBusOpenInterface](nf-ntddsd-sdbusopeninterface.md) | The SdBusOpenInterface routine obtains an interface from the Secure Digital (SD) bus driver. |
| [SdBusSubmitRequest](nf-ntddsd-sdbussubmitrequest.md) | The SdBusSubmitRequest routine sends a synchronous Secure Digital (SD) request to the bus driver. |
| [SdBusSubmitRequestAsync](nf-ntddsd-sdbussubmitrequestasync.md) | The SdBusSubmitRequestAsync routine sends an asynchronous Secure Digital (SD) request to the bus driver interface. |




## Enumerations
| Title | Description |
| ---- |:---- |
| [SD_REQUEST_FUNCTION](ne-ntddsd-sd_request_function.md) | The SD_REQUEST_FUNCTION enumeration indicates the type of request packet that a Secure Digital (SD) card driver sends to the bus driver. |
| [SDBUS_PROPERTY](ne-ntddsd-sdbus_property.md) | The SDBUS_PROPERTY enumeration lists the properties of a Secure Digital (SD) card that an SD device driver can set with an SD request. |
| [SDPROP_MEDIA_STATE](ne-ntddsd-sdprop_media_state.md) | The SDPROP_MEDIA_STATE enumeration lists the values associated with the media states property. |