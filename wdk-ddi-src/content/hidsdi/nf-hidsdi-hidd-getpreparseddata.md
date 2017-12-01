---
UID: NF.hidsdi.HidD_GetPreparsedData
title: HidD_GetPreparsedData
author: windows-driver-content
description: The HidD_GetPreparsedData routine returns a top-level collection's preparsed data.
old-location: hid\hidd_getpreparseddata.htm
old-project: hid
ms.assetid: e5c550f0-a466-4d0b-ac6f-bcdce600245f
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HidD_GetPreparsedData
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
req.alt-api: HidD_GetPreparsedData
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

# HidD_GetPreparsedData function



## -description
<p>The <b>HidD_GetPreparsedData</b> routine returns a <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection's</a> <a href="NULL">preparsed data</a>.</p>


## -syntax

````
BOOLEAN __stdcall HidD_GetPreparsedData(
  _In_  HANDLE               HidDeviceObject,
  _Out_ PHIDP_PREPARSED_DATA *PreparsedData
);
````


## -parameters
<dl>

### -param <i>HidDeviceObject</i> [in]

<dd>
<p>Specifies an open handle to a top-level collection.</p>
</dd>

### -param <i>PreparsedData</i> [out]

<dd>
<p>Pointer to the address of a routine-allocated buffer that contains a collection's preparsed data in a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543586">_HIDP_PREPARSED_DATA</a> structure.</p>
</dd>
</dl>

## -returns
<p><b>HidD_GetPreparsedData</b> returns <b>TRUE</b> if it succeeds; otherwise, it returns <b>FALSE</b>.</p>

## -remarks
<p>Only user-mode applications can call <b>HidD_GetPreparsedData</b>. Kernel-mode drivers can use an <a href="..\hidclass\ni-hidclass-ioctl-hid-get-collection-descriptor.md">IOCTL_HID_GET_COLLECTION_DESCRIPTOR</a> request.</p>

<p>When an application no longer requires the preparsed data, it should call <a href="..\hidsdi\nf-hidsdi-hidd-freepreparseddata.md">HidD_FreePreparsedData</a> to free the preparsed data buffer.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543586">_HIDP_PREPARSED_DATA</a>
</dt>
<dt>
<a href="..\hidsdi\nf-hidsdi-hidd-freepreparseddata.md">HidD_FreePreparsedData</a>
</dt>
<dt>
<a href="..\hidclass\ni-hidclass-ioctl-hid-get-collection-descriptor.md">IOCTL_HID_GET_COLLECTION_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HidD_GetPreparsedData routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
