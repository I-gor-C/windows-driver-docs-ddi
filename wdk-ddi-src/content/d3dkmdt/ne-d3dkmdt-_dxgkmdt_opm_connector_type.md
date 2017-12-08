---
UID: NE.d3dkmdt._DXGKMDT_OPM_CONNECTOR_TYPE
title: _DXGKMDT_OPM_CONNECTOR_TYPE
author: windows-driver-content
description: Reserved for system use. Do not use in your driver.
old-location: display\dxgkmdt_opm_connector_type.htm
old-project: display
ms.assetid: 57A2F351-99F1-425A-99E3-1167CEFF9FDD
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: _DXGKMDT_OPM_CONNECTOR_TYPE, DXGKMDT_OPM_CONNECTOR_TYPE
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
---

# _DXGKMDT_OPM_CONNECTOR_TYPE enumeration



## -description
Reserved for system use. Do not use in your driver.


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

### -field DXGKMDT_OPM_CONNECTOR_TYPE_OTHER


### -field DXGKMDT_OPM_CONNECTOR_TYPE_HD15


### -field DXGKMDT_OPM_CONNECTOR_TYPE_SVIDEO


### -field DXGKMDT_OPM_CONNECTOR_TYPE_COMPOSITE_VIDEO


### -field DXGKMDT_OPM_CONNECTOR_TYPE_COMPONENT_VIDEO


### -field DXGKMDT_OPM_CONNECTOR_TYPE_DVI


### -field DXGKMDT_OPM_CONNECTOR_TYPE_HDMI


### -field DXGKMDT_OPM_CONNECTOR_TYPE_LVDS


### -field DXGKMDT_OPM_CONNECTOR_TYPE_D_JPN


### -field DXGKMDT_OPM_CONNECTOR_TYPE_SDI


### -field DXGKMDT_OPM_CONNECTOR_TYPE_DISPLAYPORT_EXTERNAL


### -field DXGKMDT_OPM_CONNECTOR_TYPE_DISPLAYPORT_EMBEDDED


### -field DXGKMDT_OPM_CONNECTOR_TYPE_UDI_EXTERNAL


### -field DXGKMDT_OPM_CONNECTOR_TYPE_UDI_EMBEDDED


### -field DXGKMDT_OPM_CONNECTOR_TYPE_RESERVED


### -field DXGKMDT_OPM_CONNECTOR_TYPE_MIRACAST


### -field DXGKMDT_OPM_COPP_COMPATIBLE_CONNECTOR_TYPE_INTERNAL


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Minimum supported client
</th>
<td width="70%">
Windows 8.1
</td>
</tr>
<tr>
<th width="30%">
Minimum supported server
</th>
<td width="70%">
Windows Server 2012 R2
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>