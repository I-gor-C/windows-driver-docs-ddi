---
UID: NF.engextcpp.ExtRemoteTyped.GetFieldOffset
title: ExtRemoteTyped::GetFieldOffset
author: windows-driver-content
description: The GetFieldOffset method returns the offset of a member from the base address of an instance of the type that is represented by this object.
old-location: debugger\extremotetyped_getfieldoffset.htm
ms.assetid: d74d5b61-f8e8-4ee0-83d2-cfb003189ef4
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
req.alt-api: ExtRemoteTyped.GetFieldOffset
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
ms.keywords: ExtRemoteTyped, GetFieldOffset, ExtRemoteTyped::GetFieldOffset
req.iface: ExtRemoteTyped
---

# ExtRemoteTyped::GetFieldOffset method



## -description
<p>The <b>GetFieldOffset</b> method returns the offset of a member from the base address of an instance of the type that is represented by this object.</p>


## -syntax

````
ULONG GetFieldOffset(
  [in] PCSTR Field
);
````


## -parameters
<dl>

### -param <i>Field</i> [in]

<dd>
<p>The name of the member whose offset is requested.  Sub-members can be specified using a dot-separated path (for example, <b>mymember.mysubmember</b>).</p>
</dd>
</dl>

## -returns
<p><b>GetFieldOffset</b> returns the offset of the member from the base address of an instance of the type.</p>

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
<dt>Engextcpp.hpp (include Engextcpp.hpp)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544162">ExtRemoteTyped</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546758">GetFieldOffset</a>
</dt>
<dt><b>IDebugSymbols::GetFieldOffset</b></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20ExtRemoteTyped.GetFieldOffset method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
