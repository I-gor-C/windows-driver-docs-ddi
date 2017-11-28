---
UID: NF.ks.KsFilterCreateNode
title: KsFilterCreateNode
author: windows-driver-content
description: The KsFilterCreateNode function creates a new topology node on the specified filter.
old-location: stream\ksfiltercreatenode.htm
old-project: stream
ms.assetid: 2a796bb9-7d55-47da-9a57-2829cd193e23
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsFilterCreateNode
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsFilterCreateNode
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# KsFilterCreateNode function



## -description
<p>The<b> KsFilterCreateNode</b> function creates a new topology node on the specified filter.</p>


## -syntax

````
KSDDKAPI NTSTATUS NTAPI KsFilterCreateNode(
  _In_        PKSFILTER         Filter,
  _In_  const KSNODE_DESCRIPTOR *NodeDescriptor,
  _Out_       PULONG            NodeID
);
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff562522">KSFILTER</a> structure on which to create a new topology node.</p>
</dd>

### -param <i>NodeDescriptor</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563473">KSNODE_DESCRIPTOR</a> structure that describes the new node.</p>
</dd>

### -param <i>NodeID</i> [out]

<dd>
<p>A pointer to a ULONG where AVStream places the ID of the new node.</p>
</dd>
</dl>

## -returns
<p><b>KsFilterCreateNode</b>  returns the success or failure of creating the node. The call may fail because of invalid parameters, low memory, or other reasons.</p>

## -remarks
<p>Note that the filter control mutex must be held before calling this function. For more information, see <a href="NULL">Filter Control Mutex in AVStream</a>.</p>

<p>Note that the filter control mutex must be held before calling this function. For more information, see <a href="NULL">Filter Control Mutex in AVStream</a>.</p>

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
<dt>Ks.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562529">KsFilterCreatePinFactory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFilterCreateNode function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
