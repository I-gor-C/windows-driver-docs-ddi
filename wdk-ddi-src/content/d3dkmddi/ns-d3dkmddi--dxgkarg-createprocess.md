---
UID: NS.d3dkmddi._DXGKARG_CREATEPROCESS
title: DXGKARG_CREATEPROCESS
author: windows-driver-content
description: DXGKARG_CREATEPROCESS is used with DxgkDdiCreateProcess to create a kernel mode driver object for a Microsoft DirectX graphics kernel process object.
old-location: display\dxgkarg_createprocess.htm
old-project: display
ms.assetid: F4FDF254-1C36-43DC-B1FD-376AD7658E61
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKARG_CREATEPROCESS, DXGKARG_CREATEPROCESS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKARG_CREATEPROCESS
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

# DXGKARG_CREATEPROCESS structure



## -description
<p><b>DXGKARG_CREATEPROCESS</b> is used with <a href="display.dxgkddicreateprocess">DxgkDdiCreateProcess</a> to create a kernel mode driver object for a Microsoft DirectX graphics kernel process object.</p>


## -syntax

````
typedef struct _DXGKARG_CREATEPROCESS {
  HANDLE                  hDxgkProcess;
  HANDLE                  hKmdProcess;
  DXGK_CREATEPROCESSFLAGS Flags;
  UINT                    NumPasid;
  ULONG*                  pPasid;
} DXGKARG_CREATEPROCESS;
````


## -struct-fields
<dl>

### -field <b>hDxgkProcess</b>

<dd>
<p>[in] The handle to the DirectX graphics kernel process.</p>
</dd>

### -field <b>hKmdProcess</b>

<dd>
<p>[out] The handle to the kernel mode driver process.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-createprocessflags.md">DXGK_CREATEPROCESSFLAGS</a> structure describing the operation.</p>
</dd>

### -field <b>NumPasid</b>

<dd>
<p>[in] The number of elements in the process address space identifier array located in the <b>pPasid</b>  member. </p>
</dd>

### -field <b>pPasid</b>

<dd>
<p>[in] A pointer to an array of process address identifiers. There will be one for each physical GPUs.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
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

## -see-also
<dl>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-createprocessflags.md">DXGK_CREATEPROCESSFLAGS</a>
</dt>
<dt>
<a href="display.dxgkddicreateprocess">DxgkDdiCreateProcess</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKARG_CREATEPROCESS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
