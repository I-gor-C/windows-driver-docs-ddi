---
UID: NF.drmk.DrmDestroyContent
title: DrmDestroyContent
author: windows-driver-content
description: The DrmDestroyContent function deletes a DRM content ID that was created by DrmCreateContentMixed.
old-location: audio\drmdestroycontent.htm
old-project: audio
ms.assetid: 197f74f8-050e-4b0b-a95d-f640c565c17e
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: DrmDestroyContent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: drmk.h
req.include-header: Drmk.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DrmDestroyContent
req.alt-loc: Drmk.lib,Drmk.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Drmk.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# DrmDestroyContent function



## -description
<p>The <code>DrmDestroyContent</code> function deletes a DRM content ID that was created by <a href="https://msdn.microsoft.com/library/windows/hardware/ff536348">DrmCreateContentMixed</a>.</p>


## -syntax

````
NTSTATUS DrmDestroyContent(
  _In_ ULONG ContentId
);
````


## -parameters
<dl>

### -param <i>ContentId</i> [in]

<dd>
<p>Specifies a nonzero DRM content ID assigned to a KS audio stream by <b>DrmCreateContentMixed</b>. Note that a content ID of zero represents an audio stream with default DRM content rights, and cannot be used with this function.</p>
</dd>
</dl>

## -returns
<p><b>DrmCreateContentMixed</b> returns STATUS_SUCCESS if the call was successful. Otherwise, it returns an appropriate error code.</p>

## -remarks
<p>A KS audio filter can only use <code>DrmDestroyContent</code> to delete a DRM content ID that it obtained by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff536348">DrmCreateContentMixed</a>. Note that a KS audio filter must not use <code>DrmDestroyContent</code> to delete a DRM content ID set by <a href="https://msdn.microsoft.com/library/windows/hardware/ff536570">IDrmAudioStream::SetContentId</a> or by an IOCTL_KS_PROPERTY request that sets the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537351">KSPROPERTY_DRMAUDIOSTREAM_CONTENTID</a> property. Only the KS audio filter that created the content ID should delete it.</p>

<p><code>DrmDestroyContent</code> performs the same function as <a href="https://msdn.microsoft.com/library/windows/hardware/ff537690">PcDestroyContent</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff536583">IDrmPort::DestroyContent</a>. For more information, see <a href="NULL">DRM Functions and Interfaces</a>.</p>

<p>A KS audio filter can only use <code>DrmDestroyContent</code> to delete a DRM content ID that it obtained by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff536348">DrmCreateContentMixed</a>. Note that a KS audio filter must not use <code>DrmDestroyContent</code> to delete a DRM content ID set by <a href="https://msdn.microsoft.com/library/windows/hardware/ff536570">IDrmAudioStream::SetContentId</a> or by an IOCTL_KS_PROPERTY request that sets the <a href="https://msdn.microsoft.com/library/windows/hardware/ff537351">KSPROPERTY_DRMAUDIOSTREAM_CONTENTID</a> property. Only the KS audio filter that created the content ID should delete it.</p>

<p><code>DrmDestroyContent</code> performs the same function as <a href="https://msdn.microsoft.com/library/windows/hardware/ff537690">PcDestroyContent</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff536583">IDrmPort::DestroyContent</a>. For more information, see <a href="NULL">DRM Functions and Interfaces</a>.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Drmk.h (include Drmk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Drmk.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536348">DrmCreateContentMixed</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536354">DrmGetContentRights</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536570">IDrmAudioStream::SetContentId</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537351">KSPROPERTY_DRMAUDIOSTREAM_CONTENTID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537690">PcDestroyContent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536583">IDrmPort::DestroyContent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20DrmDestroyContent function%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
