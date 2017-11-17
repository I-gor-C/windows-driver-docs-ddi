---
UID: NF.ntddk.WheaFindErrorRecordSection
title: WheaFindErrorRecordSection
author: windows-driver-content
description: The WheaFindErrorRecordSection function searches for a specified Windows Hardware Error Architecture (WHEA) error record section within a WHEA error record. The error record section is formatted as a WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure.
old-location: whea\wheafinderrorrecordsection.htm
ms.assetid: 57c94f04-82e2-4790-b198-d415e494d70b
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: whea
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WheaFindErrorRecordSection
req.alt-loc: ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: WheaFindErrorRecordSection
req.iface: 
---

# WheaFindErrorRecordSection function



## -description
<p>The <b>WheaFindErrorRecordSection</b> function searches for a specified Windows Hardware Error Architecture (WHEA) error record section within a WHEA <a href="https://msdn.microsoft.com/080da29a-b5cb-45a5-848d-048d9612ee2a">error record</a>. The error record section is formatted as a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure.</p>


## -syntax

````
NTSTATUS WheaFindErrorRecordSection(
  _In_            PWHEA_ERROR_RECORD                    Record,
  _In_      const GUID                                  *SectionType,
  _Out_           PWHEA_ERROR_RECORD_SECTION_DESCRIPTOR *SectionDescriptor,
  _Out_opt_       PVOID                                 *SectionData
);
````


## -parameters
<dl>

### -param <i>Record</i> [in]

<dd>
<p>A pointer to a WHEA <a href="https://msdn.microsoft.com/080da29a-b5cb-45a5-848d-048d9612ee2a">error record</a> that is formatted as a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560483">WHEA_ERROR_RECORD</a> structure.</p>
</dd>

### -param <i>SectionType</i> [in]

<dd>
<p>A GUID that specifies the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure to be located within the specified WHEA <a href="https://msdn.microsoft.com/080da29a-b5cb-45a5-848d-048d9612ee2a">error record</a>.</p>
</dd>

### -param <i>SectionDescriptor</i> [out]

<dd>
<p>The address of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> pointer. </p>
<p>If the <b>WheaFindErrorRecordSection</b> function locates the specified WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure, the function sets the <i>SectionDescriptor </i>parameter to the address of that structure within the specified WHEA <a href="https://msdn.microsoft.com/080da29a-b5cb-45a5-848d-048d9612ee2a">error record</a>.</p>
</dd>

### -param <i>SectionData</i> [out, optional]

<dd>
<p>The address of a PVOID pointer.</p>
<p>If the <b>WheaFindErrorRecordSection</b> function locates the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure, the function sets the <i>SectionData</i> parameter to the address of the hardware error data associated with that descriptor within the specified WHEA <a href="https://msdn.microsoft.com/080da29a-b5cb-45a5-848d-048d9612ee2a">error record</a>.</p>
<div class="alert"><b>Note</b>  This parameter is optional and must be set to <b>NULL</b> if a pointer to the hardware error data is not required.</div>
<div> </div>
</dd>
</dl>

## -returns
<p><b>WheaFindErrorRecordSection</b> returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure was found. </p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>The specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure was not found.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Either the <i>Record</i>, <i>SectionType,</i> or <i>SectionDescriptor</i> parameters were set to <b>NULL</b>, or the WHEA <a href="https://msdn.microsoft.com/080da29a-b5cb-45a5-848d-048d9612ee2a">error record</a> referenced through the <i>Record </i>parameter is invalid.</p>

<p> </p>

## -remarks
<p>If <b>WheaFindErrorRecordSection</b> returns STATUS_SUCCESS, it has located the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure that was specified through the <i>Guid </i>parameter. <b>WheaFindErrorRecordSection</b> sets the <i>SectionDescriptor</i> parameter to the address of the located <b>WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</b> structure.</p>

<p>Additionally, if <b>WheaFindErrorRecordSection</b> returns STATUS_SUCCESS and the caller set the <i>SectionData</i> parameter to the address of a PVOID pointer variable, the function updates the parameter with the address of the hardware error data associated with the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure. </p>

<p>The format of the hardware error data is dependent upon the <b>SectionType </b>member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure referenced through the <i>SectionDescriptor </i>parameter. For example, if the <b>SectionType </b>member has the value PROCESSOR_GENERIC_ERROR_SECTION_GUID, the hardware error data is formatted as a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560607">WHEA_PROCESSOR_GENERIC_ERROR_SECTION</a> structure.</p>

<p>If <b>WheaFindErrorRecordSection</b> returns STATUS_SUCCESS, it has located the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure that was specified through the <i>Guid </i>parameter. <b>WheaFindErrorRecordSection</b> sets the <i>SectionDescriptor</i> parameter to the address of the located <b>WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</b> structure.</p>

<p>Additionally, if <b>WheaFindErrorRecordSection</b> returns STATUS_SUCCESS and the caller set the <i>SectionData</i> parameter to the address of a PVOID pointer variable, the function updates the parameter with the address of the hardware error data associated with the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure. </p>

<p>The format of the hardware error data is dependent upon the <b>SectionType </b>member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure referenced through the <i>SectionDescriptor </i>parameter. For example, if the <b>SectionType </b>member has the value PROCESSOR_GENERIC_ERROR_SECTION_GUID, the hardware error data is formatted as a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560607">WHEA_PROCESSOR_GENERIC_ERROR_SECTION</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows 7 and later versions of Windows.
</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
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
<a href="https://msdn.microsoft.com/080da29a-b5cb-45a5-848d-048d9612ee2a">Error record</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560483">WHEA_ERROR_RECORD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560496">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WheaFindErrorRecordSection function%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
