---
UID: NF.dbgeng.IDebugClient3.GetKernelConnectionOptions
title: IDebugClient3::GetKernelConnectionOptions
author: windows-driver-content
description: The GetKernelConnectionOptions method returns the connection options for the current kernel target.
old-location: debugger\getkernelconnectionoptions.htm
old-project: debugger
ms.assetid: 2862fe26-1613-4fc2-98e1-3deb5078d1e2
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugClient3, GetKernelConnectionOptions, IDebugClient3::GetKernelConnectionOptions
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugClient.GetKernelConnectionOptions,IDebugClient2.GetKernelConnectionOptions,IDebugClient3.GetKernelConnectionOptions,IDebugClient4.GetKernelConnectionOptions,IDebugClient5.GetKernelConnectionOptions
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
req.iface: IDebugClient3
---

# IDebugClient3::GetKernelConnectionOptions method



## -description
<p>The <b>GetKernelConnectionOptions</b>  method returns the connection options for the current kernel target.</p>


## -syntax

````
HRESULT GetKernelConnectionOptions(
  [out, optional] PSTR   Buffer,
  [in]            ULONG  BufferSize,
  [out, optional] PULONG OptionsSize
);
````


## -parameters
<dl>

### -param <i>Buffer</i> [out, optional]

<dd>
<p>Specifies the buffer to receive the connection options.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>Specifies the size in characters of the buffer <i>Buffer</i>.</p>
</dd>

### -param <i>OptionsSize</i> [out, optional]

<dd>
<p>Receives the size in characters of the connection options.  If <i>OptionsSize</i> is <b>NULL</b>, this information is not returned.</p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>The size of the string was greater than the size of the buffer, so it was truncated to fit into the buffer.</p><dl>
<dt><b>E_UNEXPECTED</b></dt>
</dl><p>The current target is not a standard live kernel target.</p>

<p> </p>

## -remarks
<p>This method is available only for live kernel targets that are not local and not connected through eXDI.</p>

<p>The connection options returned are the same options used to connect to the kernel.</p>

<p>For more information about connecting to live kernel-mode targets, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552005">Live Kernel-Mode Targets</a>.</p>

<p>This method is available only for live kernel targets that are not local and not connected through eXDI.</p>

<p>The connection options returned are the same options used to connect to the kernel.</p>

<p>For more information about connecting to live kernel-mode targets, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552005">Live Kernel-Mode Targets</a>.</p>

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
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550481">IDebugClient2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550488">IDebugClient3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550494">IDebugClient4</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550497">IDebugClient5</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538145">AttachKernel</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient::GetKernelConnectionOptions method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
