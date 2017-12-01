---
UID: NF.ntddk.WheaFindNextErrorRecordSection
title: WheaFindNextErrorRecordSection
author: windows-driver-content
description: The WheaFindNextErrorRecordSection function allows a caller to iteratively examine the WHEA error record sections within a WHEA error record. Each error record section is formatted as a WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure.
old-location: whea\wheafindnexterrorrecordsection.htm
old-project: whea
ms.assetid: 36a0ca45-2601-4b7f-9f2b-35e2a7047520
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WheaFindNextErrorRecordSection
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WheaFindNextErrorRecordSection
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
req.iface: 
---

# WheaFindNextErrorRecordSection function



## -description
<p>The <b>WheaFindNextErrorRecordSection</b> function allows a caller to iteratively examine the WHEA error record sections within a WHEA <a href="https://msdn.microsoft.com/080da29a-b5cb-45a5-848d-048d9612ee2a">error record</a>. Each error record section is formatted as a <a href="..\ntddk\ns-ntddk--whea-error-record-section-descriptor.md">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure.</p>


## -syntax

````
NTSTATUS WheaFindNextErrorRecordSection(
  _In_      PWHEA_ERROR_RECORD                    Record,
  _Inout_   ULONG                                 *Context,
  _Out_     PWHEA_ERROR_RECORD_SECTION_DESCRIPTOR *SectionDescriptor,
  _Out_opt_ PVOID                                 *SectionData
);
````


## -parameters
<dl>

### -param <i>Record</i> [in]

<dd>
<p>A pointer to a WHEA <a href="https://msdn.microsoft.com/080da29a-b5cb-45a5-848d-048d9612ee2a">error record</a> that is formatted as a <a href="..\ntddk\ns-ntddk--whea-error-record.md">WHEA_ERROR_RECORD</a> structure.</p>
</dd>

### -param <i>Context</i> [in, out]

<dd>
<p>A pointer to a ULONG variable that maintains the current state of the search. </p>
<div class="alert"><b>Note</b>  This variable must be initialized to zero before the first call to the <b>WheaFindNextErrorRecordSection </b>function<b>.</b></div>
<div> </div>
</dd>

### -param <i>SectionDescriptor</i> [out]

<dd>
<p>The address of a <a href="..\ntddk\ns-ntddk--whea-error-record-section-descriptor.md">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> pointer. </p>
<p>If the <b>WheaFindNextErrorRecordSection </b>function locates the next WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure within the specified WHEA <a href="https://msdn.microsoft.com/080da29a-b5cb-45a5-848d-048d9612ee2a">error record</a>, the function sets the <i>SectionDescriptor </i>parameter to the address of that structure within the specified WHEA error record.</p>
</dd>

### -param <i>SectionData</i> [out, optional]

<dd>
<p>The address of a PVOID pointer.</p>
<p>If the <b>WheaFindNextErrorRecordSection</b> function locates the next <a href="..\ntddk\ns-ntddk--whea-error-record-section-descriptor.md">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure within the specified WHEA <a href="https://msdn.microsoft.com/080da29a-b5cb-45a5-848d-048d9612ee2a">error record</a>, the function sets the <i>SectionData</i> parameter to the address of the hardware error data associated with that descriptor.</p>
<div class="alert"><b>Note</b>  This parameter is optional and must be set to <b>NULL</b> if a pointer to the error record section data is not required.</div>
<div> </div>
</dd>
</dl>

## -returns
<p><b>WheaFindNextErrorRecordSection</b> returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The next  <a href="..\ntddk\ns-ntddk--whea-error-record-section-descriptor.md">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure was found. </p><dl>
<dt><b>STATUS_NOT_FOUND</b></dt>
</dl><p>The next <a href="..\ntddk\ns-ntddk--whea-error-record-section-descriptor.md">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure was not found.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Either the <i>Record</i>, <i>SectionType,</i> or <i>SectionDescriptor</i> parameters were set to <b>NULL</b>, or the <a href="..\ntddk\ns-ntddk--whea-error-record.md">WHEA_ERROR_RECORD</a> data referenced through the <i>Record </i>parameter is invalid.</p>

<p> </p>

## -remarks
<p>If the <i>Context</i> parameter is set to 0, <b>WheaFindNextErrorRecordSection </b>returns a pointer to the first <a href="..\ntddk\ns-ntddk--whea-error-record-section-descriptor.md">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure within a WHEA <a href="https://msdn.microsoft.com/080da29a-b5cb-45a5-848d-048d9612ee2a">error record</a>. <b>WheaFindNextErrorRecordSection </b>will also update the <i>Context</i> parameter with state information related to the WHEA_ERROR_RECORD_SECTION_DESCRIPTOR returned through the <i>SectionDescriptor</i> parameter.</p>

<p>On subsequent calls to <b>WheaFindNextErrorRecordSection</b>, the function returns the next WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure (if available) within the WHEA error record. If the function locates the next WHEA_ERROR_RECORD_SECTION_DESCRIPTOR structure, it will update the <i>Context</i> parameter. Otherwise, the function will return STATUS_NOT_FOUND.</p>

<p>Additionally, if <b>WheaFindNextErrorRecordSection</b> returns STATUS_SUCCESS and the caller set the <i>SectionData</i> parameter to the address of a PVOID pointer variable, the function updates the parameter with the address of the hardware error data associated with the specified <a href="..\ntddk\ns-ntddk--whea-error-record-section-descriptor.md">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure. </p>

<p>The format of the hardware error data depends upon the <b>SectionType </b>member of the <a href="..\ntddk\ns-ntddk--whea-error-record-section-descriptor.md">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a> structure that is referenced through the <i>SectionDescriptor </i>parameter. For example, if the <b>SectionType </b>member has the value PROCESSOR_GENERIC_ERROR_SECTION_GUID, the hardware error data is formatted as a <a href="..\ntddk\ns-ntddk--whea-processor-generic-error-section.md">WHEA_PROCESSOR_GENERIC_ERROR_SECTION</a> structure.</p>

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
<a href="whea.whea_error_packet">WHEA_ERROR_PACKET</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--whea-error-record.md">WHEA_ERROR_RECORD</a>
</dt>
<dt>
<a href="..\ntddk\ns-ntddk--whea-error-record-section-descriptor.md">WHEA_ERROR_RECORD_SECTION_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WheaFindNextErrorRecordSection function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
