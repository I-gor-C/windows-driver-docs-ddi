---
UID: NS.video._VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE
title: VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE
author: windows-driver-content
description: The VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE structure describes the Write Combined video memory protection service routines implemented by the video port driver. The protected video memory cannot be accessed by the CPU.
old-location: display\video_port_wcmemoryprotection_interface.htm
old-project: display
ms.assetid: ac62a738-bde1-49e7-9c18-519471ec1092
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE, VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE, *PVIDEO_PORT_WCMEMORYPROTECTION_INTERFACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: video.h
req.include-header: Video.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE
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
req.irql: See Remarks section.
req.iface: 
req.product: Windows 10 or later.
---

# VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE structure



## -description
<p>The VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE structure describes the Write Combined video memory protection service routines implemented by the video port driver. The protected video memory cannot be accessed by the CPU.</p>


## -syntax

````
typedef struct _VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE {
  USHORT                 Size;
  USHORT                 Version;
  PVOID                  Context;
  PINTERFACE_REFERENCE   InterfaceReference;
  PINTERFACE_DEREFERENCE InterfaceDereference;
  PROTECT_WC_MEMORY      VideoPortProtectWCMemory;
  RESTORE_WC_MEMORY      VideoPortRestoreWCMemory;
} VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE, *PVIDEO_PORT_WCMEMORYPROTECTION_INTERFACE;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Specifies the size in bytes of this structure.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Specifies the version of the interface to be returned by the miniport driver. The current interface version is defined in <i>video.h</i>, and has the form VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE_VERSION_<i>N</i>.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>Pointer to a miniport driver-defined context for the interface.</p>
</dd>

### -field <b>InterfaceReference</b>

<dd>
<p>Pointer to the video port driver-implemented reference routine for this interface.</p>
</dd>

### -field <b>InterfaceDereference</b>

<dd>
<p>Pointer to the video port driver-implemented dereference routine for this interface.</p>
</dd>

### -field <b>VideoPortProtectWCMemory</b>

<dd>
<p>Pointer to the video port driver's <a href="..\video\nc-video-protect-wc-memory.md">VideoPortProtectWCMemory</a> callback routine.</p>
</dd>

### -field <b>VideoPortRestoreWCMemory</b>

<dd>
<p>Pointer to the video port driver's <a href="..\video\nc-video-restore-wc-memory.md">VideoPortRestoreWCMemory</a> callback routine.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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
<a href="..\video\nc-video-protect-wc-memory.md">VideoPortProtectWCMemory</a>
</dt>
<dt>
<a href="..\video\nf-video-videoportqueryservices.md">VideoPortQueryServices</a>
</dt>
<dt>
<a href="..\video\nc-video-restore-wc-memory.md">VideoPortRestoreWCMemory</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--interface.md">INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VIDEO_PORT_WCMEMORYPROTECTION_INTERFACE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
