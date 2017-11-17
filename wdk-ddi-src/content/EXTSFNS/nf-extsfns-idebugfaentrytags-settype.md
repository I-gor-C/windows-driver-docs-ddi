---
UID: NF.extsfns.IDebugFAEntryTags.SetType
title: IDebugFAEntryTags::SetType
author: windows-driver-content
description: The SetType method sets the data type that is associated with a tag in a DebugFailureAnalysisTags object.
old-location: debugger\idebugfaentrytags_settype.htm
ms.assetid: F507864B-B20C-4F71-B068-802780243106
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: extsfns.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugFAEntryTags.SetType
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
ms.keywords: IDebugFAEntryTags, SetType, IDebugFAEntryTags::SetType
req.iface: IDebugFAEntryTags
---

# IDebugFAEntryTags::SetType method



## -description
<p>The <b>SetType</b> method sets the data type that is associated with a tag in a <a href="https://msdn.microsoft.com/B52DFB0E-0035-40C2-B2F5-5E16B16931C2">DebugFailureAnalysisTags</a> object.</p>


## -syntax

````
HRESULT SetType(
  [in] FA_TAG        Tag,
  [in] FA_ENTRY_TYPE EntryType
);
````


## -parameters
<dl>

### -param <i>Tag</i> [in]

<dd>
<p>A value in the <a href="https://msdn.microsoft.com/library/windows/hardware/jj991810">FA_TAG</a> enumeration.</p>
</dd>

### -param <i>EntryType</i> [in]

<dd>
<p>A value in the <a href="https://msdn.microsoft.com/library/windows/hardware/jj991809">FA_ENTRY_TYPE</a> enumeration.</p>
</dd>
</dl>

## -returns
<p>If this method successfully sets the data type of <i>Tag</i> to <i>EntryType</i>, it returns <b>S_OK</b>. Otherwise, it returns <b>E_INVALIDARG</b>.</p>

## -remarks
<p>This method checks to see whether the data type for <i>Tag</i> has already been set. If the data type has not already been set, this method sets the data type to <i>EntryType</i>.</p>

<p>If the data type for <i>Tag</i> has already been set, this method checks to see whether <i>EntryType</i> is compatible with the data type that has already been set. If the data types are compatible, this method sets (overwrites) the data type for <i>Tag</i> to <i>EntryType</i>. If the data types are not compatible, this method returns <b>E_INVALIDARG</b> and does not set the data type.</p>

<p>The data types <b>DEBUG_FA_ENTRY_ULONG64</b>, <b>DEBUG_FA_ENTRY_INSTRUCTION_OFFSET</b>, and <b>DEBUG_FA_ENTRY_POINTER</b> are compatible.</p>

<p>The data types <b>DEBUG_FA_ENTRY_ANSI_STRING</b> and <b>DEBUG_FA_ENTRY_EXTENSION_CMD</b> are compatible.</p>

<p>This method checks to see whether the data type for <i>Tag</i> has already been set. If the data type has not already been set, this method sets the data type to <i>EntryType</i>.</p>

<p>If the data type for <i>Tag</i> has already been set, this method checks to see whether <i>EntryType</i> is compatible with the data type that has already been set. If the data types are compatible, this method sets (overwrites) the data type for <i>Tag</i> to <i>EntryType</i>. If the data types are not compatible, this method returns <b>E_INVALIDARG</b> and does not set the data type.</p>

<p>The data types <b>DEBUG_FA_ENTRY_ULONG64</b>, <b>DEBUG_FA_ENTRY_INSTRUCTION_OFFSET</b>, and <b>DEBUG_FA_ENTRY_POINTER</b> are compatible.</p>

<p>The data types <b>DEBUG_FA_ENTRY_ANSI_STRING</b> and <b>DEBUG_FA_ENTRY_EXTENSION_CMD</b> are compatible.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/jj983404">IDebugFAEntryTags</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj983405">IDebugFailureAnalysis2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7648F789-85D5-4247-90DD-2EAA43543483">Writing an Analysis Extension Plug-in to Extend !analyze</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj991813">GetType</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj983432">_EFN_Analyze</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugFAEntryTags::SetType method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
