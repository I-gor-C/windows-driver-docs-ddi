---
UID: NF.hidpi.HidP_UnsetUsages
title: HidP_UnsetUsages
author: windows-driver-content
description: The HidP_UnsetUsages routine sets specified HID control button usages OFF (zero) in a HID report.
old-location: hid\hidp_unsetusages.htm
old-project: hid
ms.assetid: 55dcd9f3-6903-4718-98c2-ee42ee1026e3
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HidP_UnsetUsages
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
req.alt-api: HidP_UnsetUsages
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
---

# HidP_UnsetUsages function



## -description
<p>The <b>HidP_UnsetUsages</b> routine sets specified HID control button <a href="https://msdn.microsoft.com/84fed314-3554-4291-b51c-734d874a4bab">usages</a> OFF (zero) in a HID report.</p>


## -syntax

````
NTSTATUS __stdcall HidP_UnsetUsages(
  _In_     HIDP_REPORT_TYPE     ReportType,
  _In_     USAGE                UsagePage,
  _In_opt_ USHORT               LinkCollection,
  _Inout_  PUSAGE               UsageList,
  _Inout_  PULONG               UsageLength,
  _In_     PHIDP_PREPARSED_DATA PreparsedData,
  _In_     PCHAR                Report,
  _In_     ULONG                ReportLength
);
````


## -parameters
<dl>

### -param <i>ReportType</i> [in]

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff539774">HIDP_REPORT_TYPE</a> enumerator value that indicates the type of report located at <i>Report</i>.</p>
</dd>

### -param <i>UsagePage</i> [in]

<dd>
<p>Specifies the usage page of the usages specified by <i>UsageList</i>.</p>
</dd>

### -param <i>LinkCollection</i> [in, optional]

<dd>
<p>Specifies the <a href="https://msdn.microsoft.com/3f934661-c33c-4c08-82ac-ee2e0f519c8e">link collection</a> that contains the usages. If <i>LinkCollection</i> is nonzero, the routine only sets the usages, if they exist, in this link collection. If <i>LinkCollection</i> is zero, the routine sets the first usage for each usage it finds in the <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection</a> associated with <i>PreparsedData</i>.</p>
</dd>

### -param <i>UsageList</i> [in, out]

<dd>
<p>Pointer to the array of usages to set to OFF.</p>
</dd>

### -param <i>UsageLength</i> [in, out]

<dd>
<p>Specifies, on input, the number of usages in <i>UsageList</i>. See the Remarks section for information about the output value.</p>
</dd>

### -param <i>PreparsedData</i> [in]

<dd>
<p>Pointer to the <a href="NULL">preparsed data</a> of the top-level collection associated with the report located at <i>Report</i>.</p>
</dd>

### -param <i>Report</i> [in]

<dd>
<p>Pointer to a report.</p>
</dd>

### -param <i>ReportLength</i> [in]

<dd>
<p>Specifies the size, in bytes, of the report located at <i>Report</i>, which must be equal to the report length for the specified report type that <a href="https://msdn.microsoft.com/library/windows/hardware/ff539715">HidP_GetCaps</a> returns in a collection's <a href="https://msdn.microsoft.com/library/windows/hardware/ff539697">HIDP_CAPS</a> structure.</p>
</dd>
</dl>

## -returns
<p><b>HidP_UnsetUsages</b> returns HIDP_STATUS_SUCCESS if it successfully sets to OFF all the usages in <i>UsageList</i>.</p>

<p><b>HidP_UnsetUsages </b>returns one of the following status values if one of the input parameters is not valid:</p><dl>
<dt><b>HIDP_STATUS_INVALID_PREPARSED_DATA</b></dt>
</dl><p>The preparsed data specified by <i>PreparsedData</i> is not valid.</p><dl>
<dt><b>HIDP_STATUS_INVALID_REPORT_LENGTH</b></dt>
</dl><p>The report length is not valid.</p><dl>
<dt><b>HIDP_STATUS_INVALID_REPORT_TYPE</b></dt>
</dl><p>The report type is not valid.</p><dl>
<dt><b>HIDP_STATUS_REPORT_DOES_NOT_EXIST</b></dt>
</dl><p>The collection does not contain a report of the specified type.</p>

