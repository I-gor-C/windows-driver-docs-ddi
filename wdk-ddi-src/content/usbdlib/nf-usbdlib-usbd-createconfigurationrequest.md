---
UID: NF.usbdlib.USBD_CreateConfigurationRequest
title: USBD_CreateConfigurationRequest
author: windows-driver-content
description: The USBD_CreateConfigurationRequest routine has been deprecated. Use USBD_CreateConfigurationRequestEx instead.
old-location: buses\usbd_createconfigurationrequest.htm
old-project: usbref
ms.assetid: e1f397f6-2f33-4352-9bbc-2b2a49dcd067
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBD_CreateConfigurationRequest
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: usbdlib.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Deprecated. Use USBD_CreateConfigurationRequestEx instead.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBD_CreateConfigurationRequest
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

# USBD_CreateConfigurationRequest function



## -description
<p>The  <b>USBD_CreateConfigurationRequest</b> routine has been deprecated. Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff539029">USBD_CreateConfigurationRequestEx</a> instead.</p>


## -syntax

````
PURB USBD_CreateConfigurationRequest(
  _In_    PUSB_CONFIGURATION_DESCRIPTOR   ConfigurationDescriptor,
  _Inout_ PUSHORT                         Siz
    
);
````


## -parameters
<dl>

### -param <i>ConfigurationDescriptor</i> [in]

<dd>
<p>Pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff539241">USB_CONFIGURATION_DESCRIPTOR</a> structure that contains the configuration descriptor for the configuration to be selected.</p>
</dd>

### -param <i>Siz
    </i> [in, out]

<dd>
<p>Size of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a> structure.</p>
</dd>
</dl>

## -returns
<p><b>USBD_CreateConfigurationRequest</b> allocates a <a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a> structure, formats it for the URB_FUNCTION_SELECT_CONFIGURATION request (select-configuration request), and returns a pointer to the <b>URB</b>. </p>

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
<p>Deprecated. Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff539029">USBD_CreateConfigurationRequestEx</a> instead.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539029">USBD_CreateConfigurationRequestEx</a>
</dt>
<dt><a href="usb_reference.htm#client">USB device driver programming reference</a></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBD_CreateConfigurationRequest routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
