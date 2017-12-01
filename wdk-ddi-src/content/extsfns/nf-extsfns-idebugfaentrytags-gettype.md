---
UID: NF.extsfns.IDebugFAEntryTags.GetType
title: IDebugFAEntryTags::GetType
author: windows-driver-content
description: The GetType method gets the data type that is associated with a tag in a DebugFailureAnalysisTags object.
old-location: debugger\idebugfaentrytags_gettype.htm
old-project: debugger
ms.assetid: CE43711F-E17B-4234-A885-4FE04EA53903
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: IDebugFAEntryTags, GetType, IDebugFAEntryTags::GetType
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
req.alt-api: IDebugFAEntryTags.GetType
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

# IDebugFAEntryTags::GetType method



## -description
<p>The <b>GetType</b> method gets the data type that is associated with a tag in a <a href="debugger.idebugfaentrytags">DebugFailureAnalysisTags</a> object.</p>


## -syntax

````
FA_ENTRY_TYPE GetType(
   FA_TAG Tag
);
````


## -parameters
<dl>

### -param <i>Tag</i> 

<dd>
<p>A value in the <a href="https://msdn.microsoft.com/library/windows/hardware/jj991810">FA_TAG</a> enumeration.</p>
</dd>
</dl>

## -returns
<p>A value in the <a href="..\extsfns\ne-extsfns--fa-entry-type.md">FA_ENTRY_TYPE</a> enumeration.</p>

## -remarks


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
<a href="debugger.idebugfaentrytags_settype">SetType</a>
</dt>
<dt>
<a href="debugger._efn_analyze">_EFN_Analyze</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugFAEntryTags::GetType method%20 RELEASE:%20(11/27/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
