---
UID: NF.ksproxy.IKsTopology.CreateNodeInstance
title: IKsTopology::CreateNodeInstance
author: windows-driver-content
description: The CreateNodeInstance method requests a KS filter object to open a topology node object.
old-location: stream\ikstopology_createnodeinstance.htm
old-project: stream
ms.assetid: 882b47c2-8fbe-4de0-8ef3-206faaf1e990
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IKsTopology, CreateNodeInstance, IKsTopology::CreateNodeInstance
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ksproxy.h
req.include-header: Ksproxy.h
req.target-type: Desktop
Mobile
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKsTopology.CreateNodeInstance
req.alt-loc: ksproxy.h
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
req.iface: IKsTopology
---

# IKsTopology::CreateNodeInstance method



## -description
<p>The <b>CreateNodeInstance</b> method requests a KS filter object to open a topology node object.</p>


## -syntax

````
HRESULT CreateNodeInstance(
  [in]           ULONG       NodeId,
  [in]           ULONG       Flags,
  [in]           ACCESS_MASK DesiredAccess,
  [in, optional] IUnknown    *UnkOuter,
  [in]           REFGUID     InterfaceId,
  [out]          LPVOID      *Interface
);
````


## -parameters
<dl>

### -param <i>NodeId</i> [in]

<dd>
<p>Identifier for the topology node object to open. </p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A bitmask enumerating the type of topology node object. No flags are currently defined.</p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a> bitmask specifying the type of access that the caller requires to the topology node object. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff566424">ZwCreateFile</a> for a description of each access-right value.</p>
</dd>

### -param <i>UnkOuter</i> [in, optional]

<dd>
<p>Pointer to an <b>IUnknown</b> interface that supports the topology node interface.</p>
</dd>

### -param <i>InterfaceId</i> [in]

<dd>
<p>Identifier of the topology node interface being requested.</p>
</dd>

### -param <i>Interface</i> [out]

<dd>
<p>Pointer to a variable that receives the interface pointer requested in <i>InterfaceId</i>. Upon successful return, *<i>Interface</i> contains the requested interface pointer to the object. If the object does not support the interface specified in <i>InterfaceId</i>, *<i>Interface</i> is set to <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p>Returns NOERROR if successful; otherwise, returns an error code.</p>

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
<dt>Mobile</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksproxy.h (include Ksproxy.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560737">IKsTopology</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566424">ZwCreateFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20IKsTopology::CreateNodeInstance method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
