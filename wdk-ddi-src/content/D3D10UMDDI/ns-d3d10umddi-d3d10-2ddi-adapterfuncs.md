---
UID: NS.d3d10umddi.D3D10_2DDI_ADAPTERFUNCS
title: D3D10_2DDI_ADAPTERFUNCS
author: windows-driver-content
description: The D3D10_2DDI_ADAPTERFUNCS structure contains functions that the user-mode display driver can implement to communicate with a graphics adapter object.
old-location: display\d3d10_2ddi_adapterfuncs.htm
ms.assetid: b8ccd6f0-d1bf-430f-bffb-dd161793096f
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: D3D10_2DDI_ADAPTERFUNCS is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10_2DDI_ADAPTERFUNCS
req.alt-loc: d3d10umddi.h
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
ms.keywords: D3D10_2DDI_ADAPTERFUNCS, D3D10_2DDI_ADAPTERFUNCS
req.iface: 
---

# D3D10_2DDI_ADAPTERFUNCS structure



## -description
<p>The D3D10_2DDI_ADAPTERFUNCS structure contains functions that the user-mode display driver can implement to communicate with a graphics adapter object. </p>


## -syntax

````
typedef struct D3D10_2DDI_ADAPTERFUNCS {
  PFND3D10DDI_CALCPRIVATEDEVICESIZE  pfnCalcPrivateDeviceSize;
  PFND3D10DDI_CREATEDEVICE           pfnCreateDevice;
  PFND3D10DDI_CLOSEADAPTER           pfnCloseAdapter;
  PFND3D10_2DDI_GETSUPPORTEDVERSIONS pfnGetSupportedVersions;
  PFND3D10_2DDI_GETCAPS              pfnGetCaps;
} D3D10_2DDI_ADAPTERFUNCS;
````


## -struct-fields
<dl>

### -field <b>pfnCalcPrivateDeviceSize</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/8221a99a-1b46-48ba-8930-ac973e009eee">CalcPrivateDeviceSize</a> function that specifies the size of a memory block that the user-mode display driver requires from the Microsoft Direct3D runtime to store frequently-accessed data.</p>
</dd>

### -field <b>pfnCreateDevice</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/c69eedb1-c975-412c-aa9f-cf64a702f937">CreateDevice(D3D10)</a> function that creates a representation of a display device that handles a collection of rendering state.</p>
</dd>

### -field <b>pfnCloseAdapter</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/bc7ccd91-becc-4596-a56a-562cfe9a18b9">CloseAdapter(D3D10)</a> function that releases resources for a graphics adapter object.</p>
</dd>

### -field <b>pfnGetSupportedVersions</b>

<dd>
<p>A pointer to the driver's <a href="NULL">GetSupportedVersions</a> function that retrieves the version of the operating system that the driver supports and the hardware capabilities that are available (for example, Direct3D version 10.0, Direct3D version 10.1, and so on).</p>
</dd>

### -field <b>pfnGetCaps</b>

<dd>
<p>A pointer to the driver's <a href="https://msdn.microsoft.com/83cd5f34-5f12-4ead-ad33-366fc3c6e804">GetCaps(D3D10_2)</a> function that queries for capabilities of the graphics hardware. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>D3D10_2DDI_ADAPTERFUNCS is supported beginning with the Windows 7 operating system. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/8221a99a-1b46-48ba-8930-ac973e009eee">CalcPrivateDeviceSize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/bc7ccd91-becc-4596-a56a-562cfe9a18b9">CloseAdapter(D3D10)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c69eedb1-c975-412c-aa9f-cf64a702f937">CreateDevice(D3D10)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541724">D3D10DDIARG_OPENADAPTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/83cd5f34-5f12-4ead-ad33-366fc3c6e804">GetCaps(D3D10_2)</a>
</dt>
<dt>
<a href="NULL">GetSupportedVersions</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/50c10021-2bad-4e3c-99cc-24cf31fbc95d">OpenAdapter10</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10_2DDI_ADAPTERFUNCS structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
