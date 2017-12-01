---
UID: NS.video._VIDEO_PORT_AGP_INTERFACE
title: VIDEO_PORT_AGP_INTERFACE
author: windows-driver-content
description: The VIDEO_PORT_AGP_INTERFACE structure describes the AGP service routines provided by the video port driver.
old-location: display\video_port_agp_interface.htm
old-project: display
ms.assetid: a2be4958-3f11-4b9d-9c0c-c339ebbbce04
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VIDEO_PORT_AGP_INTERFACE, VIDEO_PORT_AGP_INTERFACE, *PVIDEO_PORT_AGP_INTERFACE
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
req.alt-api: VIDEO_PORT_AGP_INTERFACE
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

# VIDEO_PORT_AGP_INTERFACE structure



## -description
<p>The VIDEO_PORT_AGP_INTERFACE structure describes the AGP service routines provided by the video port driver.</p>


## -syntax

````
typedef struct _VIDEO_PORT_AGP_INTERFACE {
  USHORT                 Size;
  USHORT                 Version;
  PVOID                  Context;
  PINTERFACE_REFERENCE   InterfaceReference;
  PINTERFACE_DEREFERENCE InterfaceDereference;
  PAGP_RESERVE_PHYSICAL  AgpReservePhysical;
  PAGP_RELEASE_PHYSICAL  AgpReleasePhysical;
  PAGP_COMMIT_PHYSICAL   AgpCommitPhysical;
  PAGP_FREE_PHYSICAL     AgpFreePhysical;
  PAGP_RESERVE_VIRTUAL   AgpReserveVirtual;
  PAGP_RELEASE_VIRTUAL   AgpReleaseVirtual;
  PAGP_COMMIT_VIRTUAL    AgpCommitVirtual;
  PAGP_FREE_VIRTUAL      AgpFreeVirtual;
  ULONGLONG              AgpAllocationLimit;
} VIDEO_PORT_AGP_INTERFACE, *PVIDEO_PORT_AGP_INTERFACE;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Specifies the size in bytes of this structure.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Specifies the version of the interface to be returned by the video port driver. The current interface version is defined in <i>video.h</i> and has the form VIDEO_PORT_AGP_INTERFACE_<i>N</i>.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>Pointer to a video port driver-defined context for the interface.</p>
</dd>

### -field <b>InterfaceReference</b>

<dd>
<p>Pointer to the video port driver-implemented reference routine for this interface.</p>
</dd>

### -field <b>InterfaceDereference</b>

<dd>
<p>Pointer to the video port driver-implemented dereference routine for this interface.</p>
</dd>

### -field <b>AgpReservePhysical</b>

<dd>
<p>Pointer to the video port driver-implemented <a href="..\videoagp\nc-videoagp-pagp-reserve-physical.md">AgpReservePhysical</a> routine.</p>
</dd>

### -field <b>AgpReleasePhysical</b>

<dd>
<p>Pointer to the video port driver-implemented <a href="..\videoagp\nc-videoagp-pagp-release-physical.md">AgpReleasePhysical</a> routine.</p>
</dd>

### -field <b>AgpCommitPhysical</b>

<dd>
<p>Pointer to the video port driver-implemented <a href="..\videoagp\nc-videoagp-pagp-commit-physical.md">AgpCommitPhysical</a> routine.</p>
</dd>

### -field <b>AgpFreePhysical</b>

<dd>
<p>Pointer to the video port driver-implemented <a href="..\videoagp\nc-videoagp-pagp-free-physical.md">AgpFreePhysical</a> routine.</p>
</dd>

### -field <b>AgpReserveVirtual</b>

<dd>
<p>Pointer to the video port driver-implemented <a href="..\videoagp\nc-videoagp-pagp-reserve-virtual.md">AgpReserveVirtual</a> routine.</p>
</dd>

### -field <b>AgpReleaseVirtual</b>

<dd>
<p>Pointer to the video port driver-implemented <a href="..\videoagp\nc-videoagp-pagp-release-virtual.md">AgpReleaseVirtual</a> routine.</p>
</dd>

### -field <b>AgpCommitVirtual</b>

<dd>
<p>Pointer to the video port driver-implemented <a href="..\videoagp\nc-videoagp-pagp-commit-virtual.md">AgpCommitVirtual</a> routine.</p>
</dd>

### -field <b>AgpFreeVirtual</b>

<dd>
<p>Pointer to the video port driver-implemented <a href="..\videoagp\nc-videoagp-pagp-free-virtual.md">AgpFreeVirtual</a> routine.</p>
</dd>

### -field <b>AgpAllocationLimit</b>

<dd>
<p>Specifies the maximum total number of bytes of AGP memory that a miniport driver can commit.</p>
</dd>
</dl>

## -remarks
<p>PnP video miniport drivers that can use AGP must fill in the <b>Size</b> and <b>Version</b> members, and then call the <a href="..\video\nf-video-videoportqueryservices.md">VideoPortQueryServices</a> function, which initializes the remaining members of this structure.</p>

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
<a href="..\video\nf-video-videoportqueryservices.md">VideoPortQueryServices</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--interface.md">INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20VIDEO_PORT_AGP_INTERFACE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
