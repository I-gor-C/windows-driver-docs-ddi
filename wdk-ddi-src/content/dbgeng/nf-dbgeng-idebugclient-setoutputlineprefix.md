---
UID: NF.dbgeng.IDebugClient.SetOutputLinePrefix
title: IDebugClient::SetOutputLinePrefix
author: windows-driver-content
description: Sets a prefix for multiple lines of output.
old-location: debugger\idebugclient_setoutputlineprefix.htm
old-project: debugger
ms.assetid: 59A3FD7D-153D-4580-84C1-2408A485F684
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugClient, SetOutputLinePrefix, IDebugClient::SetOutputLinePrefix
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugClient.SetOutputLinePrefix
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
req.iface: IDebugClient
---

# IDebugClient::SetOutputLinePrefix method



## -description
<p>    Sets a prefix for multiple lines of output. </p>


## -syntax

````
HRESULT SetOutputLinePrefix(
  [in, optional] PCSTR Prefix
);
````


## -parameters
<dl>

### -param <i>Prefix</i> [in, optional]

<dd>
<p>A pointer to the prefix value.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p>

<p> </p>

## -remarks
<p>Some of the engine commands produce
    multiple lines of output.  This function sets a prefix that the engine adds to each line. This function allows the caller to control indentation or identifying marks.
</p>

<p> The prefix value  is not a general setting for any output
    that contains a newline. Methods which use
    the line prefix are marked in their documentation.</p>

<p>Some of the engine commands produce
    multiple lines of output.  This function sets a prefix that the engine adds to each line. This function allows the caller to control indentation or identifying marks.
</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient::SetOutputLinePrefix method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
