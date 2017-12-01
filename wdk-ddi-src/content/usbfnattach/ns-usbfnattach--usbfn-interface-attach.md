---
UID: NS.usbfnattach._USBFN_INTERFACE_ATTACH
title: USBFN_INTERFACE_ATTACH
author: windows-driver-content
description: Stores pointers to driver-implemented callback functions for handling attach and detach operations.
old-location: buses\usbfn_interface_attach.htm
old-project: usbref
ms.assetid: C7D7935C-0536-43E6-8924-1DC13B258007
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBFN_INTERFACE_ATTACH, USBFN_INTERFACE_ATTACH, *PUSBFN_INTERFACE_ATTACH
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbfnattach.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBFN_INTERFACE_ATTACH
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

# USBFN_INTERFACE_ATTACH structure



## -description
<p>Stores pointers to driver-implemented callback functions for handling attach and detach operations.</p>


## -syntax

````
typedef struct _USBFN_INTERFACE_ATTACH {
  INTERFACE                   InterfaceHeader;
  PFN_USBFN_GET_ATTACH_ACTION GetAttachAction;
  PFN_USBFN_GET_ATTACH_ACTION GetAttachActionAbortOperation;
  PFN_USBFN_SET_DEVICE_STATE  SetDeviceState;
} USBFN_INTERFACE_ATTACH, *PUSBFN_INTERFACE_ATTACH;
````


## -struct-fields
<dl>

### -field <b>InterfaceHeader</b>

<dd>
<p>The interface version number.</p>
</dd>

### -field <b>GetAttachAction</b>

<dd>
<p>A pointer to the driver's implementation of the <a href="buses.usbfn_get_attach_action">USBFN_GET_ATTACH_ACTION</a> callback function.</p>
</dd>

### -field <b>GetAttachActionAbortOperation</b>

<dd>
<p>A pointer to the driver's implementation of the <a href="buses.usbfn_get_attach_action_abort">USBFN_GET_ATTACH_ACTION_ABORT</a> callback function.</p>
</dd>

### -field <b>SetDeviceState</b>

<dd>
<p>A pointer to the driver's implementation of the <a href="buses.usbfn_set_device_state">USBFN_SET_DEVICE_STATE</a> callback function.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="buses.usb_filter_driver_for_proprietary_charging">USB filter driver for supporting proprietary chargers</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBFN_INTERFACE_ATTACH structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
