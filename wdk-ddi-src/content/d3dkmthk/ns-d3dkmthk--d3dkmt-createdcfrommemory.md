---
UID: NS.d3dkmthk._D3DKMT_CREATEDCFROMMEMORY
title: D3DKMT_CREATEDCFROMMEMORY
author: windows-driver-content
description: The D3DKMT_CREATEDCFROMMEMORY structure describes parameters for creating the display context.
old-location: display\d3dkmt_createdcfrommemory.htm
old-project: display
ms.assetid: 260fd894-fc5a-4a27-ac35-3f1b145b52b7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_CREATEDCFROMMEMORY, D3DKMT_CREATEDCFROMMEMORY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_CREATEDCFROMMEMORY
req.alt-loc: d3dkmthk.h
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

# D3DKMT_CREATEDCFROMMEMORY structure



## -description
<p>The D3DKMT_CREATEDCFROMMEMORY structure describes parameters for creating the display context.</p>


## -syntax

````
typedef struct _D3DKMT_CREATEDCFROMMEMORY {
  VOID         *pMemory;
  D3DDDIFORMAT Format;
  UINT         Width;
  UINT         Height;
  UINT         Pitch;
  HDC          hDeviceDc;
  PALETTEENTRY *pColorTable;
  HDC          hDc;
  HANDLE       hBitmap;
} D3DKMT_CREATEDCFROMMEMORY;
````


## -struct-fields
<dl>

### -field pMemory

<dd>
<p>[in] A pointer to a block of memory for the display context.</p>
</dd>

### -field Format

<dd>
<p>[in] A <a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a>-typed value that indicates the pixel format for the memory block that <b>pMemory</b> points to.</p>
</dd>

### -field Width

<dd>
<p>[in] The width, in pixels, of the memory block that <b>pMemory</b> points to.</p>
</dd>

### -field Height

<dd>
<p>[in] The height, in pixels, of the memory block that <b>pMemory</b> points to.</p>
</dd>

### -field Pitch

<dd>
<p>[in] The pitch, in bytes, of the memory block that <b>pMemory</b> points to--that is, the distance in bytes to the start of the next line.</p>
</dd>

### -field hDeviceDc

<dd>
<p>[in] A handle to the display context for the device.</p>
</dd>

### -field pColorTable

<dd>
<p>[in] An array of 2, 4, 16, or 256 PALETTEENTRY structures that are used to initialize the colors for the memory block that <b>pMemory</b> points to. For more information about PALETTEENTRY, see the Microsoft Window SDK documentation.</p>
</dd>

### -field hDc

<dd>
<p>[out] A handle to the display context. The OpenGL runtime generates a handle and passes it back to the driver.</p>
</dd>

### -field hBitmap

<dd>
<p>[out] A handle to a bitmap that is related to the display context. The OpenGL runtime generates a handle and passes it back to the driver.</p>
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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a>
</dt>
<dt>
<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtcreatedcfrommemory.md">D3DKMTCreateDCFromMemory</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_CREATEDCFROMMEMORY structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
