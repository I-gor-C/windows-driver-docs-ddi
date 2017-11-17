---
UID: NS.d3dumddi._DXVADDI_PVP_SETKEY
title: DXVADDI_PVP_SETKEY
author: windows-driver-content
description: The DXVADDI_PVP_SETKEY structure describes a key that the decode device uses to start decoding a frame.
old-location: display\dxvaddi_pvp_setkey.htm
ms.assetid: 3707f9c9-109e-4ac2-bc34-c9f4f7651306
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVADDI_PVP_SETKEY
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
ms.keywords: DXVADDI_PVP_SETKEY, DXVADDI_PVP_SETKEY
req.iface: 
---

# DXVADDI_PVP_SETKEY structure



## -description
<p>The DXVADDI_PVP_SETKEY structure describes a key that the decode device uses to start decoding a frame. </p>


## -syntax

````
typedef struct _DXVADDI_PVP_SETKEY {
  DXVADDI_PVP_KEY128 ContentKey;
} DXVADDI_PVP_SETKEY;
````


## -struct-fields
<dl>

### -field <b>ContentKey</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562922">DXVADDI_PVP_KEY128</a> structure that contains the 128-bit key.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542987">D3DDDIARG_DECODEBEGINFRAME</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/3e6153aa-7b21-429d-8908-1ff3a4d25e17">DecodeBeginFrame</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562922">DXVADDI_PVP_KEY128</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_PVP_SETKEY structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
