---
UID: NS.d3dkmthk._D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION
title: D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION
author: windows-driver-content
description: The D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION structure describes the shared primary surface that an application just unlocked.
old-location: display\d3dkmt_sharedprimaryunlocknotification.htm
old-project: display
ms.assetid: 294fe805-4dce-4d0e-b0dd-9279a1ef9514
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION, D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION
req.alt-loc: d3dkmthk.h
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

# D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION structure



## -description
<p>The D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION structure describes the shared primary surface that an application just unlocked.</p>


## -syntax

````
typedef struct _D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION {
  LUID                           AdapterLuid;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
} D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION;
````


## -struct-fields
<dl>

### -field <b>AdapterLuid</b>

<dd>
<p>[in] The locally unique identifier (<a href="https://msdn.microsoft.com/library/windows/hardware/ff557080">LUID</a>) of the graphics adapter on which the GDI shared primary surface exists.</p>
</dd>

### -field <b>VidPnSourceId</b>

<dd>
<p>[in] The zero-based identification number of the video present source in a path of a video present network (VidPN) topology on which the GDI shared primary surface exists.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547214">D3DKMTSharedPrimaryUnLockNotification</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_SHAREDPRIMARYUNLOCKNOTIFICATION structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
