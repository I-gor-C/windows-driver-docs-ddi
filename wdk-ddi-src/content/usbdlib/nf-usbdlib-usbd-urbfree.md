---
UID: NF.usbdlib.USBD_UrbFree
title: USBD_UrbFree
author: windows-driver-content
description: The USBD_UrbFree routine releases the URB that is allocated by USBD_UrbAllocate, USBD_IsochUrbAllocate, USBD_SelectConfigUrbAllocateAndBuild, or USBD_SelectInterfaceUrbAllocateAndBuild.
old-location: buses\usbd_urbfree.htm
old-project: usbref
ms.assetid: DD80BAA0-EC01-4231-827A-962580D1E201
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBD_UrbFree
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: usbdlib.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Requires WDK for Windows 8. Targets Windows Vista and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBD_UrbFree
req.alt-loc: Usbdex.lib,Usbdex.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Usbdex.lib
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# USBD_UrbFree function



## -description
<p>The <b>USBD_UrbFree</b> routine releases the <a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a> that is allocated by <a href="https://msdn.microsoft.com/library/windows/hardware/hh406250">USBD_UrbAllocate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh406231">USBD_IsochUrbAllocate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh406243">USBD_SelectConfigUrbAllocateAndBuild</a>, or 
    <a href="https://msdn.microsoft.com/library/windows/hardware/hh406245">USBD_SelectInterfaceUrbAllocateAndBuild</a>.</p>


## -syntax

````
void USBD_UrbFree(
  _In_ USBD_HANDLE USBDHandle,
  _In_ PURB        Urb
);
````


## -parameters
<dl>

### -param <i>USBDHandle</i> [in]

<dd>
<p>USBD handle that is retrieved by the client driver in a previous call to  the <a href="https://msdn.microsoft.com/library/windows/hardware/hh406241">USBD_CreateHandle</a> routine.</p>
</dd>

### -param <i>Urb</i> [in]

<dd>
<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff538923">URB</a> structure to be released.</p>
</dd>
</dl>

## -returns
<p>This routine does not return a value.</p>

## -remarks
<p>You must call <b>USBD_UrbFree</b> to release the URB allocated by <a href="https://msdn.microsoft.com/library/windows/hardware/hh406250">USBD_UrbAllocate</a> after the request is complete. </p>

<p>Failure to call <b>USBD_UrbFree</b> can cause a memory leak. </p>

<p>For a code example, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh406250">USBD_UrbAllocate</a>.</p>

<p>You must call <b>USBD_UrbFree</b> to release the URB allocated by <a href="https://msdn.microsoft.com/library/windows/hardware/hh406250">USBD_UrbAllocate</a> after the request is complete. </p>

<p>Failure to call <b>USBD_UrbFree</b> can cause a memory leak. </p>

<p>For a code example, see <a href="https://msdn.microsoft.com/library/windows/hardware/hh406250">USBD_UrbAllocate</a>.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Requires WDK for Windows 8. Targets Windows Vista and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbdlib.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Usbdex.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406250">USBD_UrbAllocate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450844">Allocating and Building URBs</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBD_UrbFree routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
