---
UID: NF.hidsdi.HidD_FreePreparsedData
title: HidD_FreePreparsedData
author: windows-driver-content
description: The HidD_FreePreparsedData routine releases the resources that the HID class driver allocated to hold a top-level collection's preparsed data.
old-location: hid\hidd_freepreparseddata.htm
ms.assetid: 71e2f946-706d-41bc-9d9c-d63230877e48
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: hid
req.header: hidsdi.h
req.include-header: Hidsdi.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 2000 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HidD_FreePreparsedData
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
ms.keywords: HidD_FreePreparsedData
req.iface: 
---

# HidD_FreePreparsedData function



## -description
<p>The <b>HidD_FreePreparsedData</b> routine releases the resources that the HID class driver allocated to hold a <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection's</a> <a href="NULL">preparsed data</a>.</p>


## -syntax

````
BOOLEAN __stdcall HidD_FreePreparsedData(
  _In_ PHIDP_PREPARSED_DATA PreparsedData
);
````


## -parameters
<dl>

### -param <i>PreparsedData</i> [in]

<dd>
<p>Pointer to the buffer, returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff539679">HidD_GetPreparsedData</a>, that is freed.</p>
</dd>
</dl>

## -returns
<p><b>HidD_FreePreparsedData</b> returns <b>TRUE</b> if it succeeds. Otherwise, it returns <b>FALSE</b> if the buffer was not a preparsed data buffer.</p>

## -remarks
<p>Only user-mode applications can call <b>HidD_FreePreparsedData</b>.</p>

<p>To obtain a collection's preparsed data, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff539679">HidD_GetPreparsedData</a>.</p>

<p>For more information, see <a href="NULL">HID Collections</a>.</p>

<p>Only user-mode applications can call <b>HidD_FreePreparsedData</b>.</p>

<p>To obtain a collection's preparsed data, use <a href="https://msdn.microsoft.com/library/windows/hardware/ff539679">HidD_GetPreparsedData</a>.</p>

<p>For more information, see <a href="NULL">HID Collections</a>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539679">HidD_GetPreparsedData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HidD_FreePreparsedData routine%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
