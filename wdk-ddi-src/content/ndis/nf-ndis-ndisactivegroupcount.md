---
UID: NF.ndis.NdisActiveGroupCount
title: NdisActiveGroupCount
author: windows-driver-content
description: The NdisActiveGroupCount function returns the number of processor groups that are currently active in the local computer system.
old-location: netvista\ndisactivegroupcount.htm
old-project: netvista
ms.assetid: f9dbeede-b4f2-4748-8a95-692f09ded787
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisActiveGroupCount
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisActiveGroupCount
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: Any level
req.iface: 
---

# NdisActiveGroupCount function



## -description
<p>The
  <b>NdisActiveGroupCount</b> function returns the number of processor groups that are currently active in the
  local computer system.</p>


## -syntax

````
USHORT NdisActiveGroupCount(void);
````


## -parameters


## -returns
<p><b>NdisActiveGroupCount</b> returns a USHORT value for the number of processor groups that are currently
     active and are included in the local computer system. The number of groups is a zero-based value.</p>

<p><b>NdisActiveGroupCount</b> returns a USHORT value for the number of processor groups that are currently
     active and are included in the local computer system. The number of groups is a zero-based value.</p>

<p><b>NdisActiveGroupCount</b> returns a USHORT value for the number of processor groups that are currently
     active and are included in the local computer system. The number of groups is a zero-based value.</p>

## -remarks
<p>NDIS drivers call the 
    <b>NdisActiveGroupCount</b> function to obtain the number of processor groups that are currently active
    and are included in the local computer system.</p>

<p>To obtain the maximum number of groups, call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562786">NdisMaxGroupCount</a> function.</p>

<p>NDIS drivers call the 
    <b>NdisActiveGroupCount</b> function to obtain the number of processor groups that are currently active
    and are included in the local computer system.</p>

<p>To obtain the maximum number of groups, call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562786">NdisMaxGroupCount</a> function.</p>

<p>NDIS drivers call the 
    <b>NdisActiveGroupCount</b> function to obtain the number of processor groups that are currently active
    and are included in the local computer system.</p>

<p>To obtain the maximum number of groups, call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562786">NdisMaxGroupCount</a> function.</p>

<p>NDIS drivers call the 
    <b>NdisActiveGroupCount</b> function to obtain the number of processor groups that are currently active
    and are included in the local computer system.</p>

<p>To obtain the maximum number of groups, call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562786">NdisMaxGroupCount</a> function.</p>

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
<p>Supported in NDIS 6.20 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562786">NdisMaxGroupCount</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisActiveGroupCount function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
