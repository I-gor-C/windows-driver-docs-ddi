---
UID: NF.wdfusb.WdfUsbTargetDeviceCreateIsochUrb
title: WdfUsbTargetDeviceCreateIsochUrb
author: windows-driver-content
description: The WdfUsbTargetDeviceCreateIsochUrb method allocates an isochronous USB request block (URB).
old-location: wdf\wdfusbtargetdevicecreateisochurb.htm
ms.assetid: 2D25A276-A367-4E59-9CA0-4F480675DD77
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Universal
req.target-min-winverclnt: Windows Vista
req.target-min-winversvr: 
req.kmdf-ver: 1.11
req.umdf-ver: 
req.alt-api: WdfUsbTargetDeviceCreateIsochUrb
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: WdfUsbTargetDeviceCreateIsochUrb
req.iface: 
req.product: Windows 10 or later.
---

# WdfUsbTargetDeviceCreateIsochUrb function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>
   The 
  <b>WdfUsbTargetDeviceCreateIsochUrb</b> method allocates an isochronous USB request block (URB).</p>


## -syntax

````
NTSTATUS WdfUsbTargetDeviceCreateIsochUrb(
  _In_      WDFUSBDEVICE           UsbDevice,
  _In_opt_  PWDF_OBJECT_ATTRIBUTES Attributes,
  _In_      ULONG                  NumberOfIsochPackets,
  _Out_     WDFMEMORY              *UrbMemory,
  _Out_opt_ PURB                   *Urb
);
````


## -parameters
<dl>

### -param <i>UsbDevice</i> [in]

<dd>
<p>A handle to a USB device object that was obtained from a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh439428">WdfUsbTargetDeviceCreateWithParameters</a>.</p>
</dd>

### -param <i>Attributes</i> [in, optional]

<dd>
<p>A pointer to a caller-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure that contains attributes for the new memory object.   If the driver provides this parameter, the structure's <b>ParentObject</b> member must be a USB device object (WDFUSBDEVICE) or a request object (WDFREQUEST) created by the framework, or any object whose chain of parents leads to one of these types. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.</p>
</dd>

### -param <i>NumberOfIsochPackets</i> [in]

<dd>
<p>Specifies the number of isochronous packets for which the system allocates memory in the URB.</p>
</dd>

### -param <i>UrbMemory</i> [out]

<dd>
<p>A pointer to a WDFMEMORY-typed location that receives a handle to a framework memory object.</p>
</dd>

### -param <i>Urb</i> [out, optional]

<dd>
<p>A pointer to an URB structure that receives the address of the new isochronous URB. The framework initializes contents of the URB structure to zero. This parameter is optional and can be NULL.</p>
</dd>
</dl>

## -returns
<p><b>WdfUsbTargetDeviceCreateIsochUrb</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method can return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was detected.</p><dl>
<dt><b>STATUS_INVALID_DEVICE_STATE</b></dt>
</dl><p>The driver did not specify a client contract version when it called <a href="https://msdn.microsoft.com/library/windows/hardware/hh406507">WDF_USB_DEVICE_CREATE_CONFIG_INIT</a>.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Insufficient memory was available.</p>

<p> </p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>Before calling <b>WdfUsbTargetDeviceCreateIsochUrb</b>, a driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/hh439428">WdfUsbTargetDeviceCreateWithParameters</a>. If successful, <b>WdfUsbTargetDeviceCreateIsochUrb</b> returns a handle to a framework memory object that describes the newly allocated isochronous URB.</p>

<p>A driver can call <b>WdfUsbTargetDeviceCreateIsochUrb</b> to allocate a URB structure before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff550088">WdfUsbTargetDeviceFormatRequestForUrb</a>.</p>

<p>Typically, a driver calls <b>WdfUsbTargetDeviceCreateIsochUrb</b> from within a <a href="wdf.request_handlers">request handler</a>.</p>

<p>The memory object and its buffer are deleted when the parent object is deleted. A driver can also delete a memory object and its buffer by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548734">WdfObjectDelete</a>.</p>

<p>For related information, see the Remarks section of <a href="https://msdn.microsoft.com/library/windows/hardware/hh439423">WdfUsbTargetDeviceCreateUrb</a>.</p>

<p>The following code example is based on the PerformIsochTransfer routine in the Isorwr sample driver. The example calls <b>WdfUsbTargetDeviceCreateIsochUrb</b> to allocate an isochronous USB request block. The example determines the number  of bytes required to hold the isochronous transfer request, and then manually configures the URB header and the isochronous packets in the URB.  At this point, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551139">WdfUsbTargetPipeFormatRequestForUrb</a>, as shown in the example in  <a href="https://msdn.microsoft.com/library/windows/hardware/hh439423">WdfUsbTargetDeviceCreateUrb</a>.</p>

<p>Before calling <b>WdfUsbTargetDeviceCreateIsochUrb</b>, a driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/hh439428">WdfUsbTargetDeviceCreateWithParameters</a>. If successful, <b>WdfUsbTargetDeviceCreateIsochUrb</b> returns a handle to a framework memory object that describes the newly allocated isochronous URB.</p>

<p>A driver can call <b>WdfUsbTargetDeviceCreateIsochUrb</b> to allocate a URB structure before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff550088">WdfUsbTargetDeviceFormatRequestForUrb</a>.</p>

<p>Typically, a driver calls <b>WdfUsbTargetDeviceCreateIsochUrb</b> from within a <a href="wdf.request_handlers">request handler</a>.</p>

<p>The memory object and its buffer are deleted when the parent object is deleted. A driver can also delete a memory object and its buffer by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548734">WdfObjectDelete</a>.</p>

<p>For related information, see the Remarks section of <a href="https://msdn.microsoft.com/library/windows/hardware/hh439423">WdfUsbTargetDeviceCreateUrb</a>.</p>

<p>The following code example is based on the PerformIsochTransfer routine in the Isorwr sample driver. The example calls <b>WdfUsbTargetDeviceCreateIsochUrb</b> to allocate an isochronous USB request block. The example determines the number  of bytes required to hold the isochronous transfer request, and then manually configures the URB header and the isochronous packets in the URB.  At this point, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551139">WdfUsbTargetPipeFormatRequestForUrb</a>, as shown in the example in  <a href="https://msdn.microsoft.com/library/windows/hardware/hh439423">WdfUsbTargetDeviceCreateUrb</a>.</p>

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
<p>Minimum support</p>
</th>
<td width="70%">
<p>Windows Vista</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.11</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439423">WdfUsbTargetDeviceCreateUrb</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439428">WdfUsbTargetDeviceCreateWithParameters</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfUsbTargetDeviceCreateIsochUrb method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
