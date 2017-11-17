---
UID: NF.ksproxy.KsSynchronousDeviceControl
title: KsSynchronousDeviceControl
author: windows-driver-content
description: The KsSynchronousDeviceControl function issues a synchronous device I/O control operation to the KS object that is specified by a file handle.
old-location: stream\kssynchronousdevicecontrol.htm
ms.assetid: 82c8f0c0-d9df-4f0d-8a45-dda8fa8a132a
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ksproxy.h
req.include-header: Ksproxy.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsSynchronousDeviceControl
req.alt-loc: Ksproxy.lib,Ksproxy.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ksproxy.lib
req.dll: 
req.irql: 
ms.keywords: KsSynchronousDeviceControl
req.iface: 
---

# KsSynchronousDeviceControl function



## -description
<p>The <b>KsSynchronousDeviceControl</b> function issues a synchronous device I/O control operation to the KS object that is specified by a file handle. </p>


## -syntax

````
HRESULT KsSynchronousDeviceControl(
  _In_      HANDLE Handle,
  _In_      ULONG  IoControl,
  _In_opt_  PVOID  InBuffer,
  _In_      ULONG  InLength,
  _Out_opt_ PVOID  OutBuffer,
  _In_      ULONG  OutLength,
  _Inout_   PULONG BytesReturned
);
````


## -parameters
<dl>

### -param <i>Handle</i> [in]

<dd>
<p>Handle to the KS object on which to perform the operation.</p>
</dd>

### -param <i>IoControl</i> [in]

<dd>
<p>Control code that identifies a specific type of operation to perform on a KS object. </p>
</dd>

### -param <i>InBuffer</i> [in, optional]

<dd>
<p>Pointer to a buffer that contains data that specifies the operation to perform. </p>
</dd>

### -param <i>InLength</i> [in]

<dd>
<p>Size, in bytes, of the buffer at <i>InBuffer</i>.</p>
</dd>

### -param <i>OutBuffer</i> [out, optional]

<dd>
<p>Pointer to a buffer that contains either data for the operation or buffer space that receives data for the operation. </p>
</dd>

### -param <i>OutLength</i> [in]

<dd>
<p>Size, in bytes, of the buffer at <i>OutBuffer</i>.</p>
</dd>

### -param <i>BytesReturned</i> [in, out]

<dd>
<p>Pointer to a variable that receives the size, in bytes, of the data that <b>KsSynchronousDeviceControl</b> stores in the buffer at <i>OutBuffer</i>. </p>
</dd>
</dl>

## -returns
<p>Returns NOERROR if successful; otherwise, returns an error code.</p>

## -remarks
<p>To retrieve the handle to the KS object, an application should call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559890">IKsObject::KsGetObjectHandle</a> method. </p>

<p>An application can set the control code in <i>IoControl</i> and the buffers at <i>InBuffer</i> and <i>OutBuffer</i> as follows to specify the operation to perform: </p>

<p>Set <i>IoControl</i> to <a href="https://msdn.microsoft.com/library/windows/hardware/ff560822">IOCTL_KS_PROPERTY</a> to access a property. Set <i>InBuffer</i> to point to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a> structure that specifies the property of the property set to access and whether to retrieve information about the property or set information in the property. To set information in the property, set <i>OutBuffer</i> to point to that information. To retrieve information from the property, set <i>OutBuffer</i> to receive that information. </p>

<p>Set <i>IoControl</i> to <a href="https://msdn.microsoft.com/library/windows/hardware/ff560817">IOCTL_KS_METHOD</a> to execute a method. Set <i>InBuffer</i> to point to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563398">KSMETHOD</a> structure that specifies the method of the method set to execute and whether to read and/or write data related to the method. To read data, set <i>OutBuffer</i> to point to that data. To write data, set <i>OutBuffer</i> to receive that data.</p>

<p>Set <i>IoControl</i> to <a href="https://msdn.microsoft.com/library/windows/hardware/ff560808">IOCTL_KS_ENABLE_EVENT</a> to request that the KS object specified by <i>Handle</i> notify the application whenever a specific event action occurs. Set <i>InBuffer</i> to point to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561744">KSEVENT</a> structure that specifies the event of the event set about which to notify. Set <i>OutBuffer</i> to point to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561750">KSEVENTDATA</a> structure that describes how the KS object should notify the application when the event occurs. Also see <a href="NULL">KS Events</a>.</p>

