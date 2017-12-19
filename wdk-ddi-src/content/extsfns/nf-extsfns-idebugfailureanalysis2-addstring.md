---
UID: NF.extsfns.IDebugFailureAnalysis2.AddString
title: IDebugFailureAnalysis2::AddString method
author: windows-driver-content
description: The AddString method adds a new FA entry to a DebugFailureAnalysis object and sets the data block of the FA entry to a specified string.
old-location: debugger\idebugfailureanalysis2_addstring.htm
old-project: Debugger
ms.assetid: 98023A9B-9091-4C0D-ADE0-978816E8F762
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IDebugFailureAnalysis2, IDebugFailureAnalysis2::AddString, AddString
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
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
---

# IDebugFailureAnalysis2::AddString method



## -description
The <b>AddString</b> method adds a new <a href="https://msdn.microsoft.com/759DE159-F2A8-4BB1-AAF5-B2B91C4F91B0">FA entry</a> to a <a href="..\extsfns\nn-extsfns-idebugfailureanalysis2.md">DebugFailureAnalysis</a> object and sets the data block of the FA entry to a specified string.



## -syntax

````
HRESULT AddString(
       FA_TAG Tag,
  [in] PSTR   Str
);
````


## -parameters

### -param Tag 

A value in the <a href="https://msdn.microsoft.com/library/windows/hardware/jj991810">FA_TAG</a> enumeration. The data type associated with this tag must be <b>DEBUG_FA_ENTRY_ANSI_STRING</b>.


### -param Str [in]

A pointer to a null-terminated ANSI string to be written to the data block of the new <a href="https://msdn.microsoft.com/759DE159-F2A8-4BB1-AAF5-B2B91C4F91B0">FA entry</a>.


## -returns
If this method succeeds, it returns a returns a pointer to the new <a href="debugger.fa_entry">FA_ENTRY</a> structure. If this method fails, it returns <b>NULL</b>.



## -remarks
This method sets the <b>DataSize</b> member of the new <a href="debugger.fa_entry">FA_ENTRY</a> structure to the length, in bytes, of the string including the <b>NULL</b> terminator.

Each tag is associated with one of the data types in the <a href="debugger.fa_entry_type">FA_ENTRY_TYPE</a> enumeration. To determine the data type associated with a tag, call the <a href="debugger.idebugfaentrytags_gettype">GetType</a> method of the <a href="debugger.idebugfaentrytags">IDebugFAEntryTags</a> interface.

To get a pointer to an <a href="debugger.idebugfaentrytags">IDebugFAEntryTags</a> interface, call the <a href="debugger.idebugfailureanalysis2_getdebugfatagcontrol">GetDebugFATagControl</a> method of the <a href="..\extsfns\nn-extsfns-idebugfailureanalysis2.md">IDebugFailureAnalysis2</a> interface. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="debugger.idebugfailureanalysis2_getstring">GetString</a>
</dt>
<dt>
<a href="debugger.idebugfailureanalysis2_setstring">SetString</a>
</dt>
<dt>
<a href="debugger._efn_analyze">_EFN_Analyze</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20IDebugFailureAnalysis2::AddString method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

