---
UID: NF.dbgeng.IDebugClient.GetOutputLinePrefix
title: IDebugClient::GetOutputLinePrefix
author: windows-driver-content
description: Gets the prefix used for multiple lines of output.
old-location: debugger\idebugclient_getoutputlineprefix.htm
ms.assetid: FE836B10-1782-4B0E-9D4B-2740FE94B6E1
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: debugger
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugClient.GetOutputLinePrefix
req.alt-loc: dbgeng.h
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
ms.keywords: IDebugClient, GetOutputLinePrefix, IDebugClient::GetOutputLinePrefix
req.iface: IDebugClient
---

# IDebugClient::GetOutputLinePrefix method



## -description
<p>    Gets the prefix used for multiple lines of output.</p>


## -syntax

````
HRESULT GetOutputLinePrefix(
  [out]           writes_opt_(BufferSize) PSTR Buffer,
  [in]            ULONG                        BufferSize,
  [out, optional] PULONG                       PrefixSize
);
````


## -parameters
<dl>

### -param <i>Buffer</i> [out]

<dd>
<p>A pointer to the buffer to get the prefix.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>The size of the buffer.</p>
</dd>

### -param <i>PrefixSize</i> [out, optional]

<dd>
<p>A pointer to the size of the buffer.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>Some of the engine commands produce
    multiple lines of output.  A prefix can be added to each line. </p>

<p> The prefix value  is not a general setting for any output
    that contains a newline. Methods which use
    the line prefix are marked in their documentation.</p>

<p>Some of the engine commands produce
    multiple lines of output.  A prefix can be added to each line. </p>

<p> The prefix value  is not a general setting for any output
    that contains a newline. Methods which use
    the line prefix are marked in their documentation.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549827">IDebugClient</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient::GetOutputLinePrefix method%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
