---
UID: NF.portcls.IResourceList.AddEntryFromParent
title: IResourceList::AddEntryFromParent
author: windows-driver-content
description: The AddEntryFromParent method adds to a resource list an entry found in the resource list's parent list.
old-location: audio\iresourcelist_addentryfromparent.htm
ms.assetid: 83733c17-1f1f-4be6-ae14-aa921e481a73
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: audio
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IResourceList.AddEntryFromParent
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
ms.keywords: IResourceList, AddEntryFromParent, IResourceList::AddEntryFromParent
req.iface: IResourceList
---

# IResourceList::AddEntryFromParent method



## -description
<p>The <code>AddEntryFromParent</code> method adds to a resource list an entry found in the resource list's parent list.</p>


## -syntax

````
NTSTATUS AddEntryFromParent(
  [in] struct IResourceList *Parent,
  [in] CM_RESOURCE_TYPE     Type,
  [in] ULONG                Index
);
````


## -parameters
<dl>

### -param <i>Parent</i> [in]

<dd>
<p>Pointer to parent <b>IResourceList</b> object from which the entry is to be taken.</p>
</dd>

### -param <i>Type</i> [in]

<dd>
<p>Identifies the resource type of the entry that is to be added. For a list of valid resource-type values, see the description of the <b>Type</b> member of the <a href="https://msdn.microsoft.com/96bf7bab-b8f5-439c-8717-ea6956ed0213">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure.</p>
</dd>

### -param <i>Index</i> [in]

<dd>
<p>Specifies the index in the parent list of the entry to add. If the parent's <a href="https://msdn.microsoft.com/library/windows/hardware/ff536988">IResourceList::NumberOfEntriesOfType</a> method returns a value <i>n</i> for the number of entries of type <i>Type</i>, valid indices range from 0 to <i>n</i>-1. If <i>Index</i> is zero, for example, the method adds the first occurrence of an entry of the specified type from the parent list.</p>
</dd>
</dl>

## -returns
<p><code>AddEntryFromParent</code> returns STATUS_SUCCESS if the call was successful. Otherwise, the method returns an appropriate error code. The following table shows some of the possible return status codes.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Indicates there are no free entries in the list.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Indicates the entry was not found in the parent list.</p>

<p> </p>

## -remarks
<p>For each resource type, a macro is defined to call this method. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff536976">IResourceList</a>.</p>

<p>The <i>Parent</i> parameter follows the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

<p>For each resource type, a macro is defined to call this method. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff536976">IResourceList</a>.</p>

<p>The <i>Parent</i> parameter follows the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

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
<a href="https://msdn.microsoft.com/96bf7bab-b8f5-439c-8717-ea6956ed0213">CM_PARTIAL_RESOURCE_DESCRIPTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536988">IResourceList::NumberOfEntriesOfType</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IResourceList::AddEntryFromParent method%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