<p> </p>

<p><b>HidP_UnsetUsages</b> returns one of the following status values if it was not able to set to OFF one of the usages in <i>UsageList</i>:</p><dl>
<dt><b>HIDP_STATUS_BUTTON_NOT_PRESSED</b></dt>
</dl><p>
A usage is already set to OFF.
</p><dl>
<dt><b>HIDP_STATUS_INCOMPATIBLE_REPORT_ID</b></dt>
</dl><p>
A usage is not contained in the specified report, but is contained in another report of the specified type.</p><dl>
<dt><b>HIDP_STATUS_USAGE_NOT_FOUND</b></dt>
</dl><p>

The routine did not find a usage in any report of the specified type.</p>

<p> </p>

## -remarks
<p><b>HidP_UnsetUsages</b> sets <i>UsageLength</i> as follows:</p>

<p></p><dl>
<dt><a id="ReportType__PreparsedData__Report__or_ReportLength_is_not_valid."></a><a id="reporttype__preparseddata__report__or_reportlength_is_not_valid."></a><a id="REPORTTYPE__PREPARSEDDATA__REPORT__OR_REPORTLENGTH_IS_NOT_VALID."></a>ReportType, PreparsedData, Report, or ReportLength is not valid.</dt>
<dd>
<p>The input value is unchanged.</p>
</dd>
<dt><a id="All_usages_are_successfully_set_to_OFF."></a><a id="all_usages_are_successfully_set_to_off."></a><a id="ALL_USAGES_ARE_SUCCESSFULLY_SET_TO_OFF."></a>All usages are successfully set to OFF.</dt>
<dd>
<p>The input value is unchanged.</p>
</dd>
<dt><a id="A_usage_could_not_be_set_to_OFF."></a><a id="a_usage_could_not_be_set_to_off."></a><a id="A_USAGE_COULD_NOT_BE_SET_TO_OFF."></a>A usage could not be set to OFF.</dt>
<dd>
<p>Set to the index of the usage in <i>UsageList</i> that caused the error.</p>
</dd>
</dl><p>The input value is unchanged.</p>

<p>The input value is unchanged.</p>

<p>Set to the index of the usage in <i>UsageList</i> that caused the error.</p>

<p>For more information, see <a href="NULL">HID Collections</a>. </p>

<p><b>HidP_UnsetUsages</b> sets <i>UsageLength</i> as follows:</p>

<p></p><dl>
<dt><a id="ReportType__PreparsedData__Report__or_ReportLength_is_not_valid."></a><a id="reporttype__preparseddata__report__or_reportlength_is_not_valid."></a><a id="REPORTTYPE__PREPARSEDDATA__REPORT__OR_REPORTLENGTH_IS_NOT_VALID."></a>ReportType, PreparsedData, Report, or ReportLength is not valid.</dt>
<dd>
<p>The input value is unchanged.</p>
</dd>
<dt><a id="All_usages_are_successfully_set_to_OFF."></a><a id="all_usages_are_successfully_set_to_off."></a><a id="ALL_USAGES_ARE_SUCCESSFULLY_SET_TO_OFF."></a>All usages are successfully set to OFF.</dt>
<dd>
<p>The input value is unchanged.</p>
</dd>
<dt><a id="A_usage_could_not_be_set_to_OFF."></a><a id="a_usage_could_not_be_set_to_off."></a><a id="A_USAGE_COULD_NOT_BE_SET_TO_OFF."></a>A usage could not be set to OFF.</dt>
<dd>
<p>Set to the index of the usage in <i>UsageList</i> that caused the error.</p>
</dd>
</dl><p>The input value is unchanged.</p>

<p>The input value is unchanged.</p>

<p>Set to the index of the usage in <i>UsageList</i> that caused the error.</p>

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
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543586">_HIDP_PREPARSED_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539779">HidP_SetButtons</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539783">HidP_SetData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539792">HidP_SetUsages</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539812">HidP_UnsetButtons</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HidP_UnsetUsages routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
