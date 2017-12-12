---
UID: NC.usbfnattach.USBFN_GET_ATTACH_ACTION_ABORT
title: USBFN_GET_ATTACH_ACTION_ABORT
author: windows-driver-content
description: The filter driver's implementation to abort an attach-detect operation.
old-location: buses\usbfn_get_attach_action_abort.htm
old-project: usbref
ms.assetid: 0A44551A-F379-442D-99E9-87231F5FB178
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _USBD_INTERFACE_LIST_ENTRY, *PUSBD_INTERFACE_LIST_ENTRY, USBD_INTERFACE_LIST_ENTRY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: usbfnattach.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: USBFN_SET_DEVICE_STATE
req.alt-loc: usbfnattach.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# USBFN_GET_ATTACH_ACTION_ABORT callback



## -description
The filter driver's implementation to abort an attach-detect operation.



## -prototype

````
USBFN_GET_ATTACH_ACTION_ABORT UsbFnGetAttachActionAbort;

NTSTATUS UsbFnGetAttachActionAbort(
  _In_ PVOID Context
)
{ ... }

typedef PFN_USBFN_SET_DEVICE_STATE USBFN_SET_DEVICE_STATE;
````


## -parameters

### -param Context [in]

    A pointer to a driver-defined context.


## -returns
If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it must return a status value for which NT_SUCCESS(status) equals FALSE.


## -remarks
To support attach and detatch detection, the USB lower filter driver must publish its support. During the publishing process, the driver also registers its implementation of this  callback function. For more information, see <a href="buses.usb_filter_driver_for_proprietary_charging">USB filter driver for supporting proprietary chargers</a>.


## -requirements
<table>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Usbfnattach.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.usb_filter_driver_for_proprietary_charging">USB filter driver for supporting proprietary chargers</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBFN_GET_ATTACH_ACTION_ABORT callback function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

