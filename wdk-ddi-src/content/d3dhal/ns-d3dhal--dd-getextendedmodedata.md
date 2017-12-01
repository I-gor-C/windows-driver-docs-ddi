---
UID: NS.d3dhal._DD_GETEXTENDEDMODEDATA
title: DD_GETEXTENDEDMODEDATA
author: windows-driver-content
description: DirectX 9.0 and later versions only. DD_GETEXTENDEDMODEDATA is the data structure pointed to by the lpvData field of DD_GETDRIVERINFODATA for DD_GETDRIVERINFO2DATA queries with the type D3DGDI2_TYPE_GETEXTENDEDMODE.
old-location: display\dd_getextendedmodedata.htm
old-project: display
ms.assetid: 50b2a1fd-4214-4ad8-b087-f48c14dbe587
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_GETEXTENDEDMODEDATA, DD_GETEXTENDEDMODEDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dhal.h
req.include-header: D3dhal.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DD_GETEXTENDEDMODEDATA
req.alt-loc: d3dhal.h
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

# DD_GETEXTENDEDMODEDATA structure



## -description
<p>
   DirectX 9.0 and later versions only.
   </p>
<p>DD_GETEXTENDEDMODEDATA is the data structure pointed to by the <b>lpvData</b> field of <a href="display.dd_getdriverinfodata">DD_GETDRIVERINFODATA</a> for DD_GETDRIVERINFO2DATA queries with the type D3DGDI2_TYPE_GETEXTENDEDMODE.</p>


## -syntax

````
typedef struct _DD_GETEXTENDEDMODEDATA {
  DD_GETDRIVERINFO2DATA gdi2;
  DWORD                 dwModeIndex;
  D3DDISPLAYMODE        mode;
} DD_GETEXTENDEDMODEDATA;
````


## -struct-fields
<dl>

### -field <b>gdi2</b>

<dd>
<p>Specifies a <a href="..\d3dhal\ns-d3dhal--dd-getdriverinfo2data.md">DD_GETDRIVERINFO2DATA</a> structure that contains the <b>GetDriverInfo2</b> data.</p>
</dd>

### -field <b>dwModeIndex</b>

<dd>
<p>Specifies the index of the display mode to return.</p>
</dd>

### -field <b>mode</b>

<dd>
<p>Receives a D3DDISPLAYMODE structure that specifies the actual display mode.</p>
</dd>
</dl>

## -remarks
<p>The runtime identifies the display mode to be returned with an integer index whose value varies between zero and one less than the number of supported display modes that were reported earlier by the driver in a DD_GETDRIVERINFO2DATA query with the type D3DGDI2_TYPE_GETEXTENDEDMODECOUNT. How these indices are mapped to actual display modes is left to the driver. However, each index must map uniquely to one supported display mode. The order in which the display modes are reported is not significant. </p>

<p>When processing this <b>GetDriverInfo2</b> request the driver should read the value in the <b>dwModeIndex</b> member and map that value to one of the supported display modes (probably by using the value in <b>dwModeIndex</b> as an index into an array of D3DDISPLAYMODE structures). The driver should then copy that display mode into the <b>mode</b> member. The runtime guarantees that it only passes an index to the driver that is in the range zero to one less than the number of display modes reported by the driver. The range of the index should be validated in the debug driver build.</p>

<p>For more information about D3DDISPLAYMODE, see the DirectX SDK documentation.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dhal.h (include D3dhal.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.dd_getdriverinfodata">DD_GETDRIVERINFODATA</a>
</dt>
<dt>
<a href="..\d3dhal\ns-d3dhal--dd-getdriverinfo2data.md">DD_GETDRIVERINFO2DATA</a>
</dt>
<dt>
<a href="..\d3dhal\ns-d3dhal--dd-getextendedmodecountdata.md">DD_GETEXTENDEDMODECOUNTDATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DD_GETEXTENDEDMODEDATA structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
