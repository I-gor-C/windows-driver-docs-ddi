---
UID: NC.usbfnattach.USBFN_GET_ATTACH_ACTION
title: USBFN_GET_ATTACH_ACTION
author: windows-driver-content
description: The filter driver's implementation that gets invoked when charger is attached to the port.
old-location: buses\usbfn_get_attach_action.htm
old-project: usbref
ms.assetid: D951D5A0-3A93-4B67-B25A-31EE61C0A065
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBD_INTERFACE_LIST_ENTRY, USBD_INTERFACE_LIST_ENTRY, *PUSBD_INTERFACE_LIST_ENTRY
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
req.alt-api: PFN_USBFN_GET_ATTACH_ACTION
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
req.iface: 
req.product: Windows 10 or later.
---

# USBFN_GET_ATTACH_ACTION callback



## -description
<p>The filter driver's implementation that gets invoked when charger is attached to the port.</p>


## -prototype

````
USBFN_GET_ATTACH_ACTION UsbFnGetAttachAction;

NTSTATUS UsbFnGetAttachAction(
  _In_  PVOID            Context,
  _Out_ PUSBFN_ON_ATTACH OnAttach
)
{ ... }

typedef USBFN_GET_ATTACH_ACTION PFN_USBFN_GET_ATTACH_ACTION;
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>    A pointer to a driver-defined context.</p>
</dd>

### -param <i>OnAttach</i> [out]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/mt188002">USBFN_ON_ATTACH</a> structure that the driver populates with the type of attach and port. </p>
</dd>
</dl>

## -returns
<p>If the operation is successful, the callback function must return STATUS_SUCCESS, or another status value for which NT_SUCCESS(status) equals TRUE. Otherwise it must return a status value for which NT_SUCCESS(status) equals FALSE.</p>

## -remarks
<p>To support attach and detatch detection, the USB lower filter driver must publish its support. During the publishing process, the driver also registers its implementation of this  callback function. For more information, see <a href="buses.usb_filter_driver_for_proprietary_charging">USB filter driver for supporting proprietary chargers</a>.</p>

<p>To support attach and detatch detection, the USB lower filter driver must publish its support. During the publishing process, the driver also registers its implementation of this  callback function. For more information, see <a href="buses.usb_filter_driver_for_proprietary_charging">USB filter driver for supporting proprietary chargers</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbfnattach.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.usb_filter_driver_for_proprietary_charging">USB filter driver for supporting proprietary chargers</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBFN_GET_ATTACH_ACTION callback function%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
