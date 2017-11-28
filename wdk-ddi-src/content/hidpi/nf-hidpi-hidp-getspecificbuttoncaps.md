---
UID: NF.hidpi.HidP_GetSpecificButtonCaps
title: HidP_GetSpecificButtonCaps
author: windows-driver-content
description: The HidP_GetSpecificButtonCaps routine returns a button capability array that describes all HID control buttons in a top-level collection that meet a specified selection criteria.
old-location: hid\hidp_getspecificbuttoncaps.htm
old-project: hid
ms.assetid: 923693a2-cb46-4f74-bb1b-cd7bb07014e8
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HidP_GetSpecificButtonCaps
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
req.alt-api: HidP_GetSpecificButtonCaps
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

# HidP_GetSpecificButtonCaps function



## -description
<p>The <b>HidP_GetSpecificButtonCaps</b> routine returns a <a href="https://msdn.microsoft.com/139324e5-4d46-4d00-9f5a-fd0313fc109a">button capability array</a> that describes all HID control buttons in a <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection</a> that meet a specified selection criteria.</p>


## -syntax

````
NTSTATUS __stdcall HidP_GetSpecificButtonCaps(
  _In_    HIDP_REPORT_TYPE     ReportType,
  _In_    USAGE                UsagePage,
  _In_    USHORT               LinkCollection,
  _In_    USAGE                Usage,
  _Out_   PHIDP_BUTTON_CAPS    ButtonCaps,
  _Inout_ PUSHORT              ButtonCapsLength,
  _In_    PHIDP_PREPARSED_DATA PreparsedData
);
````


## -parameters
<dl>

### -param <i>ReportType</i> [in]

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/library/windows/hardware/ff539774">HIDP_REPORT_TYPE</a> enumerator value that identifies the report type.</p>
</dd>

### -param <i>UsagePage</i> [in]

<dd>
<p>Specifies a usage page as a search criteria. If <i>UsagePage</i> is nonzero, only buttons that specify this usage page are returned.</p>
</dd>

### -param <i>LinkCollection</i> [in]

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/3f934661-c33c-4c08-82ac-ee2e0f519c8e">link collection</a> as a search criteria. If <i>LinkCollection</i> is nonzero, only buttons that are part of this link collection are returned.</p>
</dd>

### -param <i>Usage</i> [in]

<dd>
<p>Specifies a <a href="https://msdn.microsoft.com/84fed314-3554-4291-b51c-734d874a4bab">HID usage</a> as a search criteria. If <i>Usage</i> is nonzero, only buttons that specify this usage will be returned.</p>
</dd>

### -param <i>ButtonCaps</i> [out]

<dd>
<p>Pointer to a caller-allocated buffer in which the routine returns a button capability array for the specified report type.</p>
</dd>

### -param <i>ButtonCapsLength</i> [in, out]

<dd>
<p>Specifies the length on input, in array elements, of the buffer provided at <i>ButtonCaps</i>. On output, this parameter is set to the number of elements that the routine actually returned.</p>
</dd>

### -param <i>PreparsedData</i> [in]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection's</a> <a href="NULL">preparsed data</a>.</p>
</dd>
</dl>

## -returns
<p><b>HidP_GetSpecificButtonCaps</b> returns one of the following status values:</p><dl>
<dt><b>HIDP_STATUS_SUCCESS</b></dt>
</dl><p>The routine successfully returned the capability data.</p><dl>
<dt><b>HIDP_STATUS_INVALID_PREPARSED_DATA</b></dt>
</dl><p>The preparsed data is not valid.</p>

<p> </p>

## -remarks
<p>The required size of the <i>ButtonCaps</i> array is specified by the <b>Number</b><i>Xxx</i><b>ButtonCaps </b>members of a top-level collection's <a href="https://msdn.microsoft.com/library/windows/hardware/ff539697">HIDP_CAPS</a> structure.</p>

<p>When calling <b>HidP_GetSpecificButtonCaps</b>, specifying zero for <i>UsagePage</i>, <i>Usage</i>, and <i>LinkCollection</i> is equivalent to calling <b>HidP_GetButtonCaps</b>.</p>

<p>For more information about a collection's capability, see <a href="NULL">Obtaining Collection Information</a>.</p>

<p>See also <a href="NULL">HID Collections</a>. </p>

<p>The required size of the <i>ButtonCaps</i> array is specified by the <b>Number</b><i>Xxx</i><b>ButtonCaps </b>members of a top-level collection's <a href="https://msdn.microsoft.com/library/windows/hardware/ff539697">HIDP_CAPS</a> structure.</p>

<p>When calling <b>HidP_GetSpecificButtonCaps</b>, specifying zero for <i>UsagePage</i>, <i>Usage</i>, and <i>LinkCollection</i> is equivalent to calling <b>HidP_GetButtonCaps</b>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539707">HidP_GetButtonCaps</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539715">HidP_GetCaps</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539693">HIDP_BUTTON_CAPS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HidP_GetSpecificButtonCaps routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
