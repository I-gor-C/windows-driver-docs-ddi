---
UID: NC.d3dumddi.PFND3DDDI_SETMARKERMODE
title: PFND3DDDI_SETMARKERMODE
author: windows-driver-content
description: Notifies the user-mode display driver that it should support a type of Event Tracing for Windows (ETW) marker event.
old-location: display\pfnsetmarkermode.htm
old-project: display
ms.assetid: D45750D9-F722-4208-8D00-E14FD9C009CB
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3d10umddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 8.1,WDDM 1.3 and later
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnSetMarkerMode
req.alt-loc: D3dumddi.h
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

# PFND3DDDI_SETMARKERMODE callback



## -description
<p>Notifies the user-mode display driver that it should support a type of Event Tracing for Windows (ETW) marker event. Optionally implemented by Windows Display Driver Model (WDDM) 1.3 and later drivers running on Microsoft Direct3D Level 9 hardware. (See requirements in <a href="https://msdn.microsoft.com/F9AAE489-EC45-4EE6-875E-E084BB3054EE">Direct3D rendering performance improvements</a>.) For more advanced hardware, drivers should implement the <a href="..\d3d10umddi\nc-d3d10umddi-pfnd3dwddm1-3ddi-setmarkermode.md">SetMarkerMode</a> function.</p>


## -prototype

````
PFND3DDDI_SETMARKERMODE pfnSetMarkerMode;

_Check_return_ HRESULT APIENTRY* pfnSetMarkerMode(
  _In_ HANDLE            hDevice,
  _In_ D3DDDI_MARKERTYPE Type,
       UINT              Flags
)
{ ... }
````


## -parameters
<dl>

### -param hDevice [in]

<dd>
<p>A handle to the display device (graphics context).</p>
</dd>

### -param Type [in]

<dd>
<p>A value from the <a href="..\d3dumddi\ne-d3dumddi-d3dddi-markertype.md">D3DDDI_MARKERTYPE</a> enumeration that indicates the type of marker event  that the driver should support.</p>
</dd>

### -param Flags 

<dd>
<p>A <b>UINT</b> value that indicates whether the driver should provide custom info in command buffers. If set to <b>D3DDDI_SETMARKERMODE_CUSTOMDRIVEREVENTS</b>, the driver should annotate and instrument command buffers with custom event info. Otherwise, the driver should not annotate command buffers.</p>
<p>The annotation can be in the form of a text string in the English-US locale, or in the form of an index value to a location in a string table. For the latter option, the driver must also implement a function that describes the strings that the index values indicate.</p>
</dd>
</dl>

## -returns
<p>
      Returns <b>S_OK</b> or an appropriate error result if the function does not complete successfully.</p>

## -remarks
<p>Follow these guidelines when you set up profile-type marker events in your user-mode driver, indicated by the <b>D3DDDIMT_PROFILE</b> type:</p>

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
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>WDDM 1.3 and later</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\ne-d3dumddi-d3dddi-markertype.md">D3DDDI_MARKERTYPE</a>
</dt>
<dt>
<a href="..\d3d10umddi\nc-d3d10umddi-pfnd3dwddm1-3ddi-setmarkermode.md">SetMarkerMode</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETMARKERMODE callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
