---
UID: NF.engextcpp.ExtRemoteList.HasNode
title: ExtRemoteList::HasNode
author: windows-driver-content
description: The HasNode method determines if there is a current item in the list iteration.
old-location: debugger\extremotelist_hasnode.htm
ms.assetid: 412a77c8-eb10-43c5-bc45-2c61858463a7
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: engextcpp.hpp
req.include-header: Engextcpp.hpp
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExtRemoteList.HasNode
req.alt-loc: engextcpp.hpp
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
ms.keywords: ExtRemoteList, HasNode, ExtRemoteList::HasNode
req.iface: ExtRemoteList
---

# ExtRemoteList::HasNode method



## -description
<p>The <b>HasNode</b> method determines if there is a current item in the list iteration.</p>


## -syntax

````
bool HasNode();
````


## -parameters


## -returns
<p><b>HasNode</b> returns <code>true</code> if there is a current item in the list iteration, and <code>false</code> otherwise.</p>

<p><b>HasNode</b> returns <code>true</code> if there is a current item in the list iteration, and <code>false</code> otherwise.</p>

<p><b>HasNode</b> returns <code>true</code> if there is a current item in the list iteration, and <code>false</code> otherwise.</p>

## -remarks
<p>Before you call <b>HasNode</b>, you must initialize the list for iteration by calling <a href="https://msdn.microsoft.com/d7d9163b-54bb-4753-96a3-f92eddbe25f5">StartHead</a> or <a href="https://msdn.microsoft.com/fe9aec87-a464-4ea9-b9ca-3dbb91bb4e3e">StartTail</a>.</p>

<p>If this method returns <code>true</code>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544129">ExtRemoteList::GetNodeOffset</a> can be used to return the current item in the list.</p>

<p>Before you call <b>HasNode</b>, you must initialize the list for iteration by calling <a href="https://msdn.microsoft.com/d7d9163b-54bb-4753-96a3-f92eddbe25f5">StartHead</a> or <a href="https://msdn.microsoft.com/fe9aec87-a464-4ea9-b9ca-3dbb91bb4e3e">StartTail</a>.</p>

<p>If this method returns <code>true</code>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544129">ExtRemoteList::GetNodeOffset</a> can be used to return the current item in the list.</p>

<p>Before you call <b>HasNode</b>, you must initialize the list for iteration by calling <a href="https://msdn.microsoft.com/d7d9163b-54bb-4753-96a3-f92eddbe25f5">StartHead</a> or <a href="https://msdn.microsoft.com/fe9aec87-a464-4ea9-b9ca-3dbb91bb4e3e">StartTail</a>.</p>

<p>If this method returns <code>true</code>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544129">ExtRemoteList::GetNodeOffset</a> can be used to return the current item in the list.</p>

<p>Before you call <b>HasNode</b>, you must initialize the list for iteration by calling <a href="https://msdn.microsoft.com/d7d9163b-54bb-4753-96a3-f92eddbe25f5">StartHead</a> or <a href="https://msdn.microsoft.com/fe9aec87-a464-4ea9-b9ca-3dbb91bb4e3e">StartTail</a>.</p>

<p>If this method returns <code>true</code>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff544129">ExtRemoteList::GetNodeOffset</a> can be used to return the current item in the list.</p>

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
<dt>Engextcpp.hpp (include Engextcpp.hpp)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544114">ExtRemoteList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544129">ExtRemoteList::GetNodeOffset</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20ExtRemoteList.HasNode method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
