---
UID: NS.d3dumddi._DXVADDI_PRIVATEDATA
title: DXVADDI_PRIVATEDATA
author: windows-driver-content
description: The DXVADDI_PRIVATEDATA structure describes data that is required for a particular decoder to operate.
old-location: display\dxvaddi_privatedata.htm
old-project: display
ms.assetid: 51e520db-fbec-4c6b-a23c-4d401de9ae63
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXVADDI_PRIVATEDATA, DXVADDI_PRIVATEDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVADDI_PRIVATEDATA
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

# DXVADDI_PRIVATEDATA structure



## -description
<p>The DXVADDI_PRIVATEDATA structure describes data that is required for a particular decoder to operate. </p>


## -syntax

````
typedef struct _DXVADDI_PRIVATEDATA {
  VOID *pData;
  UINT DataSize;
} DXVADDI_PRIVATEDATA;
````


## -struct-fields
<dl>

### -field <b>pData</b>

<dd>
<p>[in] A pointer to a buffer that contains decoder data.</p>
</dd>

### -field <b>DataSize</b>

<dd>
<p>[in] The size, in bytes, of the buffer that is pointed to by <b>pData</b>.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542927">D3DDDIARG_CREATEDECODEDEVICE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543001">D3DDDIARG_DECODEEXECUTE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543009">D3DDDIARG_DECODEEXTENSIONEXECUTE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_PRIVATEDATA structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
