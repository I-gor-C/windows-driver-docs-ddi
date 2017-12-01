---
UID: NF.wdfusb.WdfUsbTargetDeviceAllocAndQueryString
title: WdfUsbTargetDeviceAllocAndQueryString
author: windows-driver-content
description: The WdfUsbTargetDeviceAllocAndQueryString method allocates a buffer, then it retrieves the Unicode string that is associated with a specified USB device and descriptor index value.
old-location: wdf\wdfusbtargetdeviceallocandquerystring.htm
old-project: wdf
ms.assetid: a9dea258-601b-4ff7-b03b-b3f22d86f314
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfUsbTargetDeviceAllocAndQueryString
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
req.alt-api: WdfUsbTargetDeviceAllocAndQueryString
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2, UsbKmdfIrql, UsbKmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfUsbTargetDeviceAllocAndQueryString function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfUsbTargetDeviceAllocAndQueryString</b> method allocates a buffer, then it retrieves the Unicode string that is associated with a specified USB device and descriptor index value.</p>


## -syntax

````
NTSTATUS WdfUsbTargetDeviceAllocAndQueryString(
  _In_      WDFUSBDEVICE           UsbDevice,
  _In_opt_  PWDF_OBJECT_ATTRIBUTES StringMemoryAttributes,
  _Out_     WDFMEMORY              *StringMemory,
  _Out_opt_ PUSHORT                NumCharacters,
  _In_      UCHAR                  StringIndex,
  _In_opt_  USHORT                 LangID
);
````


## -parameters
<dl>

### -param <i>UsbDevice</i> [in]

<dd>
<p>A handle to a USB device object that was obtained from a previous call to <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdevicecreatewithparameters.md">WdfUsbTargetDeviceCreateWithParameters</a>.</p>
</dd>

### -param <i>StringMemoryAttributes</i> [in, optional]

<dd>
<p>A pointer to a caller-allocated <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure that contains caller-supplied attributes for the new memory object. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.</p>
</dd>

### -param <i>StringMemory</i> [out]

<dd>
<p>A pointer to a location that receives a handle to the memory object that contains the Unicode string. The string is NULL-terminated only if the device supplies a NULL-terminated string. </p>
</dd>

### -param <i>NumCharacters</i> [out, optional]

<dd>
<p>A pointer to a location that receives the number of characters that are contained in the string descriptor. If the Unicode string is NULL-terminated, this number includes the NULL character. This parameter is optional and can be <b>NULL</b>.</p>
</dd>

### -param <i>StringIndex</i> [in]

<dd>
<p>An index value that identifies the Unicode string. This index value is obtained from a <a href="..\usbspec\ns-usbspec--usb-device-descriptor.md">USB_DEVICE_DESCRIPTOR</a>, <a href="..\usbspec\ns-usbspec--usb-configuration-descriptor.md">USB_CONFIGURATION_DESCRIPTOR</a>, or <a href="..\usbspec\ns-usbspec--usb-interface-descriptor.md">USB_INTERFACE_DESCRIPTOR</a> structure.</p>
</dd>

### -param <i>LangID</i> [in, optional]

<dd>
<p>A language identifier. The Unicode string will be retrieved for the language that this identifier specifies. For information about obtaining a device's supported language identifiers, see the USB specification. </p>
</dd>
</dl>

## -returns
<p><b>WdfUsbTargetDeviceAllocAndQueryString</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method can return one of the following values:</p><dl>
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
<p>The <b>WdfUsbTargetDeviceAllocAndQueryString</b> method, which your driver only needs to call once to obtain a string descriptor, is an alternative to the <a href="..\wdfusb\nf-wdfusb-wdfusbtargetdevicequerystring.md">WdfUsbTargetDeviceQueryString</a> method, which must be called twice to obtain a string.</p>

<p>The method locates the specified USB string descriptor, copies the Unicode string from the descriptor into a memory object, and returns a handle to the memory object. </p>

<p>After calling <b>WdfUsbTargetDeviceAllocAndQueryString</b>, your driver can pass the <i>StringMemory</i> handle to <a href="..\wdfmemory\nf-wdfmemory-wdfmemorygetbuffer.md">WdfMemoryGetBuffer</a> to access the contents of the memory object.</p>

<p>For more information about USB string descriptors, see the USB specification.</p>

<p>For more information about the <b>WdfUsbTargetDeviceAllocAndQueryString</b> method and USB I/O targets, see <a href="wdf.usb_i_o_targets">USB I/O Targets</a>.</p>

<p>The following code example calls <b>WdfUsbTargetDeviceAllocAndQueryString</b> to obtain a manufacturer's name string, in USA English (0x0409), from a USB device descriptor. (The driver previously stored the descriptor in driver-defined context space.)</p>

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
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_usbkmdfirql">UsbKmdfIrql</a>, <a href="devtest.kmdf_usbkmdfirql2">UsbKmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\usbspec\ns-usbspec--usb-configuration-descriptor.md">USB_CONFIGURATION_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\usbspec\ns-usbspec--usb-device-descriptor.md">USB_DEVICE_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\usbspec\ns-usbspec--usb-interface-descriptor.md">USB_INTERFACE_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\wdfusb\nf-wdfusb-wdfusbtargetdevicecreatewithparameters.md">WdfUsbTargetDeviceCreateWithParameters</a>
</dt>
<dt>
<a href="..\wdfusb\nf-wdfusb-wdfusbtargetdevicequerystring.md">WdfUsbTargetDeviceQueryString</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfUsbTargetDeviceAllocAndQueryString method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
