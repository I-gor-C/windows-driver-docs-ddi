---
UID: NE.mfidl.MF_TRANSFER_VIDEO_FRAME_FLAGS
title: MF_TRANSFER_VIDEO_FRAME_FLAGS
author: windows-driver-content
description: .
old-location: stream\mf_transfer_video_frame_flags.htm
old-project: stream
ms.assetid: 0F4006D0-11B7-48F3-8ED4-00B09EFA67D1
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagMetadataTimeStamps, MetadataTimeStamps
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: mfidl.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MF_TRANSFER_VIDEO_FRAME_FLAGS
req.alt-loc: Mfidl.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# MF_TRANSFER_VIDEO_FRAME_FLAGS enumeration



## -description
<p></p>


## -syntax

````
typedef enum _MF_TRANSFER_VIDEO_FRAME_FLAGS { 
  MF_TRANSFER_VIDEO_FRAME_DEFAULT     = 0,
  MF_TRANSFER_VIDEO_FRAME_STRETCH     = 1,
  MF_TRANSFER_VIDEO_FRAME_IGNORE_PAR  = 2
} MF_TRANSFER_VIDEO_FRAME_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="MF_TRANSFER_VIDEO_FRAME_DEFAULT"></a><a id="mf_transfer_video_frame_default"></a><b>MF_TRANSFER_VIDEO_FRAME_DEFAULT</b>

<dd></dd>

### -field <a id="MF_TRANSFER_VIDEO_FRAME_STRETCH"></a><a id="mf_transfer_video_frame_stretch"></a><b>MF_TRANSFER_VIDEO_FRAME_STRETCH</b>

<dd></dd>

### -field <a id="MF_TRANSFER_VIDEO_FRAME_IGNORE_PAR"></a><a id="mf_transfer_video_frame_ignore_par"></a><b>MF_TRANSFER_VIDEO_FRAME_IGNORE_PAR</b>

<dd></dd>
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
<dt>Mfidl.h</dt>
</dl>
</td>
</tr>
</table>