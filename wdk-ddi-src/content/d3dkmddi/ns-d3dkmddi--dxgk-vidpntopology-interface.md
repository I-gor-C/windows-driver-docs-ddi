---
UID: NS.d3dkmddi._DXGK_VIDPNTOPOLOGY_INTERFACE
title: DXGK_VIDPNTOPOLOGY_INTERFACE
author: windows-driver-content
description: The DXGK_VIDPNTOPOLOGY_INTERFACE structure contains pointers to functions that belong to the VidPn Topology interface, which is implemented by the video present network (VidPN) manager.
old-location: display\dxgk_vidpntopology_interface.htm
old-project: display
ms.assetid: 293103cc-217c-4dcb-82c1-971adba564a0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_VIDPNTOPOLOGY_INTERFACE, DXGK_VIDPNTOPOLOGY_INTERFACE
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
req.alt-api: DXGK_VIDPNTOPOLOGY_INTERFACE
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

# DXGK_VIDPNTOPOLOGY_INTERFACE structure



## -description
<p>The DXGK_VIDPNTOPOLOGY_INTERFACE structure contains pointers to functions that belong to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570560">VidPn Topology interface</a>, which is implemented by the video present network (VidPN) manager.</p>


## -syntax

````
typedef struct _DXGK_VIDPNTOPOLOGY_INTERFACE {
  DXGKDDI_VIDPNTOPOLOGY_GETNUMPATHS               pfnGetNumPaths;
  DXGKDDI_VIDPNTOPOLOGY_GETNUMPATHSFROMSOURCE     pfnGetNumPathsFromSource;
  DXGKDDI_VIDPNTOPOLOGY_ENUMPATHTARGETSFROMSOURCE pfnEnumPathTargetsFromSource;
  DXGKDDI_VIDPNTOPOLOGY_GETPATHSOURCEFROMTARGET   pfnGetPathSourceFromTarget;
  DXGKDDI_VIDPNTOPOLOGY_ACQUIREPATHINFO           pfnAcquirePathInfo;
  DXGKDDI_VIDPNTOPOLOGY_ACQUIREFIRSTPATHINFO      pfnAcquireFirstPathInfo;
  DXGKDDI_VIDPNTOPOLOGY_ACQUIRENEXTPATHINFO       pfnAcquireNextPathInfo;
  DXGKDDI_VIDPNTOPOLOGY_UPDATEPATHSUPPORTINFO     pfnUpdatePathSupportInfo;
  DXGKDDI_VIDPNTOPOLOGY_RELEASEPATHINFO           pfnReleasePathInfo;
  DXGKDDI_VIDPNTOPOLOGY_CREATENEWPATHINFO         pfnCreateNewPathInfo;
  DXGKDDI_VIDPNTOPOLOGY_ADDPATH                   pfnAddPath;
  DXGKDDI_VIDPNTOPOLOGY_REMOVEPATH                pfnRemovePath;
} DXGK_VIDPNTOPOLOGY_INTERFACE;
````


## -struct-fields
<dl>

### -field <b>pfnGetNumPaths</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-getnumpaths.md">pfnGetNumPaths</a> function.</p>
</dd>

### -field <b>pfnGetNumPathsFromSource</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-getnumpathsfromsource.md">pfnGetNumPathsFromSource</a> function.</p>
</dd>

### -field <b>pfnEnumPathTargetsFromSource</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-enumpathtargetsfromsource.md">pfnEnumPathTargetsFromSource</a> function.</p>
</dd>

### -field <b>pfnGetPathSourceFromTarget</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-getpathsourcefromtarget.md">pfnGetPathSourceFromTarget</a> function.</p>
</dd>

### -field <b>pfnAcquirePathInfo</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-acquirepathinfo.md">pfnAcquirePathInfo</a> function.</p>
</dd>

### -field <b>pfnAcquireFirstPathInfo</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-acquirefirstpathinfo.md">pfnAcquireFirstPathInfo</a> function.</p>
</dd>

### -field <b>pfnAcquireNextPathInfo</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-acquirenextpathinfo.md">pfnAcquireNextPathInfo</a> function.</p>
</dd>

### -field <b>pfnUpdatePathSupportInfo</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-updatepathsupportinfo.md">pfnUpdatePathSupportInfo</a> function.</p>
</dd>

### -field <b>pfnReleasePathInfo</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-releasepathinfo.md">pfnReleasePathInfo</a> function.</p>
</dd>

### -field <b>pfnCreateNewPathInfo</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-createnewpathinfo.md">pfnCreateNewPathInfo</a> function.</p>
</dd>

### -field <b>pfnAddPath</b>

<dd>
<p>
      A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-addpath.md">pfnAddPath</a> function.
     </p>
</dd>

### -field <b>pfnRemovePath</b>

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpntopology-removepath.md">pfnRemovePath</a> function.</p>
</dd>
</dl>

## -remarks
<p>The display miniport driver calls the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-vidpn-gettopology.md">pfnGetTopology</a> function of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570556">VidPn interface</a> to obtain a handle to a VidPN topology object and a pointer to a DXGK_VIDPNTOPOLOGY_INTERFACE structure. The structure contains pointers to functions that the display miniport driver can call to inspect and alter the VidPN topology object.</p>

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