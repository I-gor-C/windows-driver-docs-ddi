---
UID: NF.d3dkmthk.D3DKMTSharedPrimaryUnLockNotification
title: D3DKMTSharedPrimaryUnLockNotification
author: windows-driver-content
description: The D3DKMTSharedPrimaryUnLockNotification function notifies the operating system that a shared primary surface was unlocked.
old-location: display\d3dkmtsharedprimaryunlocknotification.htm
ms.assetid: 1d602d09-cd80-4079-9132-1caced4d1eee
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: display
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
ms.keywords: D3DKMTSharedPrimaryUnLockNotification
req.iface: 
---

# D3DKMTSharedPrimaryUnLockNotification function



## -description
<p>The <b>D3DKMTSharedPrimaryUnLockNotification</b> function notifies the operating system that a shared primary surface was unlocked.</p>


## -syntax

````
NTSTATUS APIENTRY D3DKMTSharedPrimaryUnLockNotification(
  _In_ const D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION *pData
);
````


## -parameters
<dl>

### -param <i>pData</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff548344">D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION</a> structure that describes the shared primary surface that was unlocked.</p>
</dd>
</dl>

## -returns
<p><b>D3DKMTSharedPrimaryUnLockNotification</b> returns one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>Notification about unlocking a shared primary surface was successfully performed.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>Parameters were validated and determined to be incorrect.</p>

<p> </p>

<p>This function might also return other NTSTATUS values.</p>

## -remarks
<p>The OpenGL ICD calls the <b>D3DKMTSharedPrimaryUnLockNotification</b> function to inform the operating system that an application just unlocked the GDI shared primary surface that exists on the graphics adapter and video present source that the <b>AdapterLuid</b> and <b>VidPnSourceId</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548344">D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION</a> structure specify. The OpenGL ICD should call <b>D3DKMTSharedPrimaryUnLockNotification</b> after it calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547233">D3DKMTUnlock</a> function to unlock the GDI shared primary surface.</p>

<p>The OpenGL ICD calls the <b>D3DKMTSharedPrimaryUnLockNotification</b> function to inform the operating system that an application just unlocked the GDI shared primary surface that exists on the graphics adapter and video present source that the <b>AdapterLuid</b> and <b>VidPnSourceId</b> members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548344">D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION</a> structure specify. The OpenGL ICD should call <b>D3DKMTSharedPrimaryUnLockNotification</b> after it calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff547233">D3DKMTUnlock</a> function to unlock the GDI shared primary surface.</p>

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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Gdi32.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548344">D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547233">D3DKMTUnlock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMTSharedPrimaryUnLockNotification function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
