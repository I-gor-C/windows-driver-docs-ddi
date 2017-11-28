---
UID: NF.dbgeng.IDebugClient5.IsKernelDebuggerEnabled
title: IDebugClient5::IsKernelDebuggerEnabled
author: windows-driver-content
description: The IsKernelDebuggerEnabled method checks whether kernel debugging is enabled for the local kernel.
old-location: debugger\iskerneldebuggerenabled.htm
old-project: debugger
ms.assetid: a6dc4832-6b9b-441e-a57a-6fcb2cafa2c6
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugClient5, IsKernelDebuggerEnabled, IDebugClient5::IsKernelDebuggerEnabled
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
req.alt-api: IDebugClient2.IsKernelDebuggerEnabled,IDebugClient3.IsKernelDebuggerEnabled,IDebugClient4.IsKernelDebuggerEnabled,IDebugClient5.IsKernelDebuggerEnabled
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

# IDebugClient5::IsKernelDebuggerEnabled method



## -description
<p>The <b>IsKernelDebuggerEnabled</b> method checks whether kernel debugging is enabled for the local kernel.</p>


## -syntax

````
HRESULT IsKernelDebuggerEnabled();
````


## -parameters


## -returns
<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>Kernel debugging is enabled for the local kernel.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>Kernel debugging is not enabled for the local kernel.</p>

<p> </p>

<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>Kernel debugging is enabled for the local kernel.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>Kernel debugging is not enabled for the local kernel.</p>

<p> </p>

<p>This method may also return error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>Kernel debugging is enabled for the local kernel.</p><dl>
<dt><b>S_FALSE</b></dt>
</dl><p>Kernel debugging is not enabled for the local kernel.</p>

<p> </p>

## -remarks
<p>Kernel debugging is available for the local computer if the computer was booted by using the <b>/debug</b> boot switch.  In some Windows installations, <a href="debugger.security_during_kernel_mode_debugging#local_kernel_debugging#local_kernel_debugging">local kernel debugging</a> is supported when other switches--such as <b>/debugport</b>--are used, but this is not a guaranteed feature of Windows and should not be relied on.  For more information about kernel debugging on a single computer, see <a href="https://msdn.microsoft.com/e66dc23b-9254-4148-9828-d27c30bfa492">Performing Local Kernel Debugging</a>.</p>

<p>For more information about connecting to live kernel-mode targets, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552005">Live Kernel-Mode Targets</a>.</p>

<p>Kernel debugging is available for the local computer if the computer was booted by using the <b>/debug</b> boot switch.  In some Windows installations, <a href="debugger.security_during_kernel_mode_debugging#local_kernel_debugging#local_kernel_debugging">local kernel debugging</a> is supported when other switches--such as <b>/debugport</b>--are used, but this is not a guaranteed feature of Windows and should not be relied on.  For more information about kernel debugging on a single computer, see <a href="https://msdn.microsoft.com/e66dc23b-9254-4148-9828-d27c30bfa492">Performing Local Kernel Debugging</a>.</p>

<p>For more information about connecting to live kernel-mode targets, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552005">Live Kernel-Mode Targets</a>.</p>

<p>Kernel debugging is available for the local computer if the computer was booted by using the <b>/debug</b> boot switch.  In some Windows installations, <a href="debugger.security_during_kernel_mode_debugging#local_kernel_debugging#local_kernel_debugging">local kernel debugging</a> is supported when other switches--such as <b>/debugport</b>--are used, but this is not a guaranteed feature of Windows and should not be relied on.  For more information about kernel debugging on a single computer, see <a href="https://msdn.microsoft.com/e66dc23b-9254-4148-9828-d27c30bfa492">Performing Local Kernel Debugging</a>.</p>

<p>For more information about connecting to live kernel-mode targets, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff552005">Live Kernel-Mode Targets</a>.</p>

<p>Kernel debugging is available for the local computer if the computer was booted by using the <b>/debug</b> boot switch.  In some Windows installations, <a href="debugger.security_during_kernel_mode_debugging#local_kernel_debugging#local_kernel_debugging">local kernel debugging</a> is supported when other switches--such as <b>/debugport</b>--are used, but this is not a guaranteed feature of Windows and should not be relied on.  For more information about kernel debugging on a single computer, see <a href="https://msdn.microsoft.com/e66dc23b-9254-4148-9828-d27c30bfa492">Performing Local Kernel Debugging</a>.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient2::IsKernelDebuggerEnabled method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
