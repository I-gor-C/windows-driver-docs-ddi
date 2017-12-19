---
UID: NF.extsfns.IDebugFAEntryTags.SetProperties
title: IDebugFAEntryTags::SetProperties method
author: windows-driver-content
description: The SetProperties method sets the name or description (or both) of a tag in a DebugFailureAnalysisTags object.
old-location: debugger\idebugfaentrytags_setproperties.htm
old-project: Debugger
ms.assetid: EEBD3291-4DFC-4503-9F5A-49591FE09680
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IDebugFAEntryTags, IDebugFAEntryTags::SetProperties, SetProperties
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
---

# IDebugFAEntryTags::SetProperties method



## -description
The <b>SetProperties</b> method sets the name or description (or both) of a tag in a <a href="debugger.idebugfaentrytags">DebugFailureAnalysisTags</a> object. 



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

### -param Tag [in]

A value in the <a href="https://msdn.microsoft.com/library/windows/hardware/jj991810">FA_TAG</a> enumeration. This method sets the name or description (or both) of this tag.


### -param Name [in]

A pointer to a null-terminated string that specifies the name to be set. If the tag already has a name, this method overwrites the old name. If this parameter is <b>NULL</b>, the name of the tag is not changed.


### -param Description [in]

A pointer to a null-terminated string that specifies the description to be set. If the tag already has a description, this method overwrites the old description. If this parameter is <b>NULL</b>, the description of the tag is not changed.


### -param Flags [in]

Reserved. Set this parameter to <b>NULL</b>.


## -returns
If this method succeeds, it returns <b>S_OK</b>. Otherwise it returns an error code. Error codes are defined in winerror.h and strsafe.h.


## -remarks


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
<a href="debugger.idebugfaentrytags">IDebugFAEntryTags</a>
</dt>
<dt>
<a href="..\extsfns\nn-extsfns-idebugfailureanalysis2.md">IDebugFailureAnalysis2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7648F789-85D5-4247-90DD-2EAA43543483">Writing an Analysis Extension Plug-in to Extend !analyze</a>
</dt>
<dt>
<a href="debugger.idebugfaentrytags_getproperties">GetProperties</a>
</dt>
<dt>
<a href="debugger._efn_analyze">_EFN_Analyze</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Debugger\debugger]:%20IDebugFAEntryTags::SetProperties method%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

