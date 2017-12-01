---
UID: NF.video.VideoPortGetVersion
title: VideoPortGetVersion
author: windows-driver-content
description: The VideoPortGetVersion function gets version information about the currently running operating system.
old-location: display\videoportgetversion.htm
old-project: display
ms.assetid: 242eb066-4b2e-4abe-b082-5bfd814c5774
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortGetVersion
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortGetVersion
req.alt-loc: Videoprt.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Videoprt.lib
req.dll: Videoprt.sys
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortGetVersion function



## -description
<p>The <b>VideoPortGetVersion</b> function gets version information about the currently running operating system.</p>


## -syntax

````
VP_STATUS VideoPortGetVersion(
  _In_    PVOID            HwDeviceExtension,
  _Inout_ PVPOSVERSIONINFO pVpOsVersionInfo
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>pVpOsVersionInfo</i> [in, out]

<dd>
<p>Pointer to a <a href="..\video\ns-video--vposversioninfo.md">VPOSVERSIONINFO</a> structure that will receive the operating system version information. The caller should set the <b>Size</b> member of the VPOSVERSIONINFO structure to the size, in bytes, of that structure.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortGetVersionInfo</b> returns NO_ERROR if it successfully obtained the operating system version information. If the <b>Size</b> member of the VPOSVERSIONINFO does not contains the correct size of this structure, the function returns ERROR_INVALID_PARAMETER </p>

## -remarks


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
<p>Available in Windows XP and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\video\ns-video--vposversioninfo.md">VPOSVERSIONINFO</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VideoPortGetVersion function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
