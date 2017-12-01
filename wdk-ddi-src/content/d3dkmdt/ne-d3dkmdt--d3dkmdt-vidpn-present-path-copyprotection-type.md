---
UID: NE.d3dkmdt._D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE
title: D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE
author: windows-driver-content
description: The D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE enumeration is used to indicate the type of copy protection that is supported by a VidPN present path.
old-location: display\d3dkmdt_vidpn_present_path_copyprotection_type.htm
old-project: display
ms.assetid: ee9405a6-7d56-4ca6-98c2-fd04addef8cd
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE
req.alt-loc: d3dkmdt.h
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

# D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE enumeration



## -description
<p>The D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE enumeration is used to indicate the type of copy protection that is supported by a VidPN present path.</p>


## -syntax

````
typedef enum _D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE { 
  D3DKMDT_VPPMT_UNINITIALIZED            = 0,
  D3DKMDT_VPPMT_NOPROTECTION             = 1,
  D3DKMDT_VPPMT_MACROVISION_APSTRIGGER   = 2,
  D3DKMDT_VPPMT_MACROVISION_FULLSUPPORT  = 3
} D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE;
````


## -enum-fields
<dl>

### -field <a id="D3DKMDT_VPPMT_UNINITIALIZED"></a><a id="d3dkmdt_vppmt_uninitialized"></a><b>D3DKMDT_VPPMT_UNINITIALIZED</b>

<dd>
<p>Indicates that a variable of type D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="D3DKMDT_VPPMT_NOPROTECTION"></a><a id="d3dkmdt_vppmt_noprotection"></a><b>D3DKMDT_VPPMT_NOPROTECTION</b>

<dd>
<p>Indicates that the path has no copy protection.</p>
</dd>

### -field <a id="D3DKMDT_VPPMT_MACROVISION_APSTRIGGER"></a><a id="d3dkmdt_vppmt_macrovision_apstrigger"></a><b>D3DKMDT_VPPMT_MACROVISION_APSTRIGGER</b>

<dd>
<p>Indicates that the path provides support for Rovi's (formerly Macrovision) analog protection system (APS).</p>
</dd>

### -field <a id="D3DKMDT_VPPMT_MACROVISION_FULLSUPPORT"></a><a id="d3dkmdt_vppmt_macrovision_fullsupport"></a><b>D3DKMDT_VPPMT_MACROVISION_FULLSUPPORT</b>

<dd>
<p>Indicates that the path provides full Rovi (formerly Macrovision) copy protection support.</p>
</dd>
</dl>

## -remarks
<p>The <b>CopyProtectionType</b> member of the <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-present-path-copyprotection.md">D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION</a> structure is a value from the D3DKMDT_VIDPN_PRESENT_PATH_COPYPROTECTION_TYPE enumeration.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
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