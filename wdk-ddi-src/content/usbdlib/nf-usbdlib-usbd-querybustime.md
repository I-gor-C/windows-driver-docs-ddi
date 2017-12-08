---
UID: NF.usbdlib.USBD_QueryBusTime
title: USBD_QueryBusTime
author: windows-driver-content
description: The USBD_QueryBusTime routine has been deprecated in Windows XP and later operating systems. Do not use.
old-location: buses\usbd_querybustime.htm
old-project: usbref
ms.assetid: ae59daf6-da7b-4b04-bb5c-dfd353b937a0
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBD_QueryBusTime
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: usbdlib.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Deprecated.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBD_QueryBusTime
req.alt-loc: Usbd.lib,Usbd.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Usbd.lib
req.dll: 
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# USBD_QueryBusTime function



## -description
<p>The <b>USBD_QueryBusTime</b> routine has been deprecated in Windows XP and later operating systems. Do not use. </p>
<p>See URB_FUNCTION_GET_CURRENT_FRAME_NUMBER for equivalent functionality that is supported on all versions of Windows.</p>


## -syntax

````
void USBD_QueryBusTime(
  _In_  PDEVICE_OBJECT RootHubPdo,
  _Out_ PULONG         CurrentFrame
);
````


## -parameters
<dl>

### -param RootHubPdo [in]

<dd>
<p>Obsolete.

</p>
</dd>

### -param CurrentFrame [out]

<dd>
<p>Obsolete.

</p>
</dd>
</dl>

## -returns
<p>This routine does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Deprecated.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbdlib.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Usbd.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses._urb_get_current_frame_number">URB_GET_CURRENT_FRAME_NUMBER</a>
</dt>
<dt><a href="usb_reference.htm#client">USB device driver programming reference</a></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBD_QueryBusTime routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
