---
UID: NF.hidpi.HidP_SetUsageValue
title: HidP_SetUsageValue
author: windows-driver-content
description: The HidP_SetUsageValue routine sets a HID control value in a specified HID report.
old-location: hid\hidp_setusagevalue.htm
old-project: hid
ms.assetid: e59d7087-58eb-4bc3-a4e0-4597ee28dcd6
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HidP_SetUsageValue
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
req.alt-api: HidP_SetUsageValue
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

# HidP_SetUsageValue function



## -description
<p>The <b>HidP_SetUsageValue</b> routine sets a HID control value in a specified HID report.</p>


## -syntax

````
NTSTATUS __stdcall HidP_SetUsageValue(
  _In_    HIDP_REPORT_TYPE     ReportType,
  _In_    USAGE                UsagePage,
  _In_    USHORT               LinkCollection,
  _In_    USAGE                Usage,
  _In_    ULONG                UsageValue,
  _In_    PHIDP_PREPARSED_DATA PreparsedData,
  _Inout_ PCHAR                Report,
  _In_    ULONG                ReportLength
);
````


## -parameters
<dl>

### -param <i>ReportType</i> [in]

<dd>
<p>Specifies a <a href="..\hidpi\ne-hidpi--hidp-report-type.md">HIDP_REPORT_TYPE</a> enumerator value that indicates the type of HID report located at <i>Report</i>.</p>
</dd>

### -param <i>UsagePage</i> [in]

<dd>
<p>Specifies the <a href="hid.hid_usages#usage_page#usage_page">usage page</a> of a usage.</p>
</dd>

### -param <i>LinkCollection</i> [in]

<dd>
<p>Specifies the <a href="https://msdn.microsoft.com/3f934661-c33c-4c08-82ac-ee2e0f519c8e">link collection</a> that contains the usage. If <i>LinkCollection</i> is nonzero, the routine only sets the usage, if one exists, in this link collection. If <i>LinkCollection</i> is zero, the routine sets the first usage it finds in the <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection</a> associated with <i>PreparsedData</i>.</p>
</dd>

### -param <i>Usage</i> [in]

<dd>
<p>Specifies the usage.</p>
</dd>

### -param <i>UsageValue</i> [in]

<dd>
<p>Specifies the usage value.</p>
</dd>

### -param <i>PreparsedData</i> [in]

<dd>
<p>Pointer to a top-level's <a href="NULL">preparsed data</a>.</p>
</dd>

### -param <i>Report</i> [in, out]

<dd>
<p>Pointer to a HID report.</p>
</dd>

### -param <i>ReportLength</i> [in]

<dd>
<p>Specifies the size, in bytes, of the HID report located at <i>Report</i>, which must be equal to the report length for the specified report type that <a href="..\hidpi\nf-hidpi-hidp-getcaps.md">HidP_GetCaps</a> returns in a collection's <a href="..\hidpi\ns-hidpi--hidp-caps.md">HIDP_CAPS</a> structure.</p>
</dd>
</dl>

## -returns
<p><b>HidP_SetUsageValue</b> returns one of the following status values:</p><dl>
<dt><b>HIDP_STATUS_SUCCESS</b></dt>
</dl><p>The routine successfully set the usage value.</p><dl>
<dt><b>HIDP_STATUS_INCOMPATIBLE_REPORT_ID</b></dt>
</dl><p>The usage does not exist in the specified report, but it does exist in a different report of the specified type.</p><dl>
<dt><b>HIDP_STATUS_INVALID_PREPARSED_DATA</b></dt>
</dl><p>The preparsed data is not valid.</p><dl>
<dt><b>HIDP_STATUS_REPORT_DOES_NOT_EXIST</b></dt>
</dl><p>There are no reports of the specified type.</p><dl>
<dt><b>HIDP_STATUS_USAGE_NOT_FOUND</b></dt>
</dl><p>The usage does not exist in any report of the specified report type.</p><dl>
<dt><b>HIDP_STATUS_INVALID_REPORT_LENGTH</b></dt>
</dl><p>The report length is not valid.</p><dl>
<dt><b>HIDP_STATUS_INVALID_REPORT_TYPE</b></dt>
</dl><p>The specified report type is not valid.</p>

<p> </p>

## -remarks
<p><b>HidP_SetUsageValue</b> routine does not sign the value. A user-mode application or kernel-mode driver must either sign the value, at the position provided in the <a href="..\hidpi\ns-hidpi--hidp-value-caps.md">HIDP_VALUE_CAPS</a> structure for this value, or call <a href="..\hidpi\nf-hidpi-hidp-setscaledusagevalue.md">HidP_SetScaledUsageValue</a>.</p>

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
<a href="..\hidpi\nf-hidpi-hidp-setscaledusagevalue.md">HidP_SetScaledUsageValue</a>
</dt>
<dt>
<a href="..\hidpi\ns-hidpi--hidp-value-caps.md">HIDP_VALUE_CAPS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HidP_SetUsageValue routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
