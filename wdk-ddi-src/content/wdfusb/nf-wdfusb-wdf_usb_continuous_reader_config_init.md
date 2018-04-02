---
UID: NF:wdfusb.WDF_USB_CONTINUOUS_READER_CONFIG_INIT
title: WDF_USB_CONTINUOUS_READER_CONFIG_INIT function
author: windows-driver-content
description: The WDF_USB_CONTINUOUS_READER_CONFIG_INIT function initializes a WDF_USB_CONTINUOUS_READER_CONFIG structure.
old-location: wdf\wdf_usb_continuous_reader_config_init.htm
old-project: wdf
ms.assetid: d9bf6c47-b7ce-413d-8871-4d9d68e27715
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: DFUsbRef_a179cacd-e450-4a53-93e7-4eb3a59fc605.xml, WDF_USB_CONTINUOUS_READER_CONFIG_INIT, WDF_USB_CONTINUOUS_READER_CONFIG_INIT function, kmdf.wdf_usb_continuous_reader_config_init, wdf.wdf_usb_continuous_reader_config_init, wdfusb/WDF_USB_CONTINUOUS_READER_CONFIG_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	wdfusb.h
api_name:
-	WDF_USB_CONTINUOUS_READER_CONFIG_INIT
product:
- Windows
targetos: Windows
req.typenames: WDF_USB_REQUEST_TYPE, *PWDF_USB_REQUEST_TYPE
req.product: Windows 10 or later.
---


# WDF_USB_CONTINUOUS_READER_CONFIG_INIT function
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_USB_CONTINUOUS_READER_CONFIG_INIT</b> function initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552561">WDF_USB_CONTINUOUS_READER_CONFIG</a> structure.

## Syntax

```
void WDF_USB_CONTINUOUS_READER_CONFIG_INIT(
  PWDF_USB_CONTINUOUS_READER_CONFIG     Config,
  PFN_WDF_USB_READER_COMPLETION_ROUTINE EvtUsbTargetPipeReadComplete,
  WDFCONTEXT                            EvtUsbTargetPipeReadCompleteContext,
  size_t                                TransferLength
);
```

## Parameters

`Config`

A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552561">WDF_USB_CONTINUOUS_READER_CONFIG</a> structure.

`EvtUsbTargetPipeReadComplete`

A pointer to the driver's <a href="https://msdn.microsoft.com/da762d78-6d73-4ab9-83a8-297c6f48855b">EvtUsbTargetPipeReadComplete</a> callback function.

`EvtUsbTargetPipeReadCompleteContext`

An untyped pointer to driver-defined context information that the framework passes to the driver's <a href="https://msdn.microsoft.com/da762d78-6d73-4ab9-83a8-297c6f48855b">EvtUsbTargetPipeReadComplete</a> callback function.

`TransferLength`

The maximum length, in bytes, of data that can be received from the device.


## Return Value

None

## Remarks

The <b>WDF_USB_CONTINUOUS_READER_CONFIG_INIT</b> function zeros the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff552561">WDF_USB_CONTINUOUS_READER_CONFIG</a> structure and sets the structure's <b>Size</b> member. It also sets the structure's <b>EvtUsbTargetPipeReadComplete</b>, <b>EvtUsbTargetPipeReadCompleteContext</b>, and <b>TransferLength</b> members to the specified values.

  Note that <b>WDF_USB_CONTINUOUS_READER_CONFIG_INIT</b> does <i>not</i> set the structure's <b>EvtUsbTargetPipeReadersFailed</b> member.

 After calling <b>WDF_USB_CONTINUOUS_READER_CONFIG_INIT</b>, the driver can optionally add a <b>EvtUsbTargetPipeReadersFailed</b> pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552561">WDF_USB_CONTINUOUS_READER_CONFIG</a> structure.

For a code example that uses <b>WDF_USB_CONTINUOUS_READER_CONFIG_INIT</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff551130">WdfUsbTargetPipeConfigContinuousReader</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Universal |
| **Minimum KMDF version** | 1.0 |
| **Minimum UMDF version** | 2.0 |
| **Header** | wdfusb.h (include Wdfusb.h) |

## See Also

<a href="https://msdn.microsoft.com/da762d78-6d73-4ab9-83a8-297c6f48855b">EvtUsbTargetPipeReadComplete</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff552561">WDF_USB_CONTINUOUS_READER_CONFIG</a>