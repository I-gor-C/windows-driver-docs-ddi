---
UID: NF.hidport.HidRegisterMinidriver
title: HidRegisterMinidriver
author: windows-driver-content
description: The HidRegisterMinidriver routine is called by HID minidrivers, during their initialization, to register with the HID class driver.
old-location: hid\hidregisterminidriver.htm
ms.assetid: 521928f8-6434-443a-83f0-7e8e00c756b5
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: hid
req.header: hidport.h
req.include-header: Hidport.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 2000 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HidRegisterMinidriver
req.alt-loc: Hid.lib,Hid.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Hid.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: HidRegisterMinidriver
req.iface: 
---

# HidRegisterMinidriver function



## -description
<p>The <b>HidRegisterMinidriver</b> routine is called by HID minidrivers, during their initialization, to register with the HID class driver.</p>


## -syntax

````
NTSTATUS HidRegisterMinidriver(
  _In_ PHID_MINIDRIVER_REGISTRATION MinidriverRegistration
);
````


## -parameters
<dl>

### -param <i>MinidriverRegistration</i> [in]

<dd>
<p>Pointer to a caller-allocated buffer that contains an initialized <a href="https://msdn.microsoft.com/library/windows/hardware/ff539929">HID_MINIDRIVER_REGISTRATION</a> structure for the minidriver.</p>
</dd>
</dl>

## -returns
<p><b>HidRegisterMinidriver</b> returns one of the following NTSTATUS codes:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>Indicates that the routine completed without error and the minidriver is now registered with the HID class driver.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>Indicates that there was insufficient memory for the system to register the minidriver.</p><dl>
<dt><b>STATUS_REVISION_MISMATCH</b></dt>
</dl><p>Indicates that the HID revision number provided in <i>MinidriverRegistration-&gt;</i>Revision is not supported by this version of the HID class driver.</p>

<p> </p>

## -remarks
<p>Before calling this routine, HID minidrivers must initialize all members of the HID_MINIDRIVER_REGISTRATION structure that is provided at <i>MinidriverRegistration</i>. For information about these members, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff539929">HID_MINIDRIVER_REGISTRATION</a>.</p>

<p>For more information, see <a href="NULL">HID Collections</a>. </p>

<p>Before calling this routine, HID minidrivers must initialize all members of the HID_MINIDRIVER_REGISTRATION structure that is provided at <i>MinidriverRegistration</i>. For information about these members, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff539929">HID_MINIDRIVER_REGISTRATION</a>.</p>

<p>For more information, see <a href="NULL">HID Collections</a>. </p>

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
<p>Available in Windows 2000 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hidport.h (include Hidport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Hid.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539929">HID_MINIDRIVER_REGISTRATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20HidRegisterMinidriver routine%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
