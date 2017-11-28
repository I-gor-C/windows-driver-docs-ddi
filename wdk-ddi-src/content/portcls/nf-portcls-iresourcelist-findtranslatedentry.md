---
UID: NF.portcls.IResourceList.FindTranslatedEntry
title: IResourceList::FindTranslatedEntry
author: windows-driver-content
description: The FindTranslatedEntry method returns a pointer to a translated entry of the specified type, or NULL if no such entry is found.
old-location: audio\iresourcelist_findtranslatedentry.htm
old-project: audio
ms.assetid: b3e8ae4d-a923-406e-ad1a-f7ed7277f676
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: IResourceList, FindTranslatedEntry, IResourceList::FindTranslatedEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IResourceList.FindTranslatedEntry
req.alt-loc: portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: IResourceList
---

# IResourceList::FindTranslatedEntry method



## -description
<p>The <code>FindTranslatedEntry</code> method returns a pointer to a translated entry of the specified type, or <b>NULL</b> if no such entry is found.</p>


## -syntax

````
PCM_PARTIAL_RESOURCE_DESCRIPTOR FindTranslatedEntry(
  [in] CM_RESOURCE_TYPE Type,
  [in] ULONG            Index
);
````


## -parameters
<dl>

### -param <i>Type</i> [in]

<dd>
<p>Identifies the resource type of the entry to find. For a list of valid resource-type values, see the <b>Type</b> member of the <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure.</p>
</dd>

### -param <i>Index</i> [in]

<dd>
<p>Specifies the index of the entry to find. If the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536988">IResourceList::NumberOfEntriesOfType</a> method returns a value <i>n</i> for the number of entries of type <i>Type</i>, valid indices range from 0 to <i>n</i>-1. If <i>Index</i> is zero, for example, the method returns a pointer to the translated version of the first occurrence of an entry of the specified type from the resource list.</p>
</dd>
</dl>

## -returns
<p><code>FindTranslatedEntry</code> returns a pointer to the specified entry or is <b>NULL</b> if the entry does not exist. This pointer remains valid until the resource list object is deleted.</p>

## -remarks
<p>For each resource type, a macro is defined to call this method. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff536976">IResourceList</a>.</p>

<p>The <i>Index</i> parameter indicates which occurrence of an entry of the specified type to find in the list of translated resource entries. The first occurrence in the list has an index of zero.</p>

<p>For each resource type, a macro is defined to call this method. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff536976">IResourceList</a>.</p>

<p>For more information about translated and untranslated (or "raw") resources, see <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a>.</p>

<p>For each resource type, a macro is defined to call this method. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff536976">IResourceList</a>.</p>

<p>The <i>Index</i> parameter indicates which occurrence of an entry of the specified type to find in the list of translated resource entries. The first occurrence in the list has an index of zero.</p>

<p>For each resource type, a macro is defined to call this method. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff536976">IResourceList</a>.</p>

<p>For more information about translated and untranslated (or "raw") resources, see <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536976">IResourceList</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536988">IResourceList::NumberOfEntriesOfType</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536984">IResourceList::FindUntranslatedEntry</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IResourceList::FindTranslatedEntry method%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
