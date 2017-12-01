---
UID: NF.hidpi.HidP_GetValueCaps
title: HidP_GetValueCaps
author: windows-driver-content
description: The HidP_GetValueCaps routine returns a value capability array that describes all the HID control values in a top-level collection for a specified type of HID report.
old-location: hid\hidp_getvaluecaps.htm
old-project: hid
ms.assetid: 74c26072-3b41-4d5c-96a1-d9c5b37ed97a
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HidP_GetValueCaps
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: hidpi.h
req.include-header: Hidpi.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 2000 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HidP_GetValueCaps
req.alt-loc: Hidparse.lib,Hidparse.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hidparse.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# HidP_GetValueCaps function



## -description
<p>The <b>HidP_GetValueCaps</b> routine returns a <a href="https://msdn.microsoft.com/d447dda6-a1e5-4e57-b06f-f79f8662c236">value capability array</a> that describes all the HID control values in a <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection</a> for a specified type of HID report.</p>


## -syntax

````
NTSTATUS __stdcall HidP_GetValueCaps(
  _In_    HIDP_REPORT_TYPE     ReportType,
  _Out_   PHIDP_VALUE_CAPS     ValueCaps,
  _Inout_ PUSHORT              ValueCapsLength,
  _In_    PHIDP_PREPARSED_DATA PreparsedData
);
````


## -parameters
<dl>

### -param <i>ReportType</i> [in]

<dd>
<p>Specifies a <a href="..\hidpi\ne-hidpi--hidp-report-type.md">HIDP_REPORT_TYPE</a> enumerator value that identifies the report type.</p>
</dd>

### -param <i>ValueCaps</i> [out]

<dd>
<p>Pointer to a caller-allocated buffer in which the routine returns a value capability array for the specified report type.</p>
</dd>

### -param <i>ValueCapsLength</i> [in, out]

<dd>
<p>Specifies the length, on input, in array elements, of the <i>ValueCaps </i>buffer. On output, the routine sets <i>ValueCapsLength</i> to the number of elements that the it actually returns.</p>
</dd>

### -param <i>PreparsedData</i> [in]

<dd>
<p>Pointer to a top-level collection's <a href="NULL">preparsed data</a>.</p>
</dd>
</dl>

## -returns
<p><b>HidP_GetValueCaps</b> returns one of the following status values:</p><dl>
<dt><b>HIDP_STATUS_SUCCESS</b></dt>
</dl><p>The routine successfully returned the capability data.</p><dl>
<dt><b>HIDP_STATUS_INVALID_PREPARSED_DATA</b></dt>
</dl><p>The preparsed data is not valid.</p>

<p> </p>

## -remarks
<p>The correct length for <i>ValueCapsLength</i> is specified by the <b>Number</b><i>Xxx</i><b>ValueCaps </b>members of a top-level collection's <a href="..\hidpi\ns-hidpi--hidp-caps.md">HIDP_CAPS</a> structure.</p>

<p>For more information about a collection's capability, see <a href="NULL">Obtaining Collection Information</a>.</p>

<p>See also <a href="NULL">HID Collections</a>. </p>

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
<dt>Hidpi.h (include Hidpi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Hidparse.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543586">_HIDP_PREPARSED_DATA</a>
</dt>
<dt>
<a href="..\hidpi\ns-hidpi--hidp-caps.md">HIDP_CAPS</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getcaps.md">HidP_GetCaps</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getvaluecaps.md">HidP_GetButtonCaps</a>
</dt>
<dt>
<a href="..\hidpi\ns-hidpi--hidp-value-caps.md">HIDP_VALUE_CAPS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HidP_GetValueCaps routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