<p>Set <i>IoControl</i> to <a href="https://msdn.microsoft.com/library/windows/hardware/ff560802">IOCTL_KS_DISABLE_EVENT</a> to inform the KS object specified by <i>Handle</i> to stop notifying the application whenever a specific event action occurs. Set <i>InBuffer</i> to point to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561750">KSEVENTDATA</a> structure that was previously used in the event-notification request. </p>

<p>To retrieve a list of all properties, events, or methods supported by a filter, an application can set <i>IoControl</i> to IOCTL_KS_PROPERTY, IOCTL_KS_ENABLE_EVENT, or IOCTL_KS_METHOD. For the KSPROPERTY, KSEVENT, or KSMETHOD structure to which <i>InBuffer</i> points, set the <i>Set</i> member to GUID_NULL and set the <i>Flags</i> member to KSPROPERTY_TYPE_SETSUPPORT.</p>

<p>After the call to <b>KsSynchronousDeviceControl</b>, <i>OutBuffer</i> will contain an array of set GUIDs supported by the object specified by <i>Handle</i>.</p>

<p>To retrieve the handle to the KS object, an application should call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559890">IKsObject::KsGetObjectHandle</a> method. </p>

<p>An application can set the control code in <i>IoControl</i> and the buffers at <i>InBuffer</i> and <i>OutBuffer</i> as follows to specify the operation to perform: </p>

<p>Set <i>IoControl</i> to <a href="https://msdn.microsoft.com/library/windows/hardware/ff560822">IOCTL_KS_PROPERTY</a> to access a property. Set <i>InBuffer</i> to point to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a> structure that specifies the property of the property set to access and whether to retrieve information about the property or set information in the property. To set information in the property, set <i>OutBuffer</i> to point to that information. To retrieve information from the property, set <i>OutBuffer</i> to receive that information. </p>

<p>Set <i>IoControl</i> to <a href="https://msdn.microsoft.com/library/windows/hardware/ff560817">IOCTL_KS_METHOD</a> to execute a method. Set <i>InBuffer</i> to point to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563398">KSMETHOD</a> structure that specifies the method of the method set to execute and whether to read and/or write data related to the method. To read data, set <i>OutBuffer</i> to point to that data. To write data, set <i>OutBuffer</i> to receive that data.</p>

<p>Set <i>IoControl</i> to <a href="https://msdn.microsoft.com/library/windows/hardware/ff560808">IOCTL_KS_ENABLE_EVENT</a> to request that the KS object specified by <i>Handle</i> notify the application whenever a specific event action occurs. Set <i>InBuffer</i> to point to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561744">KSEVENT</a> structure that specifies the event of the event set about which to notify. Set <i>OutBuffer</i> to point to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561750">KSEVENTDATA</a> structure that describes how the KS object should notify the application when the event occurs. Also see <a href="NULL">KS Events</a>.</p>

<p>Set <i>IoControl</i> to <a href="https://msdn.microsoft.com/library/windows/hardware/ff560802">IOCTL_KS_DISABLE_EVENT</a> to inform the KS object specified by <i>Handle</i> to stop notifying the application whenever a specific event action occurs. Set <i>InBuffer</i> to point to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561750">KSEVENTDATA</a> structure that was previously used in the event-notification request. </p>

<p>To retrieve a list of all properties, events, or methods supported by a filter, an application can set <i>IoControl</i> to IOCTL_KS_PROPERTY, IOCTL_KS_ENABLE_EVENT, or IOCTL_KS_METHOD. For the KSPROPERTY, KSEVENT, or KSMETHOD structure to which <i>InBuffer</i> points, set the <i>Set</i> member to GUID_NULL and set the <i>Flags</i> member to KSPROPERTY_TYPE_SETSUPPORT.</p>

<p>After the call to <b>KsSynchronousDeviceControl</b>, <i>OutBuffer</i> will contain an array of set GUIDs supported by the object specified by <i>Handle</i>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksproxy.h (include Ksproxy.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ksproxy.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559890">IKsObject::KsGetObjectHandle</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560802">IOCTL_KS_DISABLE_EVENT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560808">IOCTL_KS_ENABLE_EVENT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560817">IOCTL_KS_METHOD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560822">IOCTL_KS_PROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561744">KSEVENT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561750">KSEVENTDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563398">KSMETHOD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564262">KSPROPERTY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsSynchronousDeviceControl function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
