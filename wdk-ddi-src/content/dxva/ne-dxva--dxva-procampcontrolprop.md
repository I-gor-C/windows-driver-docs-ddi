---
UID: NE.dxva._DXVA_ProcAmpControlProp
title: DXVA_ProcAmpControlProp
author: windows-driver-content
description: The DXVA_ProcAmpControlProp enumeration is used to determine the required ProcAmp control adjustments.
old-location: display\dxva_procampcontrolprop.htm
old-project: display
ms.assetid: ce1bae9b-1cc3-45ea-bf46-8aa7ed0362f6
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGI_GAMMA_CONTROL_CAPABILITIES, DXGI_GAMMA_CONTROL_CAPABILITIES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: DirectX 9.0 and later versions only.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVA_ProcAmpControlProp
req.alt-loc: dxva.h
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

# DXVA_ProcAmpControlProp enumeration



## -description
<p>The DXVA_ProcAmpControlProp enumeration is used to determine the required ProcAmp control adjustments.</p>


## -syntax

````
typedef enum _DXVA_ProcAmpControlProp { 
  DXVA_ProcAmp_None        = 0x0000,
  DXVA_ProcAmp_Brightness  = 0x0001,
  DXVA_ProcAmp_Contrast    = 0x0002,
  DXVA_ProcAmp_Hue         = 0x0004,
  DXVA_ProcAmp_Saturation  = 0x0008
} DXVA_ProcAmpControlProp;
````


## -enum-fields
<dl>

### -field <a id="DXVA_ProcAmp_None"></a><a id="dxva_procamp_none"></a><a id="DXVA_PROCAMP_NONE"></a><b>DXVA_ProcAmp_None</b>

<dd>
<p>Specifies that no ProcAmp properties are used. </p>
</dd>

### -field <a id="DXVA_ProcAmp_Brightness"></a><a id="dxva_procamp_brightness"></a><a id="DXVA_PROCAMP_BRIGHTNESS"></a><b>DXVA_ProcAmp_Brightness</b>

<dd>
<p>Specifies that the ProcAmp brightness property is used. </p>
</dd>

### -field <a id="DXVA_ProcAmp_Contrast"></a><a id="dxva_procamp_contrast"></a><a id="DXVA_PROCAMP_CONTRAST"></a><b>DXVA_ProcAmp_Contrast</b>

<dd>
<p>Specifies that the ProcAmp contrast property is used. </p>
</dd>

### -field <a id="DXVA_ProcAmp_Hue"></a><a id="dxva_procamp_hue"></a><a id="DXVA_PROCAMP_HUE"></a><b>DXVA_ProcAmp_Hue</b>

<dd>
<p>Specifies that the ProcAmp hue property is used. </p>
</dd>

### -field <a id="DXVA_ProcAmp_Saturation"></a><a id="dxva_procamp_saturation"></a><a id="DXVA_PROCAMP_SATURATION"></a><b>DXVA_ProcAmp_Saturation</b>

<dd>
<p>Specifies that the ProcAmp saturation property is used.</p>
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
<p>DirectX 9.0 and later versions only.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dxva.h (include Dxva.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564019">DXVA_ProcAmpControlCaps</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564032">DXVA_ProcAmpControlQueryRange</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVA_ProcAmpControlProp enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
