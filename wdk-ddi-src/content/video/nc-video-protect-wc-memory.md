---
UID: NC.video.PROTECT_WC_MEMORY
title: PROTECT_WC_MEMORY
author: windows-driver-content
description: The VideoPortProtectWCMemory callback routine protects Write Combined (WC) video memory from being accessed by the CPU.
old-location: display\videoportprotectwcmemory.htm
old-project: display
ms.assetid: 0cee4f4d-4d9c-44be-94ad-459000f2adb1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VHF_CONFIG, VHF_CONFIG, *PVHF_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows 2000 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortProtectWCMemory
req.alt-loc: video.h
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
req.product: Windows 10 or later.
---

# PROTECT_WC_MEMORY callback



## -description
<p>The <i>VideoPortProtectWCMemory</i> callback routine protects Write Combined (WC) video memory from being accessed by the CPU.</p>


## -prototype

````
PROTECT_WC_MEMORY VideoPortProtectWCMemory;

VP_STATUS VideoPortProtectWCMemory(
  _In_ PVOID Context,
  _In_ PVOID HwDeviceExtension
)
{ ... }
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>Pointer to a caller-determined context parameter to be passed to the <i>CallbackRoutine</i>. It typically points to the <a href="..\video\ns-video--video-port-config-info.md">VIDEO_PORT_CONFIG_INFO</a> buffer.</p>
</dd>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's hardware device extension.</p>
</dd>
</dl>

## -returns
<p><i>VideoPortProtectWCMemory</i> returns NO_ERROR if it successfully protects Write Combined video memory; otherwise, it returns an error status of ERROR_INVALID_FUNCTION or ERROR_NOT_ENOUGH_MEMORY.</p>

## -remarks
<p>After <i>VideoPortProtectWCMemory</i> is called, the CPU cannot write to Write Combined (WC) memory until the <a href="..\video\nc-video-restore-wc-memory.md">VideoPortRestoreWCMemory</a> callback routine is called.</p>

<p>When WC memory protection is no longer required, the display miniport driver should call <a href="..\video\nc-video-restore-wc-memory.md">VideoPortRestoreWCMemory</a> to restore CPU access to WC memory.</p>

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
<p>Available in Windows 2000 and later versions of the Windows operating systems.</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\video\ns-video--video-port-config-info.md">VIDEO_PORT_CONFIG_INFO</a>
</dt>
<dt>
<a href="..\video\nc-video-restore-wc-memory.md">VideoPortRestoreWCMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PROTECT_WC_MEMORY callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
