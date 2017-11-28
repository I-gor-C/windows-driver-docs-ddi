---
UID: NC.d3dumddi.PFND3DDDI_SETLIGHT
title: PFND3DDDI_SETLIGHT
author: windows-driver-content
description: The SetLight function sets properties for a light source.
old-location: display\setlight.htm
old-project: display
ms.assetid: 28e3992e-a636-47e2-a5a6-5da06d276b5c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SetLight
req.alt-loc: d3dumddi.h
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

# PFND3DDDI_SETLIGHT callback



## -description
<p>The <i>SetLight</i> function sets properties for a light source.</p>


## -prototype

````
PFND3DDDI_SETLIGHT SetLight;

__checkReturn HRESULT APIENTRY SetLight(
  _In_       HANDLE             hDevice,
  _In_ const D3DDDIARG_SETLIGHT *pData,
  _In_ const D3DDDI_LIGHT       *pLightProperties
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p> A handle to the display device (graphics context).</p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p> A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff543317">D3DDDIARG_SETLIGHT</a> structure that describes how to set the light source.</p>
</dd>

### -param <i>pLightProperties</i> [in]

<dd>
<p> A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff544579">D3DDDI_LIGHT</a> structure that describes the light properties to set.</p>
</dd>
</dl>

## -returns
<p><i>SetLight</i> returns S_OK or an appropriate error result if the light properties are not successfully set.</p>

## -remarks
<p>Light properties describe the type and color of a light source. Depending on the type of light that is being used, a light can have properties for attenuation and range or for spotlight effects. However, not all types of lights will use all of the properties. For more information about light properties, see the Microsoft Windows SDK documentation.</p>

<p>Light properties describe the type and color of a light source. Depending on the type of light that is being used, a light can have properties for attenuation and range or for spotlight effects. However, not all types of lights will use all of the properties. For more information about light properties, see the Microsoft Windows SDK documentation.</p>

## -requirements
<table>
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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543317">D3DDDIARG_SETLIGHT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544579">D3DDDI_LIGHT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544519">D3DDDI_DEVICEFUNCS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20PFND3DDDI_SETLIGHT callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
