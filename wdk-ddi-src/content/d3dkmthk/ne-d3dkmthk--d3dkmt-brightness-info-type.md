---
UID: NE.d3dkmthk._D3DKMT_BRIGHTNESS_INFO_TYPE
title: D3DKMT_BRIGHTNESS_INFO_TYPE
author: windows-driver-content
description: Indicates the type of information to retrieve or set for the brightness of an integrated display panel.
old-location: display\d3dkmt_brightness_info_type.htm
old-project: display
ms.assetid: 0f37ac57-9f3b-4bbc-a927-ea85aa44f910
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKMDT_OPM_STANDARD_INFORMATION, DXGKMDT_OPM_STANDARD_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_BRIGHTNESS_INFO_TYPE
req.alt-loc: D3dkmthk.h
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

# D3DKMT_BRIGHTNESS_INFO_TYPE enumeration



## -description
<p>Indicates the type of information to retrieve or set for the brightness of an integrated display panel.</p>


## -syntax

````
typedef enum _D3DKMT_BRIGHTNESS_INFO_TYPE { 
  D3DKMT_BRIGHTNESS_INFO_GET_POSSIBLE_LEVELS  = 1,
  D3DKMT_BRIGHTNESS_INFO_GET                  = 2,
  D3DKMT_BRIGHTNESS_INFO_SET                  = 3,
  D3DKMT_BRIGHTNESS_INFO_GET_CAPS             = 4,
  D3DKMT_BRIGHTNESS_INFO_SET_STATE            = 5,
  D3DKMT_BRIGHTNESS_INFO_SET_OPTIMIZATION     = 6,
  D3DKMT_BRIGHTNESS_INFO_GET_REDUCTION        = 7,
  D3DKMT_BRIGHTNESS_INFO_BEGIN_MANUAL_MODE    = 8,
  D3DKMT_BRIGHTNESS_INFO_END_MANUAL_MODE      = 9,
  D3DKMT_BRIGHTNESS_INFO_TOGGLE_LOGGING       = 10
} D3DKMT_BRIGHTNESS_INFO_TYPE;
````


## -enum-fields
<dl>

### -field D3DKMT_BRIGHTNESS_INFO_GET_POSSIBLE_LEVELS

<dd>
<p>Retrieve all possible brightness levels that the integrated display panel supports.</p>
</dd>

### -field D3DKMT_BRIGHTNESS_INFO_GET

<dd>
<p>Retrieve the currently active brightness level.</p>
</dd>

### -field D3DKMT_BRIGHTNESS_INFO_SET

<dd>
<p> Set a new brightness level.</p>
</dd>

### -field D3DKMT_BRIGHTNESS_INFO_GET_CAPS

<dd>
<p>Retrieve brightness control capabilities of the integrated display panel.</p>
</dd>

### -field D3DKMT_BRIGHTNESS_INFO_SET_STATE

<dd>
<p>Enable smooth brightness control.</p>
</dd>

### -field D3DKMT_BRIGHTNESS_INFO_SET_OPTIMIZATION

<dd>
<p>Set the level of optimization that the display miniport driver uses to control the brightness of the integrated display panel.</p>
</dd>

### -field D3DKMT_BRIGHTNESS_INFO_GET_REDUCTION

<dd>
<p>Retrieve the current level of backlight reduction that is applied to the integrated display panel.</p>
</dd>

### -field D3DKMT_BRIGHTNESS_INFO_BEGIN_MANUAL_MODE

<dd>
<p>The user has begun to manually adjust the brightness level.</p>
</dd>

### -field D3DKMT_BRIGHTNESS_INFO_END_MANUAL_MODE

<dd>
<p>The user has ended the manual adjustment of the brightness level.</p>
</dd>

### -field D3DKMT_BRIGHTNESS_INFO_TOGGLE_LOGGING

<dd>
<p>Enable or disable Event Tracing for Windows (ETW) logging of brightness information.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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