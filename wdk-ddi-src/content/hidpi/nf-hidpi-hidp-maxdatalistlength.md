---
UID: NF.hidpi.HidP_MaxDataListLength
title: HidP_MaxDataListLength
author: windows-driver-content
description: The HidP_MaxDataListLength routine returns the maximum number of HIDP_DATA structures that HidP_GetData can return for a specified type of HID report and a specified top-level collection.
old-location: hid\hidp_maxdatalistlength.htm
old-project: hid
ms.assetid: 525a44a5-4271-4079-917e-48eb679cb96d
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HidP_MaxDataListLength
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
req.alt-api: HidP_MaxDataListLength
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

# HidP_MaxDataListLength function



## -description
<p>The <b>HidP_MaxDataListLength</b> routine returns the maximum number of <a href="..\hidpi\ns-hidpi--hidp-data.md">HIDP_DATA</a> structures that <a href="..\hidpi\nf-hidpi-hidp-getdata.md">HidP_GetData</a> can return for a specified type of HID report and a specified <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection</a>.</p>


## -syntax

````
ULONG __stdcall HidP_MaxDataListLength(
  _In_ HIDP_REPORT_TYPE     ReportType,
  _In_ PHIDP_PREPARSED_DATA PreparsedData
);
````


## -parameters
<dl>

### -param ReportType [in]

<dd>
<p>Specifies a <a href="..\hidpi\ne-hidpi--hidp-report-type.md">HIDP_REPORT_TYPE</a> enumerator value that indicates the report type.</p>
</dd>

### -param PreparsedData [in]

<dd>
<p>Pointer to a top-level collection's <a href="https://msdn.microsoft.com/50ac2877-4c45-4d55-b5cc-013486892fbf">preparsed data</a>.</p>
</dd>
</dl>

## -returns
<p>If successful, <b>HidP_MaxDataListLength</b> returns the maximum number of <a href="..\hidpi\ns-hidpi--hidp-data.md">HIDP_DATA</a> structures that <a href="..\hidpi\nf-hidpi-hidp-getdata.md">HidP_GetData</a> might return for a specified type of HID report and a specified <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection</a>. Otherwise, the routine returns zero, which indicates that either the report type or the preparsed data is not valid.</p>

## -remarks
<p>User-mode applications or kernel-mode drivers call <b>HidP_MaxDataListLength</b> to determine the maximum number of  <a href="..\hidpi\ns-hidpi--hidp-data.md">HIDP_DATA</a> structures that <b>HidP_GetData</b> can return.</p>

<p>For more information, see <a href="https://msdn.microsoft.com/2d3efb38-4eba-43db-8cff-9fac30209952">HID Collections</a>. </p>

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
<a href="..\hidpi\ns-hidpi--hidp-data.md">HIDP_DATA</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-getdata.md">HidP_GetData</a>
</dt>
<dt>
<a href="..\hidpi\nf-hidpi-hidp-setdata.md">HidP_SetData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HidP_MaxDataListLength routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
