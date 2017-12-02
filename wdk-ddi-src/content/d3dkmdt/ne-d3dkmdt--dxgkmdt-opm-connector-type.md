---
UID: NE.d3dkmdt._DXGKMDT_OPM_CONNECTOR_TYPE
title: DXGKMDT_OPM_CONNECTOR_TYPE
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\dxgkmdt_opm_connector_type.htm
old-project: display
ms.assetid: 57A2F351-99F1-425A-99E3-1167CEFF9FDD
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKMDT_OPM_CONNECTOR_TYPE
req.alt-loc: D3dkmdt.h
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

# DXGKMDT_OPM_CONNECTOR_TYPE enumeration



## -description
<p>Reserved for system use. Do not use in your driver.</p>


## -syntax

````
typedef enum _DXGKMDT_OPM_CONNECTOR_TYPE { 
  DXGKMDT_OPM_CONNECTOR_TYPE_OTHER                     = -1,
  DXGKMDT_OPM_CONNECTOR_TYPE_HD15                      = 0,
  DXGKMDT_OPM_CONNECTOR_TYPE_SVIDEO                    = 1,
  DXGKMDT_OPM_CONNECTOR_TYPE_COMPOSITE_VIDEO           = 2,
  DXGKMDT_OPM_CONNECTOR_TYPE_COMPONENT_VIDEO           = 3,
  DXGKMDT_OPM_CONNECTOR_TYPE_DVI                       = 4,
  DXGKMDT_OPM_CONNECTOR_TYPE_HDMI                      = 5,
  DXGKMDT_OPM_CONNECTOR_TYPE_LVDS                      = 6,
  DXGKMDT_OPM_CONNECTOR_TYPE_D_JPN                     = 8,
  DXGKMDT_OPM_CONNECTOR_TYPE_SDI                       = 9,
  DXGKMDT_OPM_CONNECTOR_TYPE_DISPLAYPORT_EXTERNAL      = 10,
  DXGKMDT_OPM_CONNECTOR_TYPE_DISPLAYPORT_EMBEDDED      = 11,
  DXGKMDT_OPM_CONNECTOR_TYPE_UDI_EXTERNAL              = 12,
  DXGKMDT_OPM_CONNECTOR_TYPE_UDI_EMBEDDED              = 13,
  DXGKMDT_OPM_CONNECTOR_TYPE_RESERVED                  = 14,
  DXGKMDT_OPM_CONNECTOR_TYPE_MIRACAST                  = 15,
  DXGKMDT_OPM_COPP_COMPATIBLE_CONNECTOR_TYPE_INTERNAL  = 0x80000000
} DXGKMDT_OPM_CONNECTOR_TYPE;
````


## -enum-fields
<dl>

### -field DXGKMDT_OPM_CONNECTOR_TYPE_OTHER

<dd></dd>

### -field DXGKMDT_OPM_CONNECTOR_TYPE_HD15

<dd></dd>

### -field DXGKMDT_OPM_CONNECTOR_TYPE_SVIDEO

<dd></dd>

### -field DXGKMDT_OPM_CONNECTOR_TYPE_COMPOSITE_VIDEO

<dd></dd>

### -field DXGKMDT_OPM_CONNECTOR_TYPE_COMPONENT_VIDEO

<dd></dd>

### -field DXGKMDT_OPM_CONNECTOR_TYPE_DVI

<dd></dd>

### -field DXGKMDT_OPM_CONNECTOR_TYPE_HDMI

<dd></dd>

### -field DXGKMDT_OPM_CONNECTOR_TYPE_LVDS

<dd></dd>

### -field DXGKMDT_OPM_CONNECTOR_TYPE_D_JPN

<dd></dd>

### -field DXGKMDT_OPM_CONNECTOR_TYPE_SDI

<dd></dd>

### -field DXGKMDT_OPM_CONNECTOR_TYPE_DISPLAYPORT_EXTERNAL

<dd></dd>

### -field DXGKMDT_OPM_CONNECTOR_TYPE_DISPLAYPORT_EMBEDDED

<dd></dd>

### -field DXGKMDT_OPM_CONNECTOR_TYPE_UDI_EXTERNAL

<dd></dd>

### -field DXGKMDT_OPM_CONNECTOR_TYPE_UDI_EMBEDDED

<dd></dd>

### -field DXGKMDT_OPM_CONNECTOR_TYPE_RESERVED

<dd></dd>

### -field DXGKMDT_OPM_CONNECTOR_TYPE_MIRACAST

<dd></dd>

### -field DXGKMDT_OPM_COPP_COMPATIBLE_CONNECTOR_TYPE_INTERNAL

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>