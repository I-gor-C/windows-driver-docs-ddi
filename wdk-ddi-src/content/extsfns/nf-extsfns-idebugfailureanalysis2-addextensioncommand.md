---
UID: NF.extsfns.IDebugFailureAnalysis2.AddExtensionCommand
title: IDebugFailureAnalysis2::AddExtensionCommand
author: windows-driver-content
description: The AddExtensionCommand method adds a new FA entry to a DebugFailureAnalysis object and sets the data block of the FA entry to a specified debugger command.
old-location: debugger\idebugfailureanalysis2_addextensioncommand.htm
old-project: debugger
ms.assetid: 370A4EBA-80BF-46B2-8F52-9F04A4EC98D7
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugFailureAnalysis2, AddExtensionCommand, IDebugFailureAnalysis2::AddExtensionCommand
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: extsfns.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugFailureAnalysis2.AddString
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
req.iface: IDebugFailureAnalysis2
---

# IDebugFailureAnalysis2::AddExtensionCommand method



## -description
<p>The <b>AddExtensionCommand</b> method adds a new <a href="https://msdn.microsoft.com/759DE159-F2A8-4BB1-AAF5-B2B91C4F91B0">FA entry</a> to a <a href="..\extsfns\nn-extsfns-idebugfailureanalysis2.md">DebugFailureAnalysis</a> object and sets the data block of the FA entry to a specified debugger command.</p>


## -syntax

````
HRESULT AddString(
       FA_TAG Tag,
  [in] PSTR   Str
);
````


## -parameters
<dl>

### -param <i>Tag</i> 

<dd>
<p>A value in the <a href="https://msdn.microsoft.com/library/windows/hardware/jj991810">FA_TAG</a> enumeration. The data type associated with this tag must be <b>DEBUG_FA_ENTRY_EXTENSION_CMD</b> or <b>DEBUG_FA_ENTRY_ANSI_STRING</b>.</p>
</dd>

### -param <i>Str</i> [in]

<dd>
<p>A pointer to a null-terminated ANSI string that is the debugger command. An example of debugger command is "!analyze -v".</p>
</dd>
</dl>

## -returns
<p>If this method succeeds, it returns a returns a pointer to the new <a href="..\extsfns\ns-extsfns--fa-entry.md">FA_ENTRY</a> structure. If this method fails, it returns <b>NULL</b>.
</p>

## -remarks
<p>This method sets the <b>DataSize</b> member of the new <a href="..\extsfns\ns-extsfns--fa-entry.md">FA_ENTRY</a> structure to the length, in bytes, of the extension command including the <b>NULL</b> terminator.</p>

<p>Each tag is associated with one of the data types in the <a href="..\extsfns\ne-extsfns--fa-entry-type.md">FA_ENTRY_TYPE</a> enumeration. To determine the data type associated with a tag, call the <a href="debugger.idebugfaentrytags_gettype">GetType</a> method of the <a href="debugger.idebugfaentrytags">IDebugFAEntryTags</a> interface.</p>

<p>To get a pointer to an <a href="debugger.idebugfaentrytags">IDebugFAEntryTags</a> interface, call the <a href="debugger.idebugfailureanalysis2_getdebugfatagcontrol">GetDebugFATagControl</a> method of the <a href="..\extsfns\nn-extsfns-idebugfailureanalysis2.md">IDebugFailureAnalysis2</a> interface.</p>

<p>[sperry] Note to Self: If the given tag has not already had its data type fixed, this method sets and fixes the data type for the tag. That would be the case if the DebugFailureAnalysis object does not yet have an FA entry with this tag. But if the DebugFailureAnalysis object already has an FA entry with this tag, then the data type of the tag is fixed. This method creates a new FA entry with the same tag. Now what if the data type that we're trying to write into the new data buffer does not match the data type that has been fixed for this tag. Then we see whether it's OK to cast from the fixed data type to the type we want to write.</p>

<p>It's OK to cast among ULONG64, POINTER, and InstructionOffset. It's OK to cast among String and ExtensionCommand. ULONG can only be ULONG. STRINGs can only be STRINGs.</p>

<p>Question: When does the data type of a tag get fixed? Is it when the first FA entry with that tag is created?</p>

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
<a href="..\extsfns\nn-extsfns-idebugfailureanalysis2.md">IDebugFailureAnalysis2</a>
</dt>
<dt>
<a href="debugger.idebugfaentrytags">IDebugFAEntryTags</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7648F789-85D5-4247-90DD-2EAA43543483">Writing an Analysis Extension Plug-in to Extend !analyze</a>
</dt>
<dt>
<a href="debugger.idebugfailureanalysis2_setextensioncommand">SetExtensionCommand</a>
</dt>
<dt>
<a href="debugger._efn_analyze">_EFN_Analyze</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugFailureAnalysis2::AddString method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
