---
UID: NF.wdfusb.WdfUsbTargetDeviceQueryString
title: WdfUsbTargetDeviceQueryString
author: windows-driver-content
description: The WdfUsbTargetDeviceQueryString method retrieves the Unicode string that is associated with a specified USB device and descriptor index value.
old-location: wdf\wdfusbtargetdevicequerystring.htm
old-project: wdf
ms.assetid: e7b25a47-e197-4670-9907-409d5aeb5462
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfUsbTargetDeviceQueryString
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
req.alt-api: WdfUsbTargetDeviceQueryString
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
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfUsbTargetDeviceQueryString function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfUsbTargetDeviceQueryString</b> method retrieves the Unicode string that is associated with a specified USB device and descriptor index value.</p>


## -syntax

````
NTSTATUS WdfUsbTargetDeviceQueryString(
  _In_      WDFUSBDEVICE              UsbDevice,
  _In_opt_  WDFREQUEST                Request,
  _In_opt_  PWDF_REQUEST_SEND_OPTIONS RequestOptions,
  _Out_opt_ PUSHORT                   String,
  _Inout_   PUSHORT                   NumCharacters,
  _In_      UCHAR                     StringIndex,
  _In_opt_  USHORT                    LangID
);
````


## -parameters
<dl>

### -param <i>UsbDevice</i> [in]

<dd>
<p>A handle to a USB device object that was obtained from a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh439428">WdfUsbTargetDeviceCreateWithParameters</a>.</p>
</dd>

### -param <i>Request</i> [in, optional]

<dd>
<p>A handle to a framework request object. This parameter is optional and can be <b>NULL</b>. For more information, see the following Remarks section. </p>
</dd>

### -param <i>RequestOptions</i> [in, optional]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a> structure that specifies options for the request. This pointer is optional and can be <b>NULL</b>. For more information, see the following Remarks section. </p>
</dd>

### -param <i>String</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated buffer that receives the requested Unicode string. The string is NULL-terminated only if the device supplies a NULL-terminated string. If this pointer is <b>NULL</b>, <b>WdfUsbTargetDeviceQueryString</b> returns the required buffer size (that is, the required number of Unicode characters) in the location that <i>NumCharacters</i> points to.</p>
</dd>

### -param <i>NumCharacters</i> [in, out]

<dd>
<p>A pointer to a caller-allocated variable. The caller supplies the number of Unicode characters that the buffer can hold. When <b>WdfUsbTargetDeviceQueryString</b> returns, the variable receives the number of characters (including the NULL terminator, if supplied) that are in the Unicode string that the <i>String</i> buffer receives. </p>
</dd>

### -param <i>StringIndex</i> [in]

<dd>
<p>An index value that identifies the Unicode string. This index value is obtained from a <a href="https://msdn.microsoft.com/library/windows/hardware/ff539280">USB_DEVICE_DESCRIPTOR</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff539241">USB_CONFIGURATION_DESCRIPTOR</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff540065">USB_INTERFACE_DESCRIPTOR</a> structure.</p>
</dd>

### -param <i>LangID</i> [in, optional]

<dd>
<p>A language identifier. The Unicode string will be retrieved for the language that this identifier specifies. For information about obtaining a device's supported language identifiers, see the USB specification. </p>
</dd>
</dl>

## -returns
<p><b>WdfUsbTargetDeviceQueryString</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method can return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was detected.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>A memory buffer could not be allocated.</p><dl>
<dt><b>STATUS_DEVICE_DATA_ERROR</b></dt>
</dl><p>The USB device returned an invalid descriptor.</p><dl>
<dt><b>STATUS_BUFFER_OVERFLOW</b></dt>
</dl><p>The supplied buffer was too small.</p>

<p> </p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>Drivers should call <b>WdfUsbTargetDeviceQueryString</b> twice, by using the following steps:</p>

<p>Set the <i>String</i> pointer to <b>NULL</b>, so that <b>WdfUsbTargetDeviceQueryString</b> will return the required buffer size in the address that the <i>NumCharacters</i> parameter points to.</p>

<p> Allocate buffer space to hold the number of Unicode characters that are in the requested string. For example, a driver might call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544520">ExAllocatePoolWithTag</a> to allocate a buffer, or it might call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548706">WdfMemoryCreate</a> to create a framework memory object.</p>

<p>Call <b>WdfUsbTargetDeviceQueryString</b> again, setting the <i>String</i> value to a pointer to the new buffer and setting <i>NumCharacters</i> to the buffer's length (that is, the number of Unicode characters, not the byte length).</p>

