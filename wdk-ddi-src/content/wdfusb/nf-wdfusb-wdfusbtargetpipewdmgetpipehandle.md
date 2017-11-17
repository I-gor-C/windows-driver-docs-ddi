---
UID: NF.wdfusb.WdfUsbTargetPipeWdmGetPipeHandle
title: WdfUsbTargetPipeWdmGetPipeHandle
author: windows-driver-content
description: The WdfUsbTargetPipeWdmGetPipeHandle method returns the USBD_PIPE_HANDLE-typed handle that is associated with a specified framework pipe object.
old-location: wdf\wdfusbtargetpipewdmgetpipehandle.htm
ms.assetid: d24577e3-3124-4ce7-a6ea-bed75ff18a1e
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfUsbTargetPipeWdmGetPipeHandle
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2, UsbKmdfIrql, UsbKmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: WdfUsbTargetPipeWdmGetPipeHandle
req.iface: 
req.product: Windows 10 or later.
---

# WdfUsbTargetPipeWdmGetPipeHandle function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfUsbTargetPipeWdmGetPipeHandle</b> method returns the USBD_PIPE_HANDLE-typed handle that is associated with a specified framework pipe object. </p>


## -syntax

````
USBD_PIPE_HANDLE WdfUsbTargetPipeWdmGetPipeHandle(
  _In_ WDFUSBPIPE UsbPipe
);
````


## -parameters
<dl>

### -param <i>UsbPipe</i> [in]

<dd>
<p>A handle to a framework pipe object that was obtained by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff550057">WdfUsbInterfaceGetConfiguredPipe</a>.</p>
</dd>
</dl>

## -returns
<p><b>WdfUsbTargetPipeWdmGetPipeHandle</b> returns a USBD_PIPE_HANDLE-typed handle. </p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>A framework-based driver needs to obtain a USBD_PIPE_HANDLE-typed handle only if it creates a <a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a> that requires a pipe handle.</p>

<p>The driver can call the <b>WdfUsbTargetPipeWdmGetPipeHandle</b> method after it has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff550101">WdfUsbTargetDeviceSelectConfig</a>. The USBD_PIPE_HANDLE-typed handle that <b>WdfUsbTargetPipeWdmGetPipeHandle</b> returns is valid until the driver calls <b>WdfUsbTargetDeviceSelectConfig</b> again, the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff550073">WdfUsbInterfaceSelectSetting</a>, or the framework pipe object is deleted. If the driver provides an <a href="https://msdn.microsoft.com/aba2efca-7d1f-4594-af65-13356f0e3f8b">EvtCleanupCallback</a> function for the framework pipe object, and if the object is deleted before the driver calls <b>WdfUsbTargetDeviceSelectConfig</b> again or calls <b>WdfUsbInterfaceSelectSetting</b>, the handle is valid until the object's <i>EvtCleanupCallback</i> function returns.</p>

<p>For more information about the <b>WdfUsbTargetPipeWdmGetPipeHandle</b> method and USB I/O targets, see <a href="wdf.usb_i_o_targets">USB I/O Targets</a>.</p>

<p>The following code example obtains the USBD_PIPE_HANDLE-typed handle for a specified pipe.</p>

<p>A framework-based driver needs to obtain a USBD_PIPE_HANDLE-typed handle only if it creates a <a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a> that requires a pipe handle.</p>

<p>The driver can call the <b>WdfUsbTargetPipeWdmGetPipeHandle</b> method after it has called <a href="https://msdn.microsoft.com/library/windows/hardware/ff550101">WdfUsbTargetDeviceSelectConfig</a>. The USBD_PIPE_HANDLE-typed handle that <b>WdfUsbTargetPipeWdmGetPipeHandle</b> returns is valid until the driver calls <b>WdfUsbTargetDeviceSelectConfig</b> again, the driver calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff550073">WdfUsbInterfaceSelectSetting</a>, or the framework pipe object is deleted. If the driver provides an <a href="https://msdn.microsoft.com/aba2efca-7d1f-4594-af65-13356f0e3f8b">EvtCleanupCallback</a> function for the framework pipe object, and if the object is deleted before the driver calls <b>WdfUsbTargetDeviceSelectConfig</b> again or calls <b>WdfUsbInterfaceSelectSetting</b>, the handle is valid until the object's <i>EvtCleanupCallback</i> function returns.</p>

<p>For more information about the <b>WdfUsbTargetPipeWdmGetPipeHandle</b> method and USB I/O targets, see <a href="wdf.usb_i_o_targets">USB I/O Targets</a>.</p>

<p>The following code example obtains the USBD_PIPE_HANDLE-typed handle for a specified pipe.</p>

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
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550057">WdfUsbInterfaceGetConfiguredPipe</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550101">WdfUsbTargetDeviceSelectConfig</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfUsbTargetPipeWdmGetPipeHandle method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
