---
UID: NF.portcls.PcNewResourceSublist
title: PcNewResourceSublist
author: windows-driver-content
description: The PcNewResourceSublist function creates and initializes an empty resource list that is derived from another resource list.
old-location: audio\pcnewresourcesublist.htm
ms.assetid: a7e1a7cf-60ea-4489-a1c2-eac5b218af8c
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: audio
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: The PortCls system driver implements the PcNewResourceSublist function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PcNewResourceSublist
req.alt-loc: Portcls.lib,Portcls.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Portcls.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: PcNewResourceSublist
req.iface: 
---

# PcNewResourceSublist function



## -description
<p>The <b>PcNewResourceSublist</b> function creates and initializes an empty resource list that is derived from another resource list.</p>


## -syntax

````
NTSTATUS PcNewResourceSublist(
  _Out_    PRESOURCELIST *OutResourceList,
  _In_opt_ PUNKNOWN      OuterUnknown,
  _In_     POOL_TYPE     PoolType,
  _In_     PRESOURCELIST ParentList,
  _In_     ULONG         MaximumEntries
);
````


## -parameters
<dl>

### -param <i>OutResourceList</i> [out]

<dd>
<p>Output pointer to the resource-list object that this function creates. This parameter points to the caller-allocated pointer variable into which the function outputs the pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536976">IResourceList</a> object. Specify a valid, non-<b>NULL</b> pointer value for this parameter.</p>
</dd>

### -param <i>OuterUnknown</i> [in, optional]

<dd>
<p>Pointer to the <a href="com.iunknown">IUnknown</a> interface of an object that needs to aggregate the object. Unless aggregation is required, set this parameter to <b>NULL</b>.</p>
</dd>

### -param <i>PoolType</i> [in]

<dd>
<p>Specifies the type of pool from which the object is to be allocated. This is a <a href="https://msdn.microsoft.com/library/windows/hardware/ff559707">POOL_TYPE</a> enumeration value.</p>
</dd>

### -param <i>ParentList</i> [in]

<dd>
<p>Pointer to the resource list from which the child list will be created. The resource list has an <a href="https://msdn.microsoft.com/library/windows/hardware/ff536976">IResourceList</a> interface.</p>
</dd>

### -param <i>MaximumEntries</i> [in]

<dd>
<p>Specifies the maximum number of entries that will be added to the resource list.</p>
</dd>
</dl>

## -returns
<p><b>PcNewResourceSublist</b> returns STATUS_SUCCESS if the call was successful. Otherwise, it returns an appropriate error code.</p>

## -remarks
<p>This function creates an empty resource sublist.</p>

<p>An adapter driver typically uses the <b>PcNewResourceSublist</b> function in combination with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536981">IResourceList::AddEntryFromParent</a> method to take the original list of resources that it received from the system and divide them up into sublists that it assigns to its various subdevices.</p>

<p>The <i>OutResourceList</i>, <i>OuterUnknown</i>, and <i>ParentList</i> parameters follow the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

<p>This function creates an empty resource sublist.</p>

<p>An adapter driver typically uses the <b>PcNewResourceSublist</b> function in combination with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536981">IResourceList::AddEntryFromParent</a> method to take the original list of resources that it received from the system and divide them up into sublists that it assigns to its various subdevices.</p>

<p>The <i>OutResourceList</i>, <i>OuterUnknown</i>, and <i>ParentList</i> parameters follow the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>The PortCls system driver implements the PcNewResourceSublist function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.</p>
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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559707">POOL_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536981">IResourceList::AddEntryFromParent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PcNewResourceSublist function%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
