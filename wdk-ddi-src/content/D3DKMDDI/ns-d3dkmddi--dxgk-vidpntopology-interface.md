---
UID: NS.d3dkmddi._DXGK_VIDPNTOPOLOGY_INTERFACE
title: DXGK_VIDPNTOPOLOGY_INTERFACE
author: windows-driver-content
description: The DXGK_VIDPNTOPOLOGY_INTERFACE structure contains pointers to functions that belong to the VidPn Topology interface, which is implemented by the video present network (VidPN) manager.
old-location: display\dxgk_vidpntopology_interface.htm
ms.assetid: 293103cc-217c-4dcb-82c1-971adba564a0
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
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
ms.keywords: DXGK_VIDPNTOPOLOGY_INTERFACE, DXGK_VIDPNTOPOLOGY_INTERFACE
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
<p>A pointer to the <a href="https://msdn.microsoft.com/60960774-3f90-4eeb-a408-fa37122f22ea">pfnGetNumPaths</a> function.</p>
</dd>

### -field <b>pfnGetNumPathsFromSource</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/6c5ee84d-e106-47fc-88bd-b184e9cdd561">pfnGetNumPathsFromSource</a> function.</p>
</dd>

### -field <b>pfnEnumPathTargetsFromSource</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/ca925b3c-8141-419d-99a1-43764ec07315">pfnEnumPathTargetsFromSource</a> function.</p>
</dd>

### -field <b>pfnGetPathSourceFromTarget</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/c3e7b025-2382-4a81-8d78-9333b62b556a">pfnGetPathSourceFromTarget</a> function.</p>
</dd>

### -field <b>pfnAcquirePathInfo</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/27a03106-a5b5-489c-968a-81b3ea9940cb">pfnAcquirePathInfo</a> function.</p>
</dd>

### -field <b>pfnAcquireFirstPathInfo</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/b5dc35dc-f4fb-4209-9a4d-50dc11f16216">pfnAcquireFirstPathInfo</a> function.</p>
</dd>

### -field <b>pfnAcquireNextPathInfo</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/9f09ac0e-057c-48fb-a246-35e8ed7ddfc2">pfnAcquireNextPathInfo</a> function.</p>
</dd>

### -field <b>pfnUpdatePathSupportInfo</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/affe9ab2-49ef-4284-b441-49c311158827">pfnUpdatePathSupportInfo</a> function.</p>
</dd>

### -field <b>pfnReleasePathInfo</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/fdd34377-6b11-4005-93f1-ab42be7633c2">pfnReleasePathInfo</a> function.</p>
</dd>

### -field <b>pfnCreateNewPathInfo</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/2d9a4e10-514d-4ea9-9d60-0bbb7cdca29d">pfnCreateNewPathInfo</a> function.</p>
</dd>

### -field <b>pfnAddPath</b>

<dd>
<p>
      A pointer to the <a href="https://msdn.microsoft.com/893e0be1-aa29-429a-a3ca-a9f19053fd92">pfnAddPath</a> function.
     </p>
</dd>

### -field <b>pfnRemovePath</b>

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/463973e0-c443-417a-86ff-0b78773d40cc">pfnRemovePath</a> function.</p>
</dd>
</dl>

## -remarks
<p>The display miniport driver calls the <a href="https://msdn.microsoft.com/2bc43cd0-97a2-4120-8e6f-425664d3d28c">pfnGetTopology</a> function of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff570556">VidPn interface</a> to obtain a handle to a VidPN topology object and a pointer to a DXGK_VIDPNTOPOLOGY_INTERFACE structure. The structure contains pointers to functions that the display miniport driver can call to inspect and alter the VidPN topology object.</p>

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