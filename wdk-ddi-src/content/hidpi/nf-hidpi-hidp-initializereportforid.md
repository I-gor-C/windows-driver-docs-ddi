---
UID: NF.hidpi.HidP_InitializeReportForID
title: HidP_InitializeReportForID
author: windows-driver-content
description: The HidP_InitializeReportForID routine initializes a HID report.
old-location: hid\hidp_initializereportforid.htm
old-project: hid
ms.assetid: 9d56a07e-8898-4bd6-93ae-752ff7d3b215
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HidP_InitializeReportForID
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
req.alt-api: HidP_InitializeReportForID
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

# HidP_InitializeReportForID function



## -description
<p>The <b>HidP_InitializeReportForID</b> routine initializes a HID report.</p>


## -syntax

````
NTSTATUS __stdcall HidP_InitializeReportForID(
  _In_  HIDP_REPORT_TYPE     ReportType,
  _In_  UCHAR                ReportID,
  _In_  PHIDP_PREPARSED_DATA PreparsedData,
  _Out_ PCHAR                Report,
  _In_  ULONG                ReportLength
);
````


## -parameters
<dl>

### -param <i>ReportType</i> [in]

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff539774">HIDP_REPORT_TYPE</a> enumerator that indicates the type of HID report located at <i>Report</i>.</p>
</dd>

### -param <i>ReportID</i> [in]

<dd>
<p>Specifies a report ID.</p>
</dd>

### -param <i>PreparsedData</i> [in]

<dd>
<p>Pointer to the <a href="NULL">preparsed data</a> of the <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection</a> associated with the HID report located at <i>Report</i>.</p>
</dd>

### -param <i>Report</i> [out]

<dd>
<p>Pointer to the caller-allocated buffer containing the HID report that <b>HidP_InitializeReportForID</b> initializes.</p>
</dd>

### -param <i>ReportLength</i> [in]

<dd>
<p>Specifies the size, in bytes, of the HID report located at <i>Report</i>. <i>ReportLength</i> must be equal to the collection's report length for the specified report type, as specified by the <i>Xxx</i><b>ReportByteLength</b> members of a collection's <a href="https://msdn.microsoft.com/library/windows/hardware/ff539697">HIDP_CAPS</a> structure.</p>
</dd>
</dl>

## -returns
<p><b>HidP_InitializeReportForID</b> returns one of the following status values:</p><dl>
<dt><b>HIDP_STATUS_SUCCESS</b></dt>
</dl><p>The report was successfully initialized.</p><dl>
<dt><b>HIDP_STATUS_INVALID_PREPARSED_DATA</b></dt>
</dl><p>The preparsed data is not valid.</p><dl>
<dt><b>HIDP_STATUS_INVALID_REPORT_LENGTH</b></dt>
</dl><p>The specified length of the report is not equal to the collection's report length for the specified report type. </p><dl>
<dt><b>HIDP_STATUS_INVALID_REPORT_TYPE</b></dt>
</dl><p>The report type is not valid.</p><dl>
<dt><b>HIDP_STATUS_REPORT_DOES_NOT_EXIST</b></dt>
</dl><p>The specified report ID is not valid.</p>

<p> </p>

## -remarks
<p>Initializing a HID report sets all control data to zero or a control's <i>null value</i>, as defined by the USB HID standard. (Sending or receiving a null value indicates that the current value of a control should not be modified.)</p>

<p><b>HidP_InitializeReportForID</b> does the following:</p>

<p>Sets to zero the bitfields of all buttons and values without null values.</p>

<p>Sets the bitfield of all controls with null values to their corresponding null value.</p>

<p>For more information, see <a href="NULL">HID Collections</a>. </p>

<p>Initializing a HID report sets all control data to zero or a control's <i>null value</i>, as defined by the USB HID standard. (Sending or receiving a null value indicates that the current value of a control should not be modified.)</p>

<p><b>HidP_InitializeReportForID</b> does the following:</p>

<p>Sets to zero the bitfields of all buttons and values without null values.</p>

<p>Sets the bitfield of all controls with null values to their corresponding null value.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539697">HIDP_CAPS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539715">HidP_GetCaps</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539774">HIDP_REPORT_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HidP_InitializeReportForID routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
