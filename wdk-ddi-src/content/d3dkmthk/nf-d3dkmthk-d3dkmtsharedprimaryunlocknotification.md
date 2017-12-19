---
UID: NF.d3dkmthk.D3DKMTSharedPrimaryUnLockNotification
title: D3DKMTSharedPrimaryUnLockNotification function
author: windows-driver-content
description: The D3DKMTSharedPrimaryUnLockNotification function notifies the operating system that a shared primary surface was unlocked.
old-location: display\d3dkmtsharedprimaryunlocknotification.htm
old-project: display
ms.assetid: 1d602d09-cd80-4079-9132-1caced4d1eee
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: D3DKMTSharedPrimaryUnLockNotification
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTSharedPrimaryUnLockNotification
req.alt-loc: Gdi32.dll,API-MS-Win-dx-d3dkmt-l1-1-0.dll,API-MS-Win-dx-d3dkmt-l1-1-1.dll,API-MS-Win-DX-D3DKMT-L1-1-2.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Gdi32.lib
req.dll: Gdi32.dll
req.irql: 
---

# D3DKMTSharedPrimaryUnLockNotification function



## -description
The <b>D3DKMTSharedPrimaryUnLockNotification</b> function notifies the operating system that a shared primary surface was unlocked.



## -syntax

````
NTSTATUS APIENTRY D3DKMTSharedPrimaryUnLockNotification(
  _In_ const D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION *pData
);
````


## -parameters

### -param pData [in]

A pointer to a <a href="display.d3dkmt_sharedprimaryunlocknotification">D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION</a> structure that describes the shared primary surface that was unlocked.


## -returns
<b>D3DKMTSharedPrimaryUnLockNotification</b> returns one of the following values:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>Notification about unlocking a shared primary surface was successfully performed.
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>Parameters were validated and determined to be incorrect.

 

This function might also return other NTSTATUS values.


## -remarks
The OpenGL ICD calls the <b>D3DKMTSharedPrimaryUnLockNotification</b> function to inform the operating system that an application just unlocked the GDI shared primary surface that exists on the graphics adapter and video present source that the <b>AdapterLuid</b> and <b>VidPnSourceId</b> members of the <a href="display.d3dkmt_sharedprimaryunlocknotification">D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION</a> structure specify. The OpenGL ICD should call <b>D3DKMTSharedPrimaryUnLockNotification</b> after it calls the <a href="display.d3dkmtunlock">D3DKMTUnlock</a> function to unlock the GDI shared primary surface.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows Vista and later versions of the Windows operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Gdi32.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>Gdi32.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.d3dkmt_sharedprimaryunlocknotification">D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION</a>
</dt>
<dt>
<a href="display.d3dkmtunlock">D3DKMTUnlock</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMTSharedPrimaryUnLockNotification function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