<p><b>WdfUsbTargetDeviceQueryString</b> locates the specified USB string descriptor and copies the Unicode string from the descriptor into the supplied buffer. </p>

<p>If your driver specifies a non-<b>NULL</b> value for the <i>Request</i> parameter, the framework uses the specified request object, and another driver thread can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549941">WdfRequestCancelSentRequest</a>, if necessary, to attempt to cancel the string query request. If the driver specifies a <b>NULL</b> value for <i>Request</i>, the framework uses an internal request object that the driver cannot cancel. </p>

<p>Your driver can specify a non-<b>NULL</b> <i>RequestOptions</i> parameter, whether the driver provides a non-<b>NULL</b> or a <b>NULL</b> <i>Request</i> parameter. You can, for example, use the <i>RequestOptions</i> parameter to specify a time-out value. </p>

<p>For more information about USB string descriptors, see the USB specification.</p>

<p>For more information about the <b>WdfUsbTargetDeviceQueryString</b> method and USB I/O targets, see <a href="wdf.usb_i_o_targets">USB I/O Targets</a>.</p>

<p>The following code example calls <b>WdfUsbTargetDeviceQueryString</b> to obtain the required buffer size, calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548706">WdfMemoryCreate</a> to create a memory object and buffer, and then calls <b>WdfUsbTargetDeviceQueryString</b> again to obtain the manufacturer's name string, in USA English (0x0409), from a USB device descriptor. (The driver previously stored the descriptor in driver-defined context space.)</p>

<p>Drivers should call <b>WdfUsbTargetDeviceQueryString</b> twice, by using the following steps:</p>

<p>Set the <i>String</i> pointer to <b>NULL</b>, so that <b>WdfUsbTargetDeviceQueryString</b> will return the required buffer size in the address that the <i>NumCharacters</i> parameter points to.</p>

<p> Allocate buffer space to hold the number of Unicode characters that are in the requested string. For example, a driver might call <a href="https://msdn.microsoft.com/library/windows/hardware/ff544520">ExAllocatePoolWithTag</a> to allocate a buffer, or it might call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548706">WdfMemoryCreate</a> to create a framework memory object.</p>

<p>Call <b>WdfUsbTargetDeviceQueryString</b> again, setting the <i>String</i> value to a pointer to the new buffer and setting <i>NumCharacters</i> to the buffer's length (that is, the number of Unicode characters, not the byte length).</p>

<p><b>WdfUsbTargetDeviceQueryString</b> locates the specified USB string descriptor and copies the Unicode string from the descriptor into the supplied buffer. </p>

<p>If your driver specifies a non-<b>NULL</b> value for the <i>Request</i> parameter, the framework uses the specified request object, and another driver thread can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549941">WdfRequestCancelSentRequest</a>, if necessary, to attempt to cancel the string query request. If the driver specifies a <b>NULL</b> value for <i>Request</i>, the framework uses an internal request object that the driver cannot cancel. </p>

<p>Your driver can specify a non-<b>NULL</b> <i>RequestOptions</i> parameter, whether the driver provides a non-<b>NULL</b> or a <b>NULL</b> <i>Request</i> parameter. You can, for example, use the <i>RequestOptions</i> parameter to specify a time-out value. </p>

<p>For more information about USB string descriptors, see the USB specification.</p>

<p>For more information about the <b>WdfUsbTargetDeviceQueryString</b> method and USB I/O targets, see <a href="wdf.usb_i_o_targets">USB I/O Targets</a>.</p>

<p>The following code example calls <b>WdfUsbTargetDeviceQueryString</b> to obtain the required buffer size, calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548706">WdfMemoryCreate</a> to create a memory object and buffer, and then calls <b>WdfUsbTargetDeviceQueryString</b> again to obtain the manufacturer's name string, in USA English (0x0409), from a USB device descriptor. (The driver previously stored the descriptor in driver-defined context space.)</p>

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
<p>PASSIVE_LEVEL</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539241">USB_CONFIGURATION_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539280">USB_DEVICE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540065">USB_INTERFACE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552491">WDF_REQUEST_SEND_OPTIONS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549941">WdfRequestCancelSentRequest</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550074">WdfUsbTargetDeviceAllocAndQueryString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439428">WdfUsbTargetDeviceCreateWithParameters</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfUsbTargetDeviceQueryString method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
