---
UID: NF.hidpi.HidP_GetUsages
title: HidP_GetUsages
author: windows-driver-content
description: The HidP_GetUsages routine returns a list of all the HID control button usages that are on a specified usage page and are set to ON in a HID report.
old-location: hid\hidp_getusages.htm
old-project: hid
ms.assetid: e35ae7c6-2cf4-4f20-bb00-7f33ae133118
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HidP_GetUsages
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
req.alt-api: HidP_GetUsages
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

# HidP_GetUsages function



## -description
<p>The <b>HidP_GetUsages </b>routine returns a list of all the HID control button <a href="https://msdn.microsoft.com/84fed314-3554-4291-b51c-734d874a4bab">usages</a> that are on a specified <a href="hid.hid_usages#usage_page#usage_page">usage page</a> and are set to ON in a HID report. </p>


## -syntax

````
NTSTATUS __stdcall HidP_GetUsages(
  _In_    HIDP_REPORT_TYPE     ReportType,
  _In_    USAGE                UsagePage,
  _In_    USHORT               LinkCollection,
  _Out_   PUSAGE               UsageList,
  _Inout_ PULONG               UsageLength,
  _In_    PHIDP_PREPARSED_DATA PreparsedData,
  _Out_   PCHAR                Report,
  _In_    ULONG                ReportLength
);
````


## -parameters
<dl>

### -param <i>ReportType</i> [in]

<dd>
<p>Specifies a <a href="..\hidpi\ne-hidpi--hidp-report-type.md">HIDP_REPORT_TYPE</a> enumerator value that identifies the report type.</p>
</dd>

### -param <i>UsagePage</i> [in]

<dd>
<p>Specifies the <a href="hid.hid_usages#usage_page#usage_page">usage page</a> of the button usages. The routine only returns information about buttons on this usage page.</p>
</dd>

### -param <i>LinkCollection</i> [in]

<dd>
<p>Specifies the <a href="https://msdn.microsoft.com/3f934661-c33c-4c08-82ac-ee2e0f519c8e">link collection</a> of the button usages. If <i>LinkCollection</i> is nonzero, the routine only returns information about the buttons that this link collection contains; otherwise, if <i>LinkCollection</i> is zero, the routine returns information about all the buttons in the <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection</a> associated with <i>PreparsedData</i>.</p>
</dd>

### -param <i>UsageList</i> [out]

<dd>
<p>Pointer to a caller-allocated buffer that the routine uses to return the usages of all buttons that are set to ON and belong to the usage page specified by <i>UsagePage</i>. </p>
</dd>

### -param <i>UsageLength</i> [in, out]

<dd>
<p>Specifies, on input, the length, in array elements, of the <i>UsageList</i> buffer. Specifies, on output, the number of buttons that are set to ON on the specified usage page.</p>
</dd>

### -param <i>PreparsedData</i> [in]

<dd>
<p>Pointer to a top-level collection's <a href="NULL">preparsed data</a>.</p>
</dd>

### -param <i>Report</i> [out]

<dd>
<p>Pointer to a report.</p>
</dd>

### -param <i>ReportLength</i> [in]

<dd>
<p>Specifies the length, in bytes, of the report located at <i>Report</i>.</p>
</dd>
</dl>

## -returns
<p><b>HidP_GetUsages</b> returns one of the following status values:</p><dl>
<dt><b>HIDP_STATUS_SUCCESS</b></dt>
</dl><p>The routine successfully returned all button usages set to ON.</p><dl>
<dt><b>HIDP_INVALID_REPORT_LENGTH</b></dt>
</dl><p>The report length is not valid.</p><dl>
<dt><b>HIDP_INVALID_REPORT_TYPE</b></dt>
</dl><p>The specified report type is not valid.</p><dl>
<dt><b>HIDP_STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The <i>UsageList</i> buffer is too small to hold all the usages that are currently set to ON on the specified usage page.</p><dl>
<dt><b>HIDP_STATUS_INCOMPATIBLE_REPORT_ID</b></dt>
</dl><p>The collection contains buttons on the specified usage page in a report of the specified type, but there are no such usages in the specified report.</p><dl>
<dt><b>HIDP_STATUS_INVALID_PREPARSED_DATA</b></dt>
</dl><p>The preparsed data is not valid.</p><dl>
<dt><b>HIDP_STATUS_USAGE_NOT_FOUND</b></dt>
</dl><p>The collection does not contain any buttons on the specified usage page in any report of the specified report type.</p>

<p> </p>

## -remarks
<p>User-mode applications and kernel-mode drivers call <a href="..\hidpi\nf-hidpi-hidp-maxusagelistlength.md">HidP_MaxUsageListLength</a> to determine the maximum number of buttons that can be returned for specified report type. Alternatively, applications or drivers can call <b>HidP_GetUsages</b> and set <i>UsageList </i>to zero to return the required length in <i>UsageLength</i>.</p>

<p>Applications or drivers determine the required report length from the <i>Xxx</i><b>ReportByteLength</b> members in a top-level collection's <a href="..\hidpi\ns-hidpi--hidp-caps.md">HIDP_CAPS</a> structure.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539708">HidP_GetButtons</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539712">HidP_GetButtonsEx</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getcaps.md">HidP_GetCaps</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getscaledusagevalue.md">HidP_GetScaledUsageValue</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getusagesex.md">HidP_GetUsagesEx</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getusagevalue.md">HidP_GetUsageValue</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getusagevaluearray.md">HidP_GetUsageValueArray</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-maxusagelistlength.md">HidP_MaxUsageListLength</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HidP_GetUsages routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
