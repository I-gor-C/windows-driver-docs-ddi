---
UID: NS.d3dkmddi._DXGK_VIDPN_INTERFACE
title: DXGK_VIDPN_INTERFACE
author: windows-driver-content
description: The DXGK_VIDPN_INTERFACE structure contains pointers to functions that belong to the VidPn interface, which is implemented by the video present network (VidPN) manager.
old-location: display\dxgk_vidpn_interface.htm
old-project: display
ms.assetid: 7ddd110c-2521-4df6-a936-e702a0f15312
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_VIDPN_INTERFACE,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_VIDPN_INTERFACE
req.alt-loc: d3dkmddi.h
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

# DXGK_VIDPN_INTERFACE structure



## -description
<p>The DXGK_VIDPN_INTERFACE structure contains pointers to functions that belong to the <a href="display.vidpn_interface">VidPn interface</a>, which is implemented by the video present network (VidPN) manager.</p>


## -syntax

````
typedef struct _DXGK_VIDPN_INTERFACE {
  DXGK_VIDPN_INTERFACE_VERSION               Version;
  DXGKDDI_VIDPN_GETTOPOLOGY                  pfnGetTopology;
  DXGKDDI_VIDPN_ACQUIRESOURCEMODESET         pfnAcquireSourceModeSet;
  DXGKDDI_VIDPN_RELEASESOURCEMODESET         pfnReleaseSourceModeSet;
  DXGKDDI_VIDPN_CREATENEWSOURCEMODESET       pfnCreateNewSourceModeSet;
  DXGKDDI_VIDPN_ASSIGNSOURCEMODESET          pfnAssignSourceModeSet;
  DXGKDDI_VIDPN_ASSIGNMULTISAMPLINGMETHODSET pfnAssignMultisamplingMethodSet;
  DXGKDDI_VIDPN_ACQUIRETARGETMODESET         pfnAcquireTargetModeSet;
  DXGKDDI_VIDPN_RELEASETARGETMODESET         pfnReleaseTargetModeSet;
  DXGKDDI_VIDPN_CREATENEWTARGETMODESET       pfnCreateNewTargetModeSet;
  DXGKDDI_VIDPN_ASSIGNTARGETMODESET          pfnAssignTargetModeSet;
} DXGK_VIDPN_INTERFACE;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>A <a href="..\d3dkmddi\ne-d3dkmddi--dxgk-vidpn-interface-version.md">DXGK_VIDPN_INTERFACE_VERSION</a> enumerator that specifies the version of the interface.</p>
</dd>

### -field <b>pfnGetTopology</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-gettopology.md">pfnGetTopology</a> function.</p>
</dd>

### -field <b>pfnAcquireSourceModeSet</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-acquiresourcemodeset.md">pfnAcquireSourceModeSet</a> function.</p>
</dd>

### -field <b>pfnReleaseSourceModeSet</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-releasesourcemodeset.md">pfnReleaseSourceModeSet</a> function.</p>
</dd>

### -field <b>pfnCreateNewSourceModeSet</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-createnewsourcemodeset.md">pfnCreateNewSourceModeSet</a> function.</p>
</dd>

### -field <b>pfnAssignSourceModeSet</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-assignsourcemodeset.md">pfnAssignSourceModeSet</a> function.</p>
</dd>

### -field <b>pfnAssignMultisamplingMethodSet</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-assignmultisamplingmethodset.md">pfnAssignMultisamplingMethodSet</a> function.</p>
</dd>

### -field <b>pfnAcquireTargetModeSet</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-acquiretargetmodeset.md">pfnAcquireTargetModeSet</a> function.</p>
</dd>

### -field <b>pfnReleaseTargetModeSet</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-releasetargetmodeset.md">pfnReleaseTargetModeSet</a> function.</p>
</dd>

### -field <b>pfnCreateNewTargetModeSet</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-createnewtargetmodeset.md">pfnCreateNewTargetModeSet</a> function.</p>
</dd>

### -field <b>pfnAssignTargetModeSet</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-assigntargetmodeset.md">pfnAssignTargetModeSet</a> function.</p>
</dd>
</dl>

## -remarks
<p>The display miniport driver calls <a href="..\d3dkmddi\nc-d3dkmddi-dxgkcb-queryvidpninterface.md">DxgkCbQueryVidPnInterface</a> to obtain a pointer to a DXGK_VIDPN_INTERFACE structure. The structure contains pointers to functions that the display miniport driver can call to inspect and alter a VidPN object.</p>

<p>For more information about the VidPN interface, see <a href="https://msdn.microsoft.com/5dedac8c-9a99-4b3a-81be-39819135cd97">VidPN Objects and Interfaces</a>.</p>

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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>