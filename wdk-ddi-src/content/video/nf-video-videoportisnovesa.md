---
UID: NF.video.VideoPortIsNoVesa
title: VideoPortIsNoVesa
author: windows-driver-content
description: The VideoPortIsNoVesa function determines whether a video miniport driver that does not support Plug and Play (PnP) is restricted to legacy VGA resources.
old-location: display\videoportisnovesa.htm
old-project: display
ms.assetid: e3de4e58-c3e7-426f-bc96-b45cad6b5807
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortIsNoVesa
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Server 2003 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortIsNoVesa
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

# VideoPortIsNoVesa function



## -description
<p>The <b>VideoPortIsNoVesa</b> function determines whether a video miniport driver that does not support Plug and Play (PnP) is restricted to legacy VGA resources.</p>


## -syntax

````
BOOLEAN VideoPortIsNoVesa(void);
````


## -parameters


## -returns
<p>If <b>VideoPortIsNoVesa</b> returns <b>TRUE</b>, then a non-PnP video miniport driver must restrict its hardware access to legacy VGA resources. Otherwise, the video miniport driver is permitted to use non-legacy VGA resources.</p>

<p>If <b>VideoPortIsNoVesa</b> returns <b>TRUE</b>, then a non-PnP video miniport driver must restrict its hardware access to legacy VGA resources. Otherwise, the video miniport driver is permitted to use non-legacy VGA resources.</p>

<p>If <b>VideoPortIsNoVesa</b> returns <b>TRUE</b>, then a non-PnP video miniport driver must restrict its hardware access to legacy VGA resources. Otherwise, the video miniport driver is permitted to use non-legacy VGA resources.</p>

## -remarks
<p>This function is useful only to vga.sys, which is a system-supplied video miniport driver that does not support PnP. This function provides no pertinent information to video miniport drivers that support PnP and therefore is no use to IHVs.</p>

<p>If <b>VideoPortIsNoVesa</b> returns <b>TRUE</b>, then the video miniport driver must access the display adapter only through legacy VGA resources (I/O 3B0 through 3DF; memory A0000 through BFFFF). Specifically, if <b>VideoPortIsNoVesa</b> returns <b>TRUE</b>, the video miniport driver must not attempt to call the Int10 functions, which are implemented by the video port driver.</p>

<p>For more information about the Int10 functions, see <a href="display.int10_functions_implemented_by_the_video_port_driver">Int10 Functions Implemented by the Video Port Driver</a>. </p>

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
<p>Available in Windows Server 2003 and later versions of the Windows operating systems.</p>
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