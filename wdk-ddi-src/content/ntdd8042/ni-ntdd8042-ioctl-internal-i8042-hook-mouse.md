---
UID: NI.ntdd8042.IOCTL_INTERNAL_I8042_HOOK_MOUSE
title: IOCTL_INTERNAL_I8042_HOOK_MOUSE
author: windows-driver-content
description: The IOCTL_INTERNAL_I8042_HOOK_MOUSE request adds an ISR callback routine to the I8042prt mouse ISR.
old-location: hid\ioctl_internal_i8042_hook_mouse.htm
old-project: hid
ms.assetid: 606b9ae4-186c-47b1-84aa-3d380eaad672
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: MSFC_VirtualFibrePortAttributes, MSFC_VirtualFibrePortAttributes, *PMSFC_VirtualFibrePortAttributes
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntdd8042.h
req.include-header: Ntdd8042.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_INTERNAL_I8042_HOOK_MOUSE
req.alt-loc: ntdd8042.h
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
req.iface: 
---

# IOCTL_INTERNAL_I8042_HOOK_MOUSE IOCTL



## -description
<p>
<p>The IOCTL_INTERNAL_I8042_HOOK_MOUSE request adds an ISR callback routine to the I8042prt mouse ISR. The ISR callback is optional and is provided by an upper-level mouse filter driver.</p>
<p>I8042prt sends this request after it receives an <a href="..\kbdmou\ni-kbdmou-ioctl-internal-mouse-connect.md">IOCTL_INTERNAL_MOUSE_CONNECT</a> request. I8042prt sends a synchronous IOCTL_INTERNAL_I8042_HOOK_MOUSE request to the top of the mouse device stack.</p>
<p>After Moufiltr receives the hook mouse request, it filters the request in the following way:</p>
<ul>
<li>
<p>Saves the upper-level information passed to Moufiltr, which includes the context of an upper-level device object and a pointer to an ISR callback</p>
</li>
<li>
<p>Replaces the upper-level information with its own</p>
</li>
<li>
<p>Saves the context of I8042prt and pointers to callbacks that the Moufiltr ISR callbacks can use</p>
</li>
</ul>
<p>For more information about this request and the callbacks, see the following topics:</p>
<dl>
<dd>
<p>
<a href="hid.i8042prt_callback_routines">I8042prt Callback Routines</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/c6b60905-edd0-496e-a4e7-5ca271a51bce">Moufiltr Callback Routines</a>
</p>
</dd>
</dl>
</p>
<p>The IOCTL_INTERNAL_I8042_HOOK_MOUSE request adds an ISR callback routine to the I8042prt mouse ISR. The ISR callback is optional and is provided by an upper-level mouse filter driver.</p>
<p>I8042prt sends this request after it receives an <a href="..\kbdmou\ni-kbdmou-ioctl-internal-mouse-connect.md">IOCTL_INTERNAL_MOUSE_CONNECT</a> request. I8042prt sends a synchronous IOCTL_INTERNAL_I8042_HOOK_MOUSE request to the top of the mouse device stack.</p>
<p>After Moufiltr receives the hook mouse request, it filters the request in the following way:</p>
<p>Saves the upper-level information passed to Moufiltr, which includes the context of an upper-level device object and a pointer to an ISR callback</p>
<p>Replaces the upper-level information with its own</p>
<p>Saves the context of I8042prt and pointers to callbacks that the Moufiltr ISR callbacks can use</p>
<p>For more information about this request and the callbacks, see the following topics:</p>
<p>
<a href="hid.i8042prt_callback_routines">I8042prt Callback Routines</a>
</p>
<p>
<a href="https://msdn.microsoft.com/c6b60905-edd0-496e-a4e7-5ca271a51bce">Moufiltr Callback Routines</a>
</p>


## -ioctlparameters

### -input-buffer
<p>The <b>Parameters.DeviceIoControl.InputBufferLength</b> member is set to a value greater than or equal to the size, in bytes, of an <a href="..\ntdd8042\ns-ntdd8042--internal-i8042-hook-mouse.md">INTERNAL_I8042_HOOK_MOUSE</a> structure.</p>

<p>The <b>Parameters.DeviceIoControl.Type3InputBuffer</b> points to an INTERNAL_I8042_HOOK_MOUSE structure that is allocated and set initially by I8042prt.</p>

### -input-buffer-length
<p>The <b>Parameters.DeviceIoControl.Type3InputBuffer</b> points to an INTERNAL_I8042_HOOK_MOUSE structure that is allocated and set initially by I8042prt.</p>

<p>The <b>Parameters.DeviceIoControl.Type3InputBuffer</b> points to an INTERNAL_I8042_HOOK_MOUSE structure that is allocated and set initially by I8042prt.</p>

### -output-buffer
<p>None</p>

<p>None</p>

<p>None</p>

### -output-buffer-length
<p>None</p>

<p>None</p>

<p>None</p>

<p>None</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p>The request completed successfully.</p>

<p><b>Parameters.DeviceIoControl.InputBufferLength</b> is less than the size, in bytes, of an INTERNAL_I8042_HOOK_MOUSE structure.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p>The request completed successfully.</p>

<p><b>Parameters.DeviceIoControl.InputBufferLength</b> is less than the size, in bytes, of an INTERNAL_I8042_HOOK_MOUSE structure.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p>The request completed successfully.</p>

<p><b>Parameters.DeviceIoControl.InputBufferLength</b> is less than the size, in bytes, of an INTERNAL_I8042_HOOK_MOUSE structure.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p>The request completed successfully.</p>

<p><b>Parameters.DeviceIoControl.InputBufferLength</b> is less than the size, in bytes, of an INTERNAL_I8042_HOOK_MOUSE structure.</p>

<p>The <b>Status</b> member is set to one of the following values:</p>

<p></p>

<p>The request completed successfully.</p>

<p><b>Parameters.DeviceIoControl.InputBufferLength</b> is less than the size, in bytes, of an INTERNAL_I8042_HOOK_MOUSE structure.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntdd8042.h (include Ntdd8042.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntdd8042\ns-ntdd8042--internal-i8042-hook-mouse.md">INTERNAL_I8042_HOOK_MOUSE</a>
</dt>
<dt>
<a href="..\kbdmou\ni-kbdmou-ioctl-internal-mouse-connect.md">IOCTL_INTERNAL_MOUSE_CONNECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20IOCTL_INTERNAL_I8042_HOOK_MOUSE control code%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
