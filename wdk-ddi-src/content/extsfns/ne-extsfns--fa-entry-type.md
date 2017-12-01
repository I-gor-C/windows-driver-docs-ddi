---
UID: NE.extsfns._FA_ENTRY_TYPE
title: FA_ENTRY_TYPE
author: windows-driver-content
description: A DebugFailureAnalysis object has a collection of failure analysis entries (FA entries).
old-location: debugger\fa_entry_type.htm
old-project: debugger
ms.assetid: 49E0D15E-4214-421F-9C3F-E7C7A481CA10
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: EVENT_TRACE_HEADER, EVENT_TRACE_HEADER, *PEVENT_TRACE_HEADER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: extsfns.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FA_ENTRY_TYPE
req.alt-loc: extsfns.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# FA_ENTRY_TYPE enumeration



## -description
<p>A <a href="..\extsfns\nn-extsfns-idebugfailureanalysis2.md">DebugFailureAnalysis</a> object has a collection of <a href="https://msdn.microsoft.com/library/windows/hardware/jj991807">failure analysis entries</a> (FA entries).  Each FA entry  has a tag, and each tag is associated with one of the data types in the <b>FA_ENTRY_TYPE</b> enumeration. For more information, see <a href="debugger.writing_an_analysis_extension_to_extend__analyze#failure_analysis_entries_tags_and_data_types#failure_analysis_entries_tags_and_data_types">Failure Analysis Entries, Tags, and Data Types</a>.</p>
<p>An FA entry is an <a href="..\extsfns\ns-extsfns--fa-entry.md">FA_ENTRY</a> structure along with an optional data block. The data type of the tag indicates the type of data in the data block.</p>


## -syntax

````
typedef enum _FA_ENTRY_TYPE { 
  DEBUG_FA_ENTRY_NO_TYPE,
  DEBUG_FA_ENTRY_ULONG,
  DEBUG_FA_ENTRY_ULONG64,
  DEBUG_FA_ENTRY_INSTRUCTION_OFFSET,
  DEBUG_FA_ENTRY_POINTER,
  DEBUG_FA_ENTRY_ANSI_STRING,
  DEBUG_FA_ENTRY_EXTENSION_CMD,
  DEBUG_FA_ENTRY_STRUCTURED_DATA,
  DEBUG_FA_ENTRY_UNICODE_STRING,
  DEBUG_FA_ENTRY_ARRAY               = 0x8000
} FA_ENTRY_TYPE;
````


## -enum-fields
<dl>

### -field <a id="DEBUG_FA_ENTRY_NO_TYPE"></a><a id="debug_fa_entry_no_type"></a><b>DEBUG_FA_ENTRY_NO_TYPE</b>

<dd>
<p>There is no data type associated with the tag, and there is no data block.</p>
</dd>

### -field <a id="DEBUG_FA_ENTRY_ULONG"></a><a id="debug_fa_entry_ulong"></a><b>DEBUG_FA_ENTRY_ULONG</b>

<dd>
<p>The data block holds a <b>ULONG</b> value.</p>
</dd>

### -field <a id="DEBUG_FA_ENTRY_ULONG64"></a><a id="debug_fa_entry_ulong64"></a><b>DEBUG_FA_ENTRY_ULONG64</b>

<dd>
<p>The data block holds a <b>ULONG64</b> value.</p>
</dd>

### -field <a id="DEBUG_FA_ENTRY_INSTRUCTION_OFFSET"></a><a id="debug_fa_entry_instruction_offset"></a><b>DEBUG_FA_ENTRY_INSTRUCTION_OFFSET</b>

<dd>
<p>The data block holds a 64-bit instruction offset.</p>
</dd>

### -field <a id="DEBUG_FA_ENTRY_POINTER"></a><a id="debug_fa_entry_pointer"></a><b>DEBUG_FA_ENTRY_POINTER</b>

<dd>
<p>The data block holds a 64-bit pointer.</p>
</dd>

### -field <a id="DEBUG_FA_ENTRY_ANSI_STRING"></a><a id="debug_fa_entry_ansi_string"></a><b>DEBUG_FA_ENTRY_ANSI_STRING</b>

<dd>
<p>The data block holds a null-terminated string. The <b>DataSize</b> member of the <a href="..\extsfns\ns-extsfns--fa-entry.md">FA_ENTRY</a> structure holds the size of the string including the null terminator.</p>
</dd>

### -field <a id="DEBUG_FA_ENTRY_EXTENSION_CMD"></a><a id="debug_fa_entry_extension_cmd"></a><b>DEBUG_FA_ENTRY_EXTENSION_CMD</b>

<dd>
<p>The data block holds a null-terminated string that is a debugger command. An example of a debugger command string is "!analyze -v".</p>
</dd>

### -field <a id="DEBUG_FA_ENTRY_STRUCTURED_DATA"></a><a id="debug_fa_entry_structured_data"></a><b>DEBUG_FA_ENTRY_STRUCTURED_DATA</b>

<dd>
<p>The data block holds a  pointer to an  <a href="..\extsfns\nn-extsfns-idebugfailureanalysis2.md">IDebugFailureAnalysis2</a> interface.</p>
</dd>

### -field <a id="DEBUG_FA_ENTRY_UNICODE_STRING"></a><a id="debug_fa_entry_unicode_string"></a><b>DEBUG_FA_ENTRY_UNICODE_STRING</b>

<dd>
<p>The data block holds a null-terminated Unicode string. The <b>DataSize</b> member of the <a href="..\extsfns\ns-extsfns--fa-entry.md">FA_ENTRY</a> structure holds the size of the Unicode string including the null terminator.</p>
</dd>

### -field <a id="DEBUG_FA_ENTRY_ARRAY"></a><a id="debug_fa_entry_array"></a><b>DEBUG_FA_ENTRY_ARRAY</b>

<dd>
<p>A bitwise OR of this value and one of the basic types indicates an array. For example, if the data type is <b>DEBUG_FA_ENTRY_ARRAY | DEBUG_FA_ENTRY_POINTER</b>, the data block holds an array of pointers. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Extsfns.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/7648F789-85D5-4247-90DD-2EAA43543483">Writing an Analysis Extension Plug-in to Extend !analyze</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj991807">Failure Analysis Entries</a>
</dt>
<dt>
<a href="..\extsfns\ns-extsfns--fa-entry.md">FA_ENTRY</a>
</dt>
<dt>
<a href="..\extsfns\nn-extsfns-idebugfailureanalysis2.md">IDebugFailureAnalysis2</a>
</dt>
<dt>
<a href="debugger.idebugfaentrytags">IDebugFAEntryTag</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20FA_ENTRY_TYPE enumeration%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
