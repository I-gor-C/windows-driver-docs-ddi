---
UID: NF.hidpi.HidP_MaxUsageListLength
title: HidP_MaxUsageListLength
author: windows-driver-content
description: The HidP_MaxUsageListLength routine returns the maximum number of HID usages that HidP_GetUsages can return for a specified type of HID report and a specified top-level collection.
old-location: hid\hidp_maxusagelistlength.htm
old-project: hid
ms.assetid: 90491024-f623-4528-8d37-4a6acb394473
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HidP_MaxUsageListLength
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
req.alt-api: HidP_MaxUsageListLength
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# HidP_MaxUsageListLength function



## -description
<p>The <b>HidP_MaxUsageListLength</b> routine returns the maximum number of <a href="NULL">HID usages</a> that <a href="https://msdn.microsoft.com/library/windows/hardware/ff539742">HidP_GetUsages</a> can return for a specified type of HID report and a specified <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection</a>.</p>


## -syntax

````
ULONG __stdcall HidP_MaxUsageListLength(
  _In_ HIDP_REPORT_TYPE     ReportType,
  _In_ USAGE                UsagePage,
  _In_ PHIDP_PREPARSED_DATA PreparsedData
);
````


## -parameters
<dl>

### -param <i>ReportType</i> [in]

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff539774">HIDP_REPORT_TYPE</a> enumerator value that indicates the report type.</p>
</dd>

### -param <i>UsagePage</i> [in]

<dd>
<p>Specifies a <a href="hid.hid_usages#usage_page#usage_page">usage page</a> as a search criteria. If <i>UsagePage</i> is zero, the routine returns the number of all the buttons in the collection.</p>
</dd>

### -param <i>PreparsedData</i> [in]

<dd>
<p>Pointer to a top-level collection's <a href="NULL">preparsed data</a>.</p>
</dd>
</dl>

## -returns
<p>If successful, <b>HidP_MaxUsageListLength</b> returns the maximum number of <a href="NULL">HID usages</a> that <a href="https://msdn.microsoft.com/library/windows/hardware/ff539742">HidP_GetUsages</a> can return for a specified type of HID report and a specified <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection</a>. If the specified preparsed data or report type is not valid, the routine returns zero.</p>

## -remarks
<p>For more information, see <a href="NULL">HID Collections</a>. </p>

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
<p>PASSIVE_LEVEL</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539742">HidP_GetUsages</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HidP_MaxUsageListLength routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
