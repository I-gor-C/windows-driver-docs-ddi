---
UID: NS.d3dumddi._D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE
title: D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE
author: windows-driver-content
description: The D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE structure describes the bit-block transfer (bitblt) state of the video processor to change and the data that is used to change the state.
old-location: display\d3dddiarg_dxvahd_setvideoprocessbltstate.htm
ms.assetid: ebcd58d7-f0b3-43ea-b08f-f0c2618902d7
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE is supported beginning with the Windows 7 operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE
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
ms.keywords: D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE, D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE
req.iface: 
---

# D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE structure



## -description
<p>The D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE structure describes the bit-block transfer (bitblt) state of the video processor to change and the data that is used to change the state. </p>


## -syntax

````
typedef struct _D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE {
  HANDLE              hVideoProcessor;
  DXVAHDDDI_BLT_STATE State;
  UINT                DataSize;
  const VOID          *pData;
} D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE;
````


## -struct-fields
<dl>

### -field <b>hVideoProcessor</b>

<dd>
<p>[in] A handle to the video processor whose bitblt state is changed.</p>
</dd>

### -field <b>State</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff562978">DXVAHDDDI_BLT_STATE</a>-typed value that indicates the type of bitblt to set.</p>
</dd>

### -field <b>DataSize</b>

<dd>
<p>[in] The size, in bytes, of the data that is used to change the bitblt state.</p>
</dd>

### -field <b>pData</b>

<dd>
<p>[in] A pointer to the data that is used to change the bitblt state. For more information about the types of data that <b>pData</b> can point to, see the values of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562978">DXVAHDDDI_BLT_STATE</a> enumeration. </p>
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
<p>D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE is supported beginning with the Windows 7 operating system.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562978">DXVAHDDDI_BLT_STATE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/6796372c-279d-427c-a2a4-9b7c99494f53">SetVideoProcessBltState</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_DXVAHD_SETVIDEOPROCESSBLTSTATE structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
