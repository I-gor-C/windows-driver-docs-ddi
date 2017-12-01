---
UID: NF.hidsdi.HidD_GetNumInputBuffers
title: HidD_GetNumInputBuffers
author: windows-driver-content
description: The HidD_GetNumInputBuffers routine returns the current size, in number of reports, of the ring buffer that the HID class driver uses to queue input reports from a specified top-level collection.
old-location: hid\hidd_getnuminputbuffers.htm
old-project: hid
ms.assetid: f9ed28a5-835c-47c8-b9cf-888785013b69
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HidD_GetNumInputBuffers
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: hidsdi.h
req.include-header: Hidsdi.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 2000 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HidD_GetNumInputBuffers
req.alt-loc: Hid.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hid.lib
req.dll: Hid.dll
req.irql: 
req.iface: 
---

# HidD_GetNumInputBuffers function



## -description
<p>The <b>HidD_GetNumInputBuffers</b> routine returns the current size, in number of reports, of the ring buffer that the HID class driver uses to queue input reports from a specified <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection</a>.</p>


## -syntax

````
BOOLEAN __stdcall HidD_GetNumInputBuffers(
  _In_  HANDLE HidDeviceObject,
  _Out_ PULONG NumberBuffers
);
````


## -parameters
<dl>

### -param <i>HidDeviceObject</i> [in]

<dd>
<p>Specifies an open handle to a top-level collection.</p>
</dd>

### -param <i>NumberBuffers</i> [out]

<dd>
<p>Pointer to a caller-allocated variable that the routine uses to return the maximum number of input reports the ring buffer can hold.</p>
</dd>
</dl>

## -returns
<p><b>HidD_GetNumInputBuffers</b> returns <b>TRUE</b> if it succeeds; otherwise, it returns <b>FALSE</b>.</p>

## -remarks
<p>Only user-mode applications can call <b>HidD_GetNumInputBuffers</b>. Kernel-mode drivers can use the <a href="..\hidclass\ni-hidclass-ioctl-get-num-device-input-buffers.md">IOCTL_GET_NUM_DEVICE_INPUT_BUFFERS</a> request.</p>

<p>For more information, see <a href="NULL">HID Collections</a>. </p>

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
<p>Available in Windows 2000 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hidsdi.h (include Hidsdi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Hid.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Hid.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\hidsdi\nf-hidsdi-hidd-setnuminputbuffers.md">HidD_SetNumInputBuffers</a>
</dt>
<dt>
<a href="..\hidclass\ni-hidclass-ioctl-get-num-device-input-buffers.md">IOCTL_GET_NUM_DEVICE_INPUT_BUFFERS</a>
</dt>
<dt>
<a href="..\hidclass\ni-hidclass-ioctl-set-num-device-input-buffers.md">IOCTL_SET_NUM_DEVICE_INPUT_BUFFERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HidD_GetNumInputBuffers routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
