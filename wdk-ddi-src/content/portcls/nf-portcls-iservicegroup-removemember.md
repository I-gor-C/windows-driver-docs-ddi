---
UID: NF.portcls.IServiceGroup.RemoveMember
title: IServiceGroup::RemoveMember
author: windows-driver-content
description: The RemoveMember method removes the specified member from the service group.
old-location: audio\iservicegroup_removemember.htm
old-project: audio
ms.assetid: f257c861-036b-44d1-9f99-dc5c0ab6e715
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IServiceGroup, RemoveMember, IServiceGroup::RemoveMember
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
req.alt-api: IServiceGroup.RemoveMember
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
req.iface: IServiceGroup
---

# IServiceGroup::RemoveMember method



## -description
<p>The <code>RemoveMember</code> method removes the specified member from the service group.</p>


## -syntax

````
void RemoveMember(
  [in] PSERVICESINK pServiceSink
);
````


## -parameters
<dl>

### -param <i>pServiceSink</i> [in]

<dd>
<p>Pointer to the <a href="..\portcls\nn-portcls-iservicesink.md">IServiceSink</a> interface of the member that is to be removed</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <code>RemoveMember</code> method removes a service sink that was previously added to the service group by an <b>AddMember</b> call. The <b>AddMember</b> method called <b>AddRef</b> on the service sink object, and the <code>RemoveMember</code> method calls <b>Release</b> on the service sink object. This behavior is in accordance with the <a href="NULL">reference-counting conventions for COM objects</a>.</p>

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
<a href="..\portcls\nn-portcls-iservicegroup.md">IServiceGroup</a>
</dt>
<dt>
<a href="..\portcls\nn-portcls-iservicesink.md">IServiceSink</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IServiceGroup::RemoveMember method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
