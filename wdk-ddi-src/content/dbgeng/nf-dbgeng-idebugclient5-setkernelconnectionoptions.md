---
UID: NF.dbgeng.IDebugClient5.SetKernelConnectionOptions
title: IDebugClient5::SetKernelConnectionOptions
author: windows-driver-content
description: The SetKernelConnectionOptions method updates some of the connection options for a live kernel target.
old-location: debugger\setkernelconnectionoptions.htm
old-project: debugger
ms.assetid: 0633c710-20c4-49c0-a680-a5eff9298265
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugClient5, SetKernelConnectionOptions, IDebugClient5::SetKernelConnectionOptions
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
req.alt-api: IDebugClient.SetKernelConnectionOptions,IDebugClient2.SetKernelConnectionOptions,IDebugClient3.SetKernelConnectionOptions,IDebugClient4.SetKernelConnectionOptions,IDebugClient5.SetKernelConnectionOptions
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
req.iface: IDebugClient5
---

# IDebugClient5::SetKernelConnectionOptions method



## -description
<p>The <b>SetKernelConnectionOptions</b>  method updates some of the connection options for a live kernel target.</p>


## -syntax

````
HRESULT SetKernelConnectionOptions(
  [in] PCSTR Options
);
````


## -parameters
<dl>

### -param <i>Options</i> [in]

<dd>
<p>Specifies the connection options to update.  The possible values are:</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>"resync"</p>
</td>
<td>
<p>Re-synchronize the connection between the <a href="debugger.introduction#debugger_engine#debugger_engine">debugger engine</a> and the kernel.  For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558852">Synchronizing with the Target Computer</a>.</p>
</td>
</tr>
<tr>
<td>
<p>"cycle_speed"</p>
</td>
<td>
<p>For kernel connections through a COM port, cycle through the supported baud rates;  for other connections, do nothing.  For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540165">CTRL+A (Toggle Baud Rate)</a>.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_UNEXPECTED</b></dt>
</dl><p>The current target is not a live (non-local) kernel target.</p>

<p> </p>

## -remarks
<p>This method is available only for live kernel targets that are not local and not connected through eXDI.  This method is reentrant.</p>

<p>For more information about connecting to live kernel-mode targets, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552005">Live Kernel-Mode Targets</a>.</p>

<p>This method is available only for live kernel targets that are not local and not connected through eXDI.  This method is reentrant.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient::SetKernelConnectionOptions method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
