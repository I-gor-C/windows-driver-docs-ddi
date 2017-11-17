---
UID: NE.d3dkmdt._DXGKMDT_OPM_CONNECTOR_TYPE
title: DXGKMDT_OPM_CONNECTOR_TYPE
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\dxgkmdt_opm_connector_type.htm
ms.assetid: 57A2F351-99F1-425A-99E3-1167CEFF9FDD
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
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
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
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

### -field <a id="DXGKMDT_OPM_CONNECTOR_TYPE_OTHER"></a><a id="dxgkmdt_opm_connector_type_other"></a><b>DXGKMDT_OPM_CONNECTOR_TYPE_OTHER</b>

<dd></dd>

### -field <a id="DXGKMDT_OPM_CONNECTOR_TYPE_HD15"></a><a id="dxgkmdt_opm_connector_type_hd15"></a><b>DXGKMDT_OPM_CONNECTOR_TYPE_HD15</b>

<dd></dd>

### -field <a id="DXGKMDT_OPM_CONNECTOR_TYPE_SVIDEO"></a><a id="dxgkmdt_opm_connector_type_svideo"></a><b>DXGKMDT_OPM_CONNECTOR_TYPE_SVIDEO</b>

<dd></dd>

### -field <a id="DXGKMDT_OPM_CONNECTOR_TYPE_COMPOSITE_VIDEO"></a><a id="dxgkmdt_opm_connector_type_composite_video"></a><b>DXGKMDT_OPM_CONNECTOR_TYPE_COMPOSITE_VIDEO</b>

<dd></dd>

### -field <a id="DXGKMDT_OPM_CONNECTOR_TYPE_COMPONENT_VIDEO"></a><a id="dxgkmdt_opm_connector_type_component_video"></a><b>DXGKMDT_OPM_CONNECTOR_TYPE_COMPONENT_VIDEO</b>

<dd></dd>

### -field <a id="DXGKMDT_OPM_CONNECTOR_TYPE_DVI"></a><a id="dxgkmdt_opm_connector_type_dvi"></a><b>DXGKMDT_OPM_CONNECTOR_TYPE_DVI</b>

<dd></dd>

### -field <a id="DXGKMDT_OPM_CONNECTOR_TYPE_HDMI"></a><a id="dxgkmdt_opm_connector_type_hdmi"></a><b>DXGKMDT_OPM_CONNECTOR_TYPE_HDMI</b>

<dd></dd>

### -field <a id="DXGKMDT_OPM_CONNECTOR_TYPE_LVDS"></a><a id="dxgkmdt_opm_connector_type_lvds"></a><b>DXGKMDT_OPM_CONNECTOR_TYPE_LVDS</b>

<dd></dd>

### -field <a id="DXGKMDT_OPM_CONNECTOR_TYPE_D_JPN"></a><a id="dxgkmdt_opm_connector_type_d_jpn"></a><b>DXGKMDT_OPM_CONNECTOR_TYPE_D_JPN</b>

<dd></dd>

### -field <a id="DXGKMDT_OPM_CONNECTOR_TYPE_SDI"></a><a id="dxgkmdt_opm_connector_type_sdi"></a><b>DXGKMDT_OPM_CONNECTOR_TYPE_SDI</b>

<dd></dd>

### -field <a id="DXGKMDT_OPM_CONNECTOR_TYPE_DISPLAYPORT_EXTERNAL"></a><a id="dxgkmdt_opm_connector_type_displayport_external"></a><b>DXGKMDT_OPM_CONNECTOR_TYPE_DISPLAYPORT_EXTERNAL</b>

<dd></dd>

### -field <a id="DXGKMDT_OPM_CONNECTOR_TYPE_DISPLAYPORT_EMBEDDED"></a><a id="dxgkmdt_opm_connector_type_displayport_embedded"></a><b>DXGKMDT_OPM_CONNECTOR_TYPE_DISPLAYPORT_EMBEDDED</b>

<dd></dd>

### -field <a id="DXGKMDT_OPM_CONNECTOR_TYPE_UDI_EXTERNAL"></a><a id="dxgkmdt_opm_connector_type_udi_external"></a><b>DXGKMDT_OPM_CONNECTOR_TYPE_UDI_EXTERNAL</b>

<dd></dd>

### -field <a id="DXGKMDT_OPM_CONNECTOR_TYPE_UDI_EMBEDDED"></a><a id="dxgkmdt_opm_connector_type_udi_embedded"></a><b>DXGKMDT_OPM_CONNECTOR_TYPE_UDI_EMBEDDED</b>

<dd></dd>

### -field <a id="DXGKMDT_OPM_CONNECTOR_TYPE_RESERVED"></a><a id="dxgkmdt_opm_connector_type_reserved"></a><b>DXGKMDT_OPM_CONNECTOR_TYPE_RESERVED</b>

<dd></dd>

### -field <a id="DXGKMDT_OPM_CONNECTOR_TYPE_MIRACAST"></a><a id="dxgkmdt_opm_connector_type_miracast"></a><b>DXGKMDT_OPM_CONNECTOR_TYPE_MIRACAST</b>

<dd></dd>

### -field <a id="DXGKMDT_OPM_COPP_COMPATIBLE_CONNECTOR_TYPE_INTERNAL"></a><a id="dxgkmdt_opm_copp_compatible_connector_type_internal"></a><b>DXGKMDT_OPM_COPP_COMPATIBLE_CONNECTOR_TYPE_INTERNAL</b>

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