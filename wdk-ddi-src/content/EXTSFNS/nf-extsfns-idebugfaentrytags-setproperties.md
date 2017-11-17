---
UID: NF.extsfns.IDebugFAEntryTags.SetProperties
title: IDebugFAEntryTags::SetProperties
author: windows-driver-content
description: The SetProperties method sets the name or description (or both) of a tag in a DebugFailureAnalysisTags object.
old-location: debugger\idebugfaentrytags_setproperties.htm
ms.assetid: EEBD3291-4DFC-4503-9F5A-49591FE09680
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
req.alt-api: IDebugFAEntryTags.SetProperties
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
ms.keywords: IDebugFAEntryTags, SetProperties, IDebugFAEntryTags::SetProperties
req.iface: IDebugFAEntryTags
---

# IDebugFAEntryTags::SetProperties method



## -description
<p>The <b>SetProperties</b> method sets the name or description (or both) of a tag in a <a href="https://msdn.microsoft.com/B52DFB0E-0035-40C2-B2F5-5E16B16931C2">DebugFailureAnalysisTags</a> object. </p>


## -syntax

````
HRESULT SetProperties(
  [in] FA_TAG Tag,
  [in] PCSTR  Name,
  [in] PCSTR  Description,
  [in] ULONG  Flags
);
````


## -parameters
<dl>

### -param <i>Tag</i> [in]

<dd>
<p>A value in the <a href="https://msdn.microsoft.com/library/windows/hardware/jj991810">FA_TAG</a> enumeration. This method sets the name or description (or both) of this tag.</p>
</dd>

### -param <i>Name</i> [in]

<dd>
<p>A pointer to a null-terminated string that specifies the name to be set. If the tag already has a name, this method overwrites the old name. If this parameter is <b>NULL</b>, the name of the tag is not changed.</p>
</dd>

### -param <i>Description</i> [in]

<dd>
<p>A pointer to a null-terminated string that specifies the description to be set. If the tag already has a description, this method overwrites the old description. If this parameter is <b>NULL</b>, the description of the tag is not changed.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>Reserved. Set this parameter to <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>If this method succeeds, it returns <b>S_OK</b>. Otherwise it returns an error code. Error codes are defined in winerror.h and strsafe.h.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/jj983404">IDebugFAEntryTags</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj983405">IDebugFailureAnalysis2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7648F789-85D5-4247-90DD-2EAA43543483">Writing an Analysis Extension Plug-in to Extend !analyze</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj991811">GetProperties</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj983432">_EFN_Analyze</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugFAEntryTags::SetProperties method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
