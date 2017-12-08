---
UID: NF.usbdlib.USBD_UrbFree
title: USBD_UrbFree function
author: windows-driver-content
description: The USBD_UrbFree routine releases the URB that is allocated by USBD_UrbAllocate, USBD_IsochUrbAllocate, USBD_SelectConfigUrbAllocateAndBuild, or USBD_SelectInterfaceUrbAllocateAndBuild.
old-location: buses\usbd_urbfree.htm
old-project: usbref
ms.assetid: DD80BAA0-EC01-4231-827A-962580D1E201
ms.author: windowsdriverdev
ms.date: 12/6/2017
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
req.product: Windows 10 or later.
---

# USBD_UrbFree function



## -description
The <b>USBD_UrbFree</b> routine releases the <a href="buses.urb">URB</a> that is allocated by <a href="buses.usbd_urballocate">USBD_UrbAllocate</a>, <a href="buses.usbd_isochurballocate">USBD_IsochUrbAllocate</a>, <a href="buses.usbd_selectconfigurballocateandbuild">USBD_SelectConfigUrbAllocateAndBuild</a>, or 
    <a href="buses.usbd_selectinterfaceurballocateandbuild">USBD_SelectInterfaceUrbAllocateAndBuild</a>.


## -syntax

````
void USBD_UrbFree(
  _In_ USBD_HANDLE USBDHandle,
  _In_ PURB        Urb
);
````


## -parameters

### -param USBDHandle [in]

USBD handle that is retrieved by the client driver in a previous call to  the <a href="buses.usbd_register">USBD_CreateHandle</a> routine.

### -param Urb [in]

Pointer to the <a href="buses.urb">URB</a> structure to be released.

## -returns
This routine does not return a value.

## -remarks
You must call <b>USBD_UrbFree</b> to release the URB allocated by <a href="buses.usbd_urballocate">USBD_UrbAllocate</a> after the request is complete. 

Failure to call <b>USBD_UrbFree</b> can cause a memory leak. 

For a code example, see <a href="buses.usbd_urballocate">USBD_UrbAllocate</a>.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Requires WDK for Windows 8. Targets Windows Vista and later versions of the Windows operating system.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Usbdlib.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Usbdex.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;=DISPATCH_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.usbd_urballocate">USBD_UrbAllocate</a>
</dt>
<dt>
<a href="buses.how_to_add_xrb_support_for_client_drivers">Allocating and Building URBs</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBD_UrbFree routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
