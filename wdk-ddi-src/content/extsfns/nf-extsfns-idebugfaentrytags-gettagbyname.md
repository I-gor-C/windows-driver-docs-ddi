---
UID: NF.extsfns.IDebugFAEntryTags.GetTagByName
title: IDebugFAEntryTags::GetTagByName
author: windows-driver-content
description: The GetTagByName method searches for a tag that has a specified name.
old-location: debugger\idebugfaentrytags_gettagbyname.htm
old-project: debugger
ms.assetid: 3EA8FE2A-85CE-4C81-81EB-F08028F0F822
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugFAEntryTags, GetTagByName, IDebugFAEntryTags::GetTagByName
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
req.alt-api: IDebugFAEntryTags.GetTagByName
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
req.iface: IDebugFAEntryTags
---

# IDebugFAEntryTags::GetTagByName method



## -description
<p>The <b>GetTagByName</b> method searches for a tag that has a specified name.</p>


## -syntax

````
HRESULT GetTagByName(
  [in]  PCSTR   PluginId,
  [in]  PCSTR   TagName,
  [out] FA_TAG* Tag
);
````


## -parameters
<dl>

### -param <i>PluginId</i> [in]

<dd>
<p>A pointer to a null-terminated string that specifies the identifier of an analysis extension plug-in. This parameter can be <b>NULL</b>.</p>
</dd>

### -param <i>TagName</i> [in]

<dd>
<p>A pointer to a null-terminated string that specifies the name to search for.</p>
</dd>

### -param <i>Tag</i> [out]

<dd>
<p>A pointer to a variable that receives either a value in the <a href="https://msdn.microsoft.com/library/windows/hardware/jj991810">FA_TAG</a> enumeration or the value of a custom tag. If this method does not find a tag that has the specified name, nothing is written to this parameter.</p>
</dd>
</dl>

## -returns
<p>If this method finds a tag that has the specified name, it returns <b>S_OK</b>. Otherwise it returns a failure code.</p>

## -remarks
<p>A <a href="..\extsfns\nn-extsfns-idebugfailureanalysis2.md">DebugFailureAnalysis</a> object has a collection of <a href="https://msdn.microsoft.com/759DE159-F2A8-4BB1-AAF5-B2B91C4F91B0">FA entries</a>, each of which has a tag. A <b>DebugFailureAnalysis</b> object is associated with a <a href="debugger.idebugfaentrytags">DebugFailureAnalysisTags</a>, which contains a collection of tag properties. Also, the analysis engine has a global tag table. For more information, see <a href="debugger.writing_an_analysis_extension_to_extend__analyze#failure_analysis_entries_tags_and_data_types#failure_analysis_entries_tags_and_data_types">Failure Analysis Entries, Tags, and Data Types</a>.</p>

<p>If you specify a <i>PluginId</i>, this method does the following:</p>

<p>If you call this method from an analysis extension plug-in, and you set <i>PluginId</i> to <b>NULL</b>, this method uses the plug-in identifier of the current plug-in. Then it behaves the same way that it does when a non-NULL <i>PluginId</i> is specified.</p>

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
<a href="debugger.idebugfaentrytags">IDebugFAEntryTags</a>
</dt>
<dt>
<a href="..\extsfns\nn-extsfns-idebugfailureanalysis2.md">IDebugFailureAnalysis2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7648F789-85D5-4247-90DD-2EAA43543483">Writing an Analysis Extension Plug-in to Extend !analyze</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj983428">Metadata Files for Analysis Extension Plug-ins</a>
</dt>
<dt>
<a href="debugger._efn_analyze">_EFN_Analyze</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugFAEntryTags::GetTagByName method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
