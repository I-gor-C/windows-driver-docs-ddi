---
UID: NF.wdfusb.WdfUsbInterfaceGetEndpointInformation
title: WdfUsbInterfaceGetEndpointInformation
author: windows-driver-content
description: The WdfUsbInterfaceGetEndpointInformation method retrieves information about a specified USB device endpoint and its associated pipe.
old-location: wdf\wdfusbinterfacegetendpointinformation.htm
old-project: wdf
ms.assetid: c9e204db-f8fc-42e7-9a1b-f08099147ce7
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfUsbInterfaceGetEndpointInformation
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
req.alt-api: WdfUsbInterfaceGetEndpointInformation
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2, UsbKmdfIrql, UsbKmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfUsbInterfaceGetEndpointInformation function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfUsbInterfaceGetEndpointInformation</b> method retrieves information about a specified USB device endpoint and its associated pipe.</p>


## -syntax

````
VOID WdfUsbInterfaceGetEndpointInformation(
  _In_  WDFUSBINTERFACE           UsbInterface,
  _In_  UCHAR                     SettingIndex,
  _In_  UCHAR                     EndpointIndex,
  _Out_ PWDF_USB_PIPE_INFORMATION EndpointInfo
);
````


## -parameters
<dl>

### -param <i>UsbInterface</i> [in]

<dd>
<p>A handle to a USB interface object that was obtained by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff550092">WdfUsbTargetDeviceGetInterface</a>. </p>
</dd>

### -param <i>SettingIndex</i> [in]

<dd>
<p>An index value that identifies an alternate setting for the interface. For more information about alternate settings, see the USB specification.</p>
</dd>

### -param <i>EndpointIndex</i> [in]

<dd>
<p>An index value that identifies an endpoint that is associated with the specified alternate setting of the specified interface. (This index value is not the endpoint address.)</p>
</dd>

### -param <i>EndpointInfo</i> [out]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff553037">WDF_USB_PIPE_INFORMATION</a> structure that the framework fills in.</p>
</dd>
</dl>

## -returns
<p>None.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>For more information about the <b>WdfUsbInterfaceGetEndpointInformation</b> method and USB I/O targets, see <a href="wdf.usb_i_o_targets">USB I/O Targets</a>.</p>

<p>The following code example obtains the number of endpoints that a USB interface supports and then calls <b>WdfUsbInterfaceGetEndpointInformation</b> for each endpoint.</p>

<p>For more information about the <b>WdfUsbInterfaceGetEndpointInformation</b> method and USB I/O targets, see <a href="wdf.usb_i_o_targets">USB I/O Targets</a>.</p>

<p>The following code example obtains the number of endpoints that a USB interface supports and then calls <b>WdfUsbInterfaceGetEndpointInformation</b> for each endpoint.</p>

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
<dt>Wdfusb.h (include Wdfusb.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff554042">UsbKmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh995019">UsbKmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553037">WDF_USB_PIPE_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550068">WdfUsbInterfaceGetNumEndpoints</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550092">WdfUsbTargetDeviceGetInterface</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfUsbInterfaceGetEndpointInformation method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
